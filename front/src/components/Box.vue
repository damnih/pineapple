<template>
    <div class="d-flex justify-content-center align-items-center vh-100 bg-white">
      <div class="border rounded-4 p-5" :style="{ width: width }">
        <slot></slot>
    </div>
  </div>
</template>

<script setup>
  defineProps({
  width: {
    type: String,
    default: '400px'
  }
})
</script>

<style scoped></style>