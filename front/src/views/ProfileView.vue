<template>
  <Box>
  <div class="profile-view container my-5">
    <h2>프로필 </h2>
    <ul class="list-group">
      <li class="list-group-item"><strong>이름:</strong> {{ profile.name }}</li>
      <li class="list-group-item"><strong>나이:</strong> {{ profile.age }}</li>
      <li class="list-group-item"><strong>국적:</strong> {{ profile.nationality }}</li>
    </ul>
  </div>
  </Box>
</template>


<script setup>
import { ref, onMounted } from 'vue'
import { useRoute }       from 'vue-router'
import axios               from 'axios'
import Box from '@/components/Box.vue'

const route   = useRoute()
const username = route.params.username   // URL 파라미터
const profile  = ref({ name: '', age: '', nationality: '' })

onMounted(async () => {
  try {
    const res = await axios.get(`http://127.0.0.1:8000/accounts/${username}/`)
    profile.value = res.data
  } catch (err) {
    console.error('프로필 조회 실패', err)
    alert('사용자 프로필을 불러오지 못했습니다.')
  }
})
</script>


<style scoped>
.profile-view {
  max-width: 400px;
  margin: 0 auto;
}
</style>
