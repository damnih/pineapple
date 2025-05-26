<template>
  <ArticleBox>
    <RouterLink :to="{ name: 'article' }" class="btn btn-primary">뒤로 가기</RouterLink>
    <br>
    <br>
    <div v-if="article">
      <h3>{{ article.title }}</h3>
      <p>작성자 : {{ account.user.username }}  |  작성일 : {{ article.created_at }}</p>
      <hr>
      {{ article.content }}
    </div>

    <hr>
    <h5>댓글</h5>
    <CommentList :comments="comments" />
    <CommentForm :onSuccess="fetchComments" />
  </ArticleBox>
  
</template>

<script setup>
import ArticleBox from "@/components/ArticleBox.vue"
import axios from 'axios'
import { ref, onMounted } from "vue"
import { useRoute } from "vue-router"
import { useArticleStore } from "@/stores/articles.js"
import { useAccountStore } from "@/stores/accounts.js"
import CommentList from "@/components/CommentList.vue"
import CommentForm from '@/components/CommentForm.vue'

const account = useAccountStore()

const store = useArticleStore()
const route = useRoute()
const article = ref(null)

const comments = ref([])
const newComment = ref('')

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}${route.params.id}/`,
  })
    .then((res) => {
      article.value = res.data
    })
    .catch(err => console.log(err))

    fetchComments()
})

const fetchComments = () => {
  axios.get(`${store.API_URL}comments/`, {
    params: { article_pk: route.params.id }
  })
    .then((res) => {
      comments.value = res.data
    })
    .catch(err => console.log(err))
}

const createComment = () => {
  if (!newComment.value.trim()) return
  axios.post(`${store.API_URL}${route.params.id}/comments/`, {
    content: newComment.value,
  }, {
    headers: {
      Authorization: `Token ${account.token}`
    }
  })
    .then(() => {
      newComment.value = ''
      fetchComments()
    })
    .catch(err => console.log(err))
}
</script>

<style scoped></style>