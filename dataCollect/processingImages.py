import os
import cv2
import numpy as np

# Função para pré-processar a imagem
def preprocess_image(image_path, target_size=(128, 128)):
    try:
        # Lê a imagem com OpenCV
        image = cv2.imread(image_path)

        # Verifica se a imagem foi carregada corretamente
        if image is None:
            print(f"Não foi possível carregar a imagem: {image_path}")
            return None

        # Redimensionar para o tamanho fixo
        image_resized = cv2.resize(image, target_size)

        # Converter para escala de cinza (opcional)
        image_gray = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)

        # Normalizar os valores dos pixels
        image_normalized = image_gray / 255.0

        # Remover ruídos com um filtro gaussiano
        image_denoised = cv2.GaussianBlur(image_normalized, (5, 5), 0)

        return image_denoised
    except cv2.error as e:
        print(f"Erro ao processar a imagem: {e}")
        return None

# Função para salvar a imagem pré-processada
def save_processed_image(image, character_name, save_dir='./processed_images'):
    try:
        # Cria o diretório para salvar as imagens se não existir
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # Salva a imagem processada no diretório
        image_path = os.path.join(save_dir, f'{character_name}.png')  # Salvando como PNG
        cv2.imwrite(image_path, (image * 255).astype(np.uint8))  # Multiplica por 255 para restaurar a escala
        print(f"Imagem de {character_name} salva em {image_path}")
    except Exception as e:
        print(f"Erro ao salvar a imagem: {e}")

# Função para processar todas as imagens da pasta local
def process_and_save_images_from_folder(folder_path):
    # Verifica se o diretório existe
    if not os.path.exists(folder_path):
        print(f"A pasta {folder_path} não existe!")
        return

    # Lista todos os arquivos na pasta
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Processa cada imagem na pasta
    for image_file in image_files:
        # Caminho completo da imagem
        image_path = os.path.join(folder_path, image_file)
        
        # Extrai o nome do personagem (remover a extensão do arquivo)
        character_name = os.path.splitext(image_file)[0]

        # Pré-processa a imagem
        processed_image = preprocess_image(image_path)
        if processed_image is not None:
            # Salva a imagem pré-processada
            save_processed_image(processed_image, character_name)

# Caminho da pasta onde as imagens estão armazenadas
folder_path = '/app/dataCollect/animeImages'





# Processa e salva as imagens da pasta local
process_and_save_images_from_folder(folder_path)
