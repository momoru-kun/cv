import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import ru from 'vuetify/lib/locale/ru';

Vue.use(Vuetify);

export default new Vuetify({
    lang: {
      locales: { ru },
      current: 'ru',
    },
    icons: {
      iconfont: 'mdi',
      values: {
        vk: { component: () => import(/* webpackChunkName: "about" */ /* webpackMode: "lazy" */ '@/components/icons/VK.vue') }
      }
    }
});
