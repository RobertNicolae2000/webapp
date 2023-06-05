<template>
    <div style="max-width: 350px" class="signup m-auto">
        <h1>Sign Up</h1>
        <form @submit.prevent="submitForm" style="display: flex; flex-direction: column; row-gap: 5px">
            <div class="form-floating">
                <input type="email" class="form-control" id="floatingInput" name="username" v-model="username">
                <label for="floatingInput">Email address</label>
            </div>
            <div class="form-floating">
                <input class="w-100 form-control" id="floatingPassword" type="password" name="password" v-model="password">
                <label for="floatingPassword">Password</label>
            </div>
            <button class="w-100 btn btn-lg btn-primary" type="submit">Inregistrare</button>
        </form>
        <router-link to="/login">Aveti deja cont? Conectati-va aici!</router-link>
    </div>
</template>

<script>
import axios from 'axios'
  export default {
      name: 'SignUp',
      data() {
          return {
              username: '',
              password: ''
          }
      },
      methods: {
              submitForm(){
                  const formData = {
                      username: this.username,
                      password: this.password
                  }

              axios
                  .post('/api/v1/users/', formData)
                  .then(response => {
                      this.$router.push('/login')
                      console.log(response)
                  })
                  .catch(error => {
                      console.log(error)
                  })
          }
      }
  }
</script>
