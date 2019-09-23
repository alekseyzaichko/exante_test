<template>
  <div class="news-block">
      <div class="date">{{ newsItem.datetime }}</div>
      <div class='title'><router-link :to="`/${categorySlug}/${newsItem.id}/`">{{ newsItem.title }}</router-link></div>
  </div>
</template>

<script>

export default {
  name: 'NewsItem',
  props: {
    newsItem: Object,
    categorySlug: String
  }
}
</script>

<style>
.news-block {
    padding: 5px;
}
.date {
    display: inline-block;
    font-style: italic;
    padding: 10px;
}
.title {
    display: inline-block;
    font-weight: bold;
}

</style>