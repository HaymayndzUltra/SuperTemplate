export interface User {
  id: string
  email: string
  fullName: string
  phoneNumber?: string
  avatar?: string
  role: 'user' | 'admin'
  isActive: boolean
  isEmailVerified: boolean
  lastLoginAt?: string
  createdAt: string
  updatedAt: string
}

export interface LoginCredentials {
  email: string
  password: string
}

export interface RegisterData {
  email: string
  password: string
  fullName: string
  phoneNumber?: string
}

export interface AuthTokens {
  accessToken: string
  refreshToken: string
  tokenType: string
  expiresIn: number
}

export interface AuthResponse {
  user: User
  tokens: AuthTokens
}

