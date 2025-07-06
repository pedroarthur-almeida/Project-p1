import time
from utils import Utils
from prompt_toolkit import prompt
from rich.align import Align
from rich.panel import Panel
from rich.text import Text
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from manage_json import GerenciarJson
from user import Usuario
c = Console()

class Cadastro:
    def __init__(self):
        self.gerenciador = GerenciarJson()
        self.usuarios = self.gerenciador.carregar_dadosjson()
        
    def cadastro_de_usuario(self,usuarios): 
        """Cadastra o usuário e salva seus dados em um dicionário,
        em que a chave é o email.
        """
        Utils.limpar_tela_universal() 
        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
        print(' ')
        cadastro_texto_boas_vindas = Text()
        cadastro_texto_boas_vindas.append('\n')
        cadastro_texto_boas_vindas.append("✨ Crie sua conta no VitalTrack!\n", style="bold yellow")
        cadastro_texto_boas_vindas.append("Preencha os dados abaixo para começar sua jornada conosco.", style="dim")
        cadastro_texto_boas_vindas.append('\n')

        cadastro_panel = Panel(cadastro_texto_boas_vindas,title="[bold blue]Cadastro de Usuário[/bold blue]",border_style="bold blue",expand=False)
        c.print(Align.center(cadastro_panel))

        while True:
            c.print(Panel('📧 [bold yellow]Digite o seu email:[/bold yellow] ', expand = False, border_style = 'yellow'))
            email = input('>>> ').strip().lower()

            if email in self.usuarios:
                erroremail_text = Text()
                erroremail_text.append('Este email já foi cadastrado!')
                erroremail_text.append('\nInsira um email ainda não cadastrado.')
                perroremail = Panel(erroremail_text, border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center")
                c.print(perroremail)
                Utils.aguardar_volta()
                continue 

            elif '@' not in email or '.com' not in email:
                erroremail_text2 = Text()
                erroremail_text2.append('O email precisa estar em um formato válido.')
                erroremail_text2.append('\nO email precisa ter ".com" e "@".')
                perroremail2 = Panel(erroremail_text2, border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center")
                c.print(perroremail2)
                Utils.aguardar_volta()
                continue 

            dominios_validos = ['gmail.com', 'outlook.com', 'hotmail.com', 'yahoo.com', 'icloud.com'] #criando essa lista pra salvar os dominios validos.
            
            if not any(email.endswith(dominio) for dominio in dominios_validos): #o comando endswith vai verficiar se o email termina com o domínio de forma correta, para evitar falsos positivos e emails no formato errado, ex: arthur@xcsgmail.com
                erroremail_text3 = Text()
                erroremail_text3.append('Domínio inválido! Use: Gmail, Outlook, Hotmail, Yahoo ou iCloud.')
                perroremail3 = Panel(erroremail_text3, border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center")
                c.print(perroremail3)
                Utils.aguardar_volta()
                continue
            break
        
        while True:
            c.print(Panel('🔑 [bold yellow]Digite sua senha(mínimo 6 caracteres):[/bold yellow] ', expand = False, border_style = 'yellow'))
            senha = prompt('>>> ', is_password = True)

            if len(senha) < 6:
                errorsenha_text = Text()
                errorsenha_text.append('Senha muito curta, a sua senha precisa ter, no mínimo, 6 caracteres.')
                perrorsenha = Panel(errorsenha_text, border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center")
                c.print(perrorsenha)
                Utils.aguardar_volta()
                continue 
                
            c.print(Panel('[bold yellow]Confirme sua senha:[/bold yellow] ', expand = False, border_style = 'yellow'))
            confirmaçao_de_senha = prompt('>>> ', is_password = True)

            if senha != confirmaçao_de_senha:
                errorsenha_text2 = Text()
                errorsenha_text2.append('As senhas não coinscidem.')
                perrorsenha2 = Panel(errorsenha_text2, border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center")
                c.print(perrorsenha2)
                Utils.aguardar_volta()
                continue 
            else:
                break
        
        c.print(Panel('[bold yellow]Digite seu nome: (Será seu nome de usuário)[/bold yellow]', expand = False, border_style = 'yellow'))
        nome = input('>>> ').strip()
        with c.status("[red]G[/red][magenta]u[/magenta][yellow]a[/yellow][green]r[/green]"
            "[cyan]d[/cyan][blue]a[/blue][red]n[/red][magenta]d[/magenta][yellow]o[/yellow] "
            "[green]o[/green][cyan]s[/cyan] "
            "[blue]d[/blue][red]a[/red][magenta]d[/magenta][yellow]o[/yellow][green]s[/green]", spinner = 'hearts'):  
            time.sleep(2)
        
        novo_usuario = Usuario(
            email=email,
            senha=senha,
            nome=nome,
            objetivo=None,
            dados=None,
            calorias_hoje=0,
            historico_dias={}
        )
        self.usuarios[email] = novo_usuario 

        c.rule('[i][blue]VitalTrack[/][/i]')
        print(' ')
        c.print(Panel('Agora vamos definir o [green][u]seu[/u][/] objetivo! 👇', expand = False, border_style = 'cyan'))
        self.escolher_objetivo(email, usuarios)
        self.gerenciador.salvar_dadosjson(self.usuarios)
        return email
        
    def escolher_objetivo(self,email_do_usuario, dicionario_usuarios):
        """
        Escolha de objetivo (parte do cadastro),
        Usuário escolhe seu objetivo e fornece seus dados,
        armazena os dados do usuário em um outro dicionário "dados".
        """
        Utils.limpar_tela_universal()

        while True:
            c.rule('[i][blue]VitalTrack[/][/i]')
            print(' ')
            textoescolhaobj_text = Text()
            textoescolhaobj_text.append('\n')
            textoescolhaobj_text.append('Qual é o seu objetivo? 🤔')
            textoescolhaobj_text.append('\n')

            textoescolhaobj_text.append('\nAntes de começarmos, é importante entender qual é o seu foco atual em relação à sua saúde. ✍\n')
            textoescolhaobj_text.append('É como uma parceria, entendeu? 👊🤝')
            textoescolhaobj_text.append('\n')
            textoescolhaobj_text.append('\nVocê pode escolher entre três caminhos:\n')
            textoescolhaobj_text.append('\n')

            textoescolhaobj_text.append('1. ', style = 'red')
            textoescolhaobj_text.append('Ganho de massa (Foco em ganho de peso e aumento da massa muscular.🏋️ 💪)\n')

            textoescolhaobj_text.append('2. ', style = 'red')
            textoescolhaobj_text.append('Perda de peso (ideal para quem deseja reduzir o percentual de gordura corporal de forma saudável.)🏃\n')

            textoescolhaobj_text.append('3. ', style = 'red')
            textoescolhaobj_text.append('Manutenção da saúde (Para quem quer manter o equilíbrio, hábitos saudáveis e o bem-estar geral.)❤\n')

            painelescolhadeobj = Panel(textoescolhaobj_text, border_style="cyan", expand = False,title="[bold cyan]Escolha de objetivo[/bold cyan]",
                title_align="center")
            painelescolhadeobj_centralizado = Align.center(painelescolhadeobj)
            c.print(painelescolhadeobj_centralizado)

            entradaescolhaobj = Text()
            entradaescolhaobj.append('Digite sua opção: ', style = 'bold yellow')

            pentradaescolhaobj= Panel(entradaescolhaobj, expand = False, border_style = 'bold yellow')
            pentradaescolhaobj_center = Align.center(pentradaescolhaobj)
            c.print(pentradaescolhaobj_center)

            objetivo = input('>>> ').strip()

            if objetivo not in ['1', '2', '3']:
                errorescolhaobj_text = Text()
                errorescolhaobj_text.append('Opção inválida! Escolha 1, 2 ou 3.')
                perrorescolhaobjt = Panel(errorescolhaobj_text, border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center")
                c.print(perrorescolhaobjt)
                Utils.aguardar_volta()
                continue 

            objetivos = {
                '1': 'GANHO DE MASSA',
                '2': 'PERDA DE PESO', 
                '3': 'MANUTENÇÃO DA SAÚDE' }
            with c.status("[red]S[/red][magenta]a[/magenta][yellow]l[/yellow]"
                "[green]v[/green][cyan]a[/cyan][blue]n[/blue]"
                "[red]d[/red][magenta]o[/magenta]", spinner = 'hearts'):  
                time.sleep(2)
            c.rule('[b][i][blue]VitalTrack[/][/i][/b]')
            print(' ')
            escolhaobj2_text = Text()
            escolhaobj2_text.append(f'Você escolheu: {objetivos[objetivo]}')
            pescolhaobj2_text = Panel(escolhaobj2_text, border_style = 'cyan', expand = False)
            pescolhaobj2_center = Align.center(pescolhaobj2_text)
            c.print(pescolhaobj2_center)
            
            if objetivo == '1':
                textoescolhaobj_text2 = Text()
                textoescolhaobj_text2.append('Boa! Você deseja aumentar sua massa corporal, tô contigo nessa! 😎 💪')
                textoescolhaobj_text2.append('\nUma dica: é importante que você consuma uma quantidade de calorias maior que a sua TMB.')
                textoescolhaobj_text2.append('\nNão sabe o que é TMB? não se preocupe! mais na frente eu te explico. 😉')
                textoescolha2 = Panel(textoescolhaobj_text2, border_style="cyan", expand = False,title="[bold cyan]Feedback[/bold cyan]",
                    title_align="center")
                textoescolha2_center = Align.center(textoescolha2)
                c.print(textoescolha2_center)

            elif objetivo == '2':
                textoescolhaobj_text3 = Text()
                textoescolhaobj_text3.append('Você escolheu perder peso, que legal! Tamo junto nessa jornada. 👊')
                textoescolhaobj_text3.append('\nCom foco e disciplina, qualquer objetivo pode se concretizar, vai dar tudo certo!')
                textoescolhaobj_text3.append('\nDica: é importante que você consuma uma quantidade de calorias inferior a sua TMB.')
                textoescolhaobj_text3.append('\nNão sabe o que é TMB? não se preocupe! mais na frente eu te explico. 😉')
                textoescolha3 = Panel(textoescolhaobj_text3, border_style="cyan", expand = False,title="[bold cyan]Feedback[/bold cyan]",
                    title_align="center")
                textoescolha3_center = Align.center(textoescolha3)
                c.print(textoescolha3_center)
                
            else:
                textoescolhaobj_text4 = Text()
                textoescolhaobj_text4.append('É isso ai! Você optou por manter-se saudável, conte comigo pra te auxiliar! ✋')
                textoescolhaobj_text4.append('\nÉ extremamente importante acompanhar a própria saúde, isso vale para pessoas de qualquer faixa etária. 🧒👨👴')
                textoescolhaobj_text4.append('\nDica: mantenha seu consumo de calorias em um valor próximo a sua TMB.')
                textoescolhaobj_text4.append('\nNão sabe o que é TMB? não se preocupe! mais na frente eu te explico. 😉')
                textoescolha4 = Panel(textoescolhaobj_text4, border_style="cyan", expand = False,title="[bold cyan]Feedback[/bold cyan]",
                    title_align="center")
                textoescolha4_center = Align.center(textoescolha4)
                c.print(textoescolha4_center)
            Utils.aguardar_volta()
            
            c.rule('[b][i][blue]VitalTrack[/][/i][/b]')
            print(' ')
            contescolhaobj_text = Text()
            contescolhaobj_text.append('Beleza! Agora vamos coletar algumas informações sobre você.')
            pcontescolhaobj = Panel(contescolhaobj_text, border_style = 'cyan', expand = False)
            pcontescolhaobj_center = Align.center(pcontescolhaobj)
            c.print(pcontescolhaobj_center)

            try:
                while True:
                    try:
                        contescolhaobj2_text = Text()
                        contescolhaobj2_text.append('Para que os cálculos de saúde e metabolismo sejam mais precisos, gostaríamos de saber sua identidade de gênero.')
                        contescolhaobj2_text.append('Essa informação nos ajuda a oferecer resultados mais adequados para você.')
                        pcontescolhaobj2 = Panel(contescolhaobj2_text, border_style = 'cyan', expand = False)
                        pcontescolhaobj2_center = Align.center(pcontescolhaobj2)
                        c.print(pcontescolhaobj2_center)
                        
                        textoidentidade_text = Text()
                        textoidentidade_text.append('\n')
                        textoidentidade_text.append('Qual é a sua identidade de gênero?\n')
                        textoidentidade_text.append('\n')

                        textoidentidade_text.append('1. ', style = 'red')
                        textoidentidade_text.append('Homem Cis ')

                        textoidentidade_text.append('2. ', style = 'red')
                        textoidentidade_text.append('Mulher Cis ')

                        textoidentidade_text.append('3. ', style = 'red')
                        textoidentidade_text.append('Homem Trans ')

                        textoidentidade_text.append('4. ', style = 'red')
                        textoidentidade_text.append('Mulher Trans ')

                        painelidentidade = Panel(textoidentidade_text, border_style="cyan", expand = False,title="[bold cyan]Sua identidade[/bold cyan]",title_align="center")
                        painelidentidade_center = Align.center(painelidentidade)
                        c.print(painelidentidade_center)

                        opcaoidentidade_text = Text()
                        opcaoidentidade_text.append('Digite sua opção: ', style = 'bold yellow')
                        popcaoidentidade = Panel(opcaoidentidade_text, expand = False, border_style = 'bold yellow')
                        popcaoidentidade_center = Align.center(popcaoidentidade)
                        c.print(popcaoidentidade_center)
                        
                        sexo_escolha = input('>>> ').strip()

                        if sexo_escolha not in ['1','2','3','4']:
                            erroridentidade_text = Text()
                            erroridentidade_text.append('Escolha uma opção disponível (1-4).')
                            perroridentidade = Panel(erroridentidade_text, border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center")
                            c.print(perroridentidade)
                            Utils.aguardar_volta()
                            continue

                        sexo = ''
                        sexo_biologico = ''
                        tempo_transicao = None
                        em_transicao = False

                        if sexo_escolha == '1':
                            sexo = 'm'
                            sexo_biologico = 'm'
                            
                        elif sexo_escolha == '2':
                            sexo = 'f'
                            sexo_biologico = 'f'
                            
                        elif sexo_escolha in ['3', '4']:
                            while True:
                                c.rule('[b][i][blue]VitalTrack[/][/i][/b]')
                                print(' ')
                                textoterapiahormonal = Text()
                                textoterapiahormonal.append('\n')
                                textoterapiahormonal.append('Para adaptar melhor os cálculos às mudanças metabólicas:')
                                textoterapiahormonal.append('\n')
                                ptextoterapiahormonal = Panel(textoterapiahormonal, border_style="cyan", expand = False,title="[bold cyan]Sua identidade[/bold cyan]",title_align="center")
                                ptextoterapiahormonal_center = Align.center(ptextoterapiahormonal)
                                c.print(ptextoterapiahormonal_center)

                                perguntaterapia_text = Text()
                                perguntaterapia_text.append('Você já fez uso de terapia hormonal? (s/n):', style = 'bold yellow')
                                painelperguntaterapia_text = Panel(perguntaterapia_text, expand = False, border_style = 'bold yellow')
                                painelperguntaterapia_text_center = Align.center(painelperguntaterapia_text)
                                c.print(painelperguntaterapia_text_center)
                                
                                resposta = input('>>> ').lower().strip()

                                if resposta not in ['s','n']:
                                    errorterapiahormonal_text = Text()
                                    errorterapiahormonal_text.append('Digite (s) ou (n).')
                                    perrorterapiahormonal = Panel(errorterapiahormonal_text, border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center")
                                    c.print(perrorterapiahormonal)
                                    Utils.aguardar_volta()
                                    continue 
                                em_transicao = resposta == 's'
                                break
                            
                            if em_transicao:
                                while True:
                                    try:
                                        c.print(Panel('[bold yellow]Há quanto tempo (em meses) você faz uso de hormônios?[bold yellow]', expand = False, border_style = 'bold yellow'))
                                        tempo_transicao = int(input('>>> '))
                                        
                                        if tempo_transicao <= 0:
                                            c.print(Panel('Digite um valor válido.', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                                            Utils.aguardar_volta()
                                            continue
                                        break
                                    except ValueError:
                                        c.print(Panel('Digite somente números.', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                                        Utils.aguardar_volta()
                                        continue

                    except ValueError:
                        c.print(Panel('Valores inválidos! Digite números válidos.', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))        
                    with c.status("[red]O[/red][magenta]r[/magenta][yellow]g[/yellow][green]a[/green]"
                                "[cyan]n[/cyan][blue]i[/blue][red]z[/red][magenta]a[/magenta][yellow]n[/yellow]"
                                "[green]d[/green][cyan]o[/cyan] "
                                "[blue]s[/blue][red]u[/red][magenta]a[/magenta][yellow]s[/yellow] "
                                "[green]i[/green][cyan]n[/cyan][blue]f[/blue][red]o[/red][magenta]r[/magenta]"
                                "[yellow]m[/yellow][green]a[/green][cyan]ç[/cyan][blue]õ[/blue][red]e[/red][magenta]s[/magenta]", spinner = 'hearts'):  
                                time.sleep(2)
                    while True:
                        try:
                            
                            c.rule('[b][i][blue]VitalTrack[/][/i][/b]')
                            print(' ')
                            maisdados_text = Text()
                            maisdados_text.append('Preciso de mais alguns de seus dados.', style = 'cyan')
                            pmaisdados = Panel(maisdados_text, expand = False, border_style = 'cyan')
                            pmaisdados_center = Align.center(pmaisdados)
                            c.print(pmaisdados_center)
                            
                            c.print(Panel('[bold yellow]Digite sua idade:[/bold yellow] ', expand = False, border_style = 'bold yellow'))
                            idade = int(input('>>> ').strip())
                            c.print(Panel('[bold yellow]Digite o seu peso em quilogramas:[/bold yellow] ', expand = False, border_style = 'bold yellow'))
                            peso = float(input('>>> ').strip())
                            c.print(Panel('[bold yellow]Digite sua altura em metros:[/bold yellow] ', expand = False, border_style = 'bold yellow'))
                            altura = float(input('>>> ').strip())
                            with c.status("[red]V[/red][magenta]a[/magenta][yellow]l[/yellow][green]i[/green]"
                                "[cyan]d[/cyan][blue]a[/blue][red]n[/red][magenta]d[/magenta][yellow]o[/yellow] "
                                "[green]s[/green][cyan]e[/cyan][blue]u[/blue][red]s[/red] "
                                "[magenta]d[/magenta][yellow]a[/yellow][green]d[/green][cyan]o[/cyan][blue]s[/blue]", spinner = 'hearts'):  
                                time.sleep(2)
                            print(' ')
                            c.print(Panel('[green]Usuário cadastrado com sucesso![/]', expand = False, border_style = 'green'))
                            print(' ')
                            with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
                                "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner = 'hearts'):  
                                time.sleep(2)

                            if idade <= 0 or peso <= 0 or altura <= 0:
                                c.print(Panel('Valores inválidos! Digite números positivos.', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                                Utils.aguardar_volta()
                                continue
                            if idade > 100 or peso > 350 or altura > 2.5:
                                c.print(Panel('Valores fora do intervalo estimado.', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                                Utils.aguardar_volta()
                                continue

                            dados = {
                                'idade': idade,
                                'peso': peso,
                                'altura': altura,
                                'sexo': sexo,
                                'sexo_biologico': sexo_biologico if sexo_escolha in ['3', '4'] else None,
                                'em_transicao': em_transicao if sexo_escolha in ['3', '4'] else None,
                                'tempo_transicao': tempo_transicao if (sexo_escolha in ['3', '4'] and em_transicao) else None,
                                'sexo_escolha': sexo_escolha
                            }
                            
                            self.usuarios[email_do_usuario]['dados'] = dados
                            self.usuarios[email_do_usuario]['objetivo'] = objetivo
                            time.sleep(0.05)
                            return True
                            
                        except ValueError:
                            c.print(Panel('Valores inválidos! Digite dados válidos para cada solicitação.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                            Utils.aguardar_volta()
                            continue

            except ValueError:
                c.print(Panel('Valores inválidos! Digite números válidos.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                Utils.aguardar_volta()

    def fazer_login(self): 
        """
        Função responsável pelo login do usuário.
        O usuário digita seu email e sua senha.
        Caso estejam corretos, libera o acesso ao menu logado.
        """
        Utils.limpar_tela_universal()
        c.rule('[i][blue]VitalTrack[/][/i]')
        print(' ')
        
        login_texto_boas_vindas = Text()
        login_texto_boas_vindas.append('\n')
        login_texto_boas_vindas.append("🔒 Seja bem-vindo(a) à etapa de login do VitalTrack!\n", style="bold yellow")
        login_texto_boas_vindas.append("Por favor, insira seus dados de acesso abaixo.", style="dim")
        login_texto_boas_vindas.append('\n')

        login_panel = Panel(login_texto_boas_vindas, title="[bold blue]Acesso ao Sistema[/bold blue]",border_style="blue",expand=False)
        c.print(Align.center(login_panel))

        while True:
            painel_email = Panel('📧 [bold yellow]Email cadastrado:[/bold yellow]', border_style='yellow', expand=False)
            c.print(painel_email)
            email = input('>>> ').lower().strip()

            if email not in self.usuarios:
                painel_erro_email = Panel('❌ Email não cadastrado.',border_style='red',expand=False,title='[bold red]ERRO[/bold red]',title_align='center')
                c.print(painel_erro_email)
                Utils.aguardar_volta()
                continue
            break

        while True:
            painel_senha = Panel(
                '🔑 [bold yellow]Senha:[/bold yellow]',border_style='yellow',expand=False)
            c.print(painel_senha)
            senha = prompt('>>> ', is_password=True).strip()

            usuario = self.usuarios[email]
            if usuario.senha != senha:
                painel_erro_senha = Panel('❌ Senha incorreta.',border_style='red',expand=False,title='[bold red]ERRO[/bold red]',title_align='center')
                c.print(painel_erro_senha)
                Utils.aguardar_volta()
                continue

            with Progress(
                SpinnerColumn(spinner_name='bouncingBall'),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
            ) as progress:
                progress.add_task(description="[bold magenta]Validando credenciais...[/bold magenta]", total=None)
                time.sleep(2)

            print('\n')

            painel_sucesso = Panel(
                f'✅ Acesso liberado, [bold blue]{usuario.nome}[/bold blue]!\n\n🚀 [green]Você está pronto para usar o VitalTrack![/green]',border_style='bold blue',expand=False, style = 'bold white')
            painel_sucesso_center = Align.center(painel_sucesso)
            c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
            print(' ')
            c.print(painel_sucesso_center)

            return email

    def atualizar_usuario(self,usuarios, usuario_logado): 
        """
        Atualiza os dados do usuário,
        o usuário escolhe o que deseja atualizar,
        é permitido atualizar email, nome ou senha,
        os novos dados são salvos após mudanças.
        """
        Utils.limpar_tela_universal()
        if usuario_logado is None: 
            c.print(Panel('Faça login primeiro!',expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
            return
        
        while True:
            c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
            print(' ')
            atualizarperfil_text = Text()
            atualizarperfil_text.append('\n')
            atualizarperfil_text.append('👤 Atualizar perfil', style = 'bold blue')
            atualizarperfil_text.append('\n')

            atualizarperfil_text.append('\n1. ', style = 'red')
            atualizarperfil_text.append(f'Alterar nome. (nome atual:{usuarios[usuario_logado].nome})',style = 'bold white')

            atualizarperfil_text.append('\n2. ', style = 'red')
            atualizarperfil_text.append('Alterar senha.',style = 'bold white')

            atualizarperfil_text.append('\n3. ', style = 'red')
            atualizarperfil_text.append(f'Alterar email. (email atual:{usuario_logado})',style = 'bold white')

            atualizarperfil_text.append('\n4. ', style = 'red')
            atualizarperfil_text.append('Voltar',style = 'bold white')
            atualizarperfil_text.append('\n')

            patualizarperfil = Panel(atualizarperfil_text, expand = False, border_style = 'bold blue', title = '🔹')
            patualizarperfil_center  = Align.center(patualizarperfil)
            c.print(patualizarperfil_center)

            opcaoatualizarperfil_text = Text()
            opcaoatualizarperfil_text.append('O que deseja atualizar? (1-4):',style = 'bold yellow')
            popcaoatualizarperfil_text = Panel(opcaoatualizarperfil_text, expand = False, border_style = 'bold yellow')
            popcaoatualizarperfil_text_center = Align.center(popcaoatualizarperfil_text)
            c.print(popcaoatualizarperfil_text_center)
            opçao3 = input('>>> ').strip()

            usuario = self.usuarios[usuario_logado] 

            if opçao3 == '1':
                c.print(Panel(f'[bold yellow]Digite o novo nome (atual: {usuarios[usuario_logado].nome}):[/bold yellow]',expand = False, border_style = 'bold yellow'))
                novo_nome = input('>>> ').strip()
                if novo_nome:
                    usuario.nome = novo_nome
                    self.gerenciador.salvar_dadosjson(self.usuarios)
                    mudancanome_text = Text()
                    mudancanome_text.append('Nome atualizado com sucesso!',style = 'bold white')
                    pmudancanome_text = Panel(mudancanome_text, expand = False, border_style = 'bold blue')
                    pmudancanome_text_center = Align.center(pmudancanome_text)
                    c.print(pmudancanome_text_center)
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal()

            elif opçao3 == '2':
                c.print(Panel('[bold yellow]Digite uma nova senha (mínimo 6 caracteres):[/bold yellow]', expand = False, border_style = 'bold yellow'))
                nova_senha = input('>>> ')
                if len(nova_senha) >=6:
                    usuario.senha = nova_senha
                    self.gerenciador.salvar_dadosjson(self.usuarios)
                    mudancasenha_text = Text()
                    mudancasenha_text.append('Senha atualizada com sucesso!',style = 'bold white')
                    pmudancasenha_text = Panel(mudancasenha_text, expand = False, border_style = 'bold blue')
                    pmudancasenha_text_center = Align.center(pmudancasenha_text)
                    c.print(pmudancasenha_text_center)
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal()

                else:
                    c.print(Panel('Senha muito curta.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal() 

            elif opçao3 == '3':
                c.print(Panel(f'[bold yellow]Digite seu novo email (atual: {usuario_logado}):[/bold yellow]', expand = False, border_style = 'bold yellow'))
                novo_email = input('>>> ').strip().lower()  
                if not novo_email:
                    continue

                if novo_email == usuario_logado:
                    c.print(Panel('O novo email é igual ao atual.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal()   

                elif '@' not in novo_email or '.com' not in novo_email:
                    c.print(Panel("Formato inválido (use '@' e '.com').", expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal()

                elif novo_email in usuarios:
                    c.print(Panel('Email já cadastrado.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center')) 
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal()

                else:
                    
                    usuario.email = novo_email
                    usuarios[novo_email] = usuario
                    del self.usuarios[usuario_logado]
                    usuario_logado = novo_email
                    self.gerenciador.salvar_dadosjson(self.usuarios)
                    mudancaemail_text = Text()
                    mudancaemail_text.append('Email atualizado com sucesso!', style = 'bold white')
                    pmudancaemail_text = Panel(mudancaemail_text, expand = False, border_style = 'bold blue')
                    pmudancaemail_text_center = Align.center(pmudancaemail_text)
                    c.print(pmudancaemail_text_center)
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal() 

            elif opçao3 == '4':
                with c.status("[red]G[/red][magenta]u[/magenta][yellow]a[/yellow][green]r[/green]"
                    "[cyan]d[/cyan][blue]a[/blue][red]n[/red][magenta]d[/magenta][yellow]o[/yellow] "
                    "[green]o[/green][cyan]s[/cyan] "
                    "[blue]d[/blue][red]a[/red][magenta]d[/magenta][yellow]o[/yellow][green]s[/green]", spinner = 'hearts'):  
                    time.sleep(2)
                    Utils.limpar_tela_universal()
                break

            else:
                c.print(Panel('Opção inválida. Digite uma opção disponível (1-4)', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                Utils.aguardar_volta()
                Utils.limpar_tela_universal()
        return usuarios, usuario_logado

    def atualizar_dados(self, usuario_logado):
        """
        Atualiza os dados físicos do usuário,
        usuário decide o que deseja atualizar.
        """
        Utils.limpar_tela_universal()

        if usuario_logado is None:
            c.print(Panel('Faça login primeiro!', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
            Utils.aguardar_volta()
            return self.usuarios, usuario_logado
        
        user = self.usuarios[usuario_logado]
        
        if not user.dados:
            c.print(Panel('Complete seus dados primeiro!', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
            self.escolher_objetivo()
            return self.usuarios, usuario_logado
        
        objetivos = {
                '1': 'GANHO DE MASSA',
                '2': 'PERDA DE PESO', 
                '3': 'MANUTENÇÃO DA SAÚDE' }
        
        while True:

            try:
                dados = user.dados
                objetivo_atual = user.objetivo
                c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                print(' ')
                atualizarusuario_text = Text()
                atualizarusuario_text.append('\n')
                atualizarusuario_text.append('Atualizar dados pessoais', style = 'bold blue')
                atualizarusuario_text.append('\n')

                atualizarusuario_text.append('\n1. ', style = 'red')
                atualizarusuario_text.append(f'Idade: {dados["idade"]} anos', style = 'bold white')

                atualizarusuario_text.append('\n2. ', style = 'red')
                atualizarusuario_text.append(f'Peso: {dados["peso"]} kg', style = 'bold white')

                atualizarusuario_text.append('\n3. ', style = 'red')
                atualizarusuario_text.append(f'Altura: {dados["altura"]} m', style = 'bold white')

                atualizarusuario_text.append('\n4. ', style = 'red')
                atualizarusuario_text.append(f'Objetivo: {objetivos[objetivo_atual]}', style = 'bold white')

                atualizarusuario_text.append('\n5. ', style = 'red')
                atualizarusuario_text.append('Voltar', style = 'bold white')

                patualizarusuario = Panel(atualizarusuario_text, expand = False, border_style = 'cyan', title = '🔹', title_align = 'center')
                patualizarusuario_center = Align.center(patualizarusuario)
                c.print(patualizarusuario_center)
                
                opcaoatualizardados_text = Text()
                opcaoatualizardados_text.append('Qual dado deseja alterar? (1-5):', style = 'bold yellow')
                popcaoatualizardados_text = Panel(opcaoatualizardados_text, expand = False, border_style = 'bold yellow')
                popcaoatualizardados_text_center = Align.center(popcaoatualizardados_text)
                c.print(popcaoatualizardados_text_center)
                campo = input('>>> ').strip()
                
                if campo == '1':
                    c.print(Panel('[bold yellow]Nova idade:[/bold yellow]', expand = False, border_style = 'yellow'))
                    nova_idade = int(input('>>> '))
                    if 0 < nova_idade <= 100:
                        dados['idade'] = nova_idade
                        self.gerenciador.salvar_dadosjson({email: u.to_dict() for email, u in self.usuarios.items()})
                        mudancaidada_text = Text()
                        mudancaidada_text.append('Idade atualizada com sucesso!', style = 'bold white')
                        pmudancaidade_text = Panel(mudancaidada_text, expand = False, border_style = 'bold blue')
                        pmudancaidade_text_center = Align.center(pmudancaidade_text)
                        c.print(pmudancaidade_text_center)
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()

                    else:
                        c.print(Panel('Idade deve ser entre 1 e 100 anos', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()
                    
                elif campo == '2':
                    c.print(Panel('[bold yellow]Novo peso, em quilogramas:[/bold yellow]', expand = False, border_style = 'yellow'))
                    novo_peso = float(input('>>> '))
                    if 0 < novo_peso <= 350:
                        dados['peso'] = novo_peso
                        self.gerenciador.salvar_dadosjson({email: u.to_dict() for email, u in self.usuarios.items()})
                        mudancapeso_text = Text()
                        mudancapeso_text.append('Peso atualizado com sucesso!',style = 'bold white')
                        pmudancapeso_text = Panel(mudancapeso_text, expand = False, border_style = 'bold blue')
                        pmudancapeso_text_center = Align.center(pmudancapeso_text)
                        c.print(pmudancapeso_text_center)
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()

                    else:
                        c.print(Panel('Peso deve ser entre 0.1 e 350 kg', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()
                    
                elif campo == '3':
                    c.print(Panel('[bold yellow]Nova altura, em metros:[/bold yellow]', expand = False, border_style = 'yellow'))
                    nova_altura = float(input('>>> '))
                    if 0 < nova_altura <= 2.5:
                        dados['altura'] = nova_altura
                        self.gerenciador.salvar_dadosjson({email: u.to_dict() for email, u in self.usuarios.items()})
                        mudancaaltura_text = Text()
                        mudancaaltura_text.append('Altura atualizada com sucesso!', style = 'bold white')
                        pmudancaaltura_text = Panel(mudancaaltura_text, expand = False, border_style = 'bold blue')
                        pmudancaaltura_text_center = Align.center(pmudancaaltura_text)
                        c.print(pmudancaaltura_text_center)
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()

                    else:
                        c.print(Panel('Altura deve ser entre 0.1 e 2.5 metros', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()
                    
                elif campo == '4':
                    mudandoobj_text = Text()
                    mudandoobj_text.append('\n')
                    mudandoobj_text.append('Objetivos disponíveis:')
                    mudandoobj_text.append('\n')

                    mudandoobj_text.append('\n1. ', style = 'red')
                    mudandoobj_text.append('Ganho de massa',style = 'bold white')

                    mudandoobj_text.append('\n2. ', style = 'red')
                    mudandoobj_text.append('Perda de peso',style = 'bold white')

                    mudandoobj_text.append('\n3. ', style = 'red')
                    mudandoobj_text.append('Manutenção da saúde',style = 'bold white')

                    pmudandoobjt = Panel(mudandoobj_text, expand = False, border_style = 'bold blue', title = 'Novo objetivo', title_align = 'center')
                    pmudandoobjt_center = Align.center(pmudandoobjt)
                    c.print(pmudandoobjt_center)
                    
                    novaescolhaobj_text = Text()
                    novaescolhaobj_text.append('Novo objetivo (1-3):',style = 'bold yellow')
                    pnovaescolhaobj_text = Panel(novaescolhaobj_text, expand = False, border_style = 'bold yellow')
                    pnovaescolhaobj_text_center = Align.center(pnovaescolhaobj_text)
                    c.print(pnovaescolhaobj_text_center)
                    novo_objetivo = input('>>> ').strip()
                    if novo_objetivo in ['1', '2', '3']:
                        user.objetivo = novo_objetivo
                        self.gerenciador.salvar_dadosjson({email: u.to_dict() for email, u in self.usuarios.items()})
                        escolhanovoobj_text = Text()
                        escolhanovoobj_text.append(f'Objetivo atualizado para: {objetivos[novo_objetivo]}', style = 'bold white')
                        pescolhanovoobj_text = Panel(escolhanovoobj_text, expand = False, border_style = 'bold blue')
                        pescolhanovoobj_text_center = Align.center(pescolhanovoobj_text)
                        c.print(pescolhanovoobj_text_center)
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()

                    else:
                        c.print(Panel('Opção inválida!', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal()
                    
                elif campo == '5':
                    with c.status("[red]S[/red][magenta]a[/magenta][yellow]i[/yellow]"
                        "[green]n[/green][cyan]d[/cyan][blue]o[/blue]", spinner = 'hearts'):  
                        time.sleep(2)
                        Utils.limpar_tela_universal()
                    break
                    
                else:
                    c.print(Panel('Opção inválida! digite uma opção disponível.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal()
                    
            except ValueError:
                c.print(Panel('Valor inválido! Digite números válidos.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                Utils.aguardar_volta()
                Utils.limpar_tela_universal()
        return self.usuarios, usuario_logado

    def deletar_usuario(self,usuario_logado, usuarios):
        """
        Deleta o usuário cadastrado,
        apaga todos os dados inseridos e salvos.
        """

        if usuario_logado is None:
            c.print(Panel('Faça login primeiro.', expand = False, border_style = 'ERRO', title = 'ERRO', title_align = 'center'))
            return
        
        while True:

            c.print(Panel('Tem certeza que deseja deletar sua conta? 😕 (s/n):', expand = False, border_style = 'bold yellow',style = 'bold yellow'))
            confirmaçao = input('>>> ').lower()

            if confirmaçao == 's':
                del usuarios[usuario_logado]
                self.gerenciador.salvar_dadosjson(self.usuarios)
                usuario_logado = None
                contadeletada_text = Text()
                contadeletada_text.append('Conta deletada com sucesso. Até logo...', style = 'bold white')
                pcontadeletadaa_text = Panel(contadeletada_text, expand = False, border_style = 'bold blue')
                pcontadeletadaa_text_center = Align.center(pcontadeletadaa_text)
                c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                print(' ')
                c.print(pcontadeletadaa_text_center)
                return usuarios, usuario_logado
            
            elif confirmaçao == 'n':
                naodeletada_text = Text()
                naodeletada_text.append('Que bom! Creio que ainda podemos te auxiliar em muitas coisas. 😉✨', style = 'bold white')
                pnaodeletada_text = Panel(naodeletada_text, expand = False, border_style = 'bold blue')
                pnaodeletada_text_center = Align.center(pnaodeletada_text)
                c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                print(' ')
                c.print(pnaodeletada_text_center)
                Utils.aguardar_volta()
                Utils.limpar_tela_universal()
                return usuarios, usuario_logado

            else:
                c.print(Panel('Digite "s" ou "n".', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                Utils.aguardar_volta()
                Utils.limpar_tela_universal()
            return usuarios, usuario_logado
