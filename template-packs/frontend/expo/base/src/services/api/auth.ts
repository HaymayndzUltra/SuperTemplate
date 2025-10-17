import apiClient from './client';
import { LoginCredentials, RegisterData, AuthResponse, User } from '../../types/auth';

export const authApi = {
  login: (credentials: LoginCredentials) => 
    apiClient.post<AuthResponse>('/auth/login', credentials),

  register: (data: RegisterData) => 
    apiClient.post<AuthResponse>('/auth/register', data),

  logout: () => 
    apiClient.post('/auth/logout'),

  refreshToken: (refreshToken: string) => 
    apiClient.post<AuthResponse>('/auth/refresh', { refreshToken }),

  getMe: () => 
    apiClient.get<User>('/users/me'),

  changePassword: (oldPassword: string, newPassword: string) => 
    apiClient.post('/auth/change-password', { oldPassword, newPassword }),
};