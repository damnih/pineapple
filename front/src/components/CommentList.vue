<!-- CommentList.vue -->

<template>
  <div v-if="comments.length">
    <CommentListItem 
    v-for="(comment, index) in comments" 
    :key="index" 
    :comment="comment"
    class="mb-3"
    @deleted="$emit('deleted')"
    />
  </div>
  <div v-else>
    <p>댓글이 없습니다.</p>
  </div>
</template>

<script setup>
import CommentListItem from "@/components/CommentListItem.vue"

defineProps({
  comments: Array
})

defineEmits(['deleted'])
</script>

<style scoped></style>