import React from "react";
import "./App.css";
import lin from ".//in.png"
import what from ".//wh.png"
import Teste from ".//teste.png"
function App() {
  return (
    <div className="App">
      <header className="App-header navbar">
        <img className="logo_bar" src={Teste} alt="perfil" />
        <div className="titulo_bar">   Douglas    </div>
        <div className="menu">
          <a href="#container_0">
            <div className="home">Home</div></a>
          <a href="#section2">
            <div className="habilidade">Habilidade</div></a>
          <a href="#section3">
            <div className="experiencias">experiencias</div></a>
          <a href="#section4">
            <div className="projetos">Projetos</div></a>

        </div>
      </header>
      <main>
        <section className="container_0" id="container_0">
          <div className="container_1" />
          <div className="container_2">
            <div className="canvas ">
              <a href="#section2">
                <img className="foto_1" src={Teste} alt="perfil" />
              </a>
              <div className="tittle">
                <h1 className="tittle1">Douglas Silva</h1>

              </div>
              <div className="subtitulo">Desenvolvedor</ div>
              <footer children="canvas" className="footcanva">
                <a href="https://www.linkedin.com/in/douglas-silva-122aa01b6/"> <img src={lin} className="lin" /></a>
                <a href="https://wa.me/5537999775765"> <img src={what} className="what" /></a>
              </footer>
            </div>
            <div className="canvas_2 ">
              <span className="span_1"> Olá Mundo</span>
              <p></p>
              <span> Um pouco sobre mim</span>
            </div>
          </div>
        </section>
        <section className="section2" id="section2"></section>
        <section className="section2" id="section3"></section>
        <section className="section2" id="section4"></section>
      </main>
      {/* <footer>
      </footer> */}
    </div>
  );
}

export default App;

