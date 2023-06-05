<template>
  <div>
      <h2>{{ casa.name }}</h2>
      <div>
          <figure class="image">
                <img v-bind:src="casa.get_image">
            </figure>
      </div>
  </div>

</template>

<script>
import axios from 'axios'
  export default {
      name: 'casadetaliata',
      data() {
          return {
              casa_id: this.$route.params.casa_id,
              casa: {}
          }
      },
      methods: {

      },
      mounted() {
          const casa_slug = this.$route.params.casa_slug
          axios
                  .get(`/api/v1/case/${casa_slug}/`)
                  .then(response => {
                      console.log(response.data)
                      this.casa = response.data
                  })
                  .catch(error => {
                      console.log(error)
                  })


      }
  }

</script>



<style scoped lang="scss">

</style>