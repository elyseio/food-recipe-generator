import CravingsList from '../components/CravingsList.jsx'

function BattlePage() {
  /*
   * 1. Generate card list:
   *  card1 = adobo (clickable)
   *          vs
   *  card2 = sinigang (clickable)
  */
  return(
    <div>
      <h1>Battle Page</h1>
      <CravingsList />
    </div>
  )
}

export default BattlePage
