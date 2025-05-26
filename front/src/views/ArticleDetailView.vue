<template>
  <ArticleBox>
    <div v-if="article">
      <h3>{{ article.title }}</h3>
      <p>작성자 : {{ article.author }}  |  작성일 : {{ article.created_at }}</p>
      <hr>
      {{ article.content }}
    </div>
  </ArticleBox>
  <RouterLink :to="{ name: 'article' }" class="btn btn-primary">뒤로 가기</RouterLink>
</template>

<script setup>
import ArticleBox from "@/components/ArticleBox.vue"
import axios from 'axios'
import { onMounted } from "vue"
import { useRoute } from "vue-router"
import { useArticleStore } from "@/stores/articles.js"

const store = useArticleStore()
const route = useRoute()
const article = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/${route.params.id}/`,
  })
    .then((res) => {
      console.log(res.data)
      article.value = res.data
    })
    .catch(err => console.log(err))
})
</script>

<style scoped></style>