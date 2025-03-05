# Use uma imagem base do Python mais completa
FROM python:3.8

RUN pip install --upgrade pip


# Instalar dependências do OpenCV (libGL, etc.)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt da raiz do projeto para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o restante do projeto para o contêiner
COPY . .

# Comando para rodar a aplicação
CMD ["python", "dataCollect/processingImages.py"]
