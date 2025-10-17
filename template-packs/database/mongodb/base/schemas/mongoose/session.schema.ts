import { Schema, model, Document, Types } from 'mongoose';

export interface ISession extends Document {
  userId: Types.ObjectId;
  refreshToken: string;
  userAgent?: string;
  ipAddress?: string;
  expiresAt: Date;
  createdAt: Date;
}

const sessionSchema = new Schema<ISession>(
  {
    userId: {
      type: Schema.Types.ObjectId,
      ref: 'User',
      required: true,
      index: true,
    },
    refreshToken: {
      type: String,
      required: true,
      unique: true,
      index: true,
    },
    userAgent: {
      type: String,
    },
    ipAddress: {
      type: String,
      validate: {
        validator: function (v: string) {
          // Basic IP validation (v4 or v6)
          return /^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$|^(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}$/.test(v);
        },
        message: 'Invalid IP address format',
      },
    },
    expiresAt: {
      type: Date,
      required: true,
      index: true,
    },
  },
  {
    timestamps: { createdAt: true, updatedAt: false },
  }
);

// TTL index to automatically delete expired sessions
sessionSchema.index({ expiresAt: 1 }, { expireAfterSeconds: 0 });

// Static method to clean up expired sessions
sessionSchema.statics.cleanupExpired = function () {
  return this.deleteMany({ expiresAt: { $lt: new Date() } });
};

// Static method to find active sessions for a user
sessionSchema.statics.findActiveByUserId = function (userId: Types.ObjectId) {
  return this.find({
    userId,
    expiresAt: { $gt: new Date() },
  }).sort({ createdAt: -1 });
};

// Method to check if session is expired
sessionSchema.methods.isExpired = function (): boolean {
  return this.expiresAt < new Date();
};

export const Session = model<ISession>('Session', sessionSchema);