from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Empresa(Base):
    __tablename__ = "empresas"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True,  nullable=False)
    cnpj = Column(String, unique=True,  nullable=False)
    endereco = Column(String,  nullable=False)
    email = Column(String,  nullable=False)
    telefone = Column(String, nullable=False)
    
    obrigacoes = relationship("ObrigacaoAcessoria", back_populates="empresa")

class ObrigacaoAcessoria(Base):
    __tablename__ = "obrigacoes_acessorias"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String,  nullable=False)
    periodicidade = Column(String,  nullable=False)  
    empresa_id = Column(Integer, ForeignKey('empresas.id'))
    
    empresa = relationship("Empresa", back_populates="obrigacoes")
