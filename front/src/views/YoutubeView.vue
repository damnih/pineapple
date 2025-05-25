<template>
  <div class="row mx-auto">
      <div class="video-container" v-if="searchResults.length">
      <div class="row" v-for="video in searchResults" :key="video.id.videoId">
        <div class="col-3">
        <VideoCard
          :videoId="video.id.videoId"
          :title="video.snippet.title"
        />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import VideoCard from '@/components/VideoCard.vue'

const route = useRoute()

const searchQuery = ref('')
const searchResults = ref([])

const searchVideos = async () => {
  const API_KEY = import.meta.env.VITE_YOUTUBE_API_KEY
  const query = searchQuery.value
  if (!query) return

  const url = `https://www.googleapis.com/youtube/v3/search?part=snippet&q=${encodeURIComponent(query)}&type=video&key=${API_KEY}&maxResults=10`

  try {
    const response = await fetch(url)
    const data = await response.json()
    searchResults.value = data.items
  } catch (error) {
    console.error('API 호출 실패:', error)
  }
}

onMounted(() => {
  searchQuery.value = route.query.q || ''
  searchVideos()
})

watch(() => route.query.q, (newQuery) => {
  searchQuery.value = newQuery
  searchVideos()
})
</script>

<style scoped>
.video-container {
  display: flex;
  flex-wrap: wrap;
  /* justify-content: space-around; */
  gap: 20px;
  padding: 20px;
}
</style>