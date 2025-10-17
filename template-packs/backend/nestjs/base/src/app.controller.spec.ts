import { Test, TestingModule } from '@nestjs/testing';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { ConfigService } from '@nestjs/config';

describe('AppController', () => {
  let appController: AppController;

  beforeEach(async () => {
    const app: TestingModule = await Test.createTestingModule({
      controllers: [AppController],
      providers: [
        AppService,
        {
          provide: ConfigService,
          useValue: {
            get: jest.fn((key: string) => {
              const config = {
                APP_NAME: 'TestApp',
                APP_VERSION: '1.0.0',
                NODE_ENV: 'test',
              };
              return config[key];
            }),
          },
        },
      ],
    }).compile();

    appController = app.get<AppController>(AppController);
  });

  describe('root', () => {
    it('should return app info', () => {
      const result = appController.getInfo();
      expect(result).toHaveProperty('name', 'TestApp');
      expect(result).toHaveProperty('version', '1.0.0');
      expect(result).toHaveProperty('environment', 'test');
    });
  });
});