<!-- ArticleDetailView.vue -->

<template>
  <ArticleBox>
    <RouterLink :to="{ name: 'article' }" class="btn btn-sm btn-primary">뒤로 가기</RouterLink>
    <br><br>

    <div v-if="article">
      <div class="d-flex justify-content-between align-items-center">
        <h3>{{ article.title }}</h3>
        <!-- 본인일 때만 삭제 버튼 표시 -->
        <button
          v-if="account.user.id === article.author.id"
          @click="deleteArticle"
          class="btn btn-sm btn-danger"
        >
          삭제
        </button>
      </div>
      <p>작성자 : {{ article.author.username }} | 작성일 : {{ article.created_at.slice(0, 10) }}</p>
      <hr>
      {{ article.content }}
      <br><br><br><br><br>
    </div>

    <hr>
    <h5>댓글</h5>
    <br>
    <CommentList :comments="comments" @deleted="fetchComments" />
    <CommentForm :onSuccess="fetchComments" />
>>>>>>> 5a65c9ff381cd715da4008e41fe2315fa6d52f9c
  </ArticleBox>
</template>

<script setup>
import ArticleBox from "@/components/ArticleBox.vue"
import axios from 'axios'
import { ref, onMounted } from "vue"
import { useRoute, useRouter } from "vue-router"
import { useArticleStore } from "@/stores/articles.js"
import { useAccountStore } from "@/stores/accounts.js"
import CommentList from "@/components/CommentList.vue"
import CommentForm from '@/components/CommentForm.vue'

const account = useAccountStore()
const store = useArticleStore()
const route = useRoute()
const router = useRouter()

const article = ref(null)
const comments = ref([])

onMounted(() => {
  axios.get(`${store.API_URL}${route.params.id}/`)
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

const deleteArticle = async () => {
  const confirmDelete = confirm("정말로 게시글을 삭제하시겠습니까?")
  if (!confirmDelete) return

  try {
    await axios.delete(`${store.API_URL}${route.params.id}/`, {
      headers: {
        Authorization: `Token ${account.token}`
      }
    })
    // 삭제 후 목록 페이지로 이동
    router.push({ name: 'article' })
  } catch (err) {
    console.error("게시글 삭제 실패:", err)
  }
}
</script>
