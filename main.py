from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models_db, schemas_db
from database import SessionLocal, engine
from typing import List 
import crud


models_db.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "API empresas e obrigaçoes acessorias"}

@app.post("/empresas", response_model=schemas_db.Empresa)
def create_empresa(empresa: schemas_db.EmpresaCreate, db: Session = Depends(get_db)):
    return crud.create_empresa(db=db, empresa=empresa)

@app.post("/obrigacoes/{empresa_id}", response_model=schemas_db.ObrigacaoAcessoria)
def create_obrigacao(empresa_id: int, obrigacao: schemas_db.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    return crud.create_obrigacao_acessoria(db=db, obrigacao=obrigacao, empresa_id=empresa_id)


@app.get("/empresas/", response_model=List[schemas_db.Empresa])
def read_empresas(db: Session = Depends(get_db)):
    return crud.get_empresas(db=db)

@app.get("/empresas/{empresa_id}", response_model=schemas_db.Empresa)
def read_empresa(empresa_id: int, db: Session = Depends(get_db)):
    return crud.get_empresa(db=db, empresa_id=empresa_id)

@app.get("/obrigacoes/", response_model=List[schemas_db.ObrigacaoAcessoria])
def read_obrigacoes(db: Session = Depends(get_db)):
    return crud.get_obrigacoes(db=db)


@app.put("/empresas/{empresa_id}", response_model=schemas_db.Empresa)
def update_empresa(empresa_id: int, empresa: schemas_db.EmpresaCreate, db: Session = Depends(get_db)):
    return crud.update_empresa(db=db, empresa_id=empresa_id, empresa_update=empresa)

@app.put("/obrigacoes/{obrigacao_id}", response_model=schemas_db.ObrigacaoAcessoria)
def update_obrigacao(obrigacao_id: int, obrigacao: schemas_db.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    return crud.update_obrigacao_acessoria(db=db, obrigacao_id=obrigacao_id, obrigacao_update=obrigacao)


@app.delete("/empresas/{empresa_id}")
def delete_empresa(empresa_id: int, db: Session = Depends(get_db)):
    return crud.delete_empresa(db=db, empresa_id=empresa_id)

@app.delete("/obrigacoes/{obrigacao_id}")
def delete_obrigacao(obrigacao_id: int, db: Session = Depends(get_db)):
    return crud.delete_obrigacao_acessoria(db=db, obrigacao_id=obrigacao_id)
