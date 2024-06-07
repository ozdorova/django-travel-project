<template>
  <div>
    <form @submit.prevent>
      <h4>Создание тура (Тест, в бд не заносится)</h4>
      <input
        v-model="tourForm.title"
        type="text"
        placeholder="Название"
        class="input"
      />
      <input
        v-model="tourForm.owner"
        type="text"
        placeholder="Организатор"
        class="input"
      />
      <input v-model="tourForm.start_date" type="date" class="input" />
      <input v-model="tourForm.end_date" type="date" class="input" />
      <button class="btn">Создать</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tourForm: {
        title: "",
        owner: "",
        start_date: Date(),
        end_date: Date(),
      },
    };
  },
};
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
}

.input {
  width: 100%;
  border: 2px solid teal;
  padding: 10px 15px;
  margin-top: 15px;
}
.btn {
  margin-top: 15px;
  align-self: flex-end;
  padding: 10px 15px;
  background: none;
  color: teal;
  border: 1px solid teal;
}
</style>
