<template>
  <div>
    <!-- 네비게이션 상단 줄 -->
    <nav class="main-navbar">
      <RouterLink class="nav-link" :to="{ name: 'home' }">HOME</RouterLink>
      <RouterLink class="nav-link" :to="{ name: 'signup' }">SIGNUP</RouterLink>
      <RouterLink class="nav-link" :to="{ name: 'login' }">LOGIN</RouterLink>

      <!-- 여행지 정보 유튜브 검색 -->
      <form class="d-flex ms-auto" role="search">
      <input v-model="searchQuery" class="form-control me-2" type="search" style="width: 250px;" placeholder="여행지 정보가 궁금하다면" aria-label="Search"/>
      <button @click="searchVideos" class="btn btn-primary" type="submit" style="white-space: nowrap;">검색</button>
      </form>
    </nav>

    <!-- 장식용 하단 줄 -->
    <div class="decorative-bar">
      <div class="bar black"></div>
      <div class="bar blue"></div>
      <div class="bar black"></div>
      <div class="bar blue flex-grow"></div>
    </div>
  </div>

  <RouterView />
</template>

<script setup>
import { ref } from 'vue'
import { RouterView, RouterLink, useRouter } from 'vue-router'

const router = useRouter()

const searchQuery = ref('')
const searchResults = ref([])

const searchVideos = async (event) => {
  event.preventDefault() // 폼 제출 방지

  if (!searchQuery.value) return

  router.push({ name: 'youtube', query: { q: searchQuery.value } })
}

</script>

<style scoped>
.main-navbar {
  display: flex;
  justify-content: left;
  align-items: center;
  background-color: white;
  padding: 16px;
  gap: 40px;
}

.nav-link {
  text-decoration: none;
  color: black;
  font-size: 24px;
  font-weight: bold;
}

.decorative-bar {
  display: flex;
  height: 50px;
}

.bar {
  width: 160px;
  height: 100%;
}

.black {
  background-color: black;
}

.blue {
  background-color: #3399ff;
}

.flex-grow {
  flex-grow: 1;
}
</style>