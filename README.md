# 🚀 FastAPI - Gerenciamento de Empresas e Obrigações Acessórias

## 📌 Descrição
Este projeto é uma API desenvolvida com **FastAPI**, **SQLAlchemy** e **Pydantic**, utilizando um banco de dados **PostgreSQL** para cadastrar empresas e gerenciar suas obrigações acessórias.

## 🛠 Tecnologias Utilizadas
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [PostgreSQL](https://www.postgresql.org/)

---
## 📂 Estrutura do Projeto
```
/                # Diretório de migrações do Alembic
├── main.py                  # Arquivo principal da API
├── models_db.py                # Modelos do banco de dados
├── schemas_db.py               # Schemas Pydantic para validação
├── crud.py                  # Funções para manipulação do banco
├── database.py              # Configuração do banco de dados
├── creta_tables.py          # Diretório de migração para gerar tabelas no banco
├── tests.py
├── .env                     # Variáveis de ambiente (banco de dados)
└── README.md                # Documentação do projeto
```

---
## 🚀 Como Rodar o Projeto

### 1️⃣ Configurar o ambiente
Clone o repositório e acesse a pasta do projeto:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

Crie e ative um ambiente virtual:
```bash
python -m venv venv  # Criar o ambiente virtual
source venv/bin/activate  # Ativar no Linux/macOS
venv\Scripts\activate  # Ativar no Windows
```

### 3️⃣ Configurar o banco de dados
Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
```ini
DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco
```

### 5️⃣ Iniciar a API
```bash
uvicorn main:app --reload
```

---
## 🛠 Endpoints Disponíveis
A documentação da API pode ser acessada via **Swagger UI**:
- 📄 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---
## ✅ Funcionalidades
- **CRUD de Empresas** (Cadastro, leitura, edição e remoção)
- **CRUD de Obrigações Acessórias**
- **Validação de dados com Pydantic**
- **Uso do Alembic para migrações do banco de dados**

---
## 🧪 Testes
Para rodar os testes unitários, utilize:
```bash
pytest
```

---
## 📜 Licença
Este projeto é de uso livre conforme a [MIT License](LICENSE).

📌 **Autor:** Caique Sanderson de Sá Borges | [LinkedIn](https://www.linkedin.com/in/caique-sanderson-de-s%C3%A1-borges-262545237/)

