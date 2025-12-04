# Usa uma imagem leve do Python
FROM python:3.9-slim

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências para dentro do container
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o resto do seu código para dentro do container
COPY . .

# Expõe a porta que sua API usa (Geralmente 5000 para Flask ou 8000 para FastAPI/Django)
# Se souber a porta exata, altere aqui. Se não, pode deixar 8000.
EXPOSE 8000

# O comando para rodar seu app.
# IMPORTANTE: Troque 'app.py' pelo nome do seu arquivo principal python!
CMD ["python", "app.py"]