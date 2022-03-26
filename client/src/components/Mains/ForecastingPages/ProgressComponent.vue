<template>
  {{$store.getters.FORMSTEP}}
  {{$store.getters.MAXFORMSTEP}}
  <el-steps :active="this.$store.getters.FORMSTEP" finish-status= "success"
             process-status = "process" simple>
    <el-step @click = "this.$store.commit('UPDATE_FORMSTEP',0)" title=" Data"></el-step>
    <el-step @click = "this.$store.commit('UPDATE_FORMSTEP',1)" title="Transform"></el-step>
    <el-step @click = "this.$store.commit('UPDATE_FORMSTEP',2)" title="Model"></el-step>
    <el-step @click = "this.$store.commit('UPDATE_FORMSTEP',3)" title="parameters"></el-step>
    <el-step @click = "this.$store.commit('UPDATE_FORMSTEP',4)" title="Forecast"></el-step>
  </el-steps>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      test: 1,
    };
  },
  methods: {},
  mounted() {
    this.$store.commit('UPDATE_FORMSTEP', 0);
    this.$store.commit('UPDATE_MAXFORMSTEP', 0);
    axios.defaults.headers.common = {
      Authorization: `Bearer ${this.$store.getters.TOKEN}`,
    };
  },
};
</script>
