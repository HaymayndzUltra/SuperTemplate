import { create } from 'zustand';
import * as SecureStore from 'expo-secure-store';
import { authApi } from '../services/api/auth';
import { User } from '../types/auth';

interface AuthState {
  user: User | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  token: string | null;
  refreshToken: string | null;
  
  // Actions
  login: (email: string, password: string) => Promise<void>;
  register: (data: { email: string; password: string; fullName: string }) => Promise<void>;
  logout: () => Promise<void>;
  initAuth: () => Promise<void>;
  setUser: (user: User | null) => void;
  setTokens: (accessToken: string, refreshToken: string) => Promise<void>;
  clearAuth: () => Promise<void>;
}

const TOKEN_KEY = 'auth_token';
const REFRESH_TOKEN_KEY = 'refresh_token';

export const useAuthStore = create<AuthState>((set, get) => ({
  user: null,
  isAuthenticated: false,
  isLoading: false,
  token: null,
  refreshToken: null,

  login: async (email: string, password: string) => {
    set({ isLoading: true });
    try {
      const response = await authApi.login({ email, password });
      const { user, tokens } = response.data;
      
      await get().setTokens(tokens.accessToken, tokens.refreshToken);
      set({ user, isAuthenticated: true });
    } catch (error) {
      await get().clearAuth();
      throw error;
    } finally {
      set({ isLoading: false });
    }
  },

  register: async (data) => {
    set({ isLoading: true });
    try {
      const response = await authApi.register(data);
      const { user, tokens } = response.data;
      
      await get().setTokens(tokens.accessToken, tokens.refreshToken);
      set({ user, isAuthenticated: true });
    } catch (error) {
      await get().clearAuth();
      throw error;
    } finally {
      set({ isLoading: false });
    }
  },

  logout: async () => {
    try {
      await authApi.logout();
    } catch (error) {
      console.error('Logout error:', error);
    } finally {
      await get().clearAuth();
    }
  },

  initAuth: async () => {
    try {
      const token = await SecureStore.getItemAsync(TOKEN_KEY);
      const refreshToken = await SecureStore.getItemAsync(REFRESH_TOKEN_KEY);
      
      if (token && refreshToken) {
        set({ token, refreshToken });
        
        // Fetch current user
        const response = await authApi.getMe();
        set({ user: response.data, isAuthenticated: true });
      }
    } catch (error) {
      console.error('Auth initialization error:', error);
      await get().clearAuth();
    }
  },

  setUser: (user) => {
    set({ user, isAuthenticated: !!user });
  },

  setTokens: async (accessToken, refreshToken) => {
    await SecureStore.setItemAsync(TOKEN_KEY, accessToken);
    await SecureStore.setItemAsync(REFRESH_TOKEN_KEY, refreshToken);
    set({ token: accessToken, refreshToken });
  },

  clearAuth: async () => {
    await SecureStore.deleteItemAsync(TOKEN_KEY);
    await SecureStore.deleteItemAsync(REFRESH_TOKEN_KEY);
    set({ user: null, isAuthenticated: false, token: null, refreshToken: null });
  },
}));