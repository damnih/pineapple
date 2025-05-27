<template>
  <div class="container-fluid my-5">
    <div 
    class="row justify-content-center g-5 fade-in"
    v-if="isVisible"
    >
      <div
        class="col-12 col-md-6 col-lg-2"
        v-for="(card, index) in cards"
        :key="index"
      >
        <RouterLink :to="{ name: card.routeName }" class="text-decoration-none text-dark">
          <div class="d-flex flex-column align-items-start">
            <img
              :src="card.image"
              alt="카드 이미지"
              class="rounded-image mb-3"
            />
            <div class="w-100 text-start px-1">
              <h5 class="fw-bold">{{ card.title }}</h5>
              <p class="text-muted small">{{ card.subtitle }}</p>
            </div>
          </div>
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const isVisible = ref(false)

onMounted(() => {
  // 약간의 지연 후 표시 (애니메이션 자연스럽게)
  setTimeout(() => {
    isVisible.value = true
  }, 100)
})

const cards = [
  {
    title: "여행 예산 모으기",
    subtitle: "여행 가기 전까지 얼마나 모을 수 있을까?",
    routeName: "recommend",
    image: "../../the-moon-2117086_1920.jpg", // 서버 이미지 경로
  },
  {
    title: "커뮤니티",
    subtitle: "여행을 가고 싶은데 예산은 어떻게 잡아야 할까?",
    routeName: "article",
    image: "../../merry-christmas-5219496_1280.jpg",
  },
  {
    title: "환율 계산",
    subtitle: "여행 가는 곳의 환율은 어느 정도일까?",
    routeName: "exchangerate",
    image: "../../wing-221525_1920.jpg",
  },
  {
    title: "주변 은행 찾기",
    subtitle: "환전할 수 있는 은행은 어디에 있을까?",
    routeName: "map",
    image: "../../sky-6768714_1280.jpg",
  },
    {
    title: "전체 예금 상품 보기",
    subtitle: "어떤 예금 상품들이 있을까?",
    routeName: "all-deposit",
    image: "../../clouds-8485592_1920.jpg",
  },
];
</script>

<style scoped>
.rounded-image {
  width: 100%;
  aspect-ratio: 1 / 2;
  border-radius: 1rem;
  object-fit: cover;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* 페이드 인 효과 */
.fade-in {
  opacity: 0;
  animation: fadeInUp 1s ease-out forwards;
}

/* 부드러운 위쪽 등장 효과 */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>