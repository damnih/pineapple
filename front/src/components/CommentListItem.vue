<!-- CommentListItem.vue -->

<template>
  <div class="d-flex justify-content-between">
    <p class="mb-1">
      {{ comment.comment_author.username }} | {{ comment.content }}
    </p>
    <button
      v-if="account.user.id === comment.comment_author.id"
      @click="deleteComment"
      class="btn btn-sm btn-outline-danger"
    >
      삭제
    </button>
  </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/accounts.js'
import { useArticleStore } from '@/stores/articles.js'
import axios from 'axios'

const account = useAccountStore()
const store = useArticleStore()

const props = defineProps({
  comment: Object
})
const emit = defineEmits(['deleted'])

const deleteComment = async () => {
  const confirmDelete = confirm("댓글을 삭제하시겠습니까?")
  if (!confirmDelete) return

  try {
    await axios.delete(`${store.API_URL}comments/${props.comment.id}/`, {
      headers: {
        Authorization: `Token ${account.token}`
      }
    })
    emit('deleted')  // 댓글 새로고침용
  } catch (error) {
    console.error("댓글 삭제 실패:", error)
  }
}
</script>
