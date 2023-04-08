import './App.css';
import { AiOutlineCheck } from 'react-icons/ai';
import { useState } from 'react';
import api from './services/api';

function App() {

  const [input, setInput] = useState('')
  const [input2, setInput2] = useState('')
  const [input3, setInput3] = useState('')
  const [input4, setInput4] = useState('')

  async function login() {
    if (input === "") {
      alert('vazio')
      return;
    }
    try {

      const response = await api.get('login/' + input + '/' + input2);
      console.log(response.data)
      if (response.data == "True") {
        alert("ok logado")
      }
      alert("ok")
    }
    catch {
      alert("erro")

    }
  }

async function cadastrar(){
  if (input === "") {
    alert('vazio')
    return;
  }
}



  return (
    <div className="conteiner">
      <h1 className='title'>Lembrei</h1>
      <input className='user' type="text"
        placeholder='usuario'
        value={input}
        onChange={(e) => setInput(e.target.value)} />

      <input className='senha' type="password"
        placeholder='senha'
        value={input2}
        onChange={(e) => setInput2(e.target.value)} />
      <button className='button-login' onClick={login}>
        <AiOutlineCheck size={25} color='#000'></AiOutlineCheck>

      </button>

      <main>
        <h2>cadastrar</h2>
        <input type="text"
          placeholder='novo usuario'
          value={input3}
          onChange={(e) => setInput3(e.target.value)} />
        <input type="password"
          placeholder='nova senha'
          value={input4}
          onChange={(e) => setInput4(e.target.value)} />
          <button className='button-cadastrar' onClick={cadastrar}>
        <AiOutlineCheck size={25} color='#000'></AiOutlineCheck></button>


      </main>



    </div>

  );
}

export default App;
