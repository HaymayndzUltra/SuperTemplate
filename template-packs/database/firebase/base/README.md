# Firebase Database Template

This template provides a production-ready Firebase setup with Firestore, Cloud Functions, Storage, and comprehensive security rules.

## Features

- **Firestore** with security rules and indexes
- **Cloud Functions** with TypeScript support
- **Storage** with file upload rules
- **Authentication** integration
- **Scheduled functions** for maintenance
- **Emulator suite** for local development
- **Comprehensive security** rules

## Quick Start

1. **Install Firebase CLI:**
   ```bash
   npm install -g firebase-tools
   ```

2. **Login to Firebase:**
   ```bash
   firebase login
   ```

3. **Initialize project:**
   ```bash
   firebase init
   # Select: Firestore, Functions, Storage, Hosting
   ```

4. **Start emulators:**
   ```bash
   firebase emulators:start
   ```

5. **Deploy to production:**
   ```bash
   firebase deploy
   ```

## Project Structure

```
firebase/
├── firebase.json          # Firebase configuration
├── firestore.rules        # Firestore security rules
├── firestore.indexes.json # Database indexes
├── storage.rules          # Storage security rules
├── functions/             # Cloud Functions
│   ├── src/
│   │   └── index.ts       # Main functions file
│   ├── package.json       # Functions dependencies
│   └── tsconfig.json      # TypeScript config
└── public/                # Hosting files
    └── index.html
```

## Firestore Collections

### Users Collection
```javascript
{
  id: "user123",
  email: "user@example.com",
  name: "John Doe",
  role: "user", // user, admin, moderator
  isActive: true,
  createdAt: Timestamp,
  updatedAt: Timestamp
}
```

### Profiles Collection
```javascript
{
  id: "user123",
  userId: "user123",
  displayName: "John Doe",
  bio: "Software developer",
  avatar: "https://...",
  createdAt: Timestamp,
  updatedAt: Timestamp
}
```

### Sessions Collection
```javascript
{
  id: "session123",
  userId: "user123",
  token: "jwt_token_here",
  expiresAt: Timestamp,
  createdAt: Timestamp,
  isActive: true
}
```

### Posts Collection
```javascript
{
  id: "post123",
  authorId: "user123",
  title: "Post Title",
  content: "Post content...",
  tags: ["tech", "programming"],
  published: true,
  createdAt: Timestamp,
  updatedAt: Timestamp
}
```

## Cloud Functions

### Available Functions

1. **healthCheck** - HTTPS endpoint for health monitoring
2. **onUserCreate** - Triggered when user is created
3. **onUserUpdate** - Triggered when user is updated
4. **onUserDelete** - Triggered when user is deleted
5. **cleanupExpiredSessions** - Scheduled cleanup (hourly)
6. **sendDailyDigest** - Daily digest notifications
7. **getUserStats** - Admin-only statistics endpoint

### Function URLs

- **Health Check**: `https://your-region-your-project.cloudfunctions.net/healthCheck`
- **User Stats**: `https://your-region-your-project.cloudfunctions.net/getUserStats`

## Security Rules

### Firestore Rules
- Users can read/write their own data
- Admins can read all user data
- Public profiles are readable by all
- Sessions are private to users
- Posts are readable by authenticated users

### Storage Rules
- Profile images are public
- User documents are private
- Post attachments are readable by authenticated users
- File size limits: 5MB for images, 10MB for documents

## Sample Code

### Web Client (JavaScript)
```javascript
import { initializeApp } from 'firebase/app';
import { getFirestore, collection, addDoc, getDocs } from 'firebase/firestore';
import { getAuth, signInWithEmailAndPassword } from 'firebase/auth';

// Initialize Firebase
const firebaseConfig = {
  // Your config
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);

// Create a user
const createUser = async (userData) => {
  try {
    const docRef = await addDoc(collection(db, 'users'), {
      ...userData,
      createdAt: new Date(),
      updatedAt: new Date()
    });
    console.log('User created with ID: ', docRef.id);
  } catch (error) {
    console.error('Error creating user: ', error);
  }
};

// Get all users
const getUsers = async () => {
  const querySnapshot = await getDocs(collection(db, 'users'));
  querySnapshot.forEach((doc) => {
    console.log(doc.id, ' => ', doc.data());
  });
};
```

### Node.js Server
```javascript
const admin = require('firebase-admin');

// Initialize Admin SDK
const serviceAccount = require('./path/to/serviceAccountKey.json');
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

const db = admin.firestore();

// Create user
const createUser = async (userData) => {
  try {
    const docRef = await db.collection('users').add({
      ...userData,
      createdAt: admin.firestore.FieldValue.serverTimestamp(),
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    });
    console.log('User created with ID: ', docRef.id);
  } catch (error) {
    console.error('Error creating user: ', error);
  }
};
```

## Environment Setup

### Development
```bash
# Install dependencies
cd functions
npm install

# Start emulators
firebase emulators:start

# Run functions locally
npm run serve
```

### Production
```bash
# Deploy all services
firebase deploy

# Deploy specific service
firebase deploy --only firestore
firebase deploy --only functions
firebase deploy --only storage
```

## Emulator Suite

The Firebase Emulator Suite provides local development environment:

- **Firestore Emulator**: http://localhost:8080
- **Functions Emulator**: http://localhost:5001
- **Storage Emulator**: http://localhost:9199
- **Auth Emulator**: http://localhost:9099
- **Emulator UI**: http://localhost:4000

## Monitoring and Logs

### View Logs
```bash
# All functions
firebase functions:log

# Specific function
firebase functions:log --only healthCheck

# Real-time logs
firebase functions:log --follow
```

### Performance Monitoring
- Monitor function execution time
- Track memory usage
- Monitor error rates
- Set up alerts for failures

## Security Best Practices

1. **Authentication**: Always verify user authentication
2. **Authorization**: Use role-based access control
3. **Data Validation**: Validate all input data
4. **Rate Limiting**: Implement rate limiting for functions
5. **Error Handling**: Don't expose sensitive information in errors
6. **Logging**: Log security events for monitoring

## Troubleshooting

### Common Issues

1. **Permission Denied**:
   - Check Firestore security rules
   - Verify user authentication
   - Ensure proper role assignments

2. **Function Timeout**:
   - Increase function timeout in firebase.json
   - Optimize function code
   - Use background functions for long operations

3. **Storage Upload Failed**:
   - Check storage security rules
   - Verify file size limits
   - Ensure proper content types

### Debug Mode
```bash
# Enable debug logging
export FIREBASE_DEBUG=true
firebase emulators:start
```

## Support

For issues and questions:
1. Check Firebase documentation
2. Review security rules
3. Check function logs
4. Verify authentication status