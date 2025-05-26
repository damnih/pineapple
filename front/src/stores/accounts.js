import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useAccountStore = defineStore('account', () => {
  const ACCOUNT_API_URL = 'http://127.0.0.1:8000/accounts'
  const token = ref(localStorage.getItem('token') || '')
  // const token = ref('')
  const router = useRouter()

    
  // const signUp = ({ username, password, password2, age, name, nationality }) => {
  //   return axios.post(`${BASE}/signup/`, {
  //     username, password, password2, age, name, nationality
  //   })
  // }
  
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
      router.push({ name: 'home' })
    } catch (err) {
      console.error(err)
      const msg = err.response?.data?.errors
                || '로그인 중 문제가 발생했습니다.'
      alert(msg)
    }
  }

  const logOut = () => {
    token.value = ''
    localStorage.removeItem('token')
    delete axios.defaults.headers.common['Authorization']
    router.push({ name: 'home' })
  }

  
  // const logIn = function({id, pw}) {
  //   axios({
  //     method: 'POST',
  //     url: `${ACCOUNT_API_URL}/login/`,
  //     data: {
  //       id, pw
  //     }
  //   })
  //     .then(res => {
  //       token.value = res.data.key
  //     })
      
  //     .catch(err => {
  //       console.error(err)          // ← 어떤 에러가 왔는지 먼저 찍어 보고  
  //       // Optional chaining 으로 안전하게 꺼내기
  //       const msg = err.response?.data?.errors
  //           || '로그인 중 알 수 없는 오류가 발생했습니다.'
  //       alert(msg)
  //     })
  //     // .catch(err => {
  //     //   // console.log(err.response.data)          // ← 이 한 줄로, 서버가 보낸 에러 메시지를 찍을 수 있습니다.
  //     //   alert(err.response.data.errors)         // ← 사용자에게도 보여주고 싶다면
  //     // })
  // }


  return { ACCOUNT_API_URL, token, signUp, logIn, logOut }
})
