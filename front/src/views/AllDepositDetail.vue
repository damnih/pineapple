<template>
  <ArticleBox>
    <div class="detail-container">
      <div class="d-flex justify-content-between align-items-center">
        <h1 class="title">정기예금 상세</h1>
        <button @click="toggleLike" class="heart-btn">
          {{ isLiked ? '♥' : '♡' }}
        </button>
      </div>
      <br><hr><br>
      <div class="row">
        <div class="label">상품명</div>
        <div class="value">{{ deposit.fin_prdt_nm }}</div>
        <br><br>
      </div>
      <div class="row">
        <div class="label">금융회사명</div>
        <div class="value">{{ deposit.kor_co_nm }}</div>
        <br><br>
      </div>
      <div class="row">
        <div class="label">가입 방법</div>
        <div class="value">{{ deposit.join_way }}</div>
        <br><br>
      </div>
      <div class="row">
        <div class="label">기본 금리</div>
        <div class="value" v-if="deposit.options">
          {{ deposit.options[0].intr_rate }} %
        </div>
        <div class="value" v-else>
          금리 정보 없음
        </div>
        <br><br>
      </div>
      <div class="row">
        <div class="label">우대 금리</div>
        <div class="value" v-if="deposit.options">
          {{ deposit.options[0].intr_rate2 }} %
        </div>
        <div class="value" v-else>
          금리 정보 없음
        </div>
        <br><br>
      </div>
      <div class="row">
        <div class="label">우대 조건</div>
        <div class="value">{{ deposit.spcl_cnd }}</div>
        <br><br>
      </div>
      <div class="row">
        <div class="label">특이사항</div>
        <div class="value">{{ deposit.etc_note }}</div>
        <br><br>
      </div>
    </div>
  </ArticleBox>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import ArticleBox from '@/components/ArticleBox.vue'
import { useAccountStore } from '@/stores/accounts.js'

const props = defineProps({
  deposit: Object,  // deposit에는 최소한 id, is_liked 같은 정보 포함되어 있어야 함
})

const account = useAccountStore()
const isLiked = ref(false)

const deposit = ref('')
const route = useRoute()

const toggleLike = async () => {
  try {
    const res = await axios.post(
      `http://127.0.0.1:8000/datas/deposit_results/${route.params.id}/toggle-like/`,
      {},
      {
        headers: {
          Authorization: `Token ${localStorage.getItem('token')}`,
        },
      }
    )

    // 뷰 함수에서 added 또는 removed 중 하나가 반환됨
    if (res.data.added) {
      isLiked.value = true
    } else if (res.data.removed) {
      isLiked.value = false
    }
  } catch (err) {
    console.error('하트 토글 실패:', err)
  }
}

onMounted(async () => {
  try {
    const res = await axios.get(`http://127.0.0.1:8000/datas/deposit_results/${route.params.id}/`)
    deposit.value = res.data
  } catch (err) {
    console.error('예금 상세 조회 실패:', err)
  }
})

// 우대조건 줄바꿈 처리용 (단순 줄바꿈 문자 기준으로 HTML 줄바꿈 처리)
const formattedSpclCnd = computed(() =>
  deposit.value?.spcl_cnd?.replace(/\n/g, '<br>') || ''
)
</script>

<style scoped>
.detail-container {
  margin-left: 30px;
  color: #4a4a4a; /* 진한 회색 */
  font-size: 16px;
}

.title {
  font-weight: bold;
  color: #2f2f2f;
}

.row {
  display: flex;
  margin-bottom: 10px;
}

.label {
  width: 150px;
  font-weight: bold;
}

.value {
  flex: 1;
  white-space: pre-wrap;
}

.heart-btn {
  font-size: 2rem;
  border: none;
  background: none;
  cursor: pointer;
  color: #ff4d4d;
}
</style>