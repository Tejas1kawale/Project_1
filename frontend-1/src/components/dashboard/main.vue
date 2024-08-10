<template>
  <div class="mt-4">
    <v-card class="pa-4">
    <v-text-field class="pt-4"
    label="Task Name"
    >

    </v-text-field>
    <v-textarea
      class="pt-4"
      label="Task Description"
    >

    </v-textarea>
    <v-btn class="my-button">+ Add Task</v-btn>
  </v-card>
  </div>

</template>

<script setup]>


</script>


<style scoped>
.mt-4{
  margin: auto;

  width: 50%;
  height: 25%;

}
.pt-4{
  padding-left: 10px;
  padding-right: 10px;
}
.my-button{
  background-color: rgb(61, 240, 106);

  margin-left: 10px;
}
</style>
