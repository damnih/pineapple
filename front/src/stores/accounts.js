import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useAccountStore = defineStore('account', () => {
  const ACCOUNT_API_URL = 'http://127.0.0.1:8000/accounts'
  const token = ref('')

    const signUp = function ({id, pw, pw2, age, name, nationality}) {
    axios({
      method: 'POST',
      url: `${ACCOUNT_API_URL}/signup/`,
      data: {
        id, pw, pw2, age, name, nationality
      }
    })
      .then(res => {
        console.log('회원가입 성공!')
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
      .catch(err => console.log(err))
  }


  return { ACCOUNT_API_URL, token, signUp, logIn }
})
