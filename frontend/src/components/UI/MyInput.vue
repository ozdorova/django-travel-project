<template>
  <input
    :value="modelValue"
    @input="updateInput"
    class="input"
    :type="in_type"
  />
</template>

<script>
export default {
  props: {
    in_type: {
      type: String,
    },
    modelValue: [Date, Number, String, Boolean],
  },
  name: "my-input",
  methods: {
    updateInput(event) {
      // двустороннее связывание v-model
      this.$emit("update:modelValue", event.target.value);
    },
  },
};
</script>

<style scoped>
.input {
  width: 100%;
  border: 2px solid teal;
  padding: 10px 15px;
  margin-top: 15px;
}
</style>
