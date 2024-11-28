function generateFood() {
  const foods = ['pizza', 'ice cream', 'hotdog']
  const random_food = foods[Math.floor(Math.random() * foods.length)]
  alert(`How about ${random_food}?`)

}
