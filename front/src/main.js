import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { useAccountStore } from '@/stores/accounts.js'

import App from './App.vue'
import router from './router'
import axios from 'axios'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'



const app = createApp(App)
const pinia = createPinia()

app.use(router)
app.use(pinia)

const accountStore = useAccountStore()

const saved = localStorage.getItem('token')
if (saved) {
  axios.defaults.headers.common['Authorization'] = `Token ${saved}`
  accountStore.fetchUser()
}


app.mount('#app')
