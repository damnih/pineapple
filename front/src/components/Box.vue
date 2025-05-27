<template>
  <div class="box-wrapper">
    <div class="box rounded-4 shadow-sm p-4" style="width: 400px;">
      <slot />
    </div>
  </div>
</template>

<script setup>
//   defineProps({
//   width: {
//     type: String,
//     default: '400px'
//   }
// })
</script>


<style scoped>
.box-wrapper {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding-top: 10vh;
}
</style>