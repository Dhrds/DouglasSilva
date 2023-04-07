from fastapi import FastAPI


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
    