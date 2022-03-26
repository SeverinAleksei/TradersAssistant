<template>
  {{summary}}
  <apexchart
    ref="FitChart"  width="100%" height="auto" type="line"
    :options="options" :series="series">
  </apexchart>
  <apexchart
    ref="ResChart"  width="100%" height="auto" type="line"
    :options="options" :series="residuals">
  </apexchart>
  <apexchart
    ref="TestChart"  width="100%" height="auto" type="line"
    :options="options" :series="testseries">
  </apexchart>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      summary: '',
      residuals: [{
        name: 'Residuals data',
        data: [],
      }],
      series: [{
        type: 'line',
        name: 'Actual',
        data: [],
      }, {
        name: 'Predicted',
        data: [],
        type: 'line',
      }],
      testseries: [{
        type: 'line',
        name: 'Actual',
        data: [],
      }, {
        name: 'Predicted',
        data: [],
        type: 'line',
      }],
      options: {
        chart: {
          id: 'vuechart-example',
        },
        yaxis: {
          decimalsInFloat: 2,
        },
        xaxis: {
          labels: {
            show: false,
          },
        },
      },
    };
  },
  methods: {
    getForecast(payload) {
      const path = 'http://192.168.1.69:5000/getarimaforecast';
      axios.post(path, payload)
        .then((res) => {
          console.log(res.data.residuals);
          this.residuals[0].data = res.data.train_residuals;
          this.series[0].data = res.data.train_actual;
          this.series[1].data = res.data.train_predictions;
          this.testseries[0].data = res.data.test_actual;
          this.testseries[1].data = res.data.test_predictions;
          this.summary = res.data.summary;
          this.$refs.FitChart.updateSeries(this.series);
          this.$refs.ResChart.updateSeries(this.residuals);
          this.$refs.TestChart.updateSeries(this.testseries);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
  },
  mounted() {
    this.getForecast({ form: this.$store.getters.FORM, token: this.$store.getters.TOKEN });
  },
};
</script>
