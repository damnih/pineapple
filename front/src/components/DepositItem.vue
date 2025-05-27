<template>
  <div class="border rounded-4 p-4 h-100 d-flex flex-column w-100" style="font-family: sans-serif;">
    <!-- 상품명 -->
    <h3 class="text-center fw-bold mb-3">{{ product_name }}</h3>
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
          <div class="fs-5">{{ maturity_amount.toLocaleString() }} 만원</div>
        </div>
      </div>
      <div class="circle">
        <div class="text-center text-white">
          <div class="fw-bold">금리</div>
          <div class="fs-5"> 최대 {{ intr_rate2 }}%</div>
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
  product_name: String,
  kor_co_nm: String,
  maturity_amount: Number,
  intr_rate2: Number,
  intr_rate: Number,
  join_way: String,
  intr_rate_type_nm: String,
  spcl_cnd: String,
  etc_note: String
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