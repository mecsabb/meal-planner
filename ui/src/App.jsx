import './App.css'
import { useNavigate } from 'react-router-dom';


function App() {
  let navigate = useNavigate();

  const handleClick = (path) => {
    navigate(path);
  };

  return (
    <>
    <p>Hello Muckers</p>
    <button onClick={() => handleClick('/generate')}>Generate shizzzz</button>
    <button onClick={() => handleClick('/discover')}>Discover meals</button>
    </>
  )
}

export default App
