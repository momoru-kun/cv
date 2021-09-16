<template>
  <v-container fluid>
    <div
      class="d-flex align-center justify-center mt-6"
      style="width: 100%"
      v-if="skills.length == 0"
    >
      <v-progress-circular size="72" color="primary" indeterminate></v-progress-circular>
    </div>
    <div v-else>
      <v-row>
        <v-col cols="12" md="4">
          <v-select
            label="Категория"
            :items="tags"
            v-model="tag"
            :loading="tags.length == 0"
            @input="val => this.$store.dispatch('fetch_skills_by_tag', val)"
          ></v-select>
        </v-col>
      </v-row>
      <v-row>
        <skill-col
          v-for="skill in skills"
          :key="skill.id"
          :skill="skill"
        >
        </skill-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>
import SkillCol from './SkillCol.vue'
import { mapGetters } from 'vuex';

export default {
    name: 'Skills',
    components: { SkillCol },
    computed: { ...mapGetters(['skills', 'tags']) },
    data: () => ({
      tag: -1
    }),
    mounted() {
        this.$store.dispatch('fetch_tags')
        this.$store.dispatch('fetch_skills')
    }
}
</script>