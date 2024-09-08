# Use uma imagem base de Python
FROM python:3.9-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar os arquivos para o container
COPY requirements.txt requirements.txt
COPY app.py app.py

# Instalar as dependências
RUN pip install -r requirements.txt

# Expor a porta que o Flask usa
EXPOSE 3000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
