import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useAccountStore = defineStore('account', () => {
  const ACCOUNT_API_URL = 'http://127.0.0.1:8000/accounts'
  const token = ref(localStorage.getItem('token') || '')
  // const token = ref('')
  const router = useRouter()

  // 로그인한 사용자 정보를 얻어오기 위해 일단 여기 비운 거 하나 만들어둠
  const user  = ref(null) 
  
  const signUp = function ({username, password, password2, age, name, nationality}) {
    axios({
      method: 'POST',
      url: `${ACCOUNT_API_URL}/signup/`,
      data: {
            username: username,
            password: password,
            password2: password2,
            age: age,
            name: name,
            nationality: nationality
          }
    })
      .then(res => {
        console.log('회원가입 성공!')
        // 회원가입 성공 시 팝업과 함께 메인 페이지로 이동하는 로직 추가 
        alert(res.data.message)  // "회원가입 성공"
        router.push('/') 
      })
      .catch(err => console.log(err))
  }


 // 2) 현재 토큰으로 내 정보 가져오기
  const fetchUser = async () => {
    if (!token.value) return
    try {
      const { data } = await axios.get(`${ACCOUNT_API_URL}/me/`)
      user.value = data
    } catch (err) {
      console.error('유저 프로필 조회 실패', err)
    }
  }

  const logIn = async ({ id, pw }) => {
    try {
      const res = await axios.post(
        `${ACCOUNT_API_URL}/login/`,
        { id, pw }
      )
      // 성공 시 토큰 저장 → 헤더 설정 → 리다이렉트
      token.value = res.data.key
      localStorage.setItem('token', token.value)
      axios.defaults.headers.common['Authorization'] = `Token ${token.value}`
      
      // 프로필 정보 가져오는 걸 여기서!! 
      await fetchUser()

      // 로그인 성공하면 홈화면으로 ㄱㄱ 
      router.push({ name: 'home' })  
    } 
    // 여긴 에러 뜨면 뭔지 출력해주기 위한 구간 
      catch (err) {
      console.error(err)
      const msg = err.response?.data?.errors
                || '로그인 중 문제가 발생했습니다.'
      alert(msg)
    }
  }

  // 3) 로그아웃
  const logOut = () => {
    token.value = ''
    localStorage.removeItem('token')
    delete axios.defaults.headers.common['Authorization']
    router.push({ name: 'home' })
  }


  return { ACCOUNT_API_URL, token, signUp, logIn, logOut, fetchUser, user }
})
