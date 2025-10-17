'use client';

import { ReactNode } from 'react';

interface ProvidersProps {
  children: ReactNode;
}

export function Providers({ children }: ProvidersProps) {
  // Add providers here as needed (auth, theme, etc.)
  return <>{children}</>;
}