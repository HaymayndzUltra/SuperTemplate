/**
 * Login Page
 * Authentication page for user login
 */
import { LoginForm } from '@/components/auth/LoginForm'

export default function LoginPage() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-gray-50 px-4 py-12 dark:bg-gray-900 sm:px-6 lg:px-8">
      <div className="w-full max-w-md space-y-8">
        <div>
          <h2 className="mt-6 text-center text-3xl font-bold tracking-tight text-gray-900 dark:text-white">
            Sign in to your account
          </h2>
          <p className="mt-2 text-center text-sm text-gray-600 dark:text-gray-400">
            Freelancer Command Center
          </p>
        </div>
        <div className="rounded-lg bg-white px-8 py-8 shadow-md dark:bg-gray-800">
          <LoginForm />
        </div>
      </div>
    </div>
  )
}

