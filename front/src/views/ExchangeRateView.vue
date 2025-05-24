<template>
  <Box>
    <div class="container">
      <h2>환율 조회</h2>
      <p>※ 주말에는 조회가 불가합니다.</p>
      <hr>

      <form>
        <select id="currency" v-model="selectedCurrency">
          <option disabled value="">통화를 선택하세요</option>
          <option v-for="(code, name) in currencyMap" :key="name" :value="name">
            {{ name }}
          </option>
        </select>
        <button @click.prevent="fetchExchangeRate" class="btn btn-primary ms-3">조회</button>
      </form>

      <div v-if="rate !== null" class="mt-3">
        <p>{{ now_selectedCurrency }} → KRW 환율: {{ rate }}</p>
        <table class="table">
          <thead>
            <tr><th>통화</th><th>환율(KRW)</th></tr>
          </thead>
          <tbody>
            <tr><td>{{ now_selectedCurrency }}</td><td>{{ rate }}</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </Box>
</template>

<script setup>
import Box from '@/components/Box.vue'
import { ref } from 'vue'
import axios from 'axios'

// 통화 선택 및 환율 저장용 상태
const selectedCurrency = ref('')
const rate = ref(null)
const now_selectedCurrency = ref('')

// 통화 코드 맵
const currencyMap = {
  USD: '0000001',
  EUR: '0000003',
  CNY: '0000053',
  JPY: '0000002',
  TWD: '0000031',
  VND: '0000035',
  THB: '0000028',
  GBP: '0000012',
  AUD: '0000017'
}

// API 키
const API_KEY = 'YHDHWWD18JE3MNFIN3JB'

// API 호출 함수
const fetchExchangeRate = async () => {
  const selectedCode = currencyMap[selectedCurrency.value]
  now_selectedCurrency.value = selectedCurrency.value

  try {
    const res = await axios.get(`http://localhost:8000/datas/exchange-rate/${selectedCode}`)
    
    if (res.data && res.data.rate) {
      rate.value = res.data.rate
    } else {
      console.error('환율 데이터를 찾을 수 없습니다.')
      rate.value = '조회 실패'
    }
  } catch (err) {
    console.error('API 요청 실패:', err)
    rate.value = '요청 오류'
  }
}
</script>

<style scoped></style>