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
  
    <div>
    <h3>좋아요 누른 상품</h3>
      <ul v-if="profile.liked_products.length" class="list-group">
        <li
          v-for="prod in profile.liked_products"
          :key="prod.id"
          class="list-group-item p-0 mb-2"
        >
          <!-- 상세 페이지 링크 -->
          <router-link
            :to="{ name: 'alldepositdetail', params: { id: prod.id } }"
            class="d-flex justify-content-between align-items-center text-decoration-none text-dark p-3"
          >
            <div>
              <strong>{{ prod.kor_co_nm }}</strong><br>
              {{ prod.fin_prdt_nm }}
              <!-- 최고 금리 표시 -->
              <small class="ms-2 text-muted">
                {{ maxRate(prod) }}%
              </small>
            </div>
            <span class="badge bg-primary rounded-pill">
              ♥
            </span>
          </router-link>
        </li>
      </ul>
      <p v-else class="text-muted">아직 좋아요 누른 상품이 없습니다.</p>
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
const profile = ref({
  name: '',
  age: '',
  nationality: '',
  liked_products: []
})

onMounted(async () => {
  try {
    const res = await axios.get(`http://127.0.0.1:8000/accounts/${username}/`)
    profile.value = res.data
  } catch (err) {
    console.error('프로필 조회 실패', err)
    alert('사용자 프로필을 불러오지 못했습니다.')
  }
})

// options 중 intr_rate2 최대값을 계산
function maxRate(prod) {
  if (!prod.options || !prod.options.length) return 0
  return prod.options
    .map(o => o.intr_rate2)
    .reduce((a, b) => (a > b ? a : b))
}
</script>


<style scoped>
.profile-view {
  max-width: 500px;
  margin: 0 auto;
}
</style>
