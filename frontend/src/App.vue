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
                            <li style="color:grey;">
                                Salut,
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
import {useRouter} from "vue-router";

const cart = useCartStore()

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

.btn {
  text-transform: unset !important;
}
</style>
