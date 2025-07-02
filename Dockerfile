# Imagem base com Python/Django
FROM python:3.13-slim AS base

# Variáveis de ambiente para o Python não gerar arquivos desnecessários e logs interativos
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalações básicas (build essentials, curl para baixar o Poetry)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
# Etapa 4: Instalar o Poetry manualmente
RUN curl -sSL https://install.python-poetry.org | python3 -

# Adicionar Poetry ao PATH
ENV PATH="/root/.local/bin:$PATH"

# Etapa 5: Criar diretório da aplicação e definir como diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências primeiro para cache de camada do Docker
COPY pyproject.toml poetry.lock* /app/


# Configurar Poetry para não criar virtualenv e instalar dependências (sem instalar pacote)
RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction --no-ansi --no-root

# Copiar o restante do código-fonte
COPY . /app

ENV DJANGO_SETTINGS_MODULE=cotacoes.app.settings

# Expor a porta 8000 (onde o Django vai rodar)
EXPOSE 8000

# Comando  para rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]