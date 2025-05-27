<template>
  <div class="card shadow border-0" style="width: 410px;">
    <a :href="'https://www.youtube.com/watch?v=' + videoId" target="_blank">
      <img
        :src="'https://img.youtube.com/vi/' + videoId + '/hqdefault.jpg'"
        class="card-img-top thumbnail-img"
        :alt="title"
      >
    </a>
    <div class="card-body">
      <h5 class="card-title">{{ title }}</h5>
    </div>
  </div>
</template>

<script setup>
defineProps({
  videoId: {
    type: String,
    required: true
  },
  title: {
    type: String,
    required: true
  },
})
</script>

<style scoped>
.card-title {
  font-family: Verdana, Geneva, Tahoma, sans-serif;
  font-size: 15pt;
}

.card-body {
  padding: 3rem;
}

.thumbnail-img {
  height: 200px;
  object-fit: cover;
}
</style>
