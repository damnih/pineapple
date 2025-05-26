import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useAccountStore = defineStore('account', () => {
  const ACCOUNT_API_URL = 'http://127.0.0.1:8000/accounts'
  const token = ref('')

    
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


  
  const logIn = function({id, pw}) {
    axios({
      method: 'POST',
      url: `${ACCOUNT_API_URL}/login/`,
      data: {
        id, pw
      }
    })
      .then(res => {
        token.value = res.data.key
      })
      .catch(err => {
        // console.log(err.response.data)          // ← 이 한 줄로, 서버가 보낸 에러 메시지를 찍을 수 있습니다.
        alert(err.response.data.errors)         // ← 사용자에게도 보여주고 싶다면
      })
  }


  return { ACCOUNT_API_URL, token, signUp, logIn }
})
