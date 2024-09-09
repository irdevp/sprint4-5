# Imagem base
FROM python:3.10-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar dependências e instalar
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copiar código do aplicativo
COPY . .

# Expor a porta 5000 para o Flask
EXPOSE 5000

# Comando para rodar o Flask
CMD ["flask", "run", "--host=0.0.0.0"]
