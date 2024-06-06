new Vue({
  el: "#travel_app",
  data: {
    tours: [],
  },
  created: function () {
    const vm = this;
    axios.get("api/v1/tour").then(function (response) {
      console.log(response.data);
      vm.tours = response.data["results"];
    });
  },
});
