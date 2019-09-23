<template>
  <div>
    <template v-if="loading">
    Loading...
    </template>
    <template v-else>
        <div class="news-details">
            <div class="date">{{ news.datetime }}</div>
            <div class="title">{{ news.title }}</div>
            <div class="image">
                <img :src='news.image'>
            </div>
            <div class="content">{{ news.content }}</div>
        </div>
    </template>
  </div>
</template>

<script>
export default {
  name: 'NewsDetails',
  data () {
    return {
      loading: true,
      news: Object
    }
  },
  watch: {
    '$route' () {
      this.loading = true
      this.fetchNews()
    }
  },
  mounted () {
    this.fetchNews()
  },
  methods: {
      fetchNews: function(){
        let newsId = this.$route.params.newsId
        let url = `/api/news/${newsId}/`
        fetch(url).then((response) => response.json()).then((data) => {
            this.news = data
            this.loading = false
        })
      }
  }
}
</script>
<style>
.news-details {
    padding: 20px;
}
.news-details .date {
    display: inline-block;
    font-style: italic;
    padding: 10px;
}
.news-details .title {
    display: inline-block;
    font-size: 20px;
}
.news-details .content {
    display: inline-block;
    font-size: 14px;
}

</style>