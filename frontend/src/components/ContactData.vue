<template>
  <v-card outlined class="pa-1 pa-md-4">
    <v-list-item single-line>
      <v-list-item-content class="align-self-start">
          <div class="text-h5">
            Ленец Александр Владимирович
          </div>
          <div class="grey--text text-subtitle-1">29 мая 1999 г.р.</div>
          <div class="grey--text text-subtitle-2">г. Санкт-Петербург</div>
        </v-list-item-content>
        <v-list-item-avatar
          tile
          :size="$vuetify.breakpoint.mdAndUp ? '160' : '80'"
        >
          <v-img src="@/assets/me.jpg">

          </v-img>
        </v-list-item-avatar>
      </v-list-item>
      <v-card-actions class="d-flex justify-end">
        <div class="d-flex justify-space-between" :class="{'mr-2': $vuetify.breakpoint.mdAndUp}" :style="$vuetify.breakpoint.mdAndUp ? 'width: 160px' : ''">
          <v-btn
            href="mailto:wowgonit@gmail.com"
            target='"_blank'
            icon
            color="primary"
          >
            <v-icon> mdi-email-outline </v-icon>
          </v-btn>
          <v-btn
            href="https://instagram.com/momoru_kun"
            target='"_blank'
            icon
            color="primary"
          >
            <v-icon> mdi-instagram </v-icon>
          </v-btn>
          <v-btn
            href="https://vk.com/momoru_kun"
            target='"_blank'
            icon
            color="primary"
          >
            <v-icon> mdi-vk </v-icon>
          </v-btn>
        </div>
      </v-card-actions>
    </v-card>
</template>

<script>
export default {
    name: 'ContactData',
}
</script>
