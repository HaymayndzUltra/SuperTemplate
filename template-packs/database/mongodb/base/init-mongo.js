// MongoDB initialization script
// This script runs when the MongoDB container starts for the first time

// Switch to the application database
db = db.getSiblingDB(process.env.MONGO_INITDB_DATABASE || 'appdb');

// Create application user
db.createUser({
  user: process.env.MONGO_APP_USER || 'appuser',
  pwd: process.env.MONGO_APP_PASSWORD || 'apppassword',
  roles: [
    {
      role: 'readWrite',
      db: process.env.MONGO_INITDB_DATABASE || 'appdb'
    }
  ]
});

// Create collections with validation
db.createCollection('users', {
  validator: {
    $jsonSchema: {
      bsonType: 'object',
      required: ['email', 'name', 'createdAt'],
      properties: {
        email: {
          bsonType: 'string',
          pattern: '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$',
          description: 'Email must be a valid email address'
        },
        name: {
          bsonType: 'string',
          minLength: 2,
          maxLength: 100,
          description: 'Name must be a string between 2 and 100 characters'
        },
        role: {
          bsonType: 'string',
          enum: ['user', 'admin', 'moderator'],
          description: 'Role must be one of: user, admin, moderator'
        },
        isActive: {
          bsonType: 'bool',
          description: 'isActive must be a boolean'
        },
        createdAt: {
          bsonType: 'date',
          description: 'createdAt must be a date'
        },
        updatedAt: {
          bsonType: 'date',
          description: 'updatedAt must be a date'
        }
      }
    }
  }
});

db.createCollection('sessions', {
  validator: {
    $jsonSchema: {
      bsonType: 'object',
      required: ['userId', 'token', 'expiresAt', 'createdAt'],
      properties: {
        userId: {
          bsonType: 'objectId',
          description: 'userId must be an ObjectId'
        },
        token: {
          bsonType: 'string',
          minLength: 32,
          description: 'Token must be a string with at least 32 characters'
        },
        expiresAt: {
          bsonType: 'date',
          description: 'expiresAt must be a date'
        },
        createdAt: {
          bsonType: 'date',
          description: 'createdAt must be a date'
        },
        isActive: {
          bsonType: 'bool',
          description: 'isActive must be a boolean'
        }
      }
    }
  }
});

// Create indexes for better performance
db.users.createIndex({ email: 1 }, { unique: true });
db.users.createIndex({ role: 1 });
db.users.createIndex({ isActive: 1 });
db.users.createIndex({ createdAt: 1 });

db.sessions.createIndex({ userId: 1 });
db.sessions.createIndex({ token: 1 }, { unique: true });
db.sessions.createIndex({ expiresAt: 1 }, { expireAfterSeconds: 0 });
db.sessions.createIndex({ isActive: 1 });

// Insert sample data
db.users.insertMany([
  {
    email: 'admin@example.com',
    name: 'Admin User',
    role: 'admin',
    isActive: true,
    createdAt: new Date(),
    updatedAt: new Date()
  },
  {
    email: 'user@example.com',
    name: 'Regular User',
    role: 'user',
    isActive: true,
    createdAt: new Date(),
    updatedAt: new Date()
  }
]);

print('MongoDB initialization completed successfully!');
print('Created collections: users, sessions');
print('Created indexes for performance optimization');
print('Inserted sample data');