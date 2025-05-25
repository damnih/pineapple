<template>
  <div class="d-flex justify-content-center bg-white py-5">
    <div class="border p-5 w-100" :style="{ maxWidth: width, minHeight: '500px' }">
      <slot></slot>
    </div>
  </div>
</template>

<script setup>
defineProps({
  width: {
    type: String,
    default: '900px'
  }
})
</script>

<style scoped></style>
