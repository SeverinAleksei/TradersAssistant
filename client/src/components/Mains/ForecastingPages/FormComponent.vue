<template>
  <div>
    {{form}}
    <el-form @click = "this.$store.commit('UPDATE_FORMSTEP', 0)">
      <h3 class = "h3style" >Product </h3>
      <el-form-item style = "text-align:center">
        <el-select v-model="form.product" filterable placeholder="Select">
          <el-option
            v-for="item in options.product"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
        <el-row>
          <el-date-picker
            v-model="form.from"
            type="date"
            placeholder="Pick a date"
            style="width: 40%"
          ></el-date-picker>

        <el-col class="line" :span="2">-</el-col>
          <el-date-picker
            v-model="form.from2"
            placeholder="Pick a time"
            style="width: 40%"
          ></el-date-picker>
        </el-row>
        <el-select v-model="form.timeframe" >
          <el-option
            v-for="item in options.timeframe"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>

        </el-select>
        <el-switch v-model="form.missingdata"></el-switch>
      </el-form-item>
    </el-form>
    <el-form @click = "this.$store.commit('UPDATE_FORMSTEP', 1)">
      <h3 class = "h3style">Transformation </h3>
      <el-form-item style = "text-align:center">
        <el-select v-model="form.transformation" placeholder="Select data transformation">
          <el-option
            v-for="item in options.transformation"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
      </el-form-item>
    </el-form>
    <el-form @click = "this.$store.commit('UPDATE_FORMSTEP', 2)">
      <h3 class = "h3style">Model </h3>
      <el-form-item style = "text-align:center">
        <el-slider
        v-model.lazy="form.traintestsplit"
        class = 'center'
        ></el-slider>
          <el-select v-model="form.model" placeholder="Select model">
            <el-option
              v-for="item in options.model"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select>
        </el-form-item>
    </el-form>
    <el-form v-if = "form.model === 'ARIMA'">
      <arima-form />
    </el-form>
    <el-form v-if = "form.model === 'SARIMA'">
      <sarima-form />
    </el-form>
  </div>
</template>

<script>
import axios from 'axios';
import ArimaForm from './formcomponents/ArimaForm.vue';
import SarimaForm from './formcomponents/SarimaForm.vue';

export default {
  data() {
    return {
      test: {},
      form: {
        product: 'MSFT',
        from: '',
        from2: Date.now(),
        timeframe: '1d',
        missingdata: '',
        transformation: 'Natural logarithm',
        model: 'ARIMA',
        trainingdate1: '',
        trainingdate2: '',
        traintestsplit: 50,
        modelparameters: '',
      },
      options: {},
    };
  },
  components: {
    ArimaForm,
    SarimaForm,
  },
  methods: {
    getOptions() {
      const path = 'http://192.168.1.69:5000/getforecastoptions';
      axios.get(path)
        .then((res) => {
          this.options = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    getMaxStep(payload) {
      const path = 'http://192.168.1.69:5000/getmaxstep';
      axios.post(path, payload)
        .then((res) => {
          this.test = res.data;
          this.$store.commit('UPDATE_MAXFORMSTEP', res.data);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
  },
  mounted() {
    axios.defaults.headers.common = {
      Authorization: `Bearer ${this.$store.getters.TOKEN}`,
    };
    this.getOptions();
    this.$store.commit('UPDATE_FORM', this.form);
  },
  watch: {
    form: {
      deep: true,
      handler() {
        this.$store.commit('UPDATE_FORM', this.form);
        this.getMaxStep(this.form);
      },
    },
  },
};
</script>
<style>
.el-form-item--label-top {
  width: auto;
  float: none;
  display: inline-block;
  text-align: center;
  padding: 0 0 10px;
}
.h3style {
  font-size: 16px;
  margin-top: 0px;
  margin-bottom: 10px;
  margin-left: 0;
  margin-right: 0;
  font-weight: normal;
  text-align:center;
}
.center {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50px;
  border: 0px solid green;

}

</style>
