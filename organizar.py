from pathlib import Path
import shutil



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

    # list(...) tira uma "foto" dos arquivos ANTES de comecar a mexer,
    # pra nao se confundir com as subpastas novas que vamos criando
    for arquivo in list(pasta.iterdir()):

        # pula subpastas (ex: PDFs/ que ja criamos numa rodada anterior)
        if arquivo.is_dir():
            continue

        extensao = arquivo.suffix.lower()   # ex: ".pdf"
        destino = mapa.get(extensao)        # None se a extensao nao estiver no mapa

        # Caso PREVISIVEL: extensao fora do mapa -> decido ignorar (if/.get)
        if destino is None:
            print(f"{arquivo.name}  ->  (tipo desconhecido, ignorado)")
            ignorados += 1
            continue

        # Cria a subpasta de destino (ex: pasta_baguncada/Imagens)
        pasta_destino = pasta / destino
        pasta_destino.mkdir(exist_ok=True)

        # Caso IMPREVISIVEL: o sistema pode negar a mudanca (arquivo aberto,
        # sem permissao...) -> try/except protege pra nao quebrar tudo
        try:
            shutil.move(arquivo, pasta_destino / arquivo.name)
            print(f"{arquivo.name}  ->  {destino}/")
            movidos += 1
        except Exception as erro:
            print(f"FALHOU ao mover {arquivo.name}: {erro}")
            ignorados += 1

    # Resumo final
    print(f"\nPronto! {movidos} movidos, {ignorados} ignorados.")
    return movidos, ignorados

organizar_pasta("pasta_baguncada")