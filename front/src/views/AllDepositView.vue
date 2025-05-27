<template>
  <div class="container mt-3">
    <label>
      은행 선택:
      <select v-model="selectedBank" @change="fetchProducts" class="form-select w-auto d-inline-block ms-2">
        <option value="">전체</option>
        <option v-for="bank in banks" :key="bank" :value="bank">
          {{ bank }}
        </option>
      </select>
    </label>

    <div v-if="loading" class="mt-3">로딩 중…</div>
    <div v-else-if="error" class="mt-3 text-danger">{{ error }}</div>

    <div v-else class="row justify-content-center mt-4">
      <div
        v-for="product in depositList"
        :key="product.id"
        class="col-12 col-md-5 col-lg-4 mb-4"
      >
        <RouterLink
          :to="{ name: 'alldepositdetail', params: { id: product.id } }"
          class="card p-3 text-decoration-none text-dark h-100 shadow-sm"
        >
          <h5 class="mb-1">{{ product.fin_prdt_nm }}</h5>
          <p class="mb-1"><strong>은행:</strong> {{ product.kor_co_nm }}</p>
          <p class="mb-1"><strong>가입방법:</strong> {{ product.join_way }}</p>
          <hr>
          <ul class="mb-0 ps-3">
            <li 
              v-for="opt in product.options" 
              :key="opt.id"
            >
              {{ opt.save_trm }}개월 · {{ opt.intr_rate }}% (우대 {{ opt.intr_rate2 }}%)
            </li>
          </ul>
        </RouterLink>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const depositList   = ref([])
const banks         = ref([])
const selectedBank  = ref('')
const loading       = ref(false)
const error         = ref('')

const fetchProducts = async () => {
  loading.value = true
  error.value   = ''
  try {
    const params = {}
    if (selectedBank.value) {
      params.kor_co_nm = selectedBank.value
    }
    const res = await axios.get(
      'http://127.0.0.1:8000/datas/deposit_results/',
      { params }
    )
    depositList.value = res.data

    // 은행 목록 추출 (중복 제거)
    banks.value = Array.from(
      new Set(res.data.map(p => p.kor_co_nm))
    )
  } catch (e) {
    console.error(e)
    error.value = '상품 목록을 불러오지 못했습니다.'
  } finally {
    loading.value = false
  }
}

onMounted(fetchProducts)
</script>

<style scoped>
select {
  padding: 0.25rem 0.5rem;
  margin-left: 0.5rem;
}
.card {
  cursor: pointer;
  transition: transform 0.1s;
}
.card:hover {
  transform: translateY(-3px);
}
</style>
