import React from "react";
import { Route, Routes, BrowserRouter } from "react-router-dom";

import Home from "./home";
import Login from "./login";
import Cadastro from "./cadastro";
import Cadastro_agenda from "./cadastro_agenda";
import Consulta from "./consulta";

const multe = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route component={Login} path="/" exact />
            </Routes>
        </BrowserRouter>
    )
}

export default multe;