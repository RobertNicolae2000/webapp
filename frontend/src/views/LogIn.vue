<template>
    <div style="max-width: 350px" class="login m-auto">
        <h1>Log In</h1>

        <form @submit.prevent="submitForm" style="display: flex; flex-direction: column; row-gap: 5px">
            <div class="form-floating">
                <input type="email" class="form-control" id="floatingInput" name="username" v-model="username">
                <label for="floatingInput">Email address</label>
            </div>
            <div class="form-floating">
                <input class="w-100 form-control" id="floatingPassword" type="password" name="password"
                       v-model="password">
                <label for="floatingPassword">Password</label>
            </div>
            <button class="w-100 btn btn-lg btn-primary" type="submit">Log In</button>
        </form>
    </div>
    <router-link to="/signup">Nu aveti cont? Inregistrati-va aici!</router-link>
</template>

<script setup>

import axios from 'axios'
import {useRouter} from "vue-router";
import {ref} from 'vue'
import { useCartStore } from '@/store/index'

const router = useRouter()
const cart = useCartStore()
const username = ref('')
const password = ref('')

const submitForm = (async () => {

    cart.logout()
    axios.defaults.headers.common["Authorization"] = ""
    const formData = {
        username: username.value,
        password: password.value,
    }

    await axios
        .post("/api/v1/token/login/", formData)
        .then(response => {
            const token = response.data.auth_token
            axios.defaults.headers.common["Authorization"] = "Token " + token
            cart.login(token)

            axios
                .get(`/api/v1/users/me/`)
                .then(response => {
                    cart.user = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            router.push('/')
        })
        .catch(error => {
            console.log(error)
        })

})
</script>
