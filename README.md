# Cotacoes Amigoz Luiz Felipe
API para consultar a melhor cotação entre Dólar e Euro, utilizando Django REST Framework. Inclui um mock local para simulação das cotações enquanto a API oficial não estiver disponível.

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
- Poetry (para gerenciamento de dependências)
- Docker (opcional, para rodar via container)
- para baixar a imagem docker: docker pull felipecunhadev/cotacoes_amigoz_luiz_felipe
## Configuração do Ambiente

1. Clone o repositório.

2. Crie um arquivo `.env` na raiz do projeto com as variáveis abaixo:
API_COTACAO=http://host.docker.internal:3000 ou http://localhost:3000 (se for rodar local) 
DEBUG=True


> O arquivo `.env` não está versionado, então deve ser criado manualmente.

3. Instale as dependências com Poetry:

poetry install

4. Ative o ambiente virtual (dependendo do sistema, use um dos scripts):
    - No Windows PowerShell:
        .\activate_venv.ps1
    - No Linux/macOS Bash:
        source ./activate_venv.sh

5. Rodando a aplicação 
    localmente:
        python manage.py runserver

    via Docker:
        docker run -p 8000:8000 felipecunhadev/cotacoes_amigoz_luiz_felipe

6. API de Cotações
    Como foi citado no inicio do documento, a imagem docker disponibilizada para o desafio não estava podendo ser localizada no docker, então criei um mock que simula API's de cotação. Para ativar a api mock localmente basta digitar:
        python mock_api.py

7. Testes
    Os testes estão localizados em `cotacoes/core/tests/aplicacao/test_melhor_cotacao.py`.

8. Considerações finais
    Para verificação dos testes, deve ser alterado o '.env' para http://localhost:3000 e ativar o mock api

