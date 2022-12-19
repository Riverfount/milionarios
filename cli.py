import typer
from rich.console import Console
from rich.table import Table


main = typer.Typer(name='Milhonários CLI')


@main.command()
def conferir(dezenas: str, filepath: str = 'jogos.csv'):
    """\
    Confere se as dezenas sorteadas com os nossos jogos.
    As dezenas devem ser passadas entre aspas assim: "01, 23, 34, 41, 53, 60".
    Deve ser informado o nome do arquivo CSV com nossos jogos. Por padrão, se não for passado será jogos.csv.
    """
    table = Table(title="Resultado do Grupo Milhonários")
    fields = ["quadra", "quina", "mega-sena", "Nº dos Jogos Premiados"]
    for header in fields:
        table.add_column(header, style="magenta")
    jogos = [jogo.strip() for jogo in open(filepath, 'r').readlines()]
    dezenas_sorteadas = [dezena.strip() for dezena in dezenas.split(',')]
    mega_sena = 0
    quina = 0
    quadra = 0
    count = 0
    jogos_premiados = []
    for i, jogo in enumerate(jogos):
        for dezena in dezenas_sorteadas:
            if dezena in jogo:
                count += 1
        if count == 4:
            quadra += 1
            jogos_premiados.append(str(i + 1))
        elif count == 5:
            quina += 1
            jogos_premiados.append(str(i + 1))
        elif count == 6:
            mega_sena +=1
            jogos_premiados.append(str(i + 1))
        count = 0

    table.add_row(str(quadra), str(quina),str(mega_sena), ', '.join(jogos_premiados))
    Console().print(table)
