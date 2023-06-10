<template>
    <div style="max-width: 350px" class="page-add-casa m-auto">
        <h1>Editare Proprietate</h1>
        <form @submit.prevent="submitForm" style="display: flex; flex-direction: column; row-gap: 5px">
            <div class="form-floating">
                <input type="text" class="form-control" id="name" name="name" autocomplete="off" v-model="casa.name">
                <label for="name">Nume</label>
            </div>

            <div class="form-floating">
                <input type="text" class="form-control" id="adresa" name="adresa" autocomplete="off"
                       v-model="casa.adresa">
                <label for="adresa">Zona</label>
            </div>
            <div class="form-floating">
                <input type="number" class="form-control" id="numar_camere" name="numar_camere" autocomplete="off"
                       v-model="casa.numar_camere">
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
                <input type="text" class="form-control" id="numar_telefon" name="numar_telefon" autocomplete="off"
                       v-model="casa.numar_telefon">
                <label for="slug">Numar de telefon</label>
            </div>
            <div class="form-floating">
                <textarea class="form-control" id="description" name="description" autocomplete="off"
                          v-model="casa.description" rows="3"></textarea>
                <label for="description">Descriere</label>
            </div>
            <div class="mb-3">
                <label for="formFile" class="form-label">Schimba imagine</label>
                <input class="form-control" type="file" id="formFile" @input="casa.image = $event.target.files[0]; editimage=true">
            </div>
            <div class="mb-3">
                <label for="formFile" class="form-label">Schimba imagine2</label>
                <input class="form-control" type="file" id="formFile" @input="casa.image2 = $event.target.files[0]; editimage2=true">
            </div>
            <div class="mb-3">
                <label for="formFile" class="form-label">Schimba imagine3</label>
                <input class="form-control" type="file" id="formFile" @input="casa.image3 = $event.target.files[0]; editimage3=true">
            </div>
            <div class="mb-3">
                <label for="formFile" class="form-label">Schimba imagine4</label>
                <input class="form-control" type="file" id="formFile" @input="casa.image4 = $event.target.files[0]; editimage4=true">
            </div>
            <div class="mb-3">
                <label for="formFile" class="form-label">Schimba imagine5</label>
                <input class="form-control" type="file" id="formFile" @input="casa.image5 = $event.target.files[0]; editimage5=true">
            </div>
            <button @click="editare" class="w-100 btn btn-lg btn-primary" type="submit">Editeaza</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios'

export default {
    name: 'casadetaliata',
    data() {
        return {
            casa_id: this.$route.params.casa_id,
            casa: {},
            isHidden: true,
            editimage: false,
            editimage2: false,
            editimage3: false,
            editimage4: false,
            editimage5: false,
        }
    },
    methods: {
        editare() {
            if (!this.editimage) {
                delete this.casa.image}
            if (!this.editimage2) {
                delete this.casa.image2}
            if (!this.editimage3) {
                delete this.casa.image3}
            if (!this.editimage4) {
                delete this.casa.image4}
            if (!this.editimage5) {
                delete this.casa.image5}

            const casa_slug = this.$route.params.casa_slug
            axios
                .put(`/api/v1/case/${casa_slug}/`, this.casa, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                })
                .then(response => {
                    this.$router.push('/')
                    console.log(response.data)
                })
                .catch(error => {
                    console.log(error)
                })
        }
    },
    mounted() {
        const casa_slug = this.$route.params.casa_slug
        axios
            .get(`/api/v1/case/${casa_slug}/`)
            .then(response => {
                console.log(response.data)
                this.casa = response.data
                console.log(this.casa.description)
            })
            .catch(error => {
                console.log(error)
            })


    }
}

</script>

<style scoped lang="scss">

</style>