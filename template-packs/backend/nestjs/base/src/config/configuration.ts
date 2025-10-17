export default () => ({
  // Application
  port: parseInt(process.env.PORT, 10) || 8000,
  appName: process.env.APP_NAME || '{{PROJECT_NAME}}',
  appVersion: process.env.APP_VERSION || '1.0.0',
  nodeEnv: process.env.NODE_ENV || 'development',
  
  // Database
  database: {
    type: process.env.DB_TYPE || 'postgres',
    host: process.env.DB_HOST || 'localhost',
    port: parseInt(process.env.DB_PORT, 10) || 5432,
    username: process.env.DB_USERNAME || 'postgres',
    password: process.env.DB_PASSWORD || 'postgres',
    database: process.env.DB_DATABASE || '{{PROJECT_NAME}}_db',
  },
  
  // JWT
  jwt: {
    secret: process.env.JWT_SECRET || 'secret',
    expiresIn: parseInt(process.env.JWT_EXPIRATION, 10) || 3600,
    refreshSecret: process.env.JWT_REFRESH_SECRET || 'refresh-secret',
    refreshExpiresIn: parseInt(process.env.JWT_REFRESH_EXPIRATION, 10) || 604800,
  },
  
  // Redis
  redis: {
    host: process.env.REDIS_HOST || 'localhost',
    port: parseInt(process.env.REDIS_PORT, 10) || 6379,
    db: parseInt(process.env.REDIS_DB, 10) || 0,
  },
  
  // Rate limiting
  throttle: {
    ttl: parseInt(process.env.THROTTLE_TTL, 10) || 60,
    limit: parseInt(process.env.THROTTLE_LIMIT, 10) || 10,
  },
  
  // Email
  mail: {
    host: process.env.MAIL_HOST,
    port: parseInt(process.env.MAIL_PORT, 10) || 587,
    user: process.env.MAIL_USER,
    password: process.env.MAIL_PASSWORD,
    from: process.env.MAIL_FROM || 'noreply@{{PROJECT_NAME}}.com',
  },
  
  // Logging
  logLevel: process.env.LOG_LEVEL || 'debug',
  
  // Sentry
  sentryDsn: process.env.SENTRY_DSN,
});