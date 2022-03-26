<template>
  <div>
    <div>
      <navigation-bar> </navigation-bar>
    </div>
    <div class="first purple">
      <form-component/>
    </div>
    <div class="another green">
        <progress-component />
        <charts-component />
    </div>
  </div>
</template>

<script>
import NavigationBar from '../NavBar.vue';
import FormComponent from './FormComponent.vue';
import ProgressComponent from './ProgressComponent.vue';
import ChartsComponent from './ChartsComponent.vue';

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
    FormComponent,
    ProgressComponent,
    ChartsComponent,
  },
  methods: {

  },
  created() {

  },
};
</script>

<style>
.first {
   position: relative;
   float:left;
   width: 30%;
   top:15px;
   border-right: 1px double purple;
   height: 100%;
}
.another {
   position: relative;
   top: 15px;
   right: 5%;
   width: 60%;
   float: right;
   height: 90%;
}
body {
  overflow-x: hidden; /* Hide scrollbars */
}
</style>
