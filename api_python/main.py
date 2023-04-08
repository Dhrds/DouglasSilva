from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import bd_lembrei as bd

#  pip install uvicorn.
# uvicorn main:app --reload

origins = ['http://localhost:3000']

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
login={
}

@app.get("/")
def home():
    return "minha api esta no ar"

@app.get("/login/{idu}/{ids}")
def checklogin(idu:str , ids:str):
    login= bd.select_bd.select('lembrei')
    bd.encerra   
    for i in login:
        print(i)
        if idu == i[2] :
            print(i[2])
            if ids == i[3]:
                print('logado')
                return login
            else:
                return login
        else:
            return login
    
@app.post("/cadastro/{idu}/{ids}/{tel}")
def cadastrar(idu:str , ids:str,tel:int):
    bd.conexao()
    tabela = 'lembrei'
    colunas = 'numero,usuario,senha'
    values=f'"+55{tel}","{idu}","{ids}"'
    bd.insert_bd.insert(tabela,colunas,values)
    bd.encerra
    return login

@app.post("usuario/msg/{msg}")
def cadmsg(msg:str):
    bd.conexao()
    parametro_mensagem = msg
    bd.insert_bd.insert(parametro_mensagem)
    

