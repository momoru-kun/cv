<template>
  <div>
    <v-tabs
      v-model="tab"
      centered
      icons-and-text
    >
      <v-tabs-slider color="primary"></v-tabs-slider>
      <v-tab>
        Скилы
        <v-icon> mdi-laptop </v-icon>
      </v-tab>
      <v-tab>
        Опыт работы
        <v-icon> mdi-briefcase </v-icon>
      </v-tab>
      <v-tab>
        Проекты
        <v-icon> mdi-semantic-web </v-icon>
      </v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab">
      <v-tab-item>
        <skills></skills>
      </v-tab-item>
      <v-tab-item>
        <work-places></work-places>
      </v-tab-item>
      <v-tab-item>
        <projects></projects>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
export default {
  name: 'Data',
  data: () => ({
    tab: 0
  }),
  components: {
    Projects: () => import(
      /* webpackChunkName: "datatab" */
      /* webpackMode: "lazy" */
      '@/components/Projects.vue'
    ),
    WorkPlaces: () => import(
      /* webpackChunkName: "datatab" */
      /* webpackMode: "lazy" */
      '@/components/WorkPlaces.vue'
    ),
    Skills: () => import(
      /* webpackChunkName: "datatab" */
      /* webpackMode: "lazy" */
      '@/components/Skills.vue'
    )
  }
}
</script>