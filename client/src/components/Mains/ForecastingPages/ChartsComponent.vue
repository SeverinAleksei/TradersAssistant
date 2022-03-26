<template>
  <div>
    <data-component v-if="this.$store.getters.FORMSTEP === 0"/>
    <transformation-component v-if="this.$store.getters.FORMSTEP === 1" />
    <model-component v-if="this.$store.getters.FORMSTEP === 2" />
    <fit-component v-if="this.$store.getters.FORMSTEP === 3" />
    <forecast-component v-if="this.$store.getters.FORMSTEP === 4" />
  </div>
</template>

<script>

import axios from 'axios';
import DataComponent from './stepcomponents/DataComponent.vue';
import TransformationComponent from './stepcomponents/TransformationComponent.vue';
import ModelComponent from './stepcomponents/ModelComponent.vue';
import FitComponent from './stepcomponents/FitComponent.vue';
import ForecastComponent from './stepcomponents/ForecastComponent.vue';

export default {
  data() {
    return {
      form: {},
    };
  },
  components: {
    DataComponent,
    TransformationComponent,
    ModelComponent,
    FitComponent,
    ForecastComponent,
  },
  methods: {

  },
  mounted() {
    axios.defaults.headers.common = {
      Authorization: `Bearer ${this.$store.getters.TOKEN}`,
    };
  },
};
</script>
