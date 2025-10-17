# {{PROJECT_NAME}} Angular Frontend

A {{INDUSTRY}} {{PROJECT_TYPE}} frontend built with Angular 20.2, TypeScript, and Tailwind CSS.

## Features

- 🅰️ **Angular 20.2** - Modern web application framework
- 🔒 **Standalone Components** - Simplified component architecture
- 🔐 **JWT Authentication** - Secure authentication with interceptors
- 🛡️ **Route Guards** - Protected routes with auth guards
- 💾 **State Management** - Signals-based reactive state
- 🎨 **Tailwind CSS** - Utility-first CSS framework
- 📱 **Responsive Design** - Mobile-first approach
- 🧪 **Testing** - Unit tests with Jasmine and Karma
- 📦 **Lazy Loading** - Optimized bundle sizes
- ♿ **Accessibility** - WCAG compliant

## Prerequisites

- Node.js 20.19+
- npm 9+
- Angular CLI 20.2+
- Backend API running (see backend README)

## Quick Start

### 1. Install Angular CLI

```bash
npm install -g @angular/cli@20.2
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Environment Setup

The environment files are pre-configured:

- `src/environments/environment.ts` - Development
- `src/environments/environment.production.ts` - Production

Update the `apiUrl` if your backend runs on a different port.

### 4. Run Development Server

```bash
ng serve
# or
npm start
```

Navigate to <http://localhost:4200/>

## Project Structure

```text
src/
├── app/
│   ├── core/                # Core functionality
│   │   ├── guards/         # Route guards
│   │   ├── interceptors/   # HTTP interceptors
│   │   ├── models/         # Data models
│   │   └── services/       # Singleton services
│   ├── features/           # Feature modules
│   │   ├── auth/          # Authentication
│   │   ├── dashboard/     # Dashboard
│   │   ├── home/          # Home page
│   │   └── not-found/     # 404 page
│   ├── shared/            # Shared components
│   ├── app.component.ts   # Root component
│   ├── app.config.ts      # App configuration
│   └── app.routes.ts      # Route definitions
├── environments/          # Environment configs
├── assets/               # Static assets
├── styles.scss           # Global styles
└── index.html           # Main HTML file
```

## Available Scripts

```bash
# Development server
ng serve

# Build for production
ng build

# Run unit tests
ng test

# Run linting
ng lint

# Run e2e tests
ng e2e

# Generate component
ng generate component features/my-component

# Generate service
ng generate service core/services/my-service

# Generate guard
ng generate guard core/guards/my-guard
```

## Development Guide

### Authentication

The app uses JWT authentication with automatic token handling:

```typescript
// Login
this.authService.login({ email, password }).subscribe({
  next: () => this.router.navigate(['/dashboard']),
  error: (error) => console.error(error)
});

// Check authentication
if (this.authService.isAuthenticated()) {
  // User is logged in
}

// Get current user
const user = this.authService.user();
```

### HTTP Requests

All HTTP requests automatically include authentication headers:

```typescript
@Injectable()
export class UserService {
  constructor(private http: HttpClient) {}

  getUsers() {
    return this.http.get<User[]>(`${environment.apiUrl}/users`);
  }
}
```

### Route Guards

Protect routes with guards:

```typescript
export const routes: Routes = [
  {
    path: 'dashboard',
    canActivate: [authGuard],
    loadComponent: () => import('./features/dashboard/dashboard.component')
  }
];
```

### Reactive State with Signals

Using Angular signals for state management:

```typescript
export class AuthService {
  private currentUser = signal<User | null>(null);
  
  get user() {
    return this.currentUser.asReadonly();
  }
}
```

### Standalone Components

All components are standalone:

```typescript
@Component({
  selector: 'app-example',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  template: `...`
})
export class ExampleComponent {}
```

## Testing

### Unit Tests

```bash
# Run tests
ng test

# Run tests with coverage
ng test --code-coverage

# Run tests in headless mode
ng test --browsers=ChromeHeadless
```

### Writing Tests

```typescript
describe('AuthService', () => {
  let service: AuthService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [AuthService]
    });
    service = TestBed.inject(AuthService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it('should authenticate user', () => {
    const mockResponse = { user: {}, tokens: {} };
    
    service.login({ email: 'test@example.com', password: 'password' })
      .subscribe(response => {
        expect(response).toEqual(mockResponse);
      });

    const req = httpMock.expectOne(`${environment.apiUrl}/auth/login`);
    expect(req.request.method).toBe('POST');
    req.flush(mockResponse);
  });
});
```

## Building for Production

### Build

```bash
# Production build
ng build --configuration production

# Build with stats
ng build --stats-json
```

### Analyze Bundle

```bash
# Install webpack-bundle-analyzer
npm install -g webpack-bundle-analyzer

# Analyze bundle
webpack-bundle-analyzer dist/{{PROJECT_NAME}}/stats.json
```

### Optimization Tips

1. **Lazy Loading**: All feature modules are lazy loaded
2. **Tree Shaking**: Unused code is automatically removed
3. **Compression**: Enable gzip/brotli on server
4. **Caching**: Configure proper cache headers
5. **CDN**: Serve static assets from CDN

## Deployment

### Docker

```dockerfile
# Build stage
FROM node:18-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM nginx:alpine
COPY --from=build /app/dist/{{PROJECT_NAME}} /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

### Nginx Configuration

```nginx
server {
    listen 80;
    server_name localhost;
    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /api {
        proxy_pass http://backend:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
}
```

## Troubleshooting

### Common Issues

1. **CORS Errors**
   - Check backend CORS configuration
   - Ensure API URL is correct in environment

2. **Build Errors**
   - Clear cache: `rm -rf .angular node_modules`
   - Reinstall: `npm install`
   - Check TypeScript errors: `ng build`

3. **Authentication Issues**
   - Check token storage in localStorage
   - Verify API endpoints
   - Check interceptor configuration

4. **Routing Issues**
   - Ensure base href is correct
   - Check server rewrite rules
   - Verify lazy loading paths

5. **Performance Issues**
   - Check bundle size: `ng build --stats-json`
   - Enable production mode
   - Implement OnPush change detection

## VS Code Extensions

Recommended extensions:

- Angular Language Service
- Angular Snippets
- Tailwind CSS IntelliSense
- ESLint
- Prettier

## Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Write/update tests
5. Submit pull request

### Code Style

- Follow Angular style guide
- Use TypeScript strict mode
- Implement proper error handling
- Write meaningful commit messages
- Add JSDoc comments

## License

Copyright © {{YEAR}} {{PROJECT_NAME}}. All rights reserved.