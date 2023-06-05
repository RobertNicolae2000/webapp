import { createRouter, createWebHistory } from 'vue-router'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import casadetaliata from "@/views/casadetaliata.vue";
import listacase from "@/views/listacase.vue";
import {useCartStore} from "@/store/index";
import adaugarecasa from "@/views/adaugarecasa.vue";

const routes = [
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },

  {
    path: '/login',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/case/:casa_slug',
    name: 'CasaDetaliata',
    component: casadetaliata
  },

  {
    path: '/',
    name: 'ListaCase',
    component: listacase
  },

  {
    path: '/adaugarecasa',
    name: 'adaugarecasa',
    component: adaugarecasa
  },

]
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})
router.beforeEach((to, from, next)=>{
  const cart = useCartStore()
  if(!cart.isAuthenticated && to.path!=='/login' && to.path!=='/signup'){
    next({path:'/login'})
  }
  else {
    next()
  }
})
export default router
