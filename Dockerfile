# Use uma imagem base do Python mais completa
FROM python:3.8

# Instalar o Git
RUN apt-get update && apt-get install -y git

# Atualizar o pip
RUN pip install --upgrade pip

# Instalar dependências do OpenCV (libGL, etc.)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo requirements.txt da raiz do projeto para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Comando para clonar o repositório de imagens
RUN git clone https://github.com/anottsu/find_person_with_python /app/dataCollect/animeImages

# Garantir que a pasta processed_images exista
RUN mkdir -p /app/dataCollect/processed_images

# Copiar o restante do projeto para o contêiner
COPY . /app

# Comando para rodar a aplicação
#CMD ["python", "dataCollect/processingImages.py"]
CMD python /app/dataCollect/processingImages.py && tail -f /dev/null
