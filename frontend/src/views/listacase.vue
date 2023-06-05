<template>
    <section class="py-5 text-center container">
        <div class="row py-lg-5">
            <div class="col-lg-6 col-md-8 mx-auto">
                <h1 class="fw-light">O noua locuinta</h1>
                <p class="lead text-body-secondary">Pentru un nou inceput</p>

                <div class="dropdown">
                    <button class="dropbtn">Alegeti zona</button>
                    <div class="dropdown-content">
                        <a class="btn" v-for="zona in this.zone" @click="alege_zona(zona)">{{zona}}</a>
                    </div>
                </div>

            </div>
        </div>
    </section>
    <main role="main">
    <div class="album py-5 bg-light">
        <div class="container">

            <div class="row  match-to-row">
                <div class="col-md-4" v-for="casa in this.case">
                    <div class="card mb-4  box-shadow">
                        <img style="margin: auto; height: 400px; object-fit:cover;" class="card-img-top" v-bind:src="casa.get_image" alt="Card image cap">
                        <div class="card-body">
                            <p class="card-text">{{ casa.name }} cu {{casa.numar_camere}} camere</p>
                            <p class="card-text">Zona {{ casa.adresa }}</p>
                            <div class="d-flex justify-content-between align-items-center">
                                <div class="btn-group">
                                    <router-link v-bind:to="`/case/`+ casa.slug">
                                        <button type="button" class="btn btn-sm btn-outline-secondary">Detalii</button>
                                    </router-link>
                                </div>
                                <p class="text-muted">{{ casa.pret }} $</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </main>
</template>

<script>

import axios from 'axios'
  export default {
      name: 'casadetaliata',
      data() {
          return {
              case: {},
              zone: [],
          }
      },
      methods: {
          alege_zona(zona){
              axios
              .post(`/api/v1/case/search/`, {'zona': zona})
              .then(response => {
                 this.case = response.data
              })
              .catch(error => {
                  console.log(error)
              })
          }
      },
      mounted() {
          axios
              .get(`/api/v1/case/`)
              .then(response => {
                  this.case = response.data


                  for (const casa of this.case) {
                      this.zone.push(casa.adresa)
                  }
                  this.zone = this.zone.filter((item, i, ar) => ar.indexOf(item) === i);
              })
              .catch(error => {
                  console.log(error)
              })
      }
  }


</script>

<style scoped lang="scss">
.dropbtn {
  background-color: #4CAF50;
  color: white;
  padding: 16px;
  font-size: 16px;
  border: none;
  cursor: pointer;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {background-color: #f1f1f1}

.dropdown:hover .dropdown-content {
  display: block;
}

.dropdown:hover .dropbtn {
  background-color: #3e8e41;
}
</style>