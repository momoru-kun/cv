import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    workplaces: [],
    projects: [],
    skills: [],
    tags: []
  },
  mutations: {
    set_workplaces(state, data) {
      state.workplaces = data
    },
    set_tags(state, data) {
      state.tags = data.map(tag => ({ text: tag.name, value: tag.id }))
      state.tags.unshift({ text: 'Все значения', value: -1 })
    },
    set_skills(state, data) {
      state.skills = data
    },
    set_projects(state, data) {
      state.projects = data
    }
  },
  actions: {
    fetch_workplaces({ commit }) {
      return new Promise((resolve, reject) => {
        axios.get('/api/workplaces').then(response => {
          commit('set_workplaces', response.data)
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },
    fetch_tags({ commit }) {
      return new Promise((resolve, reject) => {
        axios.get('/api/tags').then(response => {
          commit('set_tags', response.data)
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },
    fetch_projects({ commit }) {
      return new Promise((resolve, reject) => {
        axios.get('/api/projects').then(response => {
          commit('set_projects', response.data)
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },
    fetch_skills({ commit }) {
      return new Promise((resolve, reject) => {
        commit('set_skills', [])
        axios.get('/api/skills/').then(response => {
          commit('set_skills', response.data)
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },
    fetch_skills_by_tag({ commit, dispatch }, tagname) {
      if (tagname == -1) {
        return dispatch('fetch_skills')
      }
      return new Promise((resolve, reject) => {
        commit('set_skills', [])
        axios.get(`/api/tags/${tagname}`).then(response => {
          commit('set_skills', response.data)
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    }
  },
  getters: {
    workplaces: state => state.workplaces,
    projects: state => state.projects,
    skills: state => state.skills,
    tags: state => state.tags,
  }
})
