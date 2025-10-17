import type { User, RegisterData } from '~/types/auth'

export const useAuth = () => {
  const user = useState<User | null>('auth.user', () => null)
  const token = useCookie('auth-token', {
    httpOnly: true,
    secure: true,
    sameSite: 'lax',
    maxAge: 60 * 60 * 24 * 7, // 7 days
  })
  const refreshToken = useCookie('refresh-token', {
    httpOnly: true,
    secure: true,
    sameSite: 'lax',
    maxAge: 60 * 60 * 24 * 30, // 30 days
  })

  const isAuthenticated = computed(() => !!user.value)

  const login = async (email: string, password: string) => {
    const data = await $fetch<any>('/api/v1/auth/login', {
      baseURL: useRuntimeConfig().public.apiBaseUrl,
      method: 'POST',
      body: { email, password },
    })

    // Store tokens
    token.value = data.tokens.accessToken
    refreshToken.value = data.tokens.refreshToken
    
    // Store user
    user.value = data.user

    // Redirect to dashboard
    await navigateTo('/dashboard')
  }

  const register = async (userData: RegisterData) => {
    const data = await $fetch<any>('/api/v1/auth/register', {
      baseURL: useRuntimeConfig().public.apiBaseUrl,
      method: 'POST',
      body: userData,
    })

    // Store tokens
    token.value = data.tokens.accessToken
    refreshToken.value = data.tokens.refreshToken
    
    // Store user
    user.value = data.user

    // Redirect to dashboard
    await navigateTo('/dashboard')
  }

  const logout = async () => {
    try {
      await $fetch('/api/v1/auth/logout', {
        baseURL: useRuntimeConfig().public.apiBaseUrl,
        method: 'POST',
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      })
    } catch (error) {
      // Continue with logout even if API call fails
    }

    // Clear auth state
    user.value = null
    token.value = null
    refreshToken.value = null

    // Redirect to home
    await navigateTo('/')
  }

  const fetchUser = async () => {
    if (!token.value) return

    try {
      const data = await $fetch<any>('/api/v1/users/me', {
        baseURL: useRuntimeConfig().public.apiBaseUrl,
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      })

      user.value = data
    } catch (error) {
      // Token might be invalid
      user.value = null
      token.value = null
      refreshToken.value = null
    }
  }

  const initAuth = async () => {
    if (token.value && !user.value) {
      await fetchUser()
    }
  }

  return {
    user: readonly(user),
    isAuthenticated,
    login,
    register,
    logout,
    fetchUser,
    initAuth,
  }
}

