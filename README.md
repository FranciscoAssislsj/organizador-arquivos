# Organizador de Arquivos

Script em Python que varre uma pasta e move cada arquivo para uma subpasta organizada por tipo (PDFs, Imagens, Planilhas, Textos).

Primeiro projeto da Formação Engenheiro de IA (Projeto 1: automação pessoal em Python).

## O que faz

- Lê todos os arquivos de uma pasta.
- Identifica a extensão de cada um (`.pdf`, `.jpg`, `.png`, `.xlsx`, `.txt`).
- Move para uma subpasta correspondente, criando-a se ainda não existir.
- Ignora tipos de arquivo desconhecidos, sem quebrar.
- Mostra um resumo no fim: quantos foram movidos e quantos ignorados.

## Como rodar

1. (Opcional) Gere arquivos de teste:
   ```
   python criar_pasta_teste.py
   ```
2. Rode o organizador:
   ```
   python organizar.py
   ```

## Estrutura

- `criar_pasta_teste.py` · cria uma pasta `pasta_baguncada/` com arquivos falsos pra testar com segurança.
- `organizar.py` · o organizador em si.

## Como personalizar

Edite o dicionário `mapa` dentro de `organizar.py` para adicionar novas extensões e destinos. Exemplo:

```python
mapa = {
    ".pdf": "PDFs",
    ".pbix": "PowerBI",   # nova linha
}
```
## Autor

Francisco de Assis · [GitHub](https://github.com/FranciscoAssislsj)
