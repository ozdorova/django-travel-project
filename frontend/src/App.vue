<template>
  <div class="app">
    <tour-create-form />
    <tour-list :tours="tours" />
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
      tour: {},
      formTitle: "",
      formOwner: "",
      formStartDate: "",
      formEndDate: "",
    };
  },
  methods: {
    async getTours() {
      await HTTP.get("/tour/").then((response) => {
        this.tours = response.data;
      });
    },
    createTour() {
      const newTour = {
        id: Date.now(),
        title: this.formTitle,
        owner: this.formOwner,
        start_date: this.formStartDate,
        end_date: this.formEndDate,
      };
      this.tours.push(newTour);
      this.formTitle = "";
      this.formOwner = "";
      this.formStartDate = "";
      this.formEndDate = "";
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
