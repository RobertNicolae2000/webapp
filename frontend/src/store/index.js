import {defineStore} from "pinia";
import axios from "axios";

export const useCartStore = defineStore('cart', {
  state: () => {
    return{
      isAuthenticated: false,
      user: '',
      token: '',
    }
  },

  getters: {

  },

  actions: {
    login(new_token) {
      this.token = new_token
      this.isAuthenticated = true
    },
    logout() {
      this.token = ''
      this.isAuthenticated = false
      this.user = ''
    },


  },
  persist:true,
})