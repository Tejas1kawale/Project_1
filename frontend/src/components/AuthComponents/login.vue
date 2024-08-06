<template>
    <div class="MainContainer">
        <form @submit.prevent="authorize">
            <h3> Login Form </h3>
            <div class="container">
                <input v-model="username"  placeholder="username" type="text"></input>
                <br>
                <input v-model="password" placeholder="password" type="password"></input>
                <br>
                <button type="submit"> Login </button>
            </div>
        </form>

    </div>
  
</template>

<script setup>
import { ref,computed,watch } from 'vue'

const username = ref("")
const password = ref("")


// function check(){
//     console.log("usernmae : ",username.value)
// }
watch(username,()=>{
    console.log("username: ",username.value)
})
function authorize()
{
    console.log("username: ",username.value)
    console.log("password: ",password.value)
    
}

</script>

<style scoped>

input[type=text], input[type=password] {
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
}

button:hover {
  opacity: 0.8;
}
.container {
  padding: 16px;
}
.MainContainer{
    padding: 16px;
    display: flex;
    justify-content: center;
}
h3{
    text-align: center;
}
</style>