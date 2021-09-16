<template>
  <v-col
    cols="6"
    sm="4"
    md="3"
    class="d-flex align-center justify-center pa-2 fit-content"
  >
    <v-progress-circular
      size="200"
      width="14"
      :color="`#${skill.color}`"
      :value="skill.percentage"
      rotate="270"
    >
      <div class="text-overline">
        <span style="font-size: 1.15em">{{skill.name}}</span>
        <div class="text-body-1 text-center">{{ skill.percentage }}%</div>
      </div>
    </v-progress-circular>
  </v-col>
</template>

<script>
export default {
  name: 'Skill',
  props: {
    skill: {
      type: Object,
      default: () => ({})
    }
  }
}
</script>

<style>
.fit-content {
  height: fit-content;
}
</style>