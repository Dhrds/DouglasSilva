import './App.css';
import { AiOutlineCheck } from 'react-icons/ai';
import { useState} from 'react';

function App() {

  const [input,setInput] =useState ('')

  function login(){
    alert( `Seja bem vindo ${input}`)
  }

  return (
    <div className="conteiner">
      <h1 className='title'>Lembrei</h1>
      <input className='user' type="text"
        placeholder='usuario'
        value={input} 
        onChange={(e)=>setInput(e.target.value)}/>
      
        <input className='senha' type="password"
          placeholder='senha' />
        <button className='button-login' onClick={login}>
          <AiOutlineCheck size={25} color='#000'></AiOutlineCheck>
          
        </button>
     
      <main>
        <h2>Bem vindo</h2>

      </main>



    </div>

  );
}

export default App;
