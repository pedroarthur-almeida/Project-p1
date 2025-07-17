from perguntas_quiz import perguntas_completas
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.console import Console
from datetime import datetime
from utils import Utils
from gerenciar_json import GerenciarJson
import random

c = Console()
gerenciador = GerenciarJson()

class Quiz:
    def __init__(self):
        self.perguntas = perguntas_completas
        self.limite_semanal = 5

    def exibir_menu(self, usuarios: dict, usuario_logado: str):
        while True:
            Utils.limpar_tela_universal()
            c.rule('\n[blue][b][i]VitalTrack - Quiz[/i][/][/]')
            print(' ')

            texto_menu = Text()
            texto_menu.append("\n")
            texto_menu.append("🎓 Bem-vindo ao Quiz VitalTrack!\n", style="bold yellow")
            texto_menu.append("Aprenda sobre saúde respondendo até 5 perguntas por semana.", style="dim")
            texto_menu.append("\n")
            painel_menu = Panel(texto_menu, border_style="bold blue", expand=False)
            c.print(Align.center(painel_menu))

            opcoes = Text()
            opcoes.append('\n1. 🎯 Iniciar Quiz\n', style='bold white')
            opcoes.append('2. 📊 Ver Progresso\n', style='bold white')
            opcoes.append('3. 🏅 Ver Conquistas\n', style='bold white')
            opcoes.append('4. 🔙 Voltar\n', style='bold white')
            painel_opcoes = Panel(opcoes, border_style='bold blue', expand=False)
            c.print(Align.center(painel_opcoes))

            Utils.mensagem_centralizada("Escolha uma opção (1-4):")
            opcao = Utils.entrada_centralizada('💬 : ').strip()

            if opcao == '1':
                Utils.spinner_centralizado("Carregando...", tempo=2)
                self.iniciar_quiz(usuarios, usuario_logado)
            elif opcao == '2':
                Utils.spinner_centralizado("Carregando...", tempo=2)
                self.verificar_progresso(usuarios[usuario_logado])
            elif opcao == '3':
                Utils.spinner_centralizado("Carregando...", tempo=2)
                self.mostrar_conquistas(usuarios[usuario_logado])
            elif opcao == '4':
                Utils.spinner_centralizado("Voltando...", tempo=2)
                break
            else:
                Utils.mensagem_erro_centralizada("Opção inválida!")
                Utils.aguardar_volta()

    def iniciar_quiz(self, usuarios: dict, usuario_logado: str):
        Utils.limpar_tela_universal()
        c.rule('\n[blue][b][i]VitalTrack - Quiz[/i][/][/]')
        usuario = usuarios[usuario_logado]

        # Inicializa o dict de progresso se não existir
        if not hasattr(usuario, "quiz_progresso") or usuario.quiz_progresso is None:
            usuario.quiz_progresso = {}

        progresso = usuario.quiz_progresso.setdefault("respondidas", {})

        # Aqui armazenamos as perguntas respondidas na semana atual (ano+semana) para controlar o limite
        ano_semana_atual = datetime.now().strftime("%Y-%U")  # Exemplo: '2025-29'

        respondidas = progresso.setdefault(ano_semana_atual, [])

        if len(respondidas) >= self.limite_semanal:
            c.rule('\n[blue][b][i]VitalTrack - Quiz[/i][/][/]')
            c.print(" ")
            Utils.mensagem_erro_centralizada(f"Você já respondeu o máximo de perguntas nesta semana!\nVolte após a próxima semana.")
            Utils.aguardar_volta()
            return

        perguntas_disponiveis = [i for i in range(len(self.perguntas)) if str(i) not in respondidas]
        if not perguntas_disponiveis:
            Utils.mensagem_erro_centralizada("Você já respondeu todas as perguntas do quiz!")
            Utils.aguardar_volta()
            return

        qtd_para_sortear = min(self.limite_semanal - len(respondidas), len(perguntas_disponiveis))
        sorteadas = random.sample(perguntas_disponiveis, qtd_para_sortear)

        for indice in sorteadas:
            pergunta = self.perguntas[indice]
            self.apresentar_pergunta(usuario, pergunta, indice)
            respondidas.append(str(indice))
            usuario.quiz_progresso.setdefault("respostas", {})[str(indice)] = {
                "data": datetime.now().strftime('%d/%m/%Y')
            }

        # Salva as alterações no JSON (todos os usuários)
        usuarios_dict = {email: usuario.to_dict() for email, usuario in usuarios.items()}
        gerenciador.salvar_dadosjson(usuarios_dict)
        
        c.rule('\n[blue][b][i]VitalTrack - Quiz[/i][/][/]')
        c.print(" ")
        sucesso = Text()
        sucesso.append("Você completou as perguntas disponíveis desta semana!", style="bold white")
        sucesso_painel = Panel(sucesso, expand=False, border_style="bold blue")
        sucesso_painel_center = Align.center(sucesso_painel)
        c.print(sucesso_painel_center)
        Utils.aguardar_volta()

    def apresentar_pergunta(self, usuario, pergunta, indice):
        Utils.limpar_tela_universal()
        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
        c.print(" ")
        pergunta_text = Text()
        pergunta_text.append("\n")
        pergunta_text.append(f"{pergunta['pergunta']}\n\n", style="bold yellow")
        pergunta_text.append(f"A. {pergunta['opcoes']['A']}\n", style="bold white")
        pergunta_text.append(f"B. {pergunta['opcoes']['B']}", style="bold white")
        pergunta_text.append("\n")

        painel = Panel(pergunta_text, title=f"Pergunta #{indice + 1}", border_style="bold blue", expand=False)
        c.print(Align.center(painel))

        resposta = ""
        while resposta not in ["A", "B"]:
            Utils.mensagem_centralizada("Digite A ou B: ")
            resposta = Utils.entrada_centralizada("💬 : ").strip().upper()
            if resposta not in ["A", "B"]:
                Utils.mensagem_erro_centralizada("Escolha inválida. Digite A ou B.")

        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
        c.print(" ")
        feedback = Text()
        feedback.append(f"\n🎯 Feedback: {pergunta['feedback'][resposta]}", style="bold white")
        feedback.append("\n")
        c.print(Align.center(Panel(feedback, border_style="bold blue", expand=False)))
        Utils.aguardar_volta()

    def verificar_progresso(self, usuario):
        if not hasattr(usuario, "quiz_progresso") or usuario.quiz_progresso is None:
            usuario.quiz_progresso = {}
        # Agora mostra a data atual, não só a semana
        data_atual = datetime.now().strftime("%d/%m/%Y")
        respondidas = usuario.quiz_progresso.get("respondidas", {})
        total_respondidas_semana = 0
        # Busca se tem algum registro para a semana atual (ano+semana)
        ano_semana_atual = datetime.now().strftime("%Y-%U")

        if ano_semana_atual in respondidas:
            total_respondidas_semana = len(respondidas[ano_semana_atual])

        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
        c.print(" ")
        texto = Text()
        texto.append(f"\n📅 Data atual: {data_atual}\n", style="bold yellow")
        texto.append(f"✅ Perguntas respondidas esta semana: {total_respondidas_semana}/{self.limite_semanal}\n", style="bold white")
        painel = Panel(texto, border_style="bold blue", expand=False)
        c.print(Align.center(painel))
        Utils.aguardar_volta()

    def mostrar_conquistas(self, usuario):
        respondidas_total = sum(len(lst) for lst in usuario.quiz_progresso.get("respondidas", {}).values())
        conquistas = []

        if respondidas_total >= 1:
            conquistas.append("🏅 Começou bem – 1 pergunta respondida")
        if respondidas_total >= 5:
            conquistas.append("🥉 Aprendiz da saúde – 5 perguntas")
        if respondidas_total >= 15:
            conquistas.append("🥈 Intermediário Vital – 15 perguntas")
        if respondidas_total >= 30:
            conquistas.append("🥇 Pró da Prevenção – 30 perguntas")
        if respondidas_total >= 45:
            conquistas.append("🏆 Mestre do Conhecimento – Quiz completo!")

        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
        c.print(" ")
        texto = Text()
        texto.append("\n")
        texto.append("Suas conquistas:\n\n", style="bold yellow")
        if conquistas:
            for cpt in conquistas:
                texto.append(f"{cpt}\n", style="bold white")
        else:
            texto.append("Nenhuma conquista ainda. Participe do quiz!", style="dim")
        texto.append("\n")

        painel = Panel(texto, border_style="bold blue", expand=False)
        c.print(Align.center(painel))
        Utils.aguardar_volta()
