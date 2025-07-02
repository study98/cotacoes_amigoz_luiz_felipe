# 💱 Cotação - Amigoz (Desafio Técnico) – Luiz Felipe
API REST em Django que consulta a melhor cotação entre Dólar e Euro. Desenvolvida com arquitetura baseada em DDD, uso de Docker, testes automatizados e documentação Swagger.

## 🚀 Tecnologias Utilizadas

- Python 3.13
- Django 5.2
- Django REST Framework
- drf-spectacular (Swagger/OpenAPI)
- Docker e Docker Compose
- Poetry
- Pytest

## Estrutura do Projeto

- `cotacoes_amigoz_luiz_felipe/` (pasta raiz do projeto)
  - `manage.py` (arquivo para gerenciar comandos Django)
  - `mock_api.py` (mock local para simular a API de cotações)
  - `.env` (arquivo para variáveis de ambiente, não versionado)
  - `cotacoes/` (pasta com o código principal)
    - `app/` (configurações Django e app principal)
    - `core/` (app com lógica de negócio)
      - `tests/aplicacao/test_melhor_cotacao.py` (testes do sistema)
    - `__init__.py`
  - `pyproject.toml` (configuração do Poetry)
  - `poetry.lock`
  - `Dockerfile`

## Requisitos

- Python 3.13+
- [Poetry](https://python-poetry.org/docs/#installation) (para gerenciamento de dependências)
- Docker (opcional, para rodar via container)
- para baixar a imagem docker: docker pull felipecunhadev/cotacoes_amigoz_luiz_felipe

## ⚙️ Variáveis de Ambiente
  - Crie um arquivo `.env` na raiz do projeto com:
    - API_COTACAO=http://localhost:3000 - para testes locais usando a imagem do desafio de cotações
    - API_COTACAO=http://cotacao-service:3000
    - DEBUG=True

> O arquivo `.env` não está versionado, então deve ser criado manualmente.

## Configuração do Ambiente

1. Clone o repositório.

2. Crie um arquivo `.env` na raiz do projeto:

3. Instale as dependências com Poetry: poetry install

4. Ative o ambiente virtual (dependendo do sistema, use um dos scripts):
    - No Windows PowerShell:
        .\activate_venv.ps1
    - No Linux/macOS Bash:
        source ./activate_venv.sh

5. Rodando a aplicação:
   - localmente:
     - alterar o '.env' no campo 'API_COTACAO' para 'http://localhost:3000'
     - ativar a venv
     - rodar o projeto com: python manage.py runserver
     - api de consultas - docker run -p 3000:3000 --rm --name desafio-cotacoes mostela/desafiocotacoes
       
   - via Docker:
     - rodar a api de consultas - docker run -p 3000:3000 --rm --name desafio-cotacoes mostela/desafiocotacoes
     - acessar a pasta raiz do desafio
     - rodar o comando: docker run -p 8000:8000 --env-file .env felipecunhadev/cotacoes_amigoz_luiz_felipe

  
  
7. Endpoints principais
   - GET /api/melhor-cotacao/ → Retorna a moeda com melhor cotação no momento
   - GET /api/schema/ → Schema OpenAPI 3.0
   - GET /api/docs/ → Interface Swagger para testes

8. Testes
  - Os testes estão localizados em `cotacoes/core/tests/aplicacao/aplicacao/test_melhor_cotacao.py` e `cotacoes/core/tests/aplicacao/integracao/test_api_cotacoes.py`.
  - para rodar todos os testes de uma vez: 'pytest cotacoes' - recomendasse que a imagem docker 'desafiocotacoes' esteja ligada
   
10. Considerações finais
    - Imagem pública: docker pull felipecunhadev/cotacoes_amigoz_luiz_felipe
    - Observações
        - Arquitetura baseada em DDD: separação clara entre domínio, aplicação e infraestrutura.
        - API documentada com Swagger via drf-spectacular.
        - Mocks e testes organizados conforme boas práticas.
