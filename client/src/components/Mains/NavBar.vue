<template>
  <el-menu
    class="el-menu-demo"
    mode="horizontal"
    background-color = "purple"
    text-color = "white"
    active-text-color = "black"
    router
  >
    <el-menu-item index="/">Main page</el-menu-item>
    <el-sub-menu index="2">
      <template #title>Workspace</template>
      <el-menu-item index="2-1" icon = 'ds'>item one</el-menu-item>
      <el-menu-item index="2-2">item two</el-menu-item>
      <el-menu-item index="2-3">item three</el-menu-item>
      <el-sub-menu index="2-4">
        <template #title>item four</template>
        <el-menu-item index="2-4-1">item one</el-menu-item>
        <el-menu-item index="2-4-2">item two</el-menu-item>
        <el-menu-item index="2-4-3">item three</el-menu-item>
      </el-sub-menu>
    </el-sub-menu>
    <el-menu-item index="/forecast" >Forecast</el-menu-item>
    <el-menu-item index="/forum" disabled>Forum</el-menu-item>
    <el-menu-item index="/authorization">Log Out</el-menu-item>
  </el-menu>
  <div class="line"></div>
</template>
<script>
import axios from 'axios';

export default {
  name: 'NavBar',
  data() {
    return {
      logged: 'logged is unknown',
      username: this.$store.getters.USERNAME,
    };
  },
  methods: {
    logout() {
      this.$store.commit('UPDATE_TOKEN_USERNAME', { token: 'token', username: 'username' });
    },
    checkLogin() {
      const path = 'http://192.168.1.69:5000/check_logged';
      axios.get(path)
        .then((res) => {
          if (res.data === 'logged') {
            this.logged = 1;
          } else {
            window.location.href = '/authorization';
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.logged = 0;
          window.location.href = '/authorization';
        });
    },
  },
  created() {
    axios.defaults.headers.common = {
      Authorization: `Bearer ${this.$store.getters.TOKEN}`,
    };
    this.checkLogin();
  },
};

</script>

<style>

/* Modify the background color */
.navbar-custom {
    background-color: purple;
    margin-top: 0px;
}

</style>
