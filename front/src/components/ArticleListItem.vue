<template>
  <div>
    <RouterLink
      :to="{ name: 'Detail', params: { id: article.id } }"
      class="text-decoration-none text-dark"
    >
      <h5 class="mb-1">{{ article.title }}</h5>
    </RouterLink>
    <p class="mb-2">{{ article.author }}</p>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: Object
})
</script>
