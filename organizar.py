from pathlib import Path
import shutil
from rich.console import Console
from rich.table import Table



def organizar_pasta(pasta):
    # Pasta que vamos organizar
    pasta = Path(pasta)

    # Mapa: extensao -> nome da subpasta de destino
    mapa = {
        ".pdf": "PDFs",
        ".jpg": "Imagens",
        ".png": "Imagens",
        ".xlsx": "Planilhas",
        ".txt": "Textos",
    }

    # Contadores pro resumo do final
    movidos = 0
    ignorados = 0

    # Lista que ACUMULA uma linha por arquivo processado.
    # Cada item e uma tupla de 3 pedacos: (nome, destino, status)
    linhas = []

    # list(...) tira uma "foto" dos arquivos ANTES de comecar a mexer,
    # pra nao se confundir com as subpastas novas que vamos criando
    for arquivo in list(pasta.iterdir()):

        # pula subpastas (ex: PDFs/ que ja criamos numa rodada anterior)
        if arquivo.is_dir():
            continue

        extensao = arquivo.suffix.lower()   # ex: ".pdf"
        destino = mapa.get(extensao)        # None se a extensao nao estiver no mapa

        # Caso PREVISIVEL: extensao fora do mapa -> guardo como ignorado
        if destino is None:
            linhas.append((arquivo.name, "-", "[yellow]ignorado (tipo desconhecido)[/yellow]"))
            ignorados += 1
            continue

        # Cria a subpasta de destino (ex: pasta_baguncada/Imagens)
        pasta_destino = pasta / destino
        pasta_destino.mkdir(exist_ok=True)

        # Caso IMPREVISIVEL: o sistema pode negar a mudanca (arquivo aberto,
        # sem permissao...) -> try/except protege pra nao quebrar tudo
        try:
            shutil.move(arquivo, pasta_destino / arquivo.name)
            linhas.append((arquivo.name, f"{destino}/", "[green]movido[/green]"))
            movidos += 1
        except Exception as erro:
            linhas.append((arquivo.name, "-", f"[red]falhou: {erro}[/red]"))
            ignorados += 1

    # === EXIBICAO: agora que ja processei tudo, monto a tabela UMA vez ===
    console = Console()                          # o "printer" turbinado do rich
    tabela = Table(title="Arquivos organizados")
    tabela.add_column("Arquivo")                 # desenha o cabecalho das 3 colunas
    tabela.add_column("Destino")
    tabela.add_column("Status")

    # desempacota cada tupla acumulada e vira uma linha da tabela
    for nome, destino, status in linhas:
        tabela.add_row(nome, destino, status)

    console.print(tabela)
    console.print(f"\n[bold]Pronto![/bold] {movidos} movidos, {ignorados} ignorados.")

    return movidos, ignorados


organizar_pasta("pasta_baguncada")
