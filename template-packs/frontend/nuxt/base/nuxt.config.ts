// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  future: {
    compatibilityVersion: 4,
  },
  srcDir: 'app',
  
  modules: [
    '@nuxtjs/tailwindcss',
    '@pinia/nuxt',
    '@vueuse/nuxt',
  ],

  css: ['~/assets/css/main.css'],

  runtimeConfig: {
    public: {
      apiBaseUrl: process.env.NUXT_PUBLIC_API_BASE_URL || 'http://localhost:8000/api/v1',
      appName: '{{PROJECT_NAME}}',
      appVersion: '1.0.0',
    },
  },

  app: {
    head: {
      title: '{{PROJECT_NAME}}',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: '{{INDUSTRY}} {{PROJECT_TYPE}} application' },
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
      ],
    },
  },

  typescript: {
    strict: true,
    typeCheck: true,
  },

  nitro: {
    compressPublicAssets: true,
  },

  experimental: {
    payloadExtraction: false,
    defaults: {
      // Nuxt 4 returns shallow refs for data by default. Keep defaults but allow deep opt-in per fetch.
      // useAsyncData: { deep: true }
    }
  },

  sourcemap: {
    server: true,
    client: true,
  },

  build: {
    transpile: ['@vuepic/vue-datepicker'],
  },

  vite: {
    optimizeDeps: {
      include: ['vue', 'pinia'],
    },
  },
})