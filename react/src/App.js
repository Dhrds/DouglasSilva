import React from 'react';
import './App.css';
import lin from './/in.png'
import what from './/wh.png'
import Teste from 'C:/Users/douglas/Desktop/git/my-app/src/teste.png'
function App() {
  return (
    <div className="App">
      <header className="App-header navbar">
        <img className="logo_bar" src={Teste} alt="perfil" />
        <div className="titulo_bar">
          Douglas
        </div>
      </header>
      <main>
        <div className="container_0">
          <div className="container_1">
            <div className="canvas">
              <img className="foto_1" src={Teste} alt="perfil" />
              <div className="tittle">
                <h1 className="tittle">Douglas Silva</h1>
                <p className='subtitulo'>Desenvolvedor</p>
              </div>
              <footer children="canvas" className='footcanva'>
                <a href='https://www.linkedin.com/in/douglas-silva-122aa01b6/'> <img src={lin} className='lin' /></a>
               <a href='https://wa.me/5537999775765'> <img src={what} className='what' /></a>
              </footer>         
            </div>
            <div className='canvas_2'>
              <span>Sobre mim</span>
            </div>

          </div>
        </div>
      </main>
     {/* <footer>
      </footer> */}
    </div>
  );
}

export default App;

