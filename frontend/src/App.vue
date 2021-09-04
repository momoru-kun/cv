<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <v-app-bar-title> Резюме </v-app-bar-title>
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
          <v-tabs
            v-model="tab"
            centered
            icons-and-text
          >
            <v-tabs-slider color="primary"></v-tabs-slider>
            <v-tab>
              Опыт работы
              <v-icon> mdi-briefcase </v-icon>
            </v-tab>
            <v-tab>
              Проекты
              <v-icon> mdi-semantic-web </v-icon>
            </v-tab>
            <v-tab>
              Скилы
              <v-icon> mdi-laptop </v-icon>
            </v-tab>
          </v-tabs>
        </v-col>
        <v-col cols="0" md="3" sm="2"></v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
import AboutMe from './components/AboutMe.vue';
import ContactData from './components/ContactData.vue'
export default {
  name: 'App',
  components: { ContactData, AboutMe },
  data: () => ({
    tab: ''
  }),
};
</script>
