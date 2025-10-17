"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
exports.getUserStats = exports.sendDailyDigest = exports.cleanupExpiredSessions = exports.onUserDelete = exports.onUserUpdate = exports.onUserCreate = exports.healthCheck = void 0;
const https_1 = require("firebase-functions/v2/https");
const firestore_1 = require("firebase-functions/v2/firestore");
const scheduler_1 = require("firebase-functions/v2/scheduler");
const admin = __importStar(require("firebase-admin"));
// Initialize Firebase Admin SDK
admin.initializeApp();
const db = admin.firestore();
// HTTPS Function - Health Check
exports.healthCheck = (0, https_1.onRequest)((req, res) => {
    res.status(200).json({
        status: 'healthy',
        timestamp: new Date().toISOString(),
        service: 'firebase-functions',
        version: '1.0.0'
    });
});
// Firestore Trigger - User Creation
exports.onUserCreate = (0, firestore_1.onDocumentCreated)('users/{userId}', async (event) => {
    var _a;
    const userData = ((_a = event.data) === null || _a === void 0 ? void 0 : _a.data()) || {};
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
exports.onUserUpdate = (0, firestore_1.onDocumentUpdated)('users/{userId}', async (event) => {
    var _a, _b;
    const beforeData = ((_a = event.data) === null || _a === void 0 ? void 0 : _a.before.data()) || {};
    const afterData = ((_b = event.data) === null || _b === void 0 ? void 0 : _b.after.data()) || {};
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
exports.onUserDelete = (0, firestore_1.onDocumentDeleted)('users/{userId}', async (event) => {
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
exports.cleanupExpiredSessions = (0, scheduler_1.onSchedule)('every 1 hours', async (event) => {
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
exports.sendDailyDigest = (0, scheduler_1.onSchedule)({ schedule: '0 9 * * *', timeZone: 'UTC' }, async (event) => {
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
exports.getUserStats = (0, https_1.onCall)(async (request) => {
    var _a;
    // Check if user is authenticated
    if (!request.auth)
        throw new https_1.HttpsError('unauthenticated', 'User must be authenticated');
    const userId = request.auth.uid;
    // Check if user is admin
    const userDoc = await db.collection('users').doc(userId).get();
    if (!userDoc.exists || ((_a = userDoc.data()) === null || _a === void 0 ? void 0 : _a.role) !== 'admin') {
        throw new https_1.HttpsError('permission-denied', 'Admin access required');
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
//# sourceMappingURL=index.js.map