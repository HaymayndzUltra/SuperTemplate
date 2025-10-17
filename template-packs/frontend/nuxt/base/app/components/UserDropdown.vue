<template>
  <div class="relative">
    <button
      @click="isOpen = !isOpen"
      class="flex items-center text-sm rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
    >
      <img
        class="h-8 w-8 rounded-full"
        :src="user?.avatar || `https://ui-avatars.com/api/?name=${user?.fullName}`"
        :alt="user?.fullName"
      />
    </button>

    <transition
      enter-active-class="transition ease-out duration-100"
      enter-from-class="transform opacity-0 scale-95"
      enter-to-class="transform opacity-100 scale-100"
      leave-active-class="transition ease-in duration-75"
      leave-from-class="transform opacity-100 scale-100"
      leave-to-class="transform opacity-0 scale-95"
    >
      <div
        v-if="isOpen"
        v-click-outside="() => isOpen = false"
        class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none"
      >
        <div class="py-1">
          <div class="px-4 py-2 text-sm text-gray-700 border-b">
            {{ user?.email }}
          </div>
          
          <NuxtLink
            to="/dashboard/profile"
            class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
            @click="isOpen = false"
          >
            Your Profile
          </NuxtLink>
          
          <NuxtLink
            to="/dashboard/settings"
            class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
            @click="isOpen = false"
          >
            Settings
          </NuxtLink>
          
          <hr class="my-1" />
          
          <button
            @click="handleLogout"
            class="block w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
          >
            Sign out
          </button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup lang="ts">
const { user, logout } = useAuth()
const isOpen = ref(false)

const handleLogout = async () => {
  isOpen.value = false
  await logout()
}
</script>

