<template>
  <div class="app">
    <tour-create-form @create="createTour" />
    <tour-list :tours="tours" @remove="removeTour" />
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { HTTP } from "./common";
import TourList from "@/components/TourList";
import TourCreateForm from "@/components/TourCreateForm";

export default defineComponent({
  components: {
    TourList,
    TourCreateForm,
  },
  data() {
    return {
      tours: [],
    };
  },
  methods: {
    async getTours() {
      // Получение API
      await HTTP.get("/tour/").then((response) => {
        this.tours = response.data;
      });
    },
    createTour(tourForm) {
      // Обработка формы TourCreateForm
      this.tours.push(tourForm);
    },
    removeTour(tour) {
      this.tours = this.tours.filter((t) => t.id !== tour.id);
    },
  },
  created() {
    this.getTours();
  },
});
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.app {
  padding: 20px;
}
</style>
