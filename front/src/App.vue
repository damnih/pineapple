<template>
  <div>
    <!-- 네비게이션 상단 줄 -->
    <nav class="main-navbar">
      <RouterLink class="nav-link" :to="{ name: 'home' }">HOME</RouterLink>
      <RouterLink class="nav-link" :to="{ name: 'signup' }">SIGNUP</RouterLink>
      <RouterLink class="nav-link" :to="{ name: 'login' }">LOGIN</RouterLink>
    </nav>

    <!-- 장식용 하단 줄 -->
    <div class="decorative-bar">
      <div class="bar black"></div>
      <div class="bar blue"></div>
      <div class="bar black"></div>
      <div class="bar blue flex-grow"></div>
    </div>
  </div>
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'

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