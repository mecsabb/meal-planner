import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

function Generate(){
    const [recipe, setRecipe] = useState(null);
    let navigate = useNavigate();

    const fetchRecipe = () => {
        fetch('http://127.0.0.1:8000/generate')
            .then(response => response.text())
            .then(data => setRecipe(data))
            .catch(error => console.error("Error fetching recipe: ", error));
    }

    useEffect(() => {
        fetchRecipe();
    }, []);
    
    if (!recipe) return "Loading...";

    //consider making a Button.jsx component that can be reused
    const handleClick = (path) => {
      navigate(path);
    };


    return(
        <>
        <h4>Your meal will be: </h4>
        <p>{recipe}</p>
        <button onClick={fetchRecipe}>Regenerate</button>
        <button onClick={() => handleClick('/')}>Home</button>
        </>
    );

}

export default Generate