import sqlite3
import os

# Função para criar o banco de dados e a tabela
def create_database(db_path='characters.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Cria a tabela se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS characters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            image_path TEXT NOT NULL
        )
    ''')

    # Salva e fecha a conexão
    conn.commit()
    conn.close()

# Função para inserir um personagem no banco de dados
def insert_character(name, image_path, db_path='characters.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Insere o personagem na tabela
    cursor.execute('''
        INSERT INTO characters (name, image_path)
        VALUES (?, ?)
    ''', (name, image_path))

    # Salva e fecha a conexão
    conn.commit()
    conn.close()

# Função para inserir os personagens das imagens nas subpastas
def insert_characters_from_images(image_folder, db_path='characters.db'):
    # Verifica se a pasta existe
    if not os.path.exists(image_folder):
        print(f"A pasta {image_folder} não existe!")
        return

    # Percorre todas as subpastas e arquivos na pasta principal
    for root, dirs, files in os.walk(image_folder):
        # Lista todas as imagens (PNG, JPG, JPEG) dentro das subpastas
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        
        # Insere cada personagem no banco de dados
        for image_file in image_files:
            # Extrai o nome do personagem (remover a extensão do arquivo)
            character_name = os.path.splitext(image_file)[0]
            
            # Caminho completo da imagem
            image_path = os.path.join(root, image_file)

            # Insere o personagem no banco de dados
            insert_character(character_name, image_path, db_path)
            print(f"Personagem {character_name} inserido com sucesso!")

# Caminho da pasta onde as imagens estão armazenadas
image_folder = '/home/anottsu/Documents/ALURA PYTHON/PROJETOS/FindPerson/dataCollect/animeImages'

# Cria o banco de dados e a tabela
create_database()

# Insere os personagens a partir das imagens
insert_characters_from_images(image_folder)
