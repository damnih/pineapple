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
        <img src="../../the-moon-2117086_1920.jpg" class="d-block w-50 mx-auto" alt="airplane">
        <div class="carousel-caption d-none d-md-block text-center">
          <h5>First slide label</h5>
          <p>Some representative placeholder content for the first slide.</p>
        </div>
      </div>
      <div class="carousel-item">
        <img src="../../merry-christmas-5219496_1280.jpg" class="d-block w-50 mx-auto" alt="boardingticket">
        <div class="carousel-caption d-none d-md-block text-center">
          <h5>Second slide label</h5>
          <p>Some representative placeholder content for the second slide.</p>
        </div>
      </div>
      <div class="carousel-item">
        <img src="../../sky-6768714_1280.jpg" class="d-block w-50 mx-auto" alt="sky">
        <div class="carousel-caption d-none d-md-block text-center">
          <h5>Third slide label</h5>
          <p>Some representative placeholder content for the third slide.</p>
        </div>
      </div>
      <div class="carousel-item">
        <img src="../../wing-221525_1920.jpg" class="d-block w-50 mx-auto" alt="wing">
        <div class="carousel-caption d-none d-md-block text-center">
          <h5>Fourth slide label</h5>
          <p>Some representative placeholder content for the fourth slide.</p>
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

<script setup></script>

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