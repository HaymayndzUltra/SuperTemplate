<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup lang="ts">
useHead({
  titleTemplate: (titleChunk) => {
    return titleChunk ? `${titleChunk} - {{PROJECT_NAME}}` : '{{PROJECT_NAME}}'
  },
})

// Initialize auth state on app mount
const { initAuth } = useAuth()
onMounted(() => {
  initAuth()
})
</script>

