<template>
  <div>
    <div><strong>Описание: </strong> Список туров</div>
    <div class="post" v-for:="tour in tours">
      <div><strong>Название: </strong> {{ tour.title }}</div>
      <div><strong>Организатор</strong> {{ tour.owner }}</div>
      <div><strong>Начало</strong> {{ tour.start_date }}</div>
      <div><strong>Конец</strong> {{ tour.end_date }}</div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    tours: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped>
.post {
  padding: 15px;
  border: 2px solid teal;
  margin-top: 15px;
}
</style>
