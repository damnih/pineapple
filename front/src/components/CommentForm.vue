<template>
  <div class="mt-3">
    <textarea v-model="newComment" rows="3" class="form-control" placeholder="댓글을 입력하세요" />
    <button class="btn btn-primary mt-2" @click="submitComment">등록</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useAccountStore } from '@/stores/accounts.js'
import { useRoute } from 'vue-router'

const props = defineProps({
  onSuccess: {
    type: Function,
    required: false,
  }
})

const route = useRoute()
const account = useAccountStore()
const newComment = ref('')

const submitComment = () => {
  if (!newComment.value.trim()) return

  axios.post(`http://127.0.0.1:8000/articles/${route.params.id}/comments/`, {
    content: newComment.value,
  }, {
    headers: {
      Authorization: `Token ${account.token}`
    }
  })
  .then(() => {
    newComment.value = ''
    props.onSuccess?.()  // 등록 성공 시 콜백 호출
  })
  .catch(err => {
    console.error('댓글 작성 실패:', err)
  })
}
</script>

<style scoped></style>
