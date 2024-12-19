import { useState, useEffect } from 'react'

function CravingsList() {
  const [recipes, setRecipes] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

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

  if(loading) return <p>Loading....</p>
  if(error) return <p>{`Error: ${error}`}</p>

  return(
    <div>
      <h1>{recipes[0].recipe}</h1>
      <p>vs</p>
      <h1>{recipes[1].recipe}</h1>
    </div>
  )
}

export default CravingsList
