from rich.align import Align            
from rich.columns import Columns
import random
from saudecorporal import *
from quiz import Quiz
from perguntas_quiz import perguntas_completas

class Menus:
    def __init__(self, cadastro):
        self.cadastro = cadastro
        pass
    

    def exibir_menu_inicial(self, usuarios):
        """
        Menu inicial,
        é exibido logo após iniciar o programa,
        abre ao usuário as opções de cadastro e login.
        """
        Utils.limpar_tela_universal()
    
        while True:
            
            c.rule('[blue][i][b]Boas vindas ao VitalTrack![/b][/i][/]')
            print(' ')
            textomenuinicial_text = Text()

            textomenuinicial_text.append('\n')
            textomenuinicial_text.append('Seja bem vindo(a) ao menu inicial!\n', style = 'bold yellow')
            textomenuinicial_text.append('\nEscolha uma opção dentre as disponíveis.\n', style = 'dim')

            textomenuinicial_text.append('\n1 ', style = 'red')
            textomenuinicial_text.append('Cadastro\n')

            textomenuinicial_text.append('2 ', style = 'red')
            textomenuinicial_text.append('Login\n')

            textomenuinicial_text.append('3 ', style = 'red')
            textomenuinicial_text.append('Sair\n')

            panel = Panel(textomenuinicial_text, border_style="bold blue", expand = False,title="[bold blue]Menu Inicial[/bold blue]",
        title_align="center")
            panel_centralizado = Align.center(panel)
            c.print(panel_centralizado)

            entradamenu_inicial = Text()
            entradamenu_inicial.append('Digite sua opção: ', style = 'bold yellow')

            pentradamenu_inicial = Panel(entradamenu_inicial, expand = False, border_style = 'bold yellow')
            pentradamenu_inicial_center = Align.center(pentradamenu_inicial)
            c.print(pentradamenu_inicial_center)

            opçao1 = Utils.entrada_centralizada('💬 : ')

            if opçao1 == '1':
                Utils.spinner_centralizado("Carregando...", tempo = 2)
                usuario_criado = self.cadastro.cadastro_de_usuario()
                if usuario_criado is not None:
                    self.cadastro.usuario_logado = usuario_criado
                    self.exibir_menu_logado(usuarios)
                else:
                    Utils.mensagem_erro_centralizada("Erro ao cadastrar usuário!")
                        
            elif opçao1 == '2':
                Utils.spinner_centralizado("Carregando...", tempo=2)
                usuario_logado = self.cadastro.fazer_login()
                if usuario_logado:  
                    self.cadastro.usuario_logado = usuario_logado
                    Utils.spinner_centralizado("Carregando...", tempo = 2)
                    self.exibir_menu_logado(usuarios)  
                    
            elif opçao1 == '3':
                Utils.spinner_centralizado("Saindo...", tempo = 2)
                c.print(Panel('até logo! 👋', expand = False, border_style = 'cyan'))
                break

            else:
                Utils.mensagem_erro_centralizada("Opção inválida!\nDigite uma opção presente no MENU.")
                Utils.aguardar_volta()
        return usuarios

    def exibir_menu_logado(self, usuarios):
        """
        Menu onde o usuário tem acesso as funcionalidades do programa,
        só é possível ter acesso a esse menu após o login.
        """
        while True:
            Utils.limpar_tela_universal()
            c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
            print(' ')

            usuario_logado = self.cadastro.usuario_logado
            nome = self.cadastro.usuarios[usuario_logado].nome
            saude = SaudeCorporal(usuarios, usuario_logado, self.cadastro)

            mensagens = [
            "💧 Não esqueça de se hidratar!",
            "🚀 O sucesso é uma jornada, não um destino.",
            "💡 Você é capaz de grandes coisas!",
            "🔥 Um passo por dia já é progresso.",
            "🌱 Grandes mudanças começam com pequenas atitudes.",
            "🏃 Mexa-se pelo seu bem-estar!",
            "🧠 Mente sã, corpo são.",
            "⏳ Cada segundo investido vale a pena."
            ]

            mensagem = random.choice(mensagens)
            header = Panel(f"👤 Logado como: {nome}", width=80, title="Menu Principal", style="red")

            parte1 = Text()
            parte1.append('\n')
            parte1.append('Escolha uma opção:')
            parte1.append('\n')
            parte1.append("\n[1] 👤 Ver perfil completo\n", style="cyan")
            parte1.append("[2] 📏 Calcular IMC\n", style="cyan")
            parte1.append("[3] 🔥 Calcular TMB\n", style="cyan")
            parte1.append("[4] 🍽️  Registro de calorias\n", style="cyan")
            parte1.append("[5] 💧 Registro de água",style = "cyan")
            parte1.append('\n')
            painel1 = Panel(parte1, title="Vital", border_style="cyan", width=38)

            parte2 = Text()
            parte2.append('\n')
            parte2.append('No VitalTrack, o foco é você.')
            parte2.append('\n')
            parte2.append("\n[6] ✏️  Atualizar perfil\n", style="cyan")
            parte2.append("[7] 🎯 Atualizar objetivo/dados\n", style="cyan")
            parte2.append("[8] 🚪 Deslogar\n", style="cyan")
            parte2.append("[9] ❓ Quiz\n", style="cyan")
            parte2.append("[10] 🗑️  Deletar conta", style = "red")
            parte2.append('\n')
            painel2 = Panel(parte2, title="Track", border_style="cyan", width=38)

            inspiracao = Panel(Text(mensagem, justify="center", style="magenta"), title="Seja bem vindo(a)!", border_style="magenta", width=80)

            footer = Panel(Text("Digite a opção desejada.", justify="center", style="yellow"), width=80, style="grey37")

            c.print(Align.center(header))
            c.print(Align.center(Columns([painel1, painel2], expand=False)))
            c.print(Align.center(inspiracao))
            c.print(Align.center(footer))
            
            opcao = Utils.entrada_centralizada('💬 : ').strip()
            
            if opcao == '1':
                Utils.spinner_centralizado("Carregando...", tempo = 2)
                Utils.limpar_tela_universal()
                c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                print(' ')

                verperfil_text = Text()
                verperfil_text.append('\n')
                verperfil_text.append("Menu de Perfil — Visualização de Informações Pessoais.\n", style="bold yellow")
                verperfil_text.append("Confira abaixo os dados cadastrados em seu perfil no VitalTrack.", style="dim")
                verperfil_text.append('\n')
                verperfil_text_panel = Panel(verperfil_text,border_style="blue",expand=False)
                c.print(Align.center(verperfil_text_panel))

                verpefil_text = Text()
                verpefil_text.append(f'\n👤 Nome: {self.cadastro.usuarios[usuario_logado].nome}')
                verpefil_text.append(f'\n📧 Email: {usuario_logado}')

                objetivos = {
                    '1': 'GANHO DE MASSA',
                    '2': 'PERDA DE PESO',
                    '3': 'MANUTENÇÃO DA SAÚDE'
                                            }
                if self.cadastro.usuarios[usuario_logado].dados:
                    dados = self.cadastro.usuarios[usuario_logado].dados
                    objetivo_id = self.cadastro.usuarios[usuario_logado].objetivo 
                    verpefil_text.append(f'\n🎯 Objetivo: {objetivos.get(objetivo_id, "Não definido")}')
                    verpefil_text.append(f'\n🎂 Idade: {dados["idade"]} anos')
                    verpefil_text.append(f'\n💪 Peso: {dados["peso"]} kg')
                    verpefil_text.append(f'\n📏 Altura: {dados["altura"]} m')
                    
                    pverperfil = Panel(verpefil_text, border_style="bold blue", expand = False,title="📝",
        title_align="center")
                    
                    sexo_escolha = dados.get('sexo_escolha', None)

                    if sexo_escolha in ['1', '3']:  # homem cis ou homem trans
                        sexo_exibicao = 'Masculino'

                    elif sexo_escolha in ['2', '4']:  # mulher cis ou mulher trans
                        sexo_exibicao = 'Feminino'

                    else:
                        sexo_exibicao = 'Não informado'
                verpefil_text.append(f'\n⚪ Sexo: {sexo_exibicao}')
                verpefil_text.append('\n')  
                pverperfil_center = Align.center(pverperfil)      
                c.print(pverperfil_center)    
                Utils.aguardar_volta()
                Utils.spinner_centralizado("Voltando...", tempo = 2)
                Utils.limpar_tela_universal()

            elif opcao == '2':
                Utils.spinner_centralizado("Carregando...", tempo = 2)
                saude.calcular_imc(cadastro, usuario_logado)

            elif opcao == '3':
                Utils.spinner_centralizado("Carregando...", tempo = 2)
                saude.calcular_taxametabolicabasal(self.cadastro.usuarios, usuario_logado)

            elif opcao == '4':
                Utils.spinner_centralizado("Carregando...", tempo = 2)
                usuarios = saude.registrar_calorias(self.cadastro.usuarios, usuario_logado)
            
            elif opcao == '5':
                Utils.spinner_centralizado("Carregando...", tempo = 2)
                usuarios = saude.registrar_agua(self.cadastro.usuarios, usuario_logado)
                
            elif opcao == '6':
                Utils.spinner_centralizado("Carregando...", tempo = 2)
                usuarios = self.cadastro.atualizar_usuario(self.cadastro.usuarios)

            elif opcao == '7':
                Utils.spinner_centralizado("Carregando...", tempo = 2)
                print('\nAtualizando dados...')
                usuarios, usuario_logado = self.cadastro.atualizar_dados()
                self.cadastro.usuarios = usuarios
                self.cadastro.usuario_logado = usuario_logado

            elif opcao == '8':
                Utils.spinner_centralizado("Carregando...", tempo = 2)
                Utils.limpar_tela_universal()

                while True:
                    c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                    print(' ')

                    deslogar_text = Text()
                    deslogar_text.append('\n')
                    deslogar_text.append("Área de Logout – Gerencie sua sessão.\n", style="bold yellow")
                    deslogar_text.append("Confirme se deseja deslogar do sistema.", style="dim")
                    deslogar_text.append('\n')

                    login_panel = Panel(deslogar_text,border_style="blue",expand=False)
                    c.print(Align.center(login_panel))


                    confirmedeslogar_text = Text()
                    confirmedeslogar_text.append("Deseja mesmo deslogar? (s/n):", style = "bold yellow")
                    pconfirmedeslogar_text = Panel(confirmedeslogar_text, expand = False, border_style = "bold yellow")
                    pconfirmedeslogar_text_center = Align.center(pconfirmedeslogar_text)
                    c.print(pconfirmedeslogar_text_center)


                    deslog = input('💬 : ').strip()

                    if deslog == 's':
                        self.cadastro.usuario_logado = None
                        deslogado_text = Text()
                        deslogado_text.append('✅ Deslogado com sucesso!', style = 'bold white')
                        pdeslogado_text = Panel(deslogado_text, expand = False, border_style = 'bold blue')
                        pdeslogado_text_center = Align.center(pdeslogado_text)
                        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                        print(' ')
                        c.print(pdeslogado_text_center)
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()
                        return None
                    
                    elif deslog == 'n':
                        permanecelogado_text = Text()
                        permanecelogado_text.append('Você permanece logado.')
                        painelpermanecelogado_text = Panel(permanecelogado_text, expand = False, border_style = 'bold blue')
                        painelpermanecelogado_text_center = Align.center(painelpermanecelogado_text)
                        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                        print(' ')
                        c.print(painelpermanecelogado_text_center) 
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()
                        break
                    
                    else:
                        Utils.mensagem_erro_centralizada('Digite "s" ou "n".')
                        Utils.aguardar_volta()

            elif opcao == '9':
                Utils.spinner_centralizado("Carregando...", tempo = 2)
                quiz = Quiz()
                quiz.exibir_menu(self.cadastro.usuarios, self.cadastro.usuario_logado)
                    
            elif opcao == '10':
                Utils.spinner_centralizado("Carregando...", tempo = 2)
                deletou = self.cadastro.deletar_usuario()
                if deletou:
                    usuario_logado = None
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal()
                    return
            else:
                Utils.mensagem_erro_centralizada("Opção inválida! Digite um número de 1 a 8.")
                Utils.aguardar_volta()
                Utils.limpar_tela_universal()