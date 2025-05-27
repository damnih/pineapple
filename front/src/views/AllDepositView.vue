<template>

  <div>안보이는게맞니 </div>

  <!-- 로딩 중 표시 -->
  <div v-if="isLoading">로딩 중...</div>

  <!-- 에러 났을 때 -->
  <div v-else-if="errorMsg">{{ errorMsg }}</div>


  
  
  <!-- 정상 데이터 렌더링 -->
  <div v-else class="row justify-content-center">
    <div
      class="col-12 col-md-6 d-flex align-items-stretch mb-4"
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
  
  <div> {{ depositList }} </div>


</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import DepositItem from '@/components/DepositItem.vue'

const depositList = ref([])
const isLoading = ref(true)
const errorMsg = ref('')

onMounted(async () => {
  try {
    const res = await axios.get(
      'http://127.0.0.1:8000/datas/api/deposit_results/'
    )
    console.log('[AllDepositView] res.data ▶', res.data)
    depositList.value = res.data
  } catch (err) {
    console.error('예금 상품 조회 실패:', err)
    errorMsg.value = '상품 정보를 불러오는 데 실패했습니다.'
  } finally {
    isLoading.value = false
  }
})
</script>

<style  scoped>

</style>