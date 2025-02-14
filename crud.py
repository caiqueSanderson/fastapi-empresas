from sqlalchemy.orm import Session
import models_db, schemas_db
from fastapi import HTTPException

# Create
def create_empresa(db: Session, empresa: schemas_db.EmpresaCreate):
	db_empresa = models_db.Empresa(**empresa.dict())
	db.add(db_empresa)
	db.commit()
	db.refresh(db_empresa)
	return db_empresa

def create_obrigacao_acessoria(db: Session, obrigacao: schemas_db.ObrigacaoAcessoriaCreate, empresa_id: int):
	db_obrigacao = models_db.ObrigacaoAcessoria(**obrigacao.dict(), empresa_id=empresa_id)
	db.add(db_obrigacao)
	db.commit()
	db.refresh(db_obrigacao)
	return db_obrigacao

# Read 
def get_empresa(db: Session, empresa_id: int):
	empresa = db.query(models_db.Empresa).filter(models_db.Empresa.id == empresa_id).first()
	if not empresa:
		raise HTTPException(status_code=404, detail="Empresa não encontrada")
	return empresa

def get_empresas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models_db.Empresa).offset(skip).limit(limit).all()

def get_obrigacoes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models_db.ObrigacaoAcessoria).offset(skip).limit(limit).all()

# Update
def update_empresa(db: Session, empresa_id: int, empresa_update: schemas_db.EmpresaCreate):
	empresa = db.query(models_db.Empresa).filter(models_db.Empresa.id == empresa_id).first()
	if not empresa:
		raise HTTPException(status_code=404, detail="Empresa não encontrada")

	for key, value in empresa_update.dict().items():
		setattr(empresa, key, value)

	db.commit()
	db.refresh(empresa)
	return empresa

def update_obrigacao_acessoria(db: Session, obrigacao_id: int, obrigacao_update: schemas_db.ObrigacaoAcessoriaCreate):
    obrigacao = db.query(models_db.ObrigacaoAcessoria).filter(models_db.ObrigacaoAcessoria.id == obrigacao_id).first()
    if not obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação acessória não encontrada")

    for key, value in obrigacao_update.dict().items():
        setattr(obrigacao, key, value)

    db.commit()
    db.refresh(obrigacao)
    return obrigacao

# Delete
def delete_empresa(db: Session, empresa_id: int):
    empresa = db.query(models_db.Empresa).filter(models_db.Empresa.id == empresa_id).first()
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")

    db.delete(empresa)
    db.commit()
    return {"message": "Empresa deletada com sucesso"}

def delete_obrigacao_acessoria(db: Session, obrigacao_id: int):
    obrigacao = db.query(models_db.ObrigacaoAcessoria).filter(models_db.ObrigacaoAcessoria.id == obrigacao_id).first()
    if not obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação acessória não encontrada")

    db.delete(obrigacao)
    db.commit()
    return {"message": "Obrigação acessória deletada com sucesso"}