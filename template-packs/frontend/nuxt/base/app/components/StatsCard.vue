<template>
  <div class="bg-white overflow-hidden shadow rounded-lg">
    <div class="p-5">
      <div class="flex items-center">
        <div class="flex-shrink-0">
          <Icon :name="icon" class="h-6 w-6 text-gray-400" />
        </div>
        <div class="ml-5 w-0 flex-1">
          <dl>
            <dt class="text-sm font-medium text-gray-500 truncate">
              {{ title }}
            </dt>
            <dd class="flex items-baseline">
              <div class="text-2xl font-semibold text-gray-900">
                {{ value }}
              </div>
              <div
                v-if="trend"
                class="ml-2 flex items-baseline text-sm font-semibold"
                :class="trendUp ? 'text-green-600' : 'text-red-600'"
              >
                <Icon
                  :name="trendUp ? 'trending-up' : 'trending-down'"
                  class="self-center flex-shrink-0 h-5 w-5"
                />
                <span class="sr-only">
                  {{ trendUp ? 'Increased' : 'Decreased' }} by
                </span>
                {{ trend }}
              </div>
            </dd>
          </dl>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  title: string
  value: string | number
  icon: string
  trend?: string
  trendUp?: boolean
}

defineProps<Props>()
</script>

