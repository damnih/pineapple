<template>
  <Articlebox>
    <div class="d-flex flex-column align-items-center text-center">
      <!-- 질문 1: 여행 시기 -->
      <div class="mb-4">
        <h5>언제 여행을 갈 생각인가요?</h5>
        <select class="form-select mt-2" v-model="travelDateText">
          <option disabled value="">기간을 선택하세요</option>
          <option v-for="option in travelDateOptions" :key="option">{{ option }}</option>
        </select>
      </div>

      <!-- 질문 2: 여행지 -->
      <div class="mb-4">
        <h5>어디로 여행을 갈 생각인가요?</h5>
        <select class="form-select mt-2" v-model="travelDestinationText">
          <option disabled value="">여행지를 선택하세요</option>
          <option v-for="option in destinationOptions" :key="option">{{ option }}</option>
        </select>
      </div>

      <!-- 질문 3: 금액 -->
      <div class="mb-4">
        <h5>지금까지 모은 돈은 얼마인가요?</h5>
        <input
          type="number"
          min="0"
          class="form-control mt-2"
          v-model="savedMoney"
          placeholder="0 이상의 정수를 입력하세요"
        />
      </div>

      <!-- 제출 버튼 -->
      <button class="btn btn-primary mt-3" @click="goToDeposit">금융상품 추천 받기</button>
    </div>
  </Articlebox>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAnswersStore } from '@/stores/Deposit.js'
import Articlebox from '@/components/ArticleBox.vue'

const router = useRouter()
const store = useAnswersStore()

const travelDateOptions = ['1개월 후', '3개월 후', '6개월 후', '12개월 후']
const destinationOptions = ['미국', '중국', '일본', '유럽', '대만', '베트남', '태국']

const travelDateText = ref('')
const travelDestinationText = ref('')
const savedMoney = ref('')

const convertToMonth = (text) => {
  const map = {
    '1개월 후': 1,
    '3개월 후': 3,
    '6개월 후': 6,
    '12개월 후': 12,
  }
  return map[text] || null
}

const goToDeposit = () => {
  const schedule = convertToMonth(travelDateText.value)
  const budget = parseInt(savedMoney.value)
  const destination = travelDestinationText.value

  if (schedule && destination && !isNaN(budget) && budget >= 0) {
    store.schedule_ans = schedule
    store.budget_ans = budget
    store.destination_ans = destination

    router.push({ name: 'deposit' })
  } else {
    alert('모든 항목을 올바르게 입력해주세요.')
  }
}
</script>

<style scoped>
</style>
