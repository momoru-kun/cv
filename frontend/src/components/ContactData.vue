<template>
  <v-card outlined class="pa-1 pa-md-4">
    <v-list-item single-line>
        <v-list-item-avatar
          :tile="$vuetify.breakpoint.mdAndUp"
          :size="$vuetify.breakpoint.mdAndUp ? '160' : '80'"
          class="align-self-start mt-4 mt-md-0"
        >
          <v-img src="@/assets/me.jpg">

          </v-img>
        </v-list-item-avatar>
      <v-list-item-content class="align-self-start">
          <div class="text-h5">
            Ленец Александр Владимирович<br>
            <div style="font-size: 0.75em">Fullstack Разработчик</div>
            <div style="font-size: 0.5em; line-height: 1em" class="grey--text">Полная занятость, гибкий график, удалённая работа</div>
          </div>
          <div class="grey--text text-subtitle-2 mt-4">
            <v-icon size="16"> mdi-cake-variant </v-icon> 29 мая 1999 г.р.
          </div>
          <div class="grey--text text-subtitle-2">
            <v-icon size="16"> mdi-city </v-icon> г. Санкт-Петербург
          </div>
        </v-list-item-content>
      </v-list-item>
      <v-card-actions class="d-flex flex-row flex-md-row-reverse justify-space-between">
        <div class="d-flex justify-space-between" :class="{'ml-2': $vuetify.breakpoint.mdAndUp}" :style="$vuetify.breakpoint.mdAndUp ? 'width: 160px' : ''">
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
            <v-icon> $vk </v-icon>
          </v-btn>
        </div>
        <v-btn
          outlined
          color="primary"
          href="tel:89312873477"
        >
          <v-icon size="16" class="mr-2"> mdi-phone </v-icon>
          Позвоните мне
        </v-btn>
      </v-card-actions>
    </v-card>
</template>

<script>
export default {
    name: 'ContactData',
}
</script>
