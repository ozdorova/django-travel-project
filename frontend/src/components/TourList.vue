<!-- список туров -->
<template>
  <div v-if="tours.length > 0">
    <!-- <div v-show="tours.length > 0"> -->

    <div><h3>Список туров</h3></div>
    <tour-item
      v-for="tour in tours"
      :tour="tour"
      :key="tour.id"
      @remove="$emit('remove', tour)"
    />
  </div>
  <h2 v-else style="color: red">Список пуст</h2>
  <!-- <h2 v-show="tours.length === 0" style="color: red">Список пуст</h2> -->
</template>

<script>
import TourItem from "@/components/TourItem";
export default {
  components: { TourItem },
  props: {
    // параметры компонента TourList, которые передают внутрь компонента из App
    tours: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped></style>
