import os
import psycopg2
from dotenv import load_dotenv
import string
import random

load_dotenv()

# ------------------------------------------
# CONEXÃO
# ------------------------------------------
def conectar():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        return conn
    except Exception as e:
        print("ERRO ao conectar:", e)
        return None


# ------------------------------------------
# BANCO
# ------------------------------------------
def criar_tabela():
    conn = conectar()
    if conn is None:
        return
    
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS senhas (
            id SERIAL PRIMARY KEY,
            senha TEXT NOT NULL
        );
    """)
    
    conn.commit()
    cursor.close()
    conn.close()


def inserir_senha(senha):
    conn = conectar()
    if conn is None:
        return
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO senhas (senha) VALUES (%s)", (senha,))
    
    conn.commit()
    cursor.close()
    conn.close()

    print("✔ Senha salva com sucesso!")


def listar_senhas():
    conn = conectar()
    if conn is None:
        return
    
    cursor = conn.cursor()
    cursor.execute("SELECT id, senha FROM senhas ORDER BY id DESC;")
    dados = cursor.fetchall()

    print("\n--- SENHAS SALVAS ---")
    if len(dados) == 0:
        print("Nenhuma senha encontrada.")
    else:
        for row in dados:
            print(f"ID: {row[0]} | Senha: {row[1]}")

    cursor.close()
    conn.close()


def deletar_senha(id_senha):
    conn = conectar()
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute("DELETE FROM senhas WHERE id = %s", (id_senha,))
    conn.commit()

    if cursor.rowcount > 0:
        print("✔ Senha deletada!")
    else:
        print("❌ ID não encontrado.")

    cursor.close()
    conn.close()


# ------------------------------------------
# FUNÇÃO GERAR SENHA
# ------------------------------------------
def gerar_senha(tam=12):
    chars = string.ascii_letters + string.digits + "!@#$%&*"
    return "".join(random.choice(chars) for _ in range(tam))


# ------------------------------------------
# MENU
# ------------------------------------------
def menu():
    while True:
        print("\n===== GERENCIADOR DE SENHAS =====")
        print("1 - Gerar nova senha")
        print("2 - Listar senhas")
        print("3 - Deletar senha")
        print("4 - Sair")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            tamanho = input("Tamanho da senha (12 padrão): ")
            tamanho = int(tamanho) if tamanho.isdigit() else 12
            nova = gerar_senha(tamanho)
            print("Senha gerada:", nova)
            inserir_senha(nova)

        elif opc == "2":
            listar_senhas()

        elif opc == "3":
            id_senha = input("ID da senha para deletar: ")
            if id_senha.isdigit():
                deletar_senha(int(id_senha))
            else:
                print("ID inválido.")

        elif opc == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


# ------------------------------------------
# MAIN
# ------------------------------------------
if __name__ == "__main__":
    criar_tabela()
    menu()