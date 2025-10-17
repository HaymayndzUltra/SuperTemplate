import { onRequest, onCall, HttpsError } from 'firebase-functions/v2/https';
import { onDocumentCreated, onDocumentUpdated, onDocumentDeleted } from 'firebase-functions/v2/firestore';
import { onSchedule } from 'firebase-functions/v2/scheduler';
import * as admin from 'firebase-admin';

// Initialize Firebase Admin SDK
admin.initializeApp();

const db = admin.firestore();

// HTTPS Function - Health Check
export const healthCheck = onRequest((req, res) => {
  res.status(200).json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    service: 'firebase-functions',
    version: '1.0.0'
  });
});

// Firestore Trigger - User Creation
export const onUserCreate = onDocumentCreated('users/{userId}', async (event) => {
    const userData = event.data?.data() || {} as any;
    const userId = event.params.userId;
    
    console.log(`New user created: ${userId}`);
    
    // Create user profile
    await db.collection('profiles').doc(userId).set({
      userId: userId,
      displayName: userData.name,
      bio: '',
      avatar: '',
      createdAt: admin.firestore.FieldValue.serverTimestamp(),
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    });
    
    // Send welcome notification
    await db.collection('notifications').add({
      userId: userId,
      type: 'welcome',
      title: 'Welcome!',
      message: 'Welcome to our platform!',
      read: false,
      createdAt: admin.firestore.FieldValue.serverTimestamp()
    });
    
    console.log(`User profile and welcome notification created for ${userId}`);
});

// Firestore Trigger - User Update
export const onUserUpdate = onDocumentUpdated('users/{userId}', async (event) => {
    const beforeData = event.data?.before.data() || {} as any;
    const afterData = event.data?.after.data() || {} as any;
    const userId = event.params.userId;
    
    // Update profile if name changed
    if (beforeData.name !== afterData.name) {
      await db.collection('profiles').doc(userId).update({
        displayName: afterData.name,
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      });
      
      console.log(`Profile updated for user ${userId}`);
    }
});

// Firestore Trigger - User Delete
export const onUserDelete = onDocumentDeleted('users/{userId}', async (event) => {
    const userId = event.params.userId;
    
    console.log(`User deleted: ${userId}`);
    
    // Clean up related data
    const batch = db.batch();
    
    // Delete user profile
    batch.delete(db.collection('profiles').doc(userId));
    
    // Delete user sessions
    const sessionsSnapshot = await db.collection('sessions')
      .where('userId', '==', userId)
      .get();
    
    sessionsSnapshot.forEach(doc => {
      batch.delete(doc.ref);
    });
    
    // Delete user notifications
    const notificationsSnapshot = await db.collection('notifications')
      .where('userId', '==', userId)
      .get();
    
    notificationsSnapshot.forEach(doc => {
      batch.delete(doc.ref);
    });
    
    await batch.commit();
    
    console.log(`Cleaned up data for deleted user ${userId}`);
});

// Scheduled Function - Clean up expired sessions
export const cleanupExpiredSessions = onSchedule('every 1 hours', async (event) => {
    const now = admin.firestore.Timestamp.now();
    
    const expiredSessions = await db.collection('sessions')
      .where('expiresAt', '<', now)
      .get();
    
    if (expiredSessions.empty) {
      console.log('No expired sessions to clean up');
      return;
    }
    
    const batch = db.batch();
    expiredSessions.forEach(doc => {
      batch.delete(doc.ref);
    });
    
    await batch.commit();
    
    console.log(`Cleaned up ${expiredSessions.size} expired sessions`);
});

// Scheduled Function - Send daily digest
export const sendDailyDigest = onSchedule({ schedule: '0 9 * * *', timeZone: 'UTC' }, async (event) => {
    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    
    // Get active users
    const usersSnapshot = await db.collection('users')
      .where('isActive', '==', true)
      .get();
    
    for (const userDoc of usersSnapshot.docs) {
      const userId = userDoc.id;
      
      // Create daily digest notification
      await db.collection('notifications').add({
        userId: userId,
        type: 'digest',
        title: 'Daily Digest',
        message: 'Here\'s what happened yesterday...',
        read: false,
        createdAt: admin.firestore.FieldValue.serverTimestamp()
      });
    }
    
    console.log(`Sent daily digest to ${usersSnapshot.size} users`);
});

// HTTP Function - Get user statistics
export const getUserStats = onCall(async (request) => {
  // Check if user is authenticated
  if (!request.auth) throw new HttpsError('unauthenticated', 'User must be authenticated');
  
  const userId = request.auth.uid;
  
  // Check if user is admin
  const userDoc = await db.collection('users').doc(userId).get();
  if (!userDoc.exists || userDoc.data()?.role !== 'admin') {
    throw new HttpsError('permission-denied', 'Admin access required');
  }
  
  // Get statistics
  const [usersSnapshot, sessionsSnapshot, postsSnapshot] = await Promise.all([
    db.collection('users').get(),
    db.collection('sessions').get(),
    db.collection('posts').get()
  ]);
  
  return {
    totalUsers: usersSnapshot.size,
    activeSessions: sessionsSnapshot.size,
    totalPosts: postsSnapshot.size,
    timestamp: new Date().toISOString()
  };
});