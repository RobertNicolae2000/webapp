import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import App from './App.vue'
import axios from 'axios'
axios.defaults.baseURL ='https://backendimobiliare.azurewebsites.net'

import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'
import router from "@/router";
// import "bootstrap/dist/css/bootstrap.min.css"
// import "bootstrap"

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
const app = createApp(App)

app.use(pinia)
app.use(router, axios)
app.mount('#app')








