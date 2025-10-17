# {{PROJECT_NAME}} Nuxt Frontend

A {{INDUSTRY}} {{PROJECT_TYPE}} frontend built with Nuxt 4, Vue 3, and Tailwind CSS.

## Features

- ⚡ **Nuxt 4** - The Intuitive Vue Framework
- 🎨 **Tailwind CSS** - Utility-first CSS framework
- 🔐 **Authentication** - JWT-based auth with refresh tokens
- 📦 **Pinia** - State management
- 🧭 **Vue Router** - File-based routing
- 🎯 **TypeScript** - Type safety throughout
- 🧪 **Vitest** - Unit testing framework
- 🎭 **VueUse** - Collection of Vue composition utilities
- 📱 **Responsive** - Mobile-first design
- ♿ **Accessible** - WCAG compliant components

## Prerequisites

- Node.js 20+
- npm or pnpm
- Backend API running (see backend README)

## Quick Start

### 1. Install Dependencies

```bash
# Using npm
npm install

# Using pnpm
pnpm install
```

### 2. Environment Setup

```bash
# Copy environment variables
cp .env.example .env

# Edit .env with your configuration
# Set NUXT_PUBLIC_API_BASE_URL to your backend URL
```

### 3. Run Development Server

```bash
npm run dev
```

The application will be available at http://localhost:3000

## Project Structure

```
.
├── assets/             # CSS and static assets
├── components/         # Vue components
├── composables/        # Vue composables
├── layouts/            # Nuxt layouts
├── middleware/         # Route middleware
├── pages/              # Application pages
├── plugins/            # Nuxt plugins
├── public/             # Static files
├── server/             # Server API routes
├── stores/             # Pinia stores
├── types/              # TypeScript types
├── utils/              # Utility functions
├── app.vue             # Root component
├── nuxt.config.ts      # Nuxt configuration
├── tailwind.config.js  # Tailwind configuration
└── tsconfig.json       # TypeScript configuration
```

## Available Scripts

```bash
# Development server with hot reload
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Generate static site
npm run generate

# Run linter
npm run lint

# Fix linting issues
npm run lint:fix

# Format code
npm run format

# Run tests
npm run test

# Run tests with UI
npm run test:ui

# Generate test coverage
npm run test:coverage

# Type checking
npm run typecheck
```

## Development Guide

### Authentication Flow

1. **Login/Register**: Users authenticate via `/auth/login` or `/auth/register`
2. **Token Storage**: JWT tokens stored in secure httpOnly cookies
3. **Auto Refresh**: Tokens automatically refresh before expiration
4. **Protected Routes**: Use `auth` middleware for protected pages

### State Management

Using Pinia for state management:

```typescript
// stores/user.ts
export const useUserStore = defineStore('user', () => {
  const users = ref<User[]>([])
  
  const fetchUsers = async () => {
    const { data } = await useApi()('/users')
    users.value = data
  }
  
  return { users, fetchUsers }
})
```

### API Integration

Use the `useApi` composable for API calls:

```typescript
const api = useApi()

// GET request
const { data } = await api('/users')

// POST request
const { data } = await api('/users', {
  method: 'POST',
  body: { name: 'John Doe' }
})
```

### Adding New Pages

Create a new file in the `pages/` directory:

```vue
<!-- pages/about.vue -->
<template>
  <div>
    <h1>About Page</h1>
  </div>
</template>

<script setup lang="ts">
// Page meta
definePageMeta({
  title: 'About',
  layout: 'default',
  middleware: 'auth', // Optional: require authentication
})
</script>
```

### Component Development

Create reusable components:

```vue
<!-- components/Button.vue -->
<template>
  <button
    :class="[baseClasses, variantClasses[variant]]"
    :disabled="disabled"
    @click="$emit('click')"
  >
    <slot />
  </button>
</template>

<script setup lang="ts">
interface Props {
  variant?: 'primary' | 'secondary'
  disabled?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  variant: 'primary',
  disabled: false,
})

const emit = defineEmits<{
  click: []
}>()

const baseClasses = 'px-4 py-2 rounded-md font-medium'
const variantClasses = {
  primary: 'bg-indigo-600 text-white hover:bg-indigo-700',
  secondary: 'bg-gray-200 text-gray-900 hover:bg-gray-300',
}
</script>
```

## Testing

### Unit Tests

```bash
# Run all tests
npm run test

# Run tests in watch mode
npm run test:watch

# Generate coverage report
npm run test:coverage
```

### Writing Tests

```typescript
// components/Button.test.ts
import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import Button from './Button.vue'

describe('Button', () => {
  it('renders properly', () => {
    const wrapper = mount(Button, {
      slots: {
        default: 'Click me'
      }
    })
    expect(wrapper.text()).toContain('Click me')
  })
})
```

## Production Deployment

### Build for Production

```bash
# Build application
npm run build

# Preview build locally
npm run preview
```

### Environment Variables

Set production environment variables:

```env
NUXT_PUBLIC_API_BASE_URL=https://api.{{PROJECT_NAME}}.com/api/v1
NODE_ENV=production
```

### Deployment Options

#### Vercel

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

#### Netlify

1. Connect GitHub repository
2. Set build command: `npm run build`
3. Set publish directory: `dist`

#### Docker

```dockerfile
FROM node:18-alpine as builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/.output .output
EXPOSE 3000
CMD ["node", ".output/server/index.mjs"]
```

## Performance Optimization

### Image Optimization

Use Nuxt Image for automatic optimization:

```vue
<NuxtImg
  src="/hero.jpg"
  alt="Hero image"
  width="1200"
  height="600"
  loading="lazy"
/>
```

### Code Splitting

Nuxt automatically code-splits by route. For component-level splitting:

```typescript
const HeavyComponent = defineAsyncComponent(() =>
  import('~/components/HeavyComponent.vue')
)
```

### Caching Strategies

Configure caching in `nuxt.config.ts`:

```typescript
export default defineNuxtConfig({
  routeRules: {
    '/': { prerender: true },
    '/api/*': { cors: true, headers: { 'cache-control': 's-maxage=60' } },
  }
})
```

## Troubleshooting

### Common Issues

1. **API Connection Error**
   - Check `NUXT_PUBLIC_API_BASE_URL` in `.env`
   - Ensure backend is running
   - Check CORS configuration

2. **Build Errors**
   - Clear cache: `rm -rf .nuxt node_modules`
   - Reinstall dependencies: `npm install`
   - Check for TypeScript errors: `npm run typecheck`

3. **Authentication Issues**
   - Check cookie settings in production
   - Verify JWT token format
   - Check API response format

4. **Styling Issues**
   - Ensure Tailwind classes are not purged
   - Check for CSS conflicts
   - Verify PostCSS configuration

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

### Code Style

- Use Vue 3 Composition API
- Follow TypeScript best practices
- Use Tailwind utility classes
- Write meaningful component names
- Add appropriate TypeScript types

## License

Copyright © {{YEAR}} {{PROJECT_NAME}}. All rights reserved.