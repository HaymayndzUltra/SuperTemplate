# {{PROJECT_NAME}} Frontend

This is a Next.js 14 application using the App Router.

## Getting Started

### Prerequisites
- Node.js 18+ 
- npm or yarn

### Installation

```bash
npm install
```

### Development

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser.

### Building for Production

```bash
npm run build
npm start
```

## Project Structure

```
src/
├── app/            # App Router pages and layouts
├── components/     # Reusable React components
├── hooks/          # Custom React hooks
├── lib/            # Utility functions and API client
├── types/          # TypeScript type definitions
└── styles/         # Global styles and Tailwind config
```

## Features

- **Next.js 14** with App Router
- **TypeScript** for type safety
- **Tailwind CSS** for styling
- **SWR** for data fetching
- **Axios** for API calls
- **React Hook Form** with Zod validation
- **Jest** for testing

## Environment Variables

Copy `.env.example` to `.env.local` and update the values:

```bash
cp .env.example .env.local
```

## Testing

```bash
# Run tests
npm test

# Run tests in watch mode
npm run test:watch

# Generate coverage report
npm run test:coverage
```

## Learn More

- [Next.js Documentation](https://nextjs.org/docs)
- [React Documentation](https://react.dev)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)