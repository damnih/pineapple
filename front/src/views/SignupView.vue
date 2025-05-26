<template>
    <Box>
      <form @submit.prevent="onSignUp">
        <div class="mb-3">
          <label for="id" class="form-label fw-semibold">ID</label>
          <input type="text" class="form-control" id="username" v-model="username" placeholder="Enter your ID" />
        </div>

        <div class="mb-3">
          <label for="password" class="form-label fw-semibold">Password</label>
          <input type="password" class="form-control" id="password" v-model="password" placeholder="Enter your password" />
        </div>

        <div class="mb-3">
          <label for="password2" class="form-label fw-semibold">Password</label>
          <input type="password" class="form-control" id="password2" v-model="password2" placeholder="Enter once again" />
        </div>

        <div class="mb-3">
          <label for="age" class="form-label fw-semibold">Age</label>
          <input type="number" class="form-control" id="age" v-model="age" placeholder="Enter your age" />
        </div>

        <div class="mb-3">
          <label for="name" class="form-label fw-semibold">Name</label>
          <input type="text" class="form-control" id="name" v-model="name" placeholder="Enter your name" />
        </div>

        <div class="mb-3">
          <label for="nationality" class="form-label fw-semibold">Nationality</label>
          <input type="text" class="form-control" id="nationality" v-model="nationality" placeholder="Enter your nationality" />
        </div>

        <button type="submit" class="btn btn-primary w-100">Sign Up</button>
      </form>
    </Box>
</template>

<script setup>
  import Box from '@/components/Box.vue'
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import axios from 'axios'
  import { useAccountStore } from '@/stores/accounts.js'
  
  const router = useRouter()
  const accountStore = useAccountStore()
  
  const username = ref('')
  const password = ref('')
  const password2 = ref('')
  const age = ref('')
  const name = ref('')
  const nationality = ref('')

  const onSignUp = function () {
    const userInfo = {

      username: username.value,  // "id" → "username"으로 변경
      password: password.value,
      password2: password2.value,
      age: parseInt(age.value),
      name: name.value,
      nationality: nationality.value
    }
    accountStore.signUp(userInfo)
  }


</script>

<style scoped></style>