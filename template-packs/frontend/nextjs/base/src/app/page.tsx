import Link from 'next/link';

export default function HomePage() {
  const APP_NAME = process.env.NEXT_PUBLIC_APP_NAME || '{{PROJECT_NAME}}';
  const INDUSTRY = process.env.NEXT_PUBLIC_INDUSTRY || '{{INDUSTRY}}';
  const PROJECT_TYPE = process.env.NEXT_PUBLIC_PROJECT_TYPE || '{{PROJECT_TYPE}}';

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="text-center">
        <h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl">
          Welcome to {APP_NAME}
        </h1>
        <p className="mt-6 text-lg leading-8 text-gray-600">
          Your {INDUSTRY} {PROJECT_TYPE} solution.
        </p>
        <div className="mt-10 flex items-center justify-center gap-x-6">
          <Link
            href="/dashboard"
            className="rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Get started
          </Link>
          <Link href="/docs" className="text-sm font-semibold leading-6 text-gray-900">
            Learn more <span aria-hidden="true">→</span>
          </Link>
        </div>
      </div>
    </div>
  );
}