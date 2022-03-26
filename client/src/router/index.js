import { createRouter, createWebHistory } from 'vue-router';
import Auth from '../components/Auth/Auth.vue';
import Main from '../components/Mains/Main.vue';
import Forum from '../components/Mains/Forum.vue';
import Forecast from '../components/Mains/ForecastingPages/Forecast.vue';
import Chart from '../components/Mains/ForecastingPages/ChartsComponent.vue';
import FormComponent from '../components/Mains/ForecastingPages/FormComponent.vue';

const routes = [
  {
    path: '/authorization',
    name: 'Auth',
    component: Auth,
  },
  {
    path: '/forum',
    name: 'Forum',
    component: Forum,
  },
  {
    path: '/',
    name: 'Main',
    component: Main,
  },
  {
    path: '/forecast',
    name: 'Forecast',
    component: Forecast,
  },
  {
    path: '/chart',
    name: 'Chart',
    component: Chart,
  },
  {
    path: '/FormComponent',
    name: 'FormComponent',
    component: FormComponent,
  },
];
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});
export default router;
