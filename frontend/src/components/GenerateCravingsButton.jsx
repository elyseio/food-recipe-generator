import { useNavigate } from 'react-router-dom'

function GenerateCravingsButton() {
  const navigate = useNavigate()

  function goBattle() {
    navigate('/battle-page') 
  }

  return(
    <button onClick={goBattle}>generate cravings</button>
  )
}

export default GenerateCravingsButton
