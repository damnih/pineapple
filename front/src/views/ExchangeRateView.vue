<template>
  <ArticleBox>
    <div class="container">
      <h2>💸 환율 조회</h2>
      <p>※ 주말에는 환율이 제공되지 않습니다.</p>
      <form @submit.prevent="fetchExchangeRate">
        <select v-model="selectedCurrency">
          <option disabled value="">통화를 선택하세요</option>
          <option v-for="(code, name) in currencyMap" :key="name" :value="name">
            {{ name }}
          </option>
        </select>
        <button class="btn btn-primary ms-3">조회</button>
      </form>

      <div v-if="chartData.labels.length > 0" class="mt-4">
        <Line :data="chartData" :options="chartOptions" />
      </div>
    </div>
  </ArticleBox>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import ArticleBox from '@/components/ArticleBox.vue'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement
} from 'chart.js'
import { Line } from 'vue-chartjs'

ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement)

const selectedCurrency = ref('')
const now_selectedCurrency = ref('')

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

// 차트용 데이터
const chartData = ref({
  labels: [],
  datasets: []
})

const chartOptions = {
  responsive: true,
  plugins: {
    legend: { position: 'top' },
    title: { display: true, text: '일주일간 환율 변화' }
  }
}

const fetchExchangeRate = async () => {
  const selectedCode = currencyMap[selectedCurrency.value]
  now_selectedCurrency.value = selectedCurrency.value

  try {
    const res = await axios.get(`http://localhost:8000/datas/exchange-rate/${selectedCode}`)

    if (res.data && res.data.rates) {
      const labels = res.data.rates.map(item => item.date)
      const values = res.data.rates.map(item => parseFloat(item.rate))

      chartData.value = {
        labels,
        datasets: [
          {
            label: `${selectedCurrency.value} → KRW`,
            data: values,
            fill: false,
            borderColor: 'blue',
            tension: 0.3
          }
        ]
      }
    } else {
      console.error('환율 데이터를 찾을 수 없습니다.')
    }
  } catch (err) {
    console.error('API 요청 실패:', err)
  }
}
</script>

<style scoped></style>
