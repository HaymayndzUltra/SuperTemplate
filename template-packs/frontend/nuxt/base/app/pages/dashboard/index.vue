<template>
  <div>
    <div class="mb-8">
      <h1 class="text-2xl font-semibold text-gray-900">Dashboard</h1>
      <p class="mt-1 text-sm text-gray-600">
        Welcome back, {{ user?.fullName || user?.email }}!
      </p>
    </div>

    <!-- Stats -->
    <div class="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
      <StatsCard
        title="Total Users"
        :value="stats.totalUsers"
        icon="users"
        trend="+12%"
        trendUp
      />
      <StatsCard
        title="Active Sessions"
        :value="stats.activeSessions"
        icon="status-online"
        trend="+5%"
        trendUp
      />
      <StatsCard
        title="API Calls"
        :value="stats.apiCalls"
        icon="server"
        trend="-2%"
        :trendUp="false"
      />
      <StatsCard
        title="System Health"
        value="98.5%"
        icon="heart"
        trend="+0.5%"
        trendUp
      />
    </div>

    <!-- Recent Activity -->
    <div class="mt-8">
      <h2 class="text-lg font-medium text-gray-900 mb-4">Recent Activity</h2>
      <div class="bg-white shadow overflow-hidden sm:rounded-md">
        <ul class="divide-y divide-gray-200">
          <li v-for="activity in recentActivity" :key="activity.id" class="px-6 py-4">
            <div class="flex items-center justify-between">
              <div class="flex items-center">
                <div class="flex-shrink-0">
                  <Icon :name="activity.icon" class="h-6 w-6 text-gray-400" />
                </div>
                <div class="ml-4">
                  <p class="text-sm font-medium text-gray-900">
                    {{ activity.title }}
                  </p>
                  <p class="text-sm text-gray-500">
                    {{ activity.description }}
                  </p>
                </div>
              </div>
              <div class="text-sm text-gray-500">
                {{ formatRelativeTime(activity.timestamp) }}
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'dashboard',
  middleware: 'auth',
})

const { user } = useAuth()

// Mock data - replace with API calls
const stats = ref({
  totalUsers: 1234,
  activeSessions: 89,
  apiCalls: '45.2k',
})

const recentActivity = ref([
  {
    id: 1,
    icon: 'user-add',
    title: 'New user registered',
    description: 'john.doe@example.com joined the platform',
    timestamp: new Date(Date.now() - 1000 * 60 * 5), // 5 minutes ago
  },
  {
    id: 2,
    icon: 'shield-check',
    title: 'Security scan completed',
    description: 'All systems passed security checks',
    timestamp: new Date(Date.now() - 1000 * 60 * 30), // 30 minutes ago
  },
  {
    id: 3,
    icon: 'database',
    title: 'Database backup',
    description: 'Automated backup completed successfully',
    timestamp: new Date(Date.now() - 1000 * 60 * 60 * 2), // 2 hours ago
  },
])

const formatRelativeTime = (date: Date) => {
  const seconds = Math.floor((new Date().getTime() - date.getTime()) / 1000)
  
  if (seconds < 60) return 'just now'
  if (seconds < 3600) return `${Math.floor(seconds / 60)} minutes ago`
  if (seconds < 86400) return `${Math.floor(seconds / 3600)} hours ago`
  return `${Math.floor(seconds / 86400)} days ago`
}

useHead({
  title: 'Dashboard',
})
</script>

