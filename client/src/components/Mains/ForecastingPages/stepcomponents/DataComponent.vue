<template>
  <div>
    <h1 v-show = "this.$store.getters.MAXFORMSTEP === 0"> Choose data </h1>
    <apexchart v-show= "this.$store.getters.MAXFORMSTEP "
      ref="realtimeChart"  width="100%" height="auto" type="line"
      :options="options" :series="[series[0]]">
    </apexchart>
  </div>
</template>

<script>
import axios from 'axios';

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
        data: [[]],
      }],
      form: {},
      test: 0,
    };
  },
  methods: {
    getData(payload) {
      const path = 'http://192.168.1.69:5000/getpricedata';
      axios.post(path, payload)
        .then((res) => {
          this.series[0].data = res.data.out;
          this.$refs.realtimeChart.updateSeries([{
            data: this.series[0].data,
          }], true);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    getHelloWorld() {
      const path = 'http://192.168.1.69:5000/gethelloworld';
      axios.post(path, { token: this.$store.getters.TOKEN })
        .then((res) => {
          this.series[0].data = res.data.out;
          this.$refs.realtimeChart.updateSeries([{
            data: this.series[0].data,
          }], true);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
  },
  mounted() {
    this.form = this.$store.getters.FORM;
    if (this.$store.getters.MAXFORMSTEP > 0) {
      this.getData(this.$store.getters.FORM);
    }
    this.getHelloWorld();
  },
  watch: {
    '$store.state.form': {
      deep: true,
      handler() {
        setTimeout(() => {
          this.form = this.$store.getters.FORM;
          if (this.$store.getters.MAXFORMSTEP > 0) {
            this.getData(this.$store.getters.FORM);
          }
        }, 300);
      },
    },
  },

};
</script>
