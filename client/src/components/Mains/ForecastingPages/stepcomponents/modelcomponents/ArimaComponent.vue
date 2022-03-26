<template>
  <div style = "width:100%">
    ARIMA
    <apexchart
      ref="ACFchart"  width="100%" height="auto" type="bar"
      :options="options" :series="[seriesACF[0]]">
    </apexchart>
    <apexchart
      ref="PACFchart"  width="100%" height="auto" type="bar"
      :options="options" :series="[seriesPACF[0]]">
    </apexchart>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      options: {
        yaxis: {
          min: -1,
          max: 1,
          decimalsInFloat: 2,
          labels: {
            show: true,
          },
        },
        dataLabels: {
          enabled: false,
        },
      },
      seriesACF: [{
        name: 'ACF',
        data: [0, 2],
      }],
      seriesPACF: [{
        name: 'PACF',
        data: [0, 2, 2, 5, 6, 3, 5, 6, 4],
      }],
      form: {},
      test: 0,
    };
  },
  methods: {
    getACFPACF(payload) {
      const path = 'http://192.168.1.69:5000/getACFPACF';
      axios.post(path, payload)
        .then((res) => {
          this.seriesACF[0].data = res.data.acf;
          this.seriesPACF[0].data = res.data.pacf;

          this.$refs.ACFchart.updateSeries([{
            data: this.seriesACF[0].data,
          }], true);
          this.$refs.PACFchart.updateSeries([{
            data: this.seriesPACF[0].data,
          }], true);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    check() {
      const path = 'http://192.168.1.69:5000/forecast';
      axios.get(path)
        .then((res) => {
          console.log(res.data);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
  },
  mounted() {
    this.getACFPACF({ form: this.$store.getters.FORM, token: this.$store.getters.TOKEN });
  },
  watch: {
    '$store.state.form': {
      deep: true,
      handler() {
        setTimeout(() => {
          this.form = this.$store.getters.FORM;
          if (this.$store.getters.MAXFORMSTEP > 2) {
            this.getACFPACF({ form: this.$store.getters.FORM, token: this.$store.getters.TOKEN });
          }
        }, 300);
      },
    },
  },
};
</script>
