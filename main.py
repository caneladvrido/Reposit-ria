from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def rota_inicial():
    return { 
        "message": "Olá mundo" 
    }
    
@app.get("/teste")
def rota_teste():
    return {
        "message": "Tá funcionando"
    }