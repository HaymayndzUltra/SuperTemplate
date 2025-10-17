import { Schema, model, Document, Types } from 'mongoose';

export interface IAuditLog extends Document {
  action: string;
  userId: Types.ObjectId;
  resource: string;
  resourceId?: string;
  changes?: {
    before?: any;
    after?: any;
  };
  metadata?: Record<string, any>;
  ipAddress?: string;
  userAgent?: string;
  timestamp: Date;
}

const auditLogSchema = new Schema<IAuditLog>(
  {
    action: {
      type: String,
      required: true,
      enum: [
        'CREATE',
        'READ',
        'UPDATE',
        'DELETE',
        'LOGIN',
        'LOGOUT',
        'PASSWORD_CHANGE',
        'PERMISSION_CHANGE',
        'EXPORT',
        'IMPORT',
        'SYSTEM_CONFIG_CHANGE',
      ],
      index: true,
    },
    userId: {
      type: Schema.Types.ObjectId,
      ref: 'User',
      required: true,
      index: true,
    },
    resource: {
      type: String,
      required: true,
      index: true,
    },
    resourceId: {
      type: String,
      index: true,
    },
    changes: {
      before: Schema.Types.Mixed,
      after: Schema.Types.Mixed,
    },
    metadata: {
      type: Map,
      of: Schema.Types.Mixed,
    },
    ipAddress: String,
    userAgent: String,
    timestamp: {
      type: Date,
      default: Date.now,
      required: true,
      index: true,
    },
  },
  {
    timestamps: false, // We use our own timestamp field
    capped: {
      size: 1024 * 1024 * 100, // 100MB
      max: 1000000, // Max 1 million documents
    },
  }
);

// Compound indexes for common queries
auditLogSchema.index({ userId: 1, timestamp: -1 });
auditLogSchema.index({ resource: 1, resourceId: 1, timestamp: -1 });
auditLogSchema.index({ action: 1, timestamp: -1 });

// Static method to log an action
auditLogSchema.statics.logAction = async function (
  data: Partial<IAuditLog>
): Promise<IAuditLog> {
  return this.create({
    ...data,
    timestamp: new Date(),
  });
};

// Static method to get user activity
auditLogSchema.statics.getUserActivity = function (
  userId: Types.ObjectId,
  limit = 100
) {
  return this.find({ userId })
    .sort({ timestamp: -1 })
    .limit(limit)
    .populate('userId', 'username email');
};

// Static method to get resource history
auditLogSchema.statics.getResourceHistory = function (
  resource: string,
  resourceId: string,
  limit = 50
) {
  return this.find({ resource, resourceId })
    .sort({ timestamp: -1 })
    .limit(limit)
    .populate('userId', 'username email');
};

// Virtual for formatted timestamp
auditLogSchema.virtual('formattedTimestamp').get(function () {
  return this.timestamp.toISOString();
});

export const AuditLog = model<IAuditLog>('AuditLog', auditLogSchema);