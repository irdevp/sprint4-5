FROM python:3.9-slim

# Configurar o diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema necessárias para numpy e scikit-learn
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libatlas-base-dev

# Copiar e instalar dependências do Python
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir numpy scikit-learn joblib Flask boto3 pandas Werkzeug

# Copiar o código da aplicação
COPY . .

# Expor a porta para o Flask
EXPOSE 3000

# Comando para rodar a aplicação
CMD ["python", "app.py"]