<template>
  <ArticleBox>
    <form @submit.prevent="createArticle">
    <div class="mb-3">
      <label for="title" class="form-label">제목</label>
      <input type="text" class="form-control" id="title" v-model.trim="title">
    </div>
    <div class="mb-3">
      <label for="content" class="form-label">내용</label>
      <textarea class="form-control" id="content" rows="3" v-model.trim="content"></textarea>
    </div>
    <button class="btn btn-primary" type="submit">SUBMIT</button>
    </form>
  </ArticleBox>
</template>

<script setup>
import ArticleBox from "@/components/ArticleBox.vue"
import { ref } from "vue"
import axios from "axios"
import { useArticleStore } from "@/stores/articles.js"
import { useRouter } from "vue-router"

const store = useArticleStore()
const router = useRouter()

const title = ref(null)
const content = ref(null)



const createArticle = function () {
  console.log(title.value, content.value)
  axios.post(`${store.API_URL}`, {
    title: title.value,
    content: content.value
  }, {
    headers: {
      Authorization: `Token ${localStorage.getItem('token')}`,
      'Content-Type': 'application/json'
    }
  })
    .then(() => {
      router.push({ name: article })
    }).catch(err => console.log(err))
}
</script>

<style scoped></style>