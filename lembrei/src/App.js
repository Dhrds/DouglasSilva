import './App.css';
import { AiOutlineCheck } from 'react-icons/ai';
import { useState} from 'react';
import api from './services/api';

function App() {

  const [input,setInput] =useState ('')
  const [input2,setInput2] =useState ('')
  async function login(){
    if(input===""){
      alert('vazio')
      return;
    }
    try {
      const response = await api.get('login/' + input + '/' + input2);
      console.log(response.data)
      alert("ok")
    }
    catch{
      alert("erro")

    }
  }

  return (
    <div className="conteiner">
      <h1 className='title'>Lembrei</h1>
      <input className='user' type="text"
        placeholder='usuario'
        value={input} 
        onChange={(e)=>setInput(e.target.value)}/>
      
        <input className='senha' type="password"
          placeholder='senha' 
          value={input2} 
        onChange={(e)=>setInput2(e.target.value)}/>
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
