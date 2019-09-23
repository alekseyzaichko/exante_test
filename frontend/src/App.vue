<template>
    <div id="app">
      <div class='logo'>Breaking News</div>
      <CategoryList />
      <template v-if="$route.matched.length">
        <router-view />
      </template>
    </div>
</template>

<script>
import CategoryList from './components/CategoryList.vue'

export default {
  name: 'app',
  components: {
    CategoryList
  }
}
</script>

<style>
body {
	font: 12px Tahoma, sans-serif;
	margin: 0;
}
.logo {
  font-size: 30pt;
  font-weight: bold;
  font-style: italic;
  padding: 10px;
}
#app {
  margin-top: 10px;
}
</style>
