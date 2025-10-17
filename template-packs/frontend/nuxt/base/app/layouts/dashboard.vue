<template>
  <div class="min-h-screen bg-gray-100">
    <!-- Navigation -->
    <nav class="bg-white shadow">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
          <div class="flex">
            <div class="flex-shrink-0 flex items-center">
              <NuxtLink to="/dashboard" class="text-xl font-bold text-indigo-600">
                {{ appName }}
              </NuxtLink>
            </div>
          </div>
          
          <div class="flex items-center space-x-4">
            <NotificationBell />
            <UserDropdown />
          </div>
        </div>
      </div>
    </nav>

    <div class="flex">
      <!-- Sidebar -->
      <aside class="w-64 bg-white shadow-sm min-h-screen">
        <nav class="mt-5 px-2">
          <NuxtLink
            to="/dashboard"
            class="group flex items-center px-2 py-2 text-base font-medium rounded-md text-gray-600 hover:bg-gray-50 hover:text-gray-900"
          >
            <Icon name="home" class="mr-4 h-6 w-6" />
            Dashboard
          </NuxtLink>
          <NuxtLink
            to="/dashboard/users"
            class="mt-1 group flex items-center px-2 py-2 text-base font-medium rounded-md text-gray-600 hover:bg-gray-50 hover:text-gray-900"
          >
            <Icon name="users" class="mr-4 h-6 w-6" />
            Users
          </NuxtLink>
          <NuxtLink
            to="/dashboard/settings"
            class="mt-1 group flex items-center px-2 py-2 text-base font-medium rounded-md text-gray-600 hover:bg-gray-50 hover:text-gray-900"
          >
            <Icon name="cog" class="mr-4 h-6 w-6" />
            Settings
          </NuxtLink>
        </nav>
      </aside>

      <!-- Main Content -->
      <main class="flex-1 p-6">
        <slot />
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
const appName = useRuntimeConfig().public.appName
</script>

