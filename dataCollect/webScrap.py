import requests
import os

# Lista dos animes que você mencionou
anime_titles = [
    'Fullmetal Alchemist', 
    'Solo Leveling', 
    'One Piece', 
    'Jujutsu Kaisen', 
    'Hell\'s Paradise', 
    'Mushoku Tensei', 
    'Attack on Titan'
]

# Função para salvar as imagens localmente
def save_image(image_url, character_name, anime_name):
    try:
        # Faz o download da imagem
        img_response = requests.get(image_url)
        img_response.raise_for_status()  # Levanta um erro se falhar na requisição

        # Criando o diretório para salvar as imagens, se não existir
        dir_path = f'./anime_images/{anime_name}'
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # Salvando a imagem com o nome do personagem
        image_path = os.path.join(dir_path, f'{character_name}.jpg')
        with open(image_path, 'wb') as img_file:
            img_file.write(img_response.content)
        print(f"Imagem de {character_name} salva em {image_path}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar a imagem de {character_name}: {e}")

# Função para obter informações sobre o anime e os personagens
def get_anime_info(anime_title):
    # URL da Jikan API para buscar o anime pelo título
    search_url = f'https://api.jikan.moe/v4/anime?q={anime_title}&limit=1'

    # Fazendo a requisição
    response = requests.get(search_url)

    if response.status_code == 200:
        data = response.json()
        anime_data = data['data'][0]  # Pegando o primeiro resultado

        # Exibindo informações sobre o anime
        print(f"Title: {anime_data['title']}")
        print(f"Synopsis: {anime_data['synopsis']}")
        print(f"Genres: {[genre['name'] for genre in anime_data['genres']]}")
        print(f"Image URL: {anime_data['images']['jpg']['image_url']}")
        
        # Pegando os personagens
        characters_url = f"https://api.jikan.moe/v4/anime/{anime_data['mal_id']}/characters"
        char_response = requests.get(characters_url)

        if char_response.status_code == 200:
            char_data = char_response.json()
            print("Characters:")
            for character in char_data['data']:
                character_name = character['character']['name']
                image_url = character['character']['images']['jpg']['image_url']
                print(f"- {character_name}")
                print(f"  Image: {image_url}")
                
                # Baixando e salvando a imagem do personagem
                save_image(image_url, character_name, anime_data['title'])
        else:
            print(f"Erro ao obter personagens para {anime_title}")
    else:
        print(f"Erro: {response.status_code} - Não foi possível encontrar o anime {anime_title}")

# Obtendo informações de cada anime da lista
for anime in anime_titles:
    get_anime_info(anime)
    print("\n" + "-"*40 + "\n")
