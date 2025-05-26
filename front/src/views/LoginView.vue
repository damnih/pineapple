<template>
    
    
    
    
    <Box>
      <form @submit.prevent="onLogIn">
        <div class="mb-3">
          <label for="id" class="form-label fw-semibold">ID</label>
          <input v-model="id" type="text" class="form-control" id="id" placeholder="Enter your ID" />
        </div>

        <div class="mb-3">
          <label for="password" class="form-label fw-semibold">Password</label>
          <input v-model="pw" type="password" class="form-control" id="pw" placeholder="Enter your password" />
        </div>

        <button type="submit" class="btn btn-primary w-100">Log In</button>
      </form>
    </Box>
</template>

<script setup>
  import Box from '@/components/Box.vue'
  import { ref } from 'vue'
  import { useAccountStore } from '@/stores/accounts.js'

  const accountStore = useAccountStore()

  const id = ref('')
  const pw = ref('')

  const onLogIn = function () {
    const userInfo = {
      id: id.value,
      pw: pw.value
    }
    console.log(id.value, pw.value)
    accountStore.logIn(userInfo)
  }
</script>

<style scoped></style>