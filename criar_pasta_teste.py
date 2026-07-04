from pathlib import Path

# 1. Define a pasta onde vamos simular a bagunça (ainda não cria no disco)
pasta = Path("pasta_baguncada")

# 2. Cria a pasta de verdade; exist_ok=True = "se já existir, não reclame"
pasta.mkdir(exist_ok=True)

# 3. Lista com nomes de arquivos falsos, de tipos variados
arquivos_falsos = [
    "relatorio.pdf",
    "foto1.jpg",
    "foto2.png",
    "planilha.xlsx",
    "notas.txt",
    "dashboard.pbix",  # tipo "desconhecido" de proposito, pra testar o caso 5
]

# 4. Para cada nome da lista, cria um arquivo vazio dentro da pasta
for nome in arquivos_falsos:
    (pasta / nome).touch()

# 5. Mostra um resumo do que foi feito
print(f"Pronto! Criei {len(arquivos_falsos)} arquivos em '{pasta}'.")
