<template>
  <div class="container my-5">
    <div class="text-center mb-5">
      <h4>
        👍 {{ store.destination_ans }} 여행 준비를 위한 추천 상품 Top 4
      </h4>
    </div>

    <div v-if="depositList && depositList.length > 0" class="row justify-content-center">
      <div class="col-12 col-md-6 d-flex align-items-stretch mb-4" 
      v-for="(item, index) in depositList" 
      :key="index"
      >
      <DepositItem
        :product_name="item.product_name"
        :kor_co_nm="item.kor_co_nm"
        :maturity_amount="item.maturity_amount"
        :intr_rate="item.intr_rate"
        :intr_rate2="item.intr_rate2"
        :join_way="item.join_way"
        :intr_rate_type_nm="item.intr_rate_type_nm"
        :spcl_cnd="item.spcl_cnd"
        :etc_note="item.etc_note"
      />
      </div>
    </div>
    <div v-else class="text-center text-muted">추천 가능한 상품이 없습니다.</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import DepositItem from '@/components/DepositItem.vue'
import { useAnswersStore } from '@/stores/Deposit'

const store = useAnswersStore()
const depositList = ref([])

onMounted(async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/datas/api/deposit_results/', {
      params: {
        schedule_ans: store.schedule_ans,
        destination_ans: store.destination_ans,
        budget_ans: store.budget_ans,
      }
    })
    console.log('✅ 받은 데이터:', res.data)
    depositList.value = res.data
  } catch (err) {
    console.error('예금 상품 조회 실패:', err)
  }
})

console.log('store:', store)
console.log('params:', {
  schedule_ans: store.schedule,
  destination_ans: store.destination_ans,
  budget_ans: store.budget_ans,
})
</script>
