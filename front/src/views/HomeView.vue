<template>
  <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
    <!-- 인디케이터 -->
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="3" aria-label="Slide 4"></button>
    </div>

    <!-- 이미지들 -->
  <div class="carousel-inner">
    <div class="carousel-item active">
      <RouterLink :to="{ name: 'deposit' }">
        <img src="../../the-moon-2117086_1920.jpg" class="d-block w-50 mx-auto" alt="airplane">
      </RouterLink>
      <div class="carousel-caption d-none d-md-block text-center">
        <h4>여행 예산 모으기</h4>
        <p>내가 여행을 가기 전까지 얼마나 모을 수 있을까?</p>
      </div>
    </div>

    <div class="carousel-item">
      <RouterLink :to="{ name: 'article' }">
        <img src="../../merry-christmas-5219496_1280.jpg" class="d-block w-50 mx-auto" alt="boardingticket">
      </RouterLink>
      <div class="carousel-caption d-none d-md-block text-center">
        <h4>커뮤니티</h4>
        <p>여행을 가고 싶은데 예산은 어떻게 잡아야 할까?</p>
      </div>
    </div>

    <div class="carousel-item">
      <RouterLink :to="{ name: 'exchangerate' }">
        <img src="../../wing-221525_1920.jpg" class="d-block w-50 mx-auto" alt="sky">
      </RouterLink>
      <div class="carousel-caption d-none d-md-block text-center">
        <h4>환율 계산</h4>
        <p>여행 가는 곳의 환율은 어떨까?</p>
      </div>
    </div>

    <div class="carousel-item">
      <RouterLink :to="{ name: 'map' }">
        <img src="../../sky-6768714_1280.jpg" class="d-block w-50 mx-auto" alt="wing">
      </RouterLink>
      <div class="carousel-caption d-none d-md-block text-center">
        <h5>주변 은행 찾기</h5>
        <p>환전을 할 은행의 위치는 어디일까?</p>
      </div>
    </div>
  </div>

    <!-- 좌우 버튼 -->
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
      <span class="carousel-control-prev-icon custom-arrow" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
      <span class="carousel-control-next-icon custom-arrow" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style>
.carousel-control-prev-icon,
.carousel-control-next-icon {
  background-color: black;
  border-radius: 50%;
  background-size: 70% 70%;
  background-position: center;
  background-repeat: no-repeat;
}
</style>