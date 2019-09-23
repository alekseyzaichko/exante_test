<template>
  <div class="category-list">
    <template v-if="loading">
    Loading...
    </template>
    <template v-else>
        <CategoryItem
            v-for='item in categoryList' 
            :key=item.id
            :category=item
            :isCurrent=isCurrent(item.slug)
        />
    </template>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import CategoryItem from './CategoryItem.vue'
import _ from 'lodash'

export default {
  name: 'CategoryList',
  computed: mapState({
    categoryList: state => state.categoryList
  }),
  components: {
      CategoryItem
  },
  data () {
    return {
      loading: true
    }
  },
  created: function () {    
    fetch('/api/categories/').then((response) => response.json()).then((data) => {
        this.$store.commit('initCategoryList', _.keyBy(data, 'id'))
        this.loading = false
    })
  },
  methods: {
    isCurrent: function(slug) {
      return this.$route.params.categorySlug == slug && this.$route.name == 'byCategory'
    }
  }
}
</script>