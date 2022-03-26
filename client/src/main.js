import { createApp } from 'vue';
import Notifications from '@kyvg/vue3-notification';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import VueApexCharts from 'vue3-apexcharts';
import App from './App.vue';
import router from './router';
import { store } from './store';

const app = createApp(App);

app.use(Notifications);
app.use(router);
app.use(store);
app.use(ElementPlus);
app.use(VueApexCharts);

app.mount('#app');
