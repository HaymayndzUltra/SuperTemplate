<template>
  <div class="relative">
    <button
      @click="isOpen = !isOpen"
      class="p-1 rounded-full text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
    >
      <span class="sr-only">View notifications</span>
      <Icon name="bell" class="h-6 w-6" />
      <span
        v-if="unreadCount > 0"
        class="absolute top-0 right-0 block h-2 w-2 rounded-full bg-red-400 ring-2 ring-white"
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
        class="origin-top-right absolute right-0 mt-2 w-80 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none"
      >
        <div class="py-1">
          <div class="px-4 py-2 text-sm font-medium text-gray-900 border-b">
            Notifications
          </div>
          
          <div v-if="notifications.length === 0" class="px-4 py-8 text-center text-gray-500">
            No new notifications
          </div>
          
          <div v-else class="max-h-96 overflow-y-auto">
            <div
              v-for="notification in notifications"
              :key="notification.id"
              class="px-4 py-3 hover:bg-gray-50 cursor-pointer"
              :class="{ 'bg-blue-50': !notification.read }"
              @click="markAsRead(notification.id)"
            >
              <p class="text-sm font-medium text-gray-900">
                {{ notification.title }}
              </p>
              <p class="text-sm text-gray-500">
                {{ notification.message }}
              </p>
              <p class="text-xs text-gray-400 mt-1">
                {{ formatTime(notification.createdAt) }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup lang="ts">
const isOpen = ref(false)

// Mock notifications - replace with real data
const notifications = ref([
  {
    id: '1',
    title: 'New user registered',
    message: 'A new user has signed up for your service',
    read: false,
    createdAt: new Date(Date.now() - 1000 * 60 * 5),
  },
])

const unreadCount = computed(() => 
  notifications.value.filter(n => !n.read).length
)

const markAsRead = (id: string) => {
  const notification = notifications.value.find(n => n.id === id)
  if (notification) {
    notification.read = true
  }
}

const formatTime = (date: Date) => {
  const now = new Date()
  const diff = now.getTime() - date.getTime()
  const minutes = Math.floor(diff / 60000)
  
  if (minutes < 1) return 'Just now'
  if (minutes < 60) return `${minutes}m ago`
  if (minutes < 1440) return `${Math.floor(minutes / 60)}h ago`
  return `${Math.floor(minutes / 1440)}d ago`
}
</script>

