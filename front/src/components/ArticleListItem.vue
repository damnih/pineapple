<template>
  <div>
    <RouterLink
      :to="{ name: 'detail', params: { id: article.id } }"
      class="text-decoration-none text-dark d-flex align-items-center justify-content-between"
    >
      <h5 class="mb-0 me-2">{{ article.title }}</h5>
      <p class="mb-0">{{ account.user.username }}</p>
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useAccountStore } from "@/stores/accounts.js"

const account = useAccountStore()

defineProps({
  article: Object
})
</script>
