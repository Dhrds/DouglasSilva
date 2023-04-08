from fastapi import FastAPI


#  pip install uvicorn.
#  Aqui é que vamos utilizar o uvicorn. Dentro do terminal você vai colocar o seguinte código: uvicorn + o nome do seu arquivo + : + o nome do seu aplicativo + –reload.
# uvicorn main:app –reload.


app=FastAPI()
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
                return {"True":1}
            else:
                return "False"
        else:
            return "False"
    