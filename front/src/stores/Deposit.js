import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useAnswersStore = defineStore('Answers', {
  state: () => ({
    schedule_ans: null,
    budget_ans: null,
    destination_ans: '',
  }),
})