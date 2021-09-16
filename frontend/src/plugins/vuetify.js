import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import ru from 'vuetify/lib/locale/ru';
import VkIcon from '@/components/icons/VK.vue'

Vue.use(Vuetify);

export default new Vuetify({
    lang: {
      locales: { ru },
      current: 'ru',
    },
    icons: {
      iconfont: 'mdi',
      values: {
        vk: { component: VkIcon }
      }
    }
});
