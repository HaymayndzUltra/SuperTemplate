<template>
  <div class="bg-white rounded-lg shadow p-6">
    <div class="flex items-center">
      <div class="flex-shrink-0">
        <div class="flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 text-white">
          <Icon :name="icon" class="h-6 w-6" />
        </div>
      </div>
      <div class="ml-4">
        <h3 class="text-lg font-medium text-gray-900">{{ title }}</h3>
        <p class="mt-1 text-sm text-gray-500">{{ description }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  icon: string
  title: string
  description: string
}

defineProps<Props>()
</script>

