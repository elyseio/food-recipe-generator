import { BrowserRouter, Routes, Route } from 'react-router-dom'

import HomePage from './pages/HomePage.jsx'
import BattlePage from './pages/BattlePage.jsx'

function App() {

  return(
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<HomePage />} />
        <Route path='/battle-page' element={<BattlePage />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
