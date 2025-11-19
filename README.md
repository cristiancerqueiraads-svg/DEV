🧰 Gerador de Senhas + PostgreSQL (Docker)

Um gerador de senhas simples, robusto e plug-and-play, utilizando Python, PostgreSQL e Docker.
Toda a stack roda em contêiner — nada de dor de cabeça com instalação local.

🚀 Funcionalidades

Gera senhas aleatórias automaticamente (Minimo de 12 caracteres)

Salva em um banco PostgreSQL dentro do Docker

Exibe uma lista das senhas geradas

Arquitetura pronta pra escalar e virar um microprojeto real


🗃️ O que o app faz?

Toda vez que você rodar:

Cria a tabela, se não existir

Gera uma senha

Salva no PostgreSQL

Lista todas as senhas já cadastradas

Simples, direto ao ponto e extensível.

🛠️ Tecnologias usadas

Python

PostgreSQL 15 (Docker)


⚙️ Como rodar o projeto?

1️⃣ Configure seu arquivo .env

Crie um arquivo .env na raiz com:

DB_HOST=localhost
DB_PORT=5432
DB_NAME=senhas_db
DB_USER=postgres
DB_PASSWORD=sua_senha_aqui


2️⃣ Suba o ambiente com Docker
docker compose up -d

3️⃣ Execute o app
python app.py


