<template>
    <Box>
      <form @submit.prevent="onSignUp">
        <div class="mb-3">
          <label for="id" class="form-label fw-semibold">ID</label>
          <input type="text" class="form-control" id="id" placeholder="Enter your ID" />
        </div>

        <div class="mb-3">
          <label for="password" class="form-label fw-semibold">Password</label>
          <input type="password" class="form-control" id="pw" placeholder="Enter your password" />
        </div>

        <div class="mb-3">
          <label for="password2" class="form-label fw-semibold">Password</label>
          <input type="password" class="form-control" id="pw2" placeholder="Enter once again" />
        </div>

        <div class="mb-3">
          <label for="age" class="form-label fw-semibold">Age</label>
          <input type="number" class="form-control" id="age" placeholder="Enter your age" />
        </div>

        <div class="mb-3">
          <label for="name" class="form-label fw-semibold">Name</label>
          <input type="text" class="form-control" id="name" placeholder="Enter your name" />
        </div>

        <div class="mb-3">
          <label for="nationality" class="form-label fw-semibold">Nationality</label>
          <input type="text" class="form-control" id="nationality" placeholder="Enter your nationality" />
        </div>

        <button type="submit" class="btn btn-primary w-100">Sign Up</button>
      </form>
    </Box>
</template>

<script setup>
  import Box from '@/components/Box.vue'
  import { ref } from 'vue'
  import axios from 'axios'
  import { useAccountStore } from '@/stores/accounts.js'
  
  const accountStore = useAccountStore()
  
  const id = ref('')
  const pw = ref('')
  const pw2 = ref('')
  const age = ref('')
  const nationality = ref('')

  const onSignUp = function () {
    const userInfo = {
      id: id.value,
      pw: pw.value,
      pw2: pw2.value,
      age: age.value,
      nationality: nationality.value
    }
    accountStore.signUp(userInfo)
  }
</script>

<style scoped></style>