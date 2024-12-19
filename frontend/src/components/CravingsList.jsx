import { useState, useEffect } from 'react'

import CravingsCard from './CravingsCard.jsx'

function CravingsList() {
  const [recipes, setRecipes] = useState([])

  const [recipe1, setRecipe1] = useState({})
  const [recipe2, setRecipe2] = useState({})

  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  // Set the recipes from /all-recipes.json
  useEffect(() => {
    const fetchRecipes = async() => {
      try {
        const response = await fetch('/all-recipes.json')

        if(!response.ok) throw new Error('Failed to fetch recipes!')

        const data = await response.json()
        setRecipes(data)
      } catch(err) {
          setError(`Error: ${err}`)
      } finally {
          setLoading(false) 
      }
    }

    fetchRecipes()
  }, [])

  // Set recipe data for the card
  useEffect(() => {
    if(recipes.length != 0) {
      setRecipe1(recipes[0])
      setRecipe2(recipes[2])
    }
  }, [recipes])

  if(loading) return <p>Loading....</p>
  if(error) return <p>{`Error: ${error}`}</p>

  return(
    <div>
      <CravingsCard recipe={recipe1} />
      <p>or</p>
      <CravingsCard recipe={recipe2} />
    </div>
  )
}

export default CravingsList
