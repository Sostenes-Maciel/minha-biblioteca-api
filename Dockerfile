# Usa a imagem Python 3.9 mais leve (slim)
FROM python:3.11-slim

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências para dentro do container
COPY requirements.txt .

# 🛠️ CORREÇÃO (Obrigatória para resolver o erro "exit code: 1")
# Instala ferramentas do sistema operacional (build-essential e headers do Python) necessárias para o pip compilar bibliotecas como pytest.
# O "rm -rf..." garante que a imagem não fique inchada com dados temporários.
RUN apt-get update && \
    apt-get install -y build-essential python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Instala as dependências Python listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do seu código fonte para o container
COPY . .

# Expõe a porta que sua API Python está rodando
EXPOSE 8000

# O comando final que inicia sua aplicação
# ⚠️ IMPORTANTE: Ajuste 'app.py' para o nome do seu arquivo principal (ex: main.py, api.py)
CMD ["python", "app.py"]