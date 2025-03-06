import os
import cv2
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Caminho onde as imagens pré-processadas estão armazenadas
processed_images_folder = './processed_images'

# Lista para armazenar as imagens e rótulos
images = []
labels = []

# Função para carregar as imagens e os rótulos
def load_images_and_labels(image_folder):
    # Verifica se a pasta existe
    if not os.path.exists(image_folder):
        print(f"A pasta {image_folder} não existe!")
        return [], []

    # Percorre todas as imagens na pasta
    for image_file in os.listdir(image_folder):
        if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Caminho completo da imagem
            image_path = os.path.join(image_folder, image_file)
            
            # Lê a imagem usando OpenCV
            image = cv2.imread(image_path)

            # Redimensiona para 128x128 (ou o tamanho que você estiver usando)
            image_resized = cv2.resize(image, (128, 128))

            # Adiciona a imagem à lista
            images.append(image_resized)

            # Extrai o nome do personagem (sem a extensão do arquivo)
            character_name = os.path.splitext(image_file)[0]
            labels.append(character_name)

    return np.array(images), np.array(labels)

# Carregar as imagens e rótulos
X, y = load_images_and_labels(processed_images_folder)

# Certifique-se de que X seja um numpy array
X = np.array(X)

# Normalizar as imagens (dividindo por 255 para deixar no intervalo [0, 1])
X = X / 255.0

# Codificar os rótulos (nomes dos personagens) para valores numéricos
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Verificar as dimensões dos dados
print(f"Imagens (X): {X.shape}")
print(f"Rótulos (y): {y_encoded.shape}")

# Salvar os dados em arquivos .npy (para fácil carregamento posteriormente)
np.save('X_data.npy', X)
np.save('y_labels.npy', y_encoded)

# Se você quiser salvar os rótulos de forma legível, por exemplo, em um arquivo CSV
import pandas as pd
labels_df = pd.DataFrame({'Character Name': label_encoder.classes_})
labels_df.to_csv('character_labels.csv', index=False)

print("Dataset estruturado salvo com sucesso!")
