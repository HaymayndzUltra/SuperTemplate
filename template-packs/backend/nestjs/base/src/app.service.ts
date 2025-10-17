import { Injectable } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';

@Injectable()
export class AppService {
  constructor(private configService: ConfigService) {}

  getInfo() {
    return {
      name: this.configService.get('APP_NAME'),
      version: this.configService.get('APP_VERSION'),
      description: '{{INDUSTRY}} {{PROJECT_TYPE}} API',
      environment: this.configService.get('NODE_ENV'),
      documentation: '/api/docs',
      health: '/health',
    };
  }
}