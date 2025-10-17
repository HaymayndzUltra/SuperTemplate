# MongoDB Database Template

This template provides a production-ready MongoDB setup with Docker Compose, initialization scripts, and sample schemas.

## Features

- **MongoDB 7.0** with authentication
- **Mongo Express** web interface for database management
- **Health checks** and automatic restart
- **Data persistence** with Docker volumes
- **Initialization scripts** with sample data
- **Performance indexes** for common queries
- **Backup/restore scripts** included

## Quick Start

1. **Start the database:**
   ```bash
   docker-compose up -d
   ```

2. **Access MongoDB:**
   - **Connection String**: `mongodb://appuser:apppassword@localhost:27017/appdb`
   - **Mongo Express UI**: http://localhost:8081 (admin/admin123)

3. **Stop the database:**
   ```bash
   docker-compose down
   ```

## Environment Variables

Create a `.env` file in the same directory:

```env
# Database Configuration
DB_NAME=appdb
MONGO_APP_USER=appuser
MONGO_APP_PASSWORD=apppassword

# Admin Configuration (for initial setup)
MONGO_INITDB_ROOT_USERNAME=admin
MONGO_INITDB_ROOT_PASSWORD=password123
```

## Connection Strings

### For Applications
```bash
# Local development
mongodb://appuser:apppassword@localhost:27017/appdb

# Production (replace with your domain)
mongodb://appuser:apppassword@your-mongodb-host:27017/appdb
```

### For MongoDB Compass
```
mongodb://appuser:apppassword@localhost:27017/appdb
```

## Database Schema

### Users Collection
```javascript
{
  _id: ObjectId,
  email: String (unique, required),
  name: String (required),
  role: String (enum: ['user', 'admin', 'moderator']),
  isActive: Boolean,
  createdAt: Date (required),
  updatedAt: Date
}
```

### Sessions Collection
```javascript
{
  _id: ObjectId,
  userId: ObjectId (required),
  token: String (unique, required),
  expiresAt: Date (required),
  createdAt: Date (required),
  isActive: Boolean
}
```

## Sample Code

### Node.js with Mongoose
```javascript
const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://appuser:apppassword@localhost:27017/appdb');

// Define User schema
const userSchema = new mongoose.Schema({
  email: { type: String, required: true, unique: true },
  name: { type: String, required: true },
  role: { type: String, enum: ['user', 'admin', 'moderator'], default: 'user' },
  isActive: { type: Boolean, default: true },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

const User = mongoose.model('User', userSchema);

// Create a new user
const user = new User({
  email: 'newuser@example.com',
  name: 'New User',
  role: 'user'
});

await user.save();
```

### Python with PyMongo
```python
from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient('mongodb://appuser:apppassword@localhost:27017/appdb')
db = client.appdb

# Create a new user
user = {
    'email': 'newuser@example.com',
    'name': 'New User',
    'role': 'user',
    'isActive': True,
    'createdAt': datetime.utcnow(),
    'updatedAt': datetime.utcnow()
}

result = db.users.insert_one(user)
print(f"Created user with ID: {result.inserted_id}")
```

## Backup and Restore

### Backup
```bash
# Create backup directory
mkdir -p backup

# Backup database
docker exec mongodb mongodump --out /backup --db appdb

# Copy backup to host
docker cp mongodb:/backup ./backup/
```

### Restore
```bash
# Copy backup to container
docker cp ./backup mongodb:/backup

# Restore database
docker exec mongodb mongorestore /backup/appdb
```

## Production Considerations

1. **Security:**
   - Change default passwords
   - Use strong authentication
   - Enable SSL/TLS
   - Restrict network access

2. **Performance:**
   - Monitor query performance
   - Add appropriate indexes
   - Consider sharding for large datasets

3. **Backup:**
   - Set up automated backups
   - Test restore procedures
   - Store backups securely

4. **Monitoring:**
   - Monitor memory usage
   - Track query performance
   - Set up alerts

## Troubleshooting

### Common Issues

1. **Connection refused:**
   - Check if MongoDB container is running: `docker ps`
   - Verify port 27017 is not in use: `netstat -tulpn | grep 27017`

2. **Authentication failed:**
   - Verify credentials in `.env` file
   - Check if initialization script ran successfully

3. **Mongo Express not accessible:**
   - Check if port 8081 is available
   - Verify MongoDB health check passed

### Logs
```bash
# View MongoDB logs
docker logs mongodb

# View Mongo Express logs
docker logs mongo-express

# Follow logs in real-time
docker logs -f mongodb
```

## Health Check

The MongoDB container includes a health check that verifies the database is responding to queries:

```bash
# Check container health
docker ps

# Manual health check
docker exec mongodb mongosh --eval "db.adminCommand('ping')"
```

## Support

For issues and questions:
1. Check the troubleshooting section above
2. Review MongoDB documentation
3. Check container logs for error details