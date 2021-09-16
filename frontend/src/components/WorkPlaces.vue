<template>
  <v-container fluid class="pa-4">
    <div class="d-flex align-center justify-center mt-6" style="width: 100%" v-if="workplaces.length == 0">
      <v-progress-circular size="72" color="primary" indeterminate></v-progress-circular>
    </div>
    <div v-else>
      <div class="text-h6 mb-4"> Опыт работы: {{ format_summary() }}</div>
      <v-list>
        <v-list-item v-for="workplace in workplaces" :key="workplace.id" class="flex-column align-start mb-6 px-0">
          <div class="align-self-start text-overline work-title pl-0">{{ workplace.name }}</div>
          <div class="text-overline">
            {{ format_date(workplace.date_start) }} &mdash; {{ workplace.by_today ? 'по сегодняшний день' : format_date(workplace.date_end) }}
          </div>
          <v-list-item-content class="text-body-2 align-self-start pt-1" v-html="workplace.description"></v-list-item-content>
        </v-list-item>
      </v-list>
    </div>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'WorkPlaces',
  data: () => ({
    summary: 0
  }),
  computed: {
    ...mapGetters(['workplaces'])
  },
  mounted() {
    this.$store.dispatch('fetch_workplaces').then(() => {
      this.summary_time()
    })
  },
  methods: {
    format_date(dt) {
      let months = ['янв.', 'фев.', 'мар.', 'апр.', 'май', 'июнь', 'июль', 'авг.', 'сен.', 'окт.', 'ноя.', 'дек.']
      let date = new Date(dt)
      return `${ months[date.getMonth()] } ${ date.getFullYear() }`
    },
    format_summary() {
      let dt = new Date(this.summary)
      return `${dt.getFullYear() - 1970} год, ${dt.getMonth() + 1} мес.`
    },
    summary_time() {
      this.workplaces.forEach(workplace => {
        let date_start = new Date(workplace.date_start)
        let date_end = workplace.by_today ? new Date() : new Date(workplace.date_end)
        this.summary += new Date(date_end - date_start).getTime()
      })
    },
  }
}
</script>

<style scoped>
.v-list-item {
  min-height: 0 !important;
  border-bottom: 1px #9e9e9e solid;
}
.work-title {
  letter-spacing: .0325em;
  line-height: 1.25em;
}
</style>