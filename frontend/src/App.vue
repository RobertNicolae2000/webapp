<template>
    <div id="app">
        <nav v-if="cart.isAuthenticated" class="navbar navbar-expand-md navbar-dark bg-dark mb-4">
            <div class="container-fluid">
                <a class="navbar-brand" href="/">Acasa</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse"
                        aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarCollapse">
                    <ul class="navbar-nav me-auto mb-2 mb-md-0">
                        <li  v-if="cart.user.is_staff" class="nav-item">
                            <a class="nav-link" href="/adaugarecasa">Adauga Proprietate</a>
                        </li>
                    </ul>
                    <ul style="display:flex; column-gap:10px;" class="navbar-nav mb-2 mb-md-0">
                        <form>
                            <li>
                                <i class="bi bi-emoji-smile-fill"></i>

                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="grey"
                                     class="bi bi-emoji-smile-fill" viewBox="0 0 16 16">
                                    <path
                                            d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zM7 6.5C7 7.328 6.552 8 6 8s-1-.672-1-1.5S5.448 5 6 5s1 .672 1 1.5zM4.285 9.567a.5.5 0 0 1 .683.183A3.498 3.498 0 0 0 8 11.5a3.498 3.498 0 0 0 3.032-1.75.5.5 0 1 1 .866.5A4.498 4.498 0 0 1 8 12.5a4.498 4.498 0 0 1-3.898-2.25.5.5 0 0 1 .183-.683zM10 8c-.552 0-1-.672-1-1.5S9.448 5 10 5s1 .672 1 1.5S10.552 8 10 8z"/>
                                </svg>
                            </li>
                            <li style="color:grey;">{{ cart.user.username }}</li>
                        </form>
                        <li class="nav-item">
                            <a class="nav-link btn btn-outline-danger" @click=logout>Log Out</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </div>
    <router-view/>
</template>

<script setup>
import axios from 'axios'
import {useCartStore} from '@/store/index'

const cart = useCartStore()
import {useRouter} from "vue-router";

const router = useRouter()

if (cart.token) {
    axios.defaults.headers.common['Authorization'] = "Token " + cart.token
} else {
    axios.defaults.headers.common['Authorization'] = ""
}


const logout = (async () => {
    await axios
        .post('/api/v1/token/logout/')
        .then(response => {
            cart.logout()
            axios.defaults.headers.common['Authorization'] = ""
            router.push('/login')
        })
        .catch(error => {
            console.log(error)
        })

})
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

</style>
