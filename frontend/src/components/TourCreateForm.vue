<template>
  <div>
    <form @submit.prevent>
      <h4>Создание тура (Тест, в бд не заносится)</h4>
      <my-input
        v-model="tourForm.title"
        :in_type="'text'"
        placeholder="Название"
      />
      <my-input
        v-model="tourForm.owner"
        :in_type="'text'"
        placeholder="Организатор"
      />
      <my-input v-model="tourForm.start_date" :in_type="'date'" />
      <my-input v-model="tourForm.end_date" :in_type="'date'" />
      <my-button
        @click="createTour"
        style="align-self: flex-end; margin-top: 15px"
        >Создать</my-button
      >
    </form>
  </div>
</template>

<script>
import moment from "moment";
export default {
  data() {
    return {
      tourForm: {
        title: "",
        owner: "",
        start_date: moment().format("YYYY-MM-DD"),
        end_date: moment().add(14, "days").format("YYYY-MM-DD"),
      },
    };
  },
  methods: {
    createTour() {
      this.tourForm.id = Date.now();
      // передача аргументы в функцию слушатель в App
      this.$emit("create", this.tourForm);
      this.tourForm = {
        title: "",
        owner: "",
        start_date: moment().format("YYYY-MM-DD"),
        end_date: moment().add(14, "days").format("YYYY-MM-DD"),
      };
    },
  },
};
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
}
</style>
