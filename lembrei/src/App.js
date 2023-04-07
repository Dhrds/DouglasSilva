import './App.css';
import { AiOutlineCheck } from 'react-icons/ai';

function App() {
  return (
    <div className="conteiner">
      <h1 className='title'>Lembrei</h1>
      <input className='user' type="text"
        placeholder='usuario' />
      
        <input className='senha' type="password"
          placeholder='senha' />
        <button className='button-login'>
          <AiOutlineCheck size={25} color='#000'></AiOutlineCheck>
        </button>
     
      <main>
        <h2>Bem vindo</h2>

      </main>



    </div>

  );
}

export default App;
