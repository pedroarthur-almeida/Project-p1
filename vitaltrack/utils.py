import os
import platform
from prompt_toolkit import prompt
import shutil
from rich.align import Align
from rich.text import Text
from rich.panel import Panel
from rich.console import Console
import time
from itertools import cycle
from rich.live import Live
from rich.box import ROUNDED
c = Console()

class Utils:
    @staticmethod
    def limpar_tela_universal():
        sistema_operacional = platform.system()
        if sistema_operacional == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    @staticmethod
    def aguardar_volta():
        """Pausa a execução do programa até que o usuário tecle "enter".""" 
        input('\nPressione a tecla "enter" para continuar...')

    @staticmethod
    def entrada_centralizada(mensagem, is_password=False, deslocamento=0.45):
        """
        Exibe uma entrada centralizada com leve deslocamento para esquerda.
        """
        largura_terminal = shutil.get_terminal_size().columns
        padding = int((largura_terminal - len(mensagem)) * deslocamento)
        texto_formatado = ' ' * padding + mensagem
        return prompt(texto_formatado, is_password=is_password)
    
    @staticmethod
    def mensagem_centralizada(texto: str, estilo_texto="bold yellow", estilo_borda="bold yellow", titulo=None):
        """
        Cria e retorna um painel centralizado com texto estilizado.
        """
        rich_text = Text(texto, style=estilo_texto)
        painel = Panel(rich_text, expand=False, border_style=estilo_borda, title=titulo)
        return Align.center(painel)
    
    @staticmethod
    def mensagem_erro_centralizada(
        texto: str,
        titulo="[b]ERRO[/b]",
        cor_borda="red"
    ):
        """
        Cria e imprime um painel de erro com texto centralizado (sem formatação no conteúdo).
        """
        rich_text = Text(texto)  
        painel = Panel(rich_text, border_style=cor_borda, expand=False, title=titulo, title_align="center")
        painel_centralizado = Align.center(painel)
        c.print(painel_centralizado)

    @staticmethod
    def spinner_centralizado(mensagem="Carregando...", tempo=2, simbolos=None, cor_borda="purple"):
        """
        Exibe um spinner centralizado simulando uma transição de tela estilizada.
        """
        if simbolos is None:
            simbolos = [
                "[red]♥[/red]",
                "[magenta]◆[/magenta]",
                "[blue]●[/blue]",
                "[green]■[/green]"
            ]

        cores_mensagem = cycle(["bold cyan", "bold magenta", "bold blue", "bold green"])
        simbolo_ciclo = cycle(simbolos)
        cor_mensagem_ciclo = cycle(cores_mensagem)

        fim = time.time() + tempo

        with Live(console=c, refresh_per_second=10) as live:
            while time.time() < fim:
                simbolo = next(simbolo_ciclo)
                cor_texto = next(cor_mensagem_ciclo)
                
                painel = Panel(
                    Align.center(f"{simbolo} [{cor_texto}]{mensagem}[/{cor_texto}] {simbolo}"),
                    border_style=cor_borda,
                    expand=False,
                    box=ROUNDED
                )
                live.update(Align.center(painel))  # ✅ Agora está certo
                time.sleep(0.2)