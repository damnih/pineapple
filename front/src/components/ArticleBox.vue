<template>
    <div class="d-flex justify-content-center vh-100 bg-white">
      <div class="border p-5 my-5" :style="{ width: width }">
        <slot></slot>
    </div>
  </div>
</template>

<script setup>
  defineProps({
  width: {
    type: String,
    default: '800px'
  }
})
</script>

<style scoped></style>