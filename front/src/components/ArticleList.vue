<!-- ArticleList.vue -->

<template>
  <div>
    <ArticleListItem
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import { useArticleStore } from '@/stores/articles'
import ArticleListItem from '@/components/ArticleListItem.vue'

const store = useArticleStore()
</script>
