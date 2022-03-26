<template>
  <div>
    <div style='height:100px;'>
    </div>
    <div class = 'registrationForm'>
           <button class = 'formButtonActive' >SIGN IN</button>
           <button class = 'formButtonDeactive'  @click = 'authForm'>SIGN UP</button>
            <div>
                <label>Username</label>
                <input v-model= "username" type="text"
                class= 'inputForm' placeholder = 'Username'/>
            </div>
            <div>
                <label>Password</label>
                <input v-model = "password" type="password"
                class= 'inputForm' placeholder = 'Password'/>
            </div>
            <button class = 'buttonStyle' @click = 'toParent'>SIGN IN</button>
          </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      username: 'aleksei',
      password: '0000',
    };
  },
  methods: {
    authForm() {
      this.$emit('authform', '0');
    },
    toParent() {
      this.$emit('toparent', { username: this.username, password: this.password });
    },
  },
};

</script>
<style>
  @import './formstyle.css';
</style>
