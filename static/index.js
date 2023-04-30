var SurveyComponent = Vue.component("survey-component", {
    template: '<survey :survey="survey" />',
    name: "survey-component",
    data() {
        const survey = new Survey.Model(json);
        survey.onComplete.add(async (sender, options) => {
            const stringJSON = JSON.stringify(sender.data);
            console.log(JSON.stringify(stringJSON));
            // No controlamos posible error
            await fetch("/guardar_respuestas", {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json"
                },
                body: stringJSON
            })
            window.location = "/"
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