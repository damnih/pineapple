<template>
  <div class="border rounded-4 p-4 mb-5" style="max-width: 700px; margin: auto; font-family: sans-serif;">
    <!-- 상품명 -->
    <h3 class="text-center fw-bold mb-3">{{ product }}</h3>
    <hr />

    <!-- 은행명 뱃지 -->
    <div class="text-center mb-3">
      <span class="badge bg-primary">{{ kor_co_nm }}</span>
    </div>

    <!-- 원형 2개 -->
    <div class="d-flex justify-content-center align-items-center gap-5 mb-4">
      <div class="circle">
        <div class="text-center text-white">
          <div class="fw-bold">최고</div>
          <div class="fs-5">{{ result }}원</div>
        </div>
      </div>
      <div class="circle">
        <div class="text-center text-white">
          <div class="fw-bold">금리</div>
          <div class="fs-5">{{ intr_rate2 }}%</div>
        </div>
      </div>
    </div>

    <!-- 가입 정보 -->
    <div class="row">
      <div class="col-md-6">
        <p>가입 방법 : {{ join_way }}</p>
        <p>저축 금리 유형명 : {{ intr_rate_type_nm }}</p>
        <p>기본 금리 : {{ intr_rate }}%</p>
        <p>최고 우대 금리 : {{ intr_rate2 }}%</p>
        <p>우대 조건 :</p>
        <ul>
          <li v-for="(condition, index) in spcl_cnd.split('\n')" :key="index">{{ condition }}</li>
        </ul>
      </div>
      <div class="col-md-6">
        <p>특이사항 :</p>
        <ul>
          <li v-for="(note, index) in etc_note.split('\n')" :key="index">{{ note }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  product: String,
  kor_co_nm: String,
  result: String,            // 계산된 결과: 받을 수 있는 최대금액
  intr_rate2: String,        // 최고 금리
  intr_rate: String,         // 기본 금리
  join_way: String,
  intr_rate_type_nm: String,
  spcl_cnd: String,          // 여러 줄일 수 있으므로 \n 기준으로 분리
  etc_note: String           // 여러 줄일 수 있으므로 \n 기준으로 분리
})
</script>

<style scoped>
.circle {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background-color: #3399ff;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>