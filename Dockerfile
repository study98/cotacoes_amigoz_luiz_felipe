# Etapa 1: Imagem base com Python/Django
FROM python:3.13-slim AS base

# Etapa 2: Variáveis de ambiente para o Python não gerar arquivos '.pyc' e logs interativos
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Etapa 3: Instalações básicas (build essentials, curl para baixar o Poetry)
RUN apt-get update && apt-get install -y \
    build-essential curl && \
    apt-get clean

# Etapa 4: Instalar o Poetry manualmente
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Etapa 5: Criar diretório da aplicação e definir como diretório de trabalho
WORKDIR /app

# Etapa 6: Copiar os arquivos de dependência primeiro (para cache de build)
COPY pyproject.toml poetry.lock* /app/

# Etapa 7: Instalar dependências com Poetry (sem criar venv separada)
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Etapa 8: Copiar o restante do código-fonte
COPY . /app

# Etapa 9: Expor a porta 8000 (onde o Django vai rodar)
EXPOSE 8000

# Etapa 10: Comando padrão para rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]