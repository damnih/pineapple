import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'


const saved = localStorage.getItem('token')
if (saved) {
  axios.defaults.headers.common['Authorization'] = `Token ${saved}`
}

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
