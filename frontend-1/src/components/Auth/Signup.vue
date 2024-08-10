<template>
    <div class="MainContainer">
        <form @submit.prevent="signupuser">
            <h3> Signup Form </h3>
            <div class="container">
                <input v-model="username"  placeholder="username" type="text"></input>
                <br>
                <input v-model="email"  placeholder="email" type="email"></input>
                <br>
                <input v-model="password" placeholder="password" type="password"></input>
                <br>

                <button type="submit"> Signup </button>
            </div>
        </form>

    </div>

  </template>

<script setup>

import { ref, reactive } from 'vue'
import Login from './login.vue';
import axios from 'axios'
const username = ref("")
const email = ref("")
const password = ref("")

const signupform = reactive({
  username:"",
  email:"",
 password:""
})

function  signupuser(params) {
  signupform.username = username.value
  signupform.email  = email.value
  signupform.password = password.value
  console.log("sign up data : ",signupform)
  axios.post("http://127.0.0.1:8000/create_user",signupform).then(response=>{console.log("response :")})

}
</script>

<style scoped>

input[type=text], input[type=password] ,[type=email]{
width: 100%;
padding: 12px 20px;
margin: 8px 0;
display: inline-block;
border: 1px solid #ccc;
box-sizing: border-box;
}

button {
background-color: #04AA6D;
color: white;
padding: 14px 20px;
margin: 8px 0;
border: none;
cursor: pointer;
width: 100%;
}

form {
border: 3px solid #f1f1f1;
width: 400px;
padding: 16px;
justify-content: center;
align-items: center;
}

button:hover {
opacity: 0.8;
}
.container {
padding: 16px;
}
.MainContainer{
  height: 80vh;
  padding: 16px;
  justify-content: center;
  display: flex;
  align-items: center;
}
h3{
  text-align: center;
}


</style>
