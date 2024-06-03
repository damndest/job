function moveAddFood() {
    location.href = "/foods/add/";
}

function delAreaFood() {
    location.href = "{% url 'foods:del' food.food_no %}"
}