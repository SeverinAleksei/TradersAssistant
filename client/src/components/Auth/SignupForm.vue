<template>
    <div >
      <div style='height:100px;'>
      </div>
        <div class = 'registrationForm'>
          <button class = 'formButtonDeactive' @click = 'authForm'>SIGN IN</button>
          <button class = 'formButtonActive' >SIGN UP</button>
            <div >
                <label>Username</label>
                <input v-model = "username" type="text" class='inputForm'/>
            </div>
            <div >
                <label>Email address</label>
                <input v-model = "email" type="email" class='inputForm' />
            </div>

            <div >
                <label>Password</label>
                <input v-model = "password" type="password" class='inputForm' />
            </div>

            <button @click = 'toParent' class = 'buttonStyle'>
              CREATE ACCOUNT</button>
        </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      username: 'aleksei',
      email: 'arseverin@mail.ru',
      password: '0000',
    };
  },
  methods: {
    authForm() {
      this.$emit('authform', '1');
    },
    toParent() {
      this.$emit('toparent',
        { username: this.username, email: this.email, password: this.password });
    },
  },
};

</script>
<style>
  @import './formstyle.css';
</style>
