<template>
  <v-expansion-panels class="pa-4">
    <div class="d-flex align-center justify-center mt-6" style="width: 100%" v-if="projects.length == 0">
      <v-progress-circular size="72" color="primary" indeterminate></v-progress-circular>
    </div>
    <v-expansion-panel
      v-for="project in projects"
      :key="project.id"
      elevation="2"
    >
      <v-expansion-panel-header> {{ project.name }} </v-expansion-panel-header>
      <v-expansion-panel-content>
        <div class="text-body-1 project-role"> <span class="font-weight-medium">Роль:</span> {{ project.role }} </div>
        <div class="text-body-1 font-weight-medium mt-1"> Описание: </div>
        <div class="text-body-1 ml-1">
          {{ project.description }}
        </div>
        <div class="text-body-1 mt-2">
          <span class="text-body-1 font-weight-medium">Стек</span>: {{ project.skills.reduce((skillStr, skill) => skillStr + `${skill.name}; `, '') }}
        </div>
        <v-btn
          v-if="project.link"
          text
          color="primary"
          class="float-right"
          :href="project.link"
          target="_blank"
        >
          <v-icon class="mr-2">mdi-open-in-new</v-icon>
          Ссылка на проект
        </v-btn>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
    name: 'Projects',
    computed: { ...mapGetters(['projects']) },
    mounted() {
      this.$store.dispatch('fetch_projects')
    }
}
</script>

<style scoped>
.project-role {
  letter-spacing: .0325em;
  line-height: 1.25em;
}
</style>