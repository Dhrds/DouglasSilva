from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#  pip install uvicorn.
#  Aqui é que vamos utilizar o uvicorn. Dentro do terminal você vai colocar o seguinte código: uvicorn + o nome do seu arquivo + : + o nome do seu aplicativo + –reload.
# uvicorn main:app –reload.
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
    'teste':'123'
}

@app.get("/")
def home():
    return "minha api esta no ar"

@app.get("/login/{idu}/{ids}")
def checklogin(idu:str , ids:str):
    
    for i in login:
        if idu == i :
            if ids == login[i]:
                return "True"
            else:
                return "False"
        else:
            return "False"
    
@app.post("/login/{idu}/{ids}")
def cadastrar(idu:str , ids:str):
    login[idu]=ids
    return login