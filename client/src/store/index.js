import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';

/* eslint-disable import/prefer-default-export */
export const store = new Vuex.Store({
  plugins: [createPersistedState({
    storage: window.sessionStorage,
  })],
  state: {
    token: 'token',
    username: 'username',
    form: {},
    formstep: { max: 0, actual: 0 },
  },
  getters: {
    // eslint-disable-next-line
    TOKEN: state => {
      return state.token;
    },
    // eslint-disable-next-line
    USERNAME: state => {
      return state.username;
    },
    // eslint-disable-next-line
    FORM: state => {
      return state.form;
    },
    // eslint-disable-next-line
    FORMSTEP: state => {
      return state.formstep.actual;
    },
    // eslint-disable-next-line
    MAXFORMSTEP: state => {
      console.log('aif');
      return state.formstep.max;
    },
  },
  mutations: {
    UPDATE_TOKEN_USERNAME: (state, payload) => {
      state.token = payload.token;
      state.username = payload.username;
    },
    LOGOUT: (state) => {
      state.token = 'token';
      state.username = 'username';
    },
    UPDATE_FORM: (state, payload) => {
      state.form = payload;
    },
    UPDATE_FORMSTEP: (state, payload) => {
      state.formstep = { max: state.formstep.max, actual: Math.min(state.formstep.max, payload) };
    },
    UPDATE_MAXFORMSTEP: (state, payload) => {
      state.formstep = { max: payload, actual: state.formstep.actual };
    },
  },
  actions: {},
});
