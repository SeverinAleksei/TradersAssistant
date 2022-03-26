<template>
  <div>
    <div v-show= "auth== 1">
      <auth-form @authform = "authFormChange($event)"
        @toparent= "sentForm($event)"> </auth-form>
    </div>
    <div v-show= "auth == 0">
      <signup-form @authform= "authFormChange($event)"
        @toparent = "sentForm($event)"> </signup-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ElNotification } from 'element-plus';
import AuthForm from './AuthForm.vue';
import SignupForm from './SignupForm.vue';

export default {
  name: 'Auth',
  data() {
    return {
      auth: 1,
      user: {
        username: '',
        email: '',
        password: '',
      },
      notification: '  ',
      token: {},
      allusers: '',
    };
  },
  components: {
    AuthForm,
    SignupForm,
  },
  methods: {
    authFormChange(state) {
      this.auth = state;
    },
    sentForm(result) {
      // eslint-disable-next-line
      var bodyFormData = new FormData();
      bodyFormData.append('username', result.username);
      bodyFormData.append('email', result.email);
      bodyFormData.append('password', result.password);
      bodyFormData.append('auth', this.auth);

      if (this.auth === '1') {
        const path = 'http://192.168.1.69:5000/login';
        axios.post(path, bodyFormData)
          .then((res) => {
            this.notification = res.data.result;
            this.token = res.data.access_token;
            axios.defaults.headers.common = { Authorization: `Bearer ${this.token}` };
            this.$store.commit('UPDATE_TOKEN_USERNAME', { token: this.token, username: result.username });
            if (res.data.result === 'You are logged') {
              ElNotification({ type: 'success', message: this.notification });
              window.location.href = '/';
            } else {
              ElNotification({ type: 'warning', message: this.notification });
            }
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error);
            ElNotification({ type: 'warning', message: this.notification });
          });
      }
      if (this.auth === '0') {
        const path = 'http://192.168.1.69:5000/signup';
        axios.post(path, bodyFormData)
          .then((res) => {
            this.notification = res.data.message;
            if (this.notification === 'User added successfully') {
              ElNotification({ type: 'success', message: this.notification });
            } else {
              ElNotification({ type: 'warning', message: this.notification });
            }
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error);
            ElNotification({ type: 'warning', message: this.notification });
          });
      }
      return 'Wrong input';
    },
    showUsers() {
      const path = 'http://192.168.1.69:5000/user';
      axios.get(path)
        .then((res) => {
          this.allusers = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
  },
  created() {
    this.auth = '1';
    this.$store.commit('UPDATE_TOKEN_USERNAME', { token: 'token', username: 'username' });
    ElNotification({ message: 'Hello user!' });
  },
};
</script>

<style>
.center {
  text-align: center;
}
.vue-notification {
  margin: 0 5px 5px;
  padding: 10px;
  font-size: 18px;
  border-radius: 40px;
  text-align: center;
}
</style>
<style scoped>
html,
body {
    height: 100%;
    background-color: #6e72fc;
    background-image: linear-gradient(45deg, #6e72fc 0%, #ad1deb 74%)
}
</style>
