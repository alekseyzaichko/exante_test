<template>
  <div class="category-item">
      <template v-if="isCurrent">
        {{ category.name }}
      </template>
      <template v-else>
        <router-link :to="`/${category.slug}/`">{{ category.name }}</router-link>
      </template>
  </div>
</template>

<script>

export default {
  name: 'CategoryItem',
  props: {
    category: Object,
    isCurrent: Boolean
  }
}
</script>

<style>
.category-item {
    display: inline;
    padding: 10px;
    font-size: 16pt;

}
</style>