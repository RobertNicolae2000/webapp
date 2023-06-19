<template>
    <h1 class="mb-3"><b>{{ casa.name }} cu {{ casa.numar_camere }} camere</b></h1>
    <div class="row align-items-md-stretch">
        <div class="h-100 p-5 bg-body-tertiary border rounded-3  col-md-9">
            <div
                    id="carouselBasicExample"
                    class="carousel slide carousel-fade w-75 m-auto"
                    data-mdb-ride="carousel"
            >
                <!-- Indicators -->
                <div class="carousel-indicators">
                    <button
                            type="button"
                            data-mdb-target="#carouselBasicExample"
                            data-mdb-slide-to="0"
                            class="active"
                            aria-current="true"
                            aria-label="Slide 1"
                    ></button>
                    <button
                            type="button"
                            data-mdb-target="#carouselBasicExample"
                            data-mdb-slide-to="1"
                            aria-label="Slide 2"
                    ></button>
                    <button
                            type="button"
                            data-mdb-target="#carouselBasicExample"
                            data-mdb-slide-to="2"
                            aria-label="Slide 3"
                    ></button>
                    <button
                            type="button"
                            data-mdb-target="#carouselBasicExample"
                            data-mdb-slide-to="3"
                            aria-label="Slide 4"
                    ></button>
                    <button
                            type="button"
                            data-mdb-target="#carouselBasicExample"
                            data-mdb-slide-to="4"
                            aria-label="Slide 5"
                    ></button>
                </div>

                <!-- Inner -->
                <div class="carousel-inner marime1">
                    <!-- Single item -->
                    <div class="carousel-item active">
                        <img
                                v-bind:src="casa.get_image"
                                class="d-block w-100"
                        />
                    </div>

                    <!-- Single item -->
                    <div class="carousel-item">
                        <img
                                v-bind:src="casa.get_image2"
                                class="d-block w-100"
                        />
                    </div>

                    <!-- Single item -->
                    <div class="carousel-item">
                        <img
                                v-bind:src="casa.get_image3"
                                class="d-block w-100"
                        />
                    </div>

                    <div class="carousel-item">
                        <img
                                v-bind:src="casa.get_image4"
                                class="d-block w-100"
                        />
                    </div>

                    <div class="carousel-item">
                        <img
                                v-bind:src="casa.get_image5"
                                class="d-block w-100"
                        />
                    </div>
                </div>
                <!-- Inner -->

                <!-- Controls -->
                <button
                        class="carousel-control-prev"
                        type="button"
                        data-mdb-target="#carouselBasicExample"
                        data-mdb-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                </button>

                <button
                        class="carousel-control-next"
                        type="button"
                        data-mdb-target="#carouselBasicExample"
                        data-mdb-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </button>
            </div>
        </div>

        <div class="col-md-3">
            <div class="h-100 p-5 text-bg-dark border rounded-3 inline">
                <div>
                    <br><br>
                    <h3 class="mb-3">Pret: {{ casa.pret }}$</h3>
                    <h3 class="mb-3">Numar camere: {{ casa.numar_camere }}</h3>
                    <h3 class="mb-5">Zona: {{ casa.adresa }}</h3>
                </div>
                <div>
                    <button v-on:click="isHidden = !isHidden" class="btn btn-outline-light contact mb-2">Contact
                    </button>
                    <h3 class="mb-5" v-if="!isHidden">Numar de telefon: <br> +40 {{ casa.numar_telefon }}</h3>
                </div>
            </div>
        </div>
        <div class="h-70 p-5 bg-body-tertiary border rounded-3">
            <h2><b>Descriere</b></h2>

            <div class="descriere box text-start">{{ casa.description }}</div>

        </div>
        <ul class="text-end" style="float: right;">
            <li>
                <router-link v-bind:to="`/editcasa/` + casa.slug">
                    <button v-if="casa.user===user.id" class="btn btn-outline-dark">Editare Casa</button>
                </router-link>
            </li>
            <li>

                <button v-if="casa.user===user.id" class="btn btn-outline-danger" @click="stergere">Sterge
                    Casa
                </button>
            </li>
        </ul>
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
            user: {},
        }
    },
    methods: {
        stergere() {
            const casa_slug = this.$route.params.casa_slug
            axios
                .delete(`/api/v1/case/${casa_slug}/`)
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
        axios
            .get(`/api/v1/users/me/`)
            .then(response => {
                this.user = response.data
            })
            .catch(error => {
                console.log(error)
            })


    }
}

</script>


<style scoped lang="scss">
.carousel-control-next-icon:after {
  content: "";
}

.carousel-control-prev-icon:after {
  content: "";
}

.contact {
  height: 50px;
  width: 100px;
  font-size: 18px;
}

.descriere {
  font-size: 20px;
}

.h-70 {
  height: 70% !important;
}

.h-30 {
  height: 30% !important;
}

.marime1 {
    height: 600px !important;
}

.box {
  white-space: pre-wrap;
}
</style>