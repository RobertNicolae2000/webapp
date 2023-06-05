<template>
    <div style="max-width: 350px" class="page-add-casa m-auto">
        <h1>Adauga Proprietate</h1>
        <form @submit.prevent="submitForm" style="display: flex; flex-direction: column; row-gap: 5px">
            <div class="form-floating">
                <input type="text" class="form-control" id="name" name="name" autocomplete="off" v-model="casa.name">
                <label for="name">Nume</label>
            </div>

            <div class="form-floating">
                <input type="text" class="form-control" id="adresa" name="adresa" autocomplete="off" v-model="casa.adresa">
                <label for="adresa">Zona</label>
            </div>
            <div class="form-floating">
                <input type="number" class="form-control" id="numar_camere" name="numar_camere" autocomplete="off" v-model="casa.numar_camere">
                <label for="numar_camere">Numar camere</label>
            </div>
            <div class="form-floating">
                <input type="number" class="form-control" id="pret" name="pret" autocomplete="off" v-model="casa.pret">
                <label for="pret">Pret</label>
            </div>
            <div class="form-floating">
                <input type="text" class="form-control" id="slug" name="slug" autocomplete="off" v-model="casa.slug">
                <label for="slug">Link</label>
            </div>
            <div class="form-floating">
                <input type="text" class="form-control" id="description" name="description" autocomplete="off" v-model="casa.description">
                <label for="description">Descriere</label>
            </div>
            <button class="w-100 btn btn-lg btn-primary" type="submit">Adauga</button>
        </form>
    </div>
</template>

<script setup>
import axios from 'axios'
import { useCartStore } from '@/store/index'
import {ref} from "vue";
const cart = useCartStore()
const casa =ref({})
import {useRouter} from "vue-router";
const router = useRouter()
console.log(cart.user)
const submitForm=(async()=>{
    casa.value.user = cart.user.id
    await axios
        .post("/api/v1/case/", casa.value)
        .then(response => {
            router.push('/')
            console.log(response)
        })
        .catch(error => {
            console.log(error)
        })
})

</script>


<style scoped lang="scss">

</style>