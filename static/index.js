var SurveyComponent = Vue.component("survey-component", {
    template: '<survey :survey="survey" />',
    name: "survey-component",
    data() {
        const survey = new Survey.Model(json);
        survey.onComplete.add((sender, options) => {
            console.log(JSON.stringify(sender.data, null, 3));
        });
        return {
            survey: survey
        };
    },
});
new Vue({
    el: "#app",
    delimiters: ["[[","]]"],
    component: {
        "survey-component": SurveyComponent
    },
    data()  {
        return {nombre: "Paco"}
    }
});