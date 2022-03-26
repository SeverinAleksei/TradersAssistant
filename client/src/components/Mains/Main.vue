<template>
  <div>
    <navigation-bar> </navigation-bar>
    {{this.$store.getters.TOKEN}}
  </div>
</template>

<script>
import NavigationBar from './NavBar.vue';

export default {
  name: 'Forum',
  data() {
    return {
      msg: 'dsfdsf',
      selected: '',
      tickers: ['BTC', 'MSFT'],
    };
  },
  components: {
    NavigationBar,
  },
  methods: {
  },
  created() {
  },
};
</script>
