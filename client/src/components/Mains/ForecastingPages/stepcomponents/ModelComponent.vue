<template>
  <div>
    <h1 v-show = "this.$store.getters.MAXFORMSTEP <= 2"> Model component </h1>
    <div v-show = "this.$store.getters.MAXFORMSTEP > 2">
      <arima-component />
    </div>
  </div>
</template>

<script>
import ArimaComponent from './modelcomponents/ArimaComponent.vue';

export default {
  data() {
    return {
      options: {
        chart: {
          id: 'vuechart-example',
        },
        xaxis: {
          type: 'datetime',
        },
        yaxis: {
          decimalsInFloat: 2,
        },
      },
      series: [{
        name: 'Original data',
        data: [[0, 0], [1, 1]],
      }],
      form: {},
      test: 0,
    };
  },
  components: {
    ArimaComponent,
  },
};
</script>
