<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
    <div class="container mx-auto px-4 py-16">
      <div class="text-center">
        <h1 class="text-4xl font-bold text-gray-900 mb-4">
          Welcome to {{ appName }}
        </h1>
        <p class="text-xl text-gray-600 mb-8">
          Starter Application
        </p>
        
        <div class="space-x-4">
          <NuxtLink
            v-if="!isAuthenticated"
            to="/auth/login"
            class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Get Started
          </NuxtLink>
          
          <NuxtLink
            v-else
            to="/dashboard"
            class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Go to Dashboard
          </NuxtLink>
        </div>
      </div>

      <div class="mt-16 grid grid-cols-1 md:grid-cols-3 gap-8">
        <FeatureCard
          icon="shield-check"
          title="Secure"
          description="Enterprise-grade security with JWT authentication and role-based access control."
        />
        <FeatureCard
          icon="lightning-bolt"
          title="Fast"
          description="Built with performance in mind using Nuxt 3 and optimized for speed."
        />
        <FeatureCard
          icon="puzzle"
          title="Scalable"
          description="Modular architecture designed to grow with your business needs."
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const { isAuthenticated } = useAuth()
const appName = useRuntimeConfig().public.appName

useHead({
  title: 'Home',
})
</script>

