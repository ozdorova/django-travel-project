<template>
  <div class="post">
    <div>
      <div><strong>id</strong> {{ tour.id }}</div>
      <div><strong>Название: </strong> {{ tour.title }}</div>
      <div><strong>Организатор</strong> {{ tour.owner }}</div>
      <div><strong>Начало</strong> {{ tour.start_date }}</div>
      <div><strong>Конец</strong> {{ tour.end_date }}</div>
    </div>
    <div class="post__btns">
      <!-- прокидываем в TourList событие удаление -->
      <my-button @click="$emit('remove', tour)">Удалить</my-button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    tour: Object,
    required: true,
  },
};
</script>

<style scoped>
.post {
  padding: 15px;
  border: 2px solid teal;
  margin-top: 15px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
</style>
