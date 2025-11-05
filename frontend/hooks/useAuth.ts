/**
 * useAuth Hook
 * Custom hook for authentication with loading states and error handling
 */
'use client'

import { useUser } from '@/contexts/UserContext'
import { supabase } from '@/lib/supabase/client'
import { useRouter } from 'next/navigation'
import { useState } from 'react'

export function useAuth() {
  const { user, session, loading, error, signOut } = useUser()
  const router = useRouter()
  const [isLoading, setIsLoading] = useState(false)

  const signIn = async (email: string, password: string) => {
    setIsLoading(true)
    try {
      const { data, error: authError } = await supabase.auth.signInWithPassword({
        email,
        password,
      })

      if (authError) {
        throw authError
      }

      if (data.user) {
        router.push('/')
        router.refresh()
      }

      return { data, error: null }
    } catch (err) {
      return {
        data: null,
        error: err instanceof Error ? err : new Error('Authentication failed'),
      }
    } finally {
      setIsLoading(false)
    }
  }

  const signUp = async (email: string, password: string) => {
    setIsLoading(true)
    try {
      const { data, error: authError } = await supabase.auth.signUp({
        email,
        password,
      })

      if (authError) {
        throw authError
      }

      return { data, error: null }
    } catch (err) {
      return {
        data: null,
        error: err instanceof Error ? err : new Error('Sign up failed'),
      }
    } finally {
      setIsLoading(false)
    }
  }

  const handleSignOut = async () => {
    setIsLoading(true)
    try {
      await signOut()
      router.push('/login')
      router.refresh()
    } catch (err) {
      console.error('Sign out error:', err)
    } finally {
      setIsLoading(false)
    }
  }

  return {
    user,
    session,
    loading: loading || isLoading,
    error,
    isAuthenticated: !!user,
    signIn,
    signUp,
    signOut: handleSignOut,
  }
}

