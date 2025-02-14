from database import Base, engine
from models_db import Empresa, ObrigacaoAcessoria

print("Criando as tabelas no banco de dados...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")
