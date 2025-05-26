<template>
  <ArticleBox>
    <RouterLink :to="{ name: 'create' }" class="btn btn-primary">CREATE</RouterLink>
    <ArticleList />
  </ArticleBox>
  
</template>

<script setup>
import ArticleBox from "@/components/ArticleBox.vue"
import ArticleList from '@/components/ArticleList.vue'
import { useArticleStore } from "@/stores/articles.js"
import { onMounted } from "vue"
import { RouterLink } from "vue-router"

const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})
</script>

<style scoped></style>