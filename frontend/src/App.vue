<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="text-h5"> Резюме </div>
      <v-spacer></v-spacer>
      <v-btn
        href="https://github.com/momoru-kun"
        target="_blank"
        outlined
        color="white"
      >
        <v-icon class="mr-2"> mdi-github </v-icon> GitHub
      </v-btn>
    </v-app-bar>

    <v-main class="px-4 mt-sm-4">
      <v-row>
        <v-col cols="0" md="3" sm="2"></v-col>
        <v-col cols="12" md="6" sm="8">
          <contact-data></contact-data>
          <about-me></about-me>
          <v-lazy><data-section></data-section></v-lazy>
        </v-col>
        <v-col cols="0" md="3" sm="2"></v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  components: {
    ContactData: () => import(
      /* webpackChunkName: "contact" */
      /* webpackMode: "lazy" */
      './components/ContactData.vue'
    ),
    AboutMe: () => import(
      /* webpackChunkName: "about" */
      /* webpackMode: "lazy" */
      './components/AboutMe.vue'
    ),
    DataSection: () => import(
      /* webpackChunkName: "data" */
      /* webpackMode: "lazy" */
      './components/DataSection.vue'
    )
  }
};
</script>

<style>
.v-slide-group__prev.v-slide-group__prev--disabled {
  display: none !important;
}
.v-slide-group__next.v-slide-group__next--disabled {
  display: none !important;
}
</style>
