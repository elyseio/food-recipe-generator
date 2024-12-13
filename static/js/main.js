/*
 * 0. Generate cravings -> change to screen 2: food1 or food2
 * 1. how to get food1 or food2 from array of foods, and slice them from it
 * 1.1 

*/

function startCravings() {
  const foods = ['pizza', 'ice cream', 'hotdog', 'kangkong', 'adobong manok']
  console.log("original foods: ", foods)

  // Generate random int based on foods array
  let randI1 = Math.floor(Math.random() * foods.length)
  
  // Store that food
  let food1 = foods[randI1]

  // Remove that food so we can no longer choose it again
  foods.splice(randI1, 1)

  let randI2 = Math.floor(Math.random() * foods.length)
  let food2 = foods[randI2]
  foods.splice(randI2, 1)

  console.log(food1 + " or " + food2)

  console.log("foods: ", foods)
}
