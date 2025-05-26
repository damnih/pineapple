<template>
  <p><strong>{{ comment.comment_author }}</strong> - {{ comment.created_at }}</p>
  <p>{{ comment.content }}</p>
</template>

<script setup>
defineProps({
  comment: Object
})
</script>

<style scoped></style>