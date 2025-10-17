import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getInfo() {
    return {
      name: process.env.APP_NAME || '{{PROJECT_NAME}}',
      version: process.env.APP_VERSION || '0.0.1',
      description: '{{INDUSTRY}} {{PROJECT_TYPE}} API (Prisma)',
      environment: process.env.NODE_ENV || 'development',
      documentation: '/api/docs',
      health: '/health',
    };
  }
}
