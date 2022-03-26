<template>
  <div>
    <navigation-bar> fhggf</navigation-bar>
    <chat-window
      :current-user-id="currentUserId"
      :rooms="rooms"
      :messages="messages"
      height = "830px"
    />
  </div>
</template>

<script>
import axios from 'axios';
import ChatWindow from 'vue-advanced-chat';
import 'vue-advanced-chat/dist/vue-advanced-chat.css';
import NavigationBar from './NavBar.vue';

export default {
  name: 'Forum',
  data() {
    return {
      msg: 'dsfdsf',
      selected: '',
      tickers: ['BTC', 'MSFT'],
      rooms: [],
      messages: [],
      currentUserId: 1234,
    };
  },
  components: {
    NavigationBar,
    ChatWindow,
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/forum';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
