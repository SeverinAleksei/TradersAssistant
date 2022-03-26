<template>
  {{ARIMAform}}
  <h3 class = "h3style">Model Parameters </h3>
  <el-form-item style = "text-align:center">
      <el-input v-model="ARIMAform.ar"
                style="width: 20%" placeholder="AR"></el-input>
      <el-input v-model="ARIMAform.i"
                style="width: 20%" placeholder="I"></el-input>
      <el-input v-model="ARIMAform.ma"
                style="width: 20%" placeholder="MA"></el-input>
  </el-form-item>
  <el-form-item style = "text-align:center">
      <el-input v-model="ARIMAform.sar"
                style="width: 20%" placeholder="SAR"></el-input>
      <el-input v-model="ARIMAform.si"
                style="width: 20%" placeholder="SI"></el-input>
      <el-input v-model="ARIMAform.sma"
                style="width: 20%" placeholder="SMA"></el-input>
  </el-form-item>
</template>

<script>
export default {
  data() {
    return {
      ARIMAform: {
        ar: '2',
        i: '0',
        ma: '2',
        sar: '2',
        si: '0',
        sma: '2',
      },
    };
  },
  watch: {
    ARIMAform: {
      deep: true,
      handler() {
        if (this.ARIMAform.ar !== '' && this.ARIMAform.i !== '' && this.ARIMAform.ma !== ''
         && this.ARIMAform.sar !== '' && this.ARIMAform.si !== '' && this.ARIMAform.sma !== '') {
          const form = this.$store.getters.FORM;
          form.modelparameters = {
            ar: this.ARIMAform.ar,
            i: this.ARIMAform.i,
            ma: this.ARIMAform.ma,
            sar: this.ARIMAform.sar,
            si: this.ARIMAform.si,
            sma: this.ARIMAform.sma,
          };
          this.$store.commit('UPDATE_FORM', form);
        }
      },
    },
  },
};
</script>
