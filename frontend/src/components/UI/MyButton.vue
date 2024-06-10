<template>
  <button class="btn"><slot></slot></button>
</template>

<script>
export default {
  // при загрузке компонентов через main.js, компоненты будет доступен по имени name без доп импорта
  name: "my-button",
};
</script>

<style scoped>
.btn {
  padding: 10px 15px;
  background: none;
  color: teal;
  border: 1px solid teal;
}
</style>
