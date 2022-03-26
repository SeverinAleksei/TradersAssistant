<template>
  <div>
    {{fuller}}
    <h1 v-show = "this.$store.getters.MAXFORMSTEP <= 1"> Transformation component </h1>
    <apexchart v-show = "this.$store.getters.MAXFORMSTEP > 1"
      ref="TransformedChart"  width="100%" height="auto" type="line"
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
        name: 'Transformed data',
        data: [],
      }],
      form: {},
      test: 0,
      fuller: '',
    };
  },
  methods: {
    getTransformation(payload) {
      const path = 'http://192.168.1.69:5000/gettransformation';
      axios.post(path, payload)
        .then((res) => {
          this.series[0].data = res.data.out;
          this.fuller = { adfstat: res.data.adfstat, pvalue: res.data.pvalue };
          this.$refs.TransformedChart.updateSeries([{
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
    if (this.$store.getters.MAXFORMSTEP > 1) {
      this.getTransformation(this.$store.getters.FORM);
    }
  },
  watch: {
    '$store.state.form': {
      deep: true,
      handler() {
        setTimeout(() => {
          this.form = this.$store.getters.FORM;
          if (this.$store.getters.MAXFORMSTEP > 1) {
            this.getTransformation(this.$store.getters.FORM);
          }
        }, 300);
      },
    },
  },

};
</script>
