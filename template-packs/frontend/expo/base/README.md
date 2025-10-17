# {{PROJECT_NAME}} Mobile App

A {{INDUSTRY}} {{PROJECT_TYPE}} mobile application built with React Native and Expo.

## Features

- 📱 **React Native with Expo** - Cross-platform mobile development
- 🔐 **JWT Authentication** - Secure authentication with token refresh
- 🗄️ **Zustand State Management** - Simple and performant state management
- 🧭 **React Navigation** - Native navigation patterns
- 💾 **Secure Storage** - Encrypted local storage for sensitive data
- 🎨 **Custom UI Components** - Consistent design system
- 📡 **API Integration** - Axios with interceptors
- 🔄 **React Query** - Data fetching and caching
- 🧪 **Jest Testing** - Unit and integration tests
- 📦 **EAS Build** - Cloud-based app building

## Prerequisites

- Node.js 18+
- npm or yarn
- Expo CLI (`npm install -g expo-cli`)
- iOS Simulator (Mac only) or Android Emulator
- Expo Go app on your physical device (optional)
- Backend API running

## Quick Start

### 1. Install Dependencies

```bash
npm install
# or
yarn install
```

### 2. Environment Setup

The API URL is configured in `app.config.js`:

```javascript
extra: {
  apiUrl: process.env.EXPO_PUBLIC_API_URL || "http://localhost:8000/api/v1"
}
```

For production builds, set the environment variable:

```bash
export EXPO_PUBLIC_API_URL=https://api.{{PROJECT_NAME}}.com/api/v1
```

### 3. Start Development Server

```bash
# Start Expo development server
npx expo start

# Or with specific platform
npx expo start --ios
npx expo start --android
npx expo start --web
```

### 4. Run on Device/Simulator

- **iOS Simulator**: Press `i` in the terminal
- **Android Emulator**: Press `a` in the terminal
- **Physical Device**: Scan QR code with Expo Go app

## Project Structure

```
src/
├── components/         # Reusable UI components
├── navigation/        # Navigation configuration
│   ├── RootNavigator.tsx
│   ├── AuthNavigator.tsx
│   └── AppNavigator.tsx
├── screens/           # Screen components
│   ├── auth/         # Authentication screens
│   └── app/          # Main app screens
├── services/         # API services
│   └── api/         # API client and endpoints
├── stores/          # Zustand stores
│   └── authStore.ts # Authentication state
├── types/           # TypeScript types
└── utils/           # Utility functions

assets/              # Images, fonts, etc.
├── fonts/          # Custom fonts
├── images/         # App images
└── icons/          # App icons
```

## Development Guide

### Authentication Flow

1. **Secure Token Storage**: Tokens stored in Expo SecureStore
2. **Auto Refresh**: Tokens refreshed automatically on 401 responses
3. **Persistent Login**: User stays logged in across app restarts

### State Management

Using Zustand for global state:

```typescript
import { useAuthStore } from '@/stores/authStore';

function MyComponent() {
  const { user, login, logout } = useAuthStore();
  
  // Use auth state and actions
}
```

### API Calls

Using React Query for data fetching:

```typescript
import { useQuery } from '@tanstack/react-query';
import { userApi } from '@/services/api/users';

function UsersScreen() {
  const { data, isLoading, error } = useQuery({
    queryKey: ['users'],
    queryFn: userApi.getAll,
  });
}
```

### Navigation

Navigate between screens:

```typescript
import { useNavigation } from '@react-navigation/native';

function MyScreen() {
  const navigation = useNavigation();
  
  // Navigate to another screen
  navigation.navigate('Profile');
}
```

### Custom Fonts

Fonts are loaded in `App.tsx`:

```typescript
await Font.loadAsync({
  'Inter-Regular': require('./assets/fonts/Inter-Regular.ttf'),
  'Inter-Medium': require('./assets/fonts/Inter-Medium.ttf'),
  'Inter-Bold': require('./assets/fonts/Inter-Bold.ttf'),
});
```

## Testing

### Run Tests

```bash
# Run all tests
npm test

# Run tests in watch mode
npm test -- --watch

# Run tests with coverage
npm test -- --coverage
```

### Writing Tests

```typescript
import React from 'react';
import { render, fireEvent } from '@testing-library/react-native';
import { LoginScreen } from '@/screens/auth/LoginScreen';

describe('LoginScreen', () => {
  it('should render correctly', () => {
    const { getByPlaceholderText } = render(<LoginScreen />);
    
    expect(getByPlaceholderText('Enter your email')).toBeTruthy();
    expect(getByPlaceholderText('Enter your password')).toBeTruthy();
  });
});
```

## Building for Production

### Using EAS Build

1. **Install EAS CLI**
   ```bash
   npm install -g eas-cli
   ```

2. **Configure EAS**
   ```bash
   eas build:configure
   ```

3. **Build for iOS**
   ```bash
   eas build --platform ios
   ```

4. **Build for Android**
   ```bash
   eas build --platform android
   ```

### Local Builds

#### iOS (Mac only)

```bash
npx expo run:ios --configuration Release
```

#### Android

```bash
npx expo run:android --variant release
```

## Deployment

### App Store (iOS)

1. Build with EAS: `eas build --platform ios`
2. Submit with EAS: `eas submit --platform ios`
3. Or download IPA and upload via Transporter

### Google Play (Android)

1. Build with EAS: `eas build --platform android`
2. Submit with EAS: `eas submit --platform android`
3. Or download AAB and upload via Play Console

## Performance Optimization

1. **Image Optimization**
   - Use appropriate image sizes
   - Implement lazy loading
   - Cache images with `expo-image`

2. **List Optimization**
   - Use `FlatList` for long lists
   - Implement `getItemLayout` when possible
   - Use `keyExtractor` for better performance

3. **Navigation**
   - Use lazy loading for screens
   - Minimize deep navigation stacks

4. **State Management**
   - Use React.memo for expensive components
   - Optimize Zustand subscriptions

## Troubleshooting

### Common Issues

1. **Metro bundler issues**
   ```bash
   npx expo start -c  # Clear cache
   ```

2. **iOS build errors**
   ```bash
   cd ios && pod install
   ```

3. **Android build errors**
   ```bash
   cd android && ./gradlew clean
   ```

4. **Module resolution errors**
   - Check babel.config.js aliases
   - Restart Metro bundler

5. **API connection issues**
   - Check API URL in app.config.js
   - Ensure backend is running
   - Check network permissions

## Security Best Practices

1. **Secure Storage**: Use SecureStore for sensitive data
2. **API Keys**: Never commit API keys, use environment variables
3. **Certificate Pinning**: Implement for production
4. **Code Obfuscation**: Enable for release builds
5. **Biometric Auth**: Implement where appropriate

## Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Write/update tests
5. Submit pull request

### Code Style

- Follow React Native best practices
- Use TypeScript strictly
- Maintain consistent styling
- Write meaningful commit messages

## License

Copyright © {{YEAR}} {{PROJECT_NAME}}. All rights reserved.