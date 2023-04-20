from fastapi import FastAPI, status, Response
from fastapi.middleware.cors import CORSMiddleware
import bd_lembrei as bd
from pydantic import BaseModel
import uvicorn

origins = ['http://localhost:3000']

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
login = {
}


@app.get("/")
def home():
    return "minha api esta no ar"


@app.get("/usuario/{idu}/{ids}")
def checklogin(idu: str, ids: str):
    login = bd.select('lembrei')
    bd.encerra
    for i in login:
        print(i)
        if idu == i[2]:
            print(i[2])
            if ids == i[3]:
                print('logado')
                return login
            else:
                return login
        else:
            return login


class Usuario(BaseModel):
    numero: str
    usuario: str
    senha: str
    email: str


@app.post("/usuario", status_code=status.HTTP_201_CREATED)
async def cadastro(usuario: Usuario,response: Response):
    insert = usuario.numero, usuario.usuario, usuario.senha, usuario.email
    try:
        resp = bd.insert_usuario(insert)
        response.status_code = status.HTTP_201_CREATED
        return resp 
    except:
       return "error: Ocorreu um erro ao inserir o registro"

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
