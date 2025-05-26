<!-- <template>
  <p><strong>{{ comment.comment_author.username }}</strong> - {{ comment.created_at }}</p>
  <p>{{ comment.content }}</p>
</template> -->

<template>
  <!-- <p v-if="comment.comment_author">
    <strong>{{ comment.comment_author.username }}</strong> - {{ comment.created_at }}
  </p>
  <p v-else>
    <strong>알 수 없음</strong> - {{ comment.created_at }}
  </p> -->
  <p>{{ comment.content }}</p>
</template>

<script setup>
defineProps({
  comment: Object
})
</script>

<style scoped></style>