<template>
  <div class="news-list">
    <template v-if="loading">
    Loading...
    </template>
    <template v-else>
        <NewsItem
            v-for='item in newsList' 
            :key=item.id
            :newsItem=item
            :categorySlug=getCategorySlug(item.category_id)
        />
        <br>
        <div class='pagination'>
            <template v-if="prevPage">
              <router-link :to="`?page=${prevPage}`">&lt;&lt;</router-link>
            </template>
            <template v-else>&lt;&lt;</template>

            <span v-for='pageNumber in pageCount' :key=pageNumber>
                <template v-if="pageNumber==currentPage">
                    {{ pageNumber }} 
                </template>
                <template v-else>
                    <router-link :to="`?page=${pageNumber}`">{{ pageNumber }} </router-link>
                </template>
            </span>

            <template v-if="nextPage">
              <router-link :to="`?page=${nextPage}`">&gt;&gt;</router-link>
            </template>
            <template v-else>&gt;&gt;</template>
        </div>
    </template>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import NewsItem from './NewsItem.vue'

export default {
  name: 'NewsList',
  computed: {
    pageCount() {
      return Math.ceil(this.newsCount/this.pageSize)
    },
    prevPage() {
      return this.currentPage > 1 ? this.currentPage - 1 : null
    },
    nextPage() {
      return this.currentPage < this.pageCount ? +this.currentPage + 1 : null
    },
    ...mapState({
        categoryList: 'categoryList',
        newsList: 'newsList'
    })
  },
  components: {
      NewsItem
  },
  data () {
    return {
      loading: true,
      currentPage: 0,
      newsCount: 0,
      pageSize: 5
    }
  },
  watch: {
    '$route' () {
      this.loading = true
      this.fetchNewsList()
    }
  },
  mounted () {
    this.fetchNewsList()
  },
  methods: {
      fetchNewsList: function(){
        this.currentPage = this.$route.query.page || 1
        let url = `/api/news/?page=${this.currentPage}`

        let categorySlug = this.$route.params.categorySlug
        if (categorySlug){
            url = url + `&category=${categorySlug}`
        }
        
        fetch(url).then((response) => response.json()).then((data) => {
            this.$store.commit('updateNewsList', data.results)
            this.newsCount = data.count
            this.loading = false
        })
      },
      getCategorySlug: function(categoryId){
          return this.categoryList[categoryId].slug
      }
  }
}
</script>

<style>
.pagination{
    padding: 10px;
}

.pagination a{
    padding: 5px;
}
</style>