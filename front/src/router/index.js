import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Depositview from '@/views/Depositview.vue'
import ExchangeRateView from '@/views/ExchangeRateView.vue'
import YoutubeView from '@/views/YoutubeView.vue'
import ArticleView from '@/views/ArticleView.vue'
import SignupView from '@/views/SignupView.vue'
import LoginView from '@/views/LoginView.vue'
import MapView from '@/views/MapView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import RecommendView from '@/views/RecommendView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ProfileView from '@/views/ProfileView.vue'
import AllDepositDetail from '@/views/AllDepositDetail.vue'
import AllDepositView from '@/views/AllDepositView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/deposit',
      name: 'deposit',
      component: Depositview,
    },
    {
      path: '/exchangerate',
      name: 'exchangerate',
      component: ExchangeRateView,
    },
    {
      path: '/youtubesearch',
      name: 'youtube',
      component: YoutubeView,
    },
    {
      path: '/article',
      name: 'article',
      component: ArticleView,
    },
    {
      path: '/article/:id',
      name: 'detail',
      component: ArticleDetailView,
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/map',
      name: 'map',
      component: MapView,
    },
    {
      path: '/recommend',
      name: 'recommend',
      component: RecommendView,
    },
    {
      path: '/create',
      name: 'create',
      component: ArticleCreateView,
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
      meta: { requiresAuth: true }
    },
    {
      path: '/profile/:username',
      name: 'user-profile',
      component: ProfileView,
      meta: { requiresAuth: true }
    },
    {
      path: '/all-deposit-detail/:id',
      name: 'alldepositdetail',
      component: AllDepositDetail,
    },
    {
      path: '/all-deposit',
      name: 'all-deposit',
      component: AllDepositView,
    },
  ],
})

export default router
