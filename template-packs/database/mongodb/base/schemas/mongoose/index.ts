// Export all Mongoose schemas
export { User, IUser } from './user.schema';
export { Session, ISession } from './session.schema';
export { AuditLog, IAuditLog } from './auditLog.schema';

// Database connection helper
import mongoose, { ConnectOptions } from 'mongoose';

export async function connectDatabase(
  uri: string,
  options?: ConnectOptions
): Promise<typeof mongoose> {
  try {
    const defaultOptions: ConnectOptions = {
      // Modern MongoDB driver options
      serverSelectionTimeoutMS: 5000,
      socketTimeoutMS: 45000,
      ...options,
    };

    await mongoose.connect(uri, defaultOptions);
    
    console.log('✅ MongoDB connected successfully');
    
    // Handle connection events
    mongoose.connection.on('error', (error) => {
      console.error('❌ MongoDB connection error:', error);
    });

    mongoose.connection.on('disconnected', () => {
      console.warn('⚠️ MongoDB disconnected');
    });

    // Graceful shutdown
    process.on('SIGINT', async () => {
      await mongoose.connection.close();
      console.log('MongoDB connection closed through app termination');
      process.exit(0);
    });

    return mongoose;
  } catch (error) {
    console.error('❌ MongoDB connection failed:', error);
    throw error;
  }
}

// Helper to check connection status
export function isDatabaseConnected(): boolean {
  return mongoose.connection.readyState === 1;
}

// Helper to get database stats
export async function getDatabaseStats() {
  if (!isDatabaseConnected()) {
    throw new Error('Database not connected');
  }

  const admin = mongoose.connection.db.admin();
  const dbStats = await admin.dbStats();
  
  return {
    database: mongoose.connection.db.databaseName,
    collections: dbStats.collections,
    dataSize: dbStats.dataSize,
    indexSize: dbStats.indexSize,
    ok: dbStats.ok === 1,
  };
}