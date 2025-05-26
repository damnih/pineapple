<template>
  <ArticleBox>
    <button class="btn btn-primary" @click="handleCreateClick">CREATE</button>
    <ArticleList />
  </ArticleBox>
</template>

<script setup>
import ArticleBox from "@/components/ArticleBox.vue"
import ArticleList from '@/components/ArticleList.vue'
import { useArticleStore } from "@/stores/articles.js"
import { onMounted } from "vue"
import { useRouter } from "vue-router"

const store = useArticleStore()
const router = useRouter()

const isLoggedIn = !!localStorage.getItem('token')

const handleCreateClick = () => {
  if (!isLoggedIn) {
    alert("로그인을 진행해주세요")
  } else {
    router.push({ name: 'create' })
  }
}

onMounted(() => {
  store.getArticles()
})
</script>

<style scoped></style>