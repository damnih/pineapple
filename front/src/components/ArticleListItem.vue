<!-- ArticleListItem.vue -->
<template>
  <div>
    <RouterLink
      :to="{ name: 'detail', params: { id: article.id } }"
      class="text-decoration-none text-dark d-flex align-items-center justify-content-between"
    >
      <h5 class="mb-0 me-2">{{ article.title }}</h5>
      <p class="mb-0">{{ account.user.username }}</p>
    </RouterLink>
  </div>
  <hr>
</template>

<script setup>
import { useAccountStore } from "@/stores/accounts.js"
import { useArticleStore } from "@/stores/articles.js"
import axios from 'axios'

const account = useAccountStore()
const store = useArticleStore()

const props = defineProps({
  article: Object
})

const deleteArticle = async () => {
  const confirmDelete = confirm("정말로 이 게시글을 삭제하시겠습니까?")
  if (!confirmDelete) return

  try {
    await axios.delete(`${store.API_URL}${props.article.id}/`, {
      headers: {
        Authorization: `Token ${account.token}`
      }
    })
    // 삭제 후 새로고침 or 리스트 갱신
    await store.fetchArticles()
  } catch (error) {
    console.error("게시글 삭제 실패:", error)
  }
}
</script>
