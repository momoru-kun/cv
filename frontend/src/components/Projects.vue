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
      <v-expansion-panel-content> {{ project.description }} </v-expansion-panel-content>
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