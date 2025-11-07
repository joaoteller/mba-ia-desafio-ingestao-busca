# Desafio MBA Engenharia de Software com IA - Full Cycle

Este repositório contém uma solução de ingestão e busca com chat baseada em um conjunto de scripts Python.

Principais arquivos
- `src/ingest.py` — script responsável por ingerir documentos (PDFs) e indexá-los no banco/vetor store.
- `src/chat.py` — interface de chat que realiza buscas/consultas usando os dados ingeridos.
- `src/search.py` — criação do chain para busca no banco de dados.


Pré-requisitos
- Docker e Docker Compose (para subir o banco de dados usado pela solução)
- Python 3.8+ e pip

Instalação (opcional — recomenda-se usar um ambiente virtual)

```bash
# criar e ativar um ambiente virtual (opcional)
python -m venv .venv
source .venv/bin/activate

# instalar dependências do projeto
pip install -r requirements.txt
```

Como usar

1) Subir o banco de dados (container)

```bash
docker compose up -d
```

2) Executar o processo de ingestão dos PDFs

Coloque os arquivos PDF onde o `src/ingest.py` espera (ver código) e execute:

```bash
python src/ingest.py
```

3) Rodar o chat (interface de consulta)

```bash
python src/chat.py
```

Dicas e notas
- Se algo falhar ao conectar no banco, verifique os logs do Docker: `docker compose logs`.
- Para parar e remover os containers:

```bash
docker compose down
```

- Consulte os arquivos em `src/` para mais detalhes sobre parâmetros e caminhos de entrada/saída.
