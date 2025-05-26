<template>
  <div>
    <!-- 네비게이션 상단 줄 -->
    <nav class="main-navbar">
      <RouterLink class="nav-link" :to="{ name: 'home' }">HOME</RouterLink>
      
      <RouterLink
        v-if="!isLoggedIn"
        class="nav-link"
        :to="{ name: 'signup' }"
      >SIGNUP</RouterLink>
      
      <RouterLink
        v-if="!isLoggedIn"
        class="nav-link"
        :to="{ name: 'login' }"
      >LOGIN</RouterLink>
      
      <a
        v-else
        class="nav-link"
        href="#"
        @click.prevent="accountStore.logOut()"
      >LOGOUT</a>
      
      
      <!-- <RouterLink class="nav-link" :to="{ name: 'signup' }">SIGNUP</RouterLink>
      <RouterLink class="nav-link" :to="{ name: 'login' }">LOGIN</RouterLink> -->

      <!-- 여행지 정보 유튜브 검색 -->
      <form class="d-flex ms-auto" role="search">
      <input v-model="searchQuery" class="form-control me-2" type="search" style="width: 250px;" placeholder="여행지 정보가 궁금하다면" aria-label="Search"/>
      <button @click="searchVideos" class="btn btn-primary" type="submit" style="white-space: nowrap;">검색</button>
      </form>
    </nav>

    <!-- 로그인 완료 시 누구님! 보이게 해주는 것  -->
    <!-- <nav v-if="isLoggedIn"> 
      {{ user.name }} 님 안녕하세요! 
    </nav> -->

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
import { ref, computed } from 'vue'
import { RouterView, RouterLink, useRouter } from 'vue-router'

import { useAccountStore } from '@/stores/accounts.js'

const accountStore = useAccountStore()

// 로그인 여부 계산: token이 빈 문자열이 아니면 true
const isLoggedIn = computed(() => !!accountStore.token)


const router = useRouter()

const searchQuery = ref('')
const searchResults = ref([])

const searchVideos = async (event) => {
  event.preventDefault() // 폼 제출 방지

  if (!searchQuery.value) return

  router.push({ name: 'youtube', query: { q: searchQuery.value } })
}

// 로그인 여부
const isLoggedIn = computed(() => !!accountStore.token)
// user 객체가 있으면 name 필드 꺼내기
const userName   = computed(() => accountStore.user?.name || '')

// 앱 시작 시, 저장된 토큰이 있으면 프로필 fetch
onMounted(() => {
  accountStore.fetchUser()
})


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