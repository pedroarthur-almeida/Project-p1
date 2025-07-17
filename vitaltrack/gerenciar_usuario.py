import time
from utils import Utils
from rich.align import Align
from rich.panel import Panel
from rich.text import Text
from rich.console import Console
from gerenciar_json import GerenciarJson
from usuario import Usuario
c = Console()

class GerenciarUsuario:
    def __init__(self):
        self.gerenciador = GerenciarJson()
        self.usuarios = self.gerenciador.carregar_dadosjson()
        self.usuario_logado = None
        
    def cadastro_de_usuario(self): 
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
            c.print(Utils.mensagem_centralizada("📧 Digite o seu email:"))
            email = Utils.entrada_centralizada('💬 : ').strip().lower()

            if email in self.usuarios:
                Utils.mensagem_erro_centralizada("Este email já foi cadastrado!\nInsira um email ainda não cadastrado.")
                Utils.aguardar_volta()
                continue 

            elif '@' not in email or '.com' not in email:
                Utils.mensagem_erro_centralizada('O email precisa estar em um formato válido.\nO email precisa ter ".com" e "@".')
                Utils.aguardar_volta()
                continue 

            dominios_validos = ['gmail.com', 'outlook.com', 'hotmail.com', 'yahoo.com', 'icloud.com'] #criando essa lista pra salvar os dominios validos.
            
            if not any(email.endswith(dominio) for dominio in dominios_validos): #o comando endswith vai verficiar se o email termina com o domínio de forma correta, para evitar falsos positivos e emails no formato errado, ex: arthur@xcsgmail.com
                Utils.mensagem_erro_centralizada("Domínio inválido! Use: Gmail, Outlook, Hotmail, Yahoo ou iCloud.")
                Utils.aguardar_volta()
                continue
            break
        
        while True:
            c.print(Utils.mensagem_centralizada("🔑 Digite sua senha(mínimo 6 caracteres):"))
            senha = Utils.entrada_centralizada('💬 : ', is_password = True)

            if len(senha) < 6:
                Utils.mensagem_erro_centralizada("Senha muito curta, a sua senha precisa ter, no mínimo, 6 caracteres.")
                Utils.aguardar_volta()
                continue 
                
            c.print(Utils.mensagem_centralizada("Confirme sua senha:"))
            confirmaçao_de_senha = Utils.entrada_centralizada('💬 : ', is_password = True)

            if senha != confirmaçao_de_senha:
                Utils.mensagem_erro_centralizada("As senhas não coinscidem.")
                Utils.aguardar_volta()
                continue 
            else:
                break
        
        c.print(Utils.mensagem_centralizada("Digite seu nome: (Será seu nome de usuário):"))
        nome = Utils.entrada_centralizada('💬 : ').strip()
        Utils.spinner_centralizado("Guardando seus dados...", tempo = 2)
        
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
        self.escolher_objetivo(email)
        self.gerenciador.salvar_dadosjson(self.usuarios)
        return email
        
    def escolher_objetivo(self,email_do_usuario):
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

            painelescolhadeobj = Panel(textoescolhaobj_text, border_style="bold blue", expand = False,title="Escolha de objetivo",
                title_align="center")
            painelescolhadeobj_centralizado = Align.center(painelescolhadeobj)
            c.print(painelescolhadeobj_centralizado)

            entradaescolhaobj = Text()
            entradaescolhaobj.append('Digite sua opção: ', style = 'bold yellow')

            pentradaescolhaobj= Panel(entradaescolhaobj, expand = False, border_style = 'bold yellow')
            pentradaescolhaobj_center = Align.center(pentradaescolhaobj)
            c.print(pentradaescolhaobj_center)

            objetivo = Utils.entrada_centralizada('💬 : ').strip()

            if objetivo not in ['1', '2', '3']:
                Utils.mensagem_erro_centralizada("Opção inválida! Escolha 1, 2 ou 3.")
                Utils.aguardar_volta()
                continue 

            objetivos = {
                '1': 'GANHO DE MASSA',
                '2': 'PERDA DE PESO', 
                '3': 'MANUTENÇÃO DA SAÚDE' }
            Utils.spinner_centralizado("Salvando...", tempo = 2)
            c.rule('[b][i][blue]VitalTrack[/][/i][/b]')
            print(' ')
            escolhaobj2_text = Text()
            escolhaobj2_text.append(f'Você escolheu: {objetivos[objetivo]}')
            pescolhaobj2_text = Panel(escolhaobj2_text, border_style = 'bold blue', expand = False)
            pescolhaobj2_center = Align.center(pescolhaobj2_text)
            c.print(pescolhaobj2_center)
            
            if objetivo == '1':
                textoescolhaobj_text2 = Text()
                textoescolhaobj_text2.append('Boa! Você deseja aumentar sua massa corporal, tô contigo nessa! 😎 💪')
                textoescolhaobj_text2.append('\nUma dica: é importante que você consuma uma quantidade de calorias maior que a sua TMB.')
                textoescolhaobj_text2.append('\nNão sabe o que é TMB? não se preocupe! mais na frente eu te explico. 😉')
                textoescolha2 = Panel(textoescolhaobj_text2, border_style="bold blue", expand = False,title="Feedback",
                    title_align="center")
                textoescolha2_center = Align.center(textoescolha2)
                c.print(textoescolha2_center)

            elif objetivo == '2':
                textoescolhaobj_text3 = Text()
                textoescolhaobj_text3.append('Você escolheu perder peso, que legal! Tamo junto nessa jornada. 👊')
                textoescolhaobj_text3.append('\nCom foco e disciplina, qualquer objetivo pode se concretizar, vai dar tudo certo!')
                textoescolhaobj_text3.append('\nDica: é importante que você consuma uma quantidade de calorias inferior a sua TMB.')
                textoescolhaobj_text3.append('\nNão sabe o que é TMB? não se preocupe! mais na frente eu te explico. 😉')
                textoescolha3 = Panel(textoescolhaobj_text3, border_style="bold blue", expand = False,title="Feedback",
                    title_align="center")
                textoescolha3_center = Align.center(textoescolha3)
                c.print(textoescolha3_center)
                
            else:
                textoescolhaobj_text4 = Text()
                textoescolhaobj_text4.append('É isso ai! Você optou por manter-se saudável, conte comigo pra te auxiliar! ✋')
                textoescolhaobj_text4.append('\nÉ extremamente importante acompanhar a própria saúde, isso vale para pessoas de qualquer faixa etária. 🧒👨👴')
                textoescolhaobj_text4.append('\nDica: mantenha seu consumo de calorias em um valor próximo a sua TMB.')
                textoescolhaobj_text4.append('\nNão sabe o que é TMB? não se preocupe! mais na frente eu te explico. 😉')
                textoescolha4 = Panel(textoescolhaobj_text4, border_style="bold blue", expand = False,title="Feedback",
                    title_align="center")
                textoescolha4_center = Align.center(textoescolha4)
                c.print(textoescolha4_center)
            Utils.aguardar_volta()
            
            c.rule('[b][i][blue]VitalTrack[/][/i][/b]')
            print(' ')
            contescolhaobj_text = Text()
            contescolhaobj_text.append('Beleza! Agora vamos coletar algumas informações sobre você.')
            pcontescolhaobj = Panel(contescolhaobj_text, border_style = 'bold blue', expand = False)
            pcontescolhaobj_center = Align.center(pcontescolhaobj)
            c.print(pcontescolhaobj_center)

            try:
                while True:
                    try:
                        contescolhaobj2_text = Text()
                        contescolhaobj2_text.append('Para que os cálculos de saúde e metabolismo sejam mais precisos, gostaríamos de saber sua identidade de gênero.')
                        contescolhaobj2_text.append('Essa informação nos ajuda a oferecer resultados mais adequados para você.')
                        pcontescolhaobj2 = Panel(contescolhaobj2_text, border_style = 'bold blue', expand = False)
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

                        painelidentidade = Panel(textoidentidade_text, border_style="bold blue", expand = False,title="Sua identidade",title_align="center")
                        painelidentidade_center = Align.center(painelidentidade)
                        c.print(painelidentidade_center)

                        opcaoidentidade_text = Text()
                        opcaoidentidade_text.append('Digite sua opção: ', style = 'bold yellow')
                        popcaoidentidade = Panel(opcaoidentidade_text, expand = False, border_style = 'bold yellow')
                        popcaoidentidade_center = Align.center(popcaoidentidade)
                        c.print(popcaoidentidade_center)
                        
                        sexo_escolha = Utils.entrada_centralizada('💬 : ').strip()

                        if sexo_escolha not in ['1','2','3','4']:
                            Utils.mensagem_erro_centralizada("Escolha uma opção disponível (1-4).")
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
                                ptextoterapiahormonal = Panel(textoterapiahormonal, border_style="bold blue", expand = False,title="Sua identidade",title_align="center")
                                ptextoterapiahormonal_center = Align.center(ptextoterapiahormonal)
                                c.print(ptextoterapiahormonal_center)

                                perguntaterapia_text = Text()
                                perguntaterapia_text.append('Você já fez uso de terapia hormonal? (s/n):', style = 'bold yellow')
                                painelperguntaterapia_text = Panel(perguntaterapia_text, expand = False, border_style = 'bold yellow')
                                painelperguntaterapia_text_center = Align.center(painelperguntaterapia_text)
                                c.print(painelperguntaterapia_text_center)
                                
                                resposta = Utils.entrada_centralizada('💬 : ').lower().strip()

                                if resposta not in ['s','n']:
                                    Utils.mensagem_erro_centralizada("Digite (s) ou (n).")
                                    Utils.aguardar_volta()
                                    continue 
                                em_transicao = resposta == 's'
                                break
                            
                            if em_transicao:
                                while True:
                                    try:
                                        uso_hormonios_text = Text()
                                        uso_hormonios_text.append("Há quanto tempo (em meses) você faz uso de hormônios?", style = "bold yellow")
                                        puso_hormonios_text = Panel(uso_hormonios_text, expand = False, border_style = "bold yellow")
                                        puso_hormonios_text_center = Align.center(puso_hormonios_text)
                                        c.print(puso_hormonios_text_center)
                                        
                                        tempo_transicao = int(Utils.entrada_centralizada('💬 : '))
                                        
                                        if tempo_transicao <= 0:
                                            Utils.mensagem_erro_centralizada("Digite um valor válido.")
                                            Utils.aguardar_volta()
                                            continue
                                        break
                                    except ValueError:
                                        Utils.mensagem_erro_centralizada("Digite somente números.")
                                        Utils.aguardar_volta()
                                        continue

                    except ValueError:
                        c.print(Panel('Valores inválidos! Digite números válidos.', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))        
                    Utils.spinner_centralizado("Organizando suas informações...", tempo = 2)
                    while True:
                        try:
                            
                            c.rule('[b][i][blue]VitalTrack[/][/i][/b]')
                            print(' ')
                            maisdados_text = Text()
                            maisdados_text.append('Preciso de mais alguns de seus dados.')
                            pmaisdados = Panel(maisdados_text, expand = False, border_style = 'bold blue')
                            pmaisdados_center = Align.center(pmaisdados)
                            c.print(pmaisdados_center)
                            
                            c.print(Utils.mensagem_centralizada("Digite sua idade:"))
                            idade = int(Utils.entrada_centralizada('💬 : ').strip())
                            c.print(Utils.mensagem_centralizada("Digite o seu peso em quilogramas:"))
                            peso = float(Utils.entrada_centralizada('💬 : ').strip())
                            c.print(Utils.mensagem_centralizada("Digite sua altura em metros:"))
                            altura = float(Utils.entrada_centralizada('💬 : ').strip())
                            Utils.spinner_centralizado("Validando seus dados...", tempo = 2)
                            c.rule('[b][i][blue]VitalTrack[/][/i][/b]')
                            print(' ')
                            cadastro_sucesso_text = Text()
                            cadastro_sucesso_text.append("✅ Usuário cadastrado com sucesso!")
                            pcadastro_sucesso_text = Panel(cadastro_sucesso_text, expand = False, border_style = "bold green")
                            pcadastro_sucesso_text_center = Align.center(pcadastro_sucesso_text)
                            c.print(pcadastro_sucesso_text_center)
                            
                            print(' ')
                            Utils.spinner_centralizado("Carregando...", tempo = 2)

                            if idade <= 0 or peso <= 0 or altura <= 0:
                                Utils.mensagem_erro_centralizada("Valores inválidos! Digite números positivos.")
                                Utils.aguardar_volta()
                                continue
                            if idade > 100 or peso > 350 or altura > 2.5:
                                Utils.mensagem_erro_centralizada("Valores fora do intervalo estimado.")
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
                            
                            self.usuarios[email_do_usuario].dados = dados
                            self.usuarios[email_do_usuario].objetivo = objetivo
                            time.sleep(0.05)
                            return True
                            
                        except ValueError:
                            Utils.mensagem_erro_centralizada("Valores inválidos! Digite dados válidos para cada solicitação.")
                            Utils.aguardar_volta()
                            continue

            except ValueError:
                Utils.mensagem_erro_centralizada("Valores inválidos! Digite números válidos.")
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
            
            c.print(Utils.mensagem_centralizada("📧 Email cadastrado:"))
            email = Utils.entrada_centralizada('💬 : ').lower().strip()

            if email not in self.usuarios:
                Utils.mensagem_erro_centralizada("❌ Email não cadastrado.")
                Utils.aguardar_volta()
                continue
            break

        while True:
            
            c.print(Utils.mensagem_centralizada("🔑 Senha:"))
            senha = Utils.entrada_centralizada('💬 : ', is_password=True).strip()

            usuario = self.usuarios[email]
            if usuario.senha != senha:
                Utils.mensagem_erro_centralizada("❌ Senha incorreta.")
                Utils.aguardar_volta()
                continue

            Utils.spinner_centralizado("Validando credenciais...", tempo = 2)

            print('\n')

            painel_sucesso = Panel(
                f'✅ Acesso liberado, [bold blue]{usuario.nome}[/bold blue]!\n\n🚀 [green]Você está pronto para usar o VitalTrack![/green]',border_style='bold blue',expand=False, style = 'bold white')
            painel_sucesso_center = Align.center(painel_sucesso)
            c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
            print(' ')
            c.print(painel_sucesso_center)

            return email

    def atualizar_usuario(self,usuarios): 
        """
        Atualiza os dados do usuário,
        o usuário escolhe o que deseja atualizar,
        é permitido atualizar email, nome ou senha,
        os novos dados são salvos após mudanças.
        """
        Utils.limpar_tela_universal()
        if self.usuario_logado is None: 
            Utils.mensagem_erro_centralizada("Faça login primeiro!")
            return
        
        while True:
            c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
            print(' ')

            login_texto_atualizarusuario_text = Text()
            login_texto_atualizarusuario_text.append('\n')
            login_texto_atualizarusuario_text.append("Seja bem-vindo(a) ao menu de atualização de perfil!\n", style="bold yellow")
            login_texto_atualizarusuario_text.append("Por gentileza, escolha o que deseja atualizar.", style="dim")
            login_texto_atualizarusuario_text.append('\n')

            login_panel = Panel(login_texto_atualizarusuario_text, title="[bold blue]Atualizar Perfil",border_style="blue",expand=False)
            c.print(Align.center(login_panel))


            atualizarperfil_text = Text()

            atualizarperfil_text.append('\n1. ', style = 'red')
            atualizarperfil_text.append(f'Alterar nome. (nome atual:{usuarios[self.usuario_logado].nome})',style = 'bold white')

            atualizarperfil_text.append('\n2. ', style = 'red')
            atualizarperfil_text.append('Alterar senha.',style = 'bold white')

            atualizarperfil_text.append('\n3. ', style = 'red')
            atualizarperfil_text.append(f'Alterar email. (email atual:{self.usuario_logado})',style = 'bold white')

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
            opçao3 = input('💬 : ').strip()

            usuario = self.usuarios[self.usuario_logado] 

            if opçao3 == '1':
                c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                c.print(" ")
                c.print(Utils.mensagem_centralizada(f'Digite o novo nome (atual: {usuarios[self.usuario_logado].nome}):'))
                novo_nome = Utils.entrada_centralizada('💬 : ').strip()
                if novo_nome:
                    usuario.nome = novo_nome
                    self.gerenciador.salvar_dadosjson(self.usuarios)
                    c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                    c.print(" ")
                    mudancanome_text = Text()
                    mudancanome_text.append('✅ Nome atualizado com sucesso!',style = 'bold white')
                    pmudancanome_text = Panel(mudancanome_text, expand = False, border_style = 'bold blue')
                    pmudancanome_text_center = Align.center(pmudancanome_text)
                    c.print(pmudancanome_text_center)
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal()

            elif opçao3 == '2':
                c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                c.print(" ")
                c.print(Utils.mensagem_centralizada("Digite uma nova senha (mínimo 6 caracteres):"))
                nova_senha = Utils.entrada_centralizada('💬 : ')
                if len(nova_senha) >=6:
                    usuario.senha = nova_senha
                    self.gerenciador.salvar_dadosjson(self.usuarios)
                    c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                    c.print(" ")
                    mudancasenha_text = Text()
                    mudancasenha_text.append('✅ Senha atualizada com sucesso!',style = 'bold white')
                    pmudancasenha_text = Panel(mudancasenha_text, expand = False, border_style = 'bold blue')
                    pmudancasenha_text_center = Align.center(pmudancasenha_text)
                    c.print(pmudancasenha_text_center)
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal()

                else:
                    Utils.mensagem_erro_centralizada("Senha muito curta.")
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal() 

            elif opçao3 == '3':
                c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                c.print(" ")
                c.print(Utils.mensagem_centralizada(f'Digite seu novo email (atual: {self.usuario_logado}):'))
                novo_email = Utils.entrada_centralizada('💬 : ').strip().lower()  
                if not novo_email:
                    continue

                if novo_email == self.usuario_logado:
                    Utils.mensagem_erro_centralizada("O novo email é igual ao atual.")
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal()   

                elif '@' not in novo_email or '.com' not in novo_email:
                    Utils.mensagem_erro_centralizada("Formato inválido (use '@' e '.com').")
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal()

                elif novo_email in usuarios:
                    Utils.mensagem_erro_centralizada("Email já cadastrado.")
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal()

                else:
                    
                    usuario.email = novo_email
                    usuarios[novo_email] = usuario
                    del self.usuarios[self.usuario_logado]
                    self.usuario_logado = novo_email
                    self.gerenciador.salvar_dadosjson(self.usuarios)
                    c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                    c.print(" ")
                    mudancaemail_text = Text()
                    mudancaemail_text.append('✅ Email atualizado com sucesso!', style = 'bold white')
                    pmudancaemail_text = Panel(mudancaemail_text, expand = False, border_style = 'bold blue')
                    pmudancaemail_text_center = Align.center(pmudancaemail_text)
                    c.print(pmudancaemail_text_center)
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal() 

            elif opçao3 == '4':
                Utils.spinner_centralizado("Voltando...", tempo = 2)
                Utils.limpar_tela_universal()
                break

            else:
                Utils.mensagem_erro_centralizada("Opção inválida. Digite uma opção disponível (1-4)")
                Utils.aguardar_volta()
                Utils.limpar_tela_universal()
        return usuarios, self.usuario_logado

    def atualizar_dados(self):
        """
        Atualiza os dados físicos do usuário,
        usuário decide o que deseja atualizar.
        """
        Utils.limpar_tela_universal()

        if self.usuario_logado is None:
            Utils.mensagem_erro_centralizada("Faça login primeiro!")
            Utils.aguardar_volta()
            return self.usuarios, self.usuario_logado
        
        user = self.usuarios[self.usuario_logado]
        
        if not user.dados:
            Utils.mensagem_erro_centralizada("Complete seus dados primeiro!")
            self.escolher_objetivo()
            return self.usuarios, self.usuario_logado
        
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

                login_texto_atualizardados_text = Text()
                login_texto_atualizardados_text.append('\n')
                login_texto_atualizardados_text.append("Seja bem-vindo(a) ao menu de atualização de dados!\n", style="bold yellow")
                login_texto_atualizardados_text.append("Por gentileza, escolha o que deseja atualizar.", style="dim")
                login_texto_atualizardados_text.append('\n')

                login_panel = Panel(login_texto_atualizardados_text, title="[bold blue]Atualizar Dados",border_style="blue",expand=False)
                c.print(Align.center(login_panel))

                atualizarusuario_text = Text()
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
                atualizarusuario_text.append('\n')

                patualizarusuario = Panel(atualizarusuario_text, expand = False, border_style = 'bold blue', title = '🔹', title_align = 'center')
                patualizarusuario_center = Align.center(patualizarusuario)
                c.print(patualizarusuario_center)
                
                opcaoatualizardados_text = Text()
                opcaoatualizardados_text.append('Qual dado deseja alterar? (1-5):', style = 'bold yellow')
                popcaoatualizardados_text = Panel(opcaoatualizardados_text, expand = False, border_style = 'bold yellow')
                popcaoatualizardados_text_center = Align.center(popcaoatualizardados_text)
                c.print(popcaoatualizardados_text_center)
                campo = input('💬 : ').strip()
                
                if campo == '1':
                    c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                    print(' ')
                    c.print(Utils.mensagem_centralizada("Nova idade:"))
                    nova_idade = int(Utils.entrada_centralizada('💬 : '))
                    if 0 < nova_idade <= 100:
                        dados['idade'] = nova_idade
                        self.gerenciador.salvar_dadosjson({email: u.to_dict() for email, u in self.usuarios.items()})
                        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                        print(' ')
                        mudancaidada_text = Text()
                        mudancaidada_text.append('✅ Idade atualizada com sucesso!', style = 'bold white')
                        pmudancaidade_text = Panel(mudancaidada_text, expand = False, border_style = 'bold blue')
                        pmudancaidade_text_center = Align.center(pmudancaidade_text)
                        c.print(pmudancaidade_text_center)
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()

                    else:
                        Utils.mensagem_erro_centralizada("Idade deve ser entre 1 e 100 anos")
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()
                    
                elif campo == '2':
                    c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                    print(' ')
                    c.print(Utils.mensagem_centralizada("Novo peso, em quilogramas:"))
                    novo_peso = float(Utils.entrada_centralizada('💬 : '))
                    if 0 < novo_peso <= 350:
                        dados['peso'] = novo_peso
                        self.gerenciador.salvar_dadosjson({email: u.to_dict() for email, u in self.usuarios.items()})
                        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                        print(' ')
                        mudancapeso_text = Text()
                        mudancapeso_text.append('✅ Peso atualizado com sucesso!',style = 'bold white')
                        pmudancapeso_text = Panel(mudancapeso_text, expand = False, border_style = 'bold blue')
                        pmudancapeso_text_center = Align.center(pmudancapeso_text)
                        c.print(pmudancapeso_text_center)
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()

                    else:
                        Utils.mensagem_erro_centralizada("Peso deve ser entre 0.1 e 350 kg")
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()
                    
                elif campo == '3':
                    c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                    print(' ')
                    c.print(Utils.mensagem_centralizada("Nova altura, em metros:"))
                    nova_altura = float(Utils.entrada_centralizada('💬 : '))
                    if 0 < nova_altura <= 2.5:
                        dados['altura'] = nova_altura
                        self.gerenciador.salvar_dadosjson({email: u.to_dict() for email, u in self.usuarios.items()})
                        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                        print(' ')
                        mudancaaltura_text = Text()
                        mudancaaltura_text.append('✅ Altura atualizada com sucesso!', style = 'bold white')
                        pmudancaaltura_text = Panel(mudancaaltura_text, expand = False, border_style = 'bold blue')
                        pmudancaaltura_text_center = Align.center(pmudancaaltura_text)
                        c.print(pmudancaaltura_text_center)
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()

                    else:
                        Utils.mensagem_erro_centralizada("Altura deve ser entre 0.1 e 2.5 metros")
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()
                    
                elif campo == '4':
                    c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                    print(' ')
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
                    novo_objetivo = Utils.entrada_centralizada('💬 : ').strip()
                    if novo_objetivo in ['1', '2', '3']:
                        user.objetivo = novo_objetivo
                        self.gerenciador.salvar_dadosjson({email: u.to_dict() for email, u in self.usuarios.items()})
                        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                        print(' ')
                        escolhanovoobj_text = Text()
                        escolhanovoobj_text.append(f'✅ Objetivo atualizado para: {objetivos[novo_objetivo]}', style = 'bold white')
                        pescolhanovoobj_text = Panel(escolhanovoobj_text, expand = False, border_style = 'bold blue')
                        pescolhanovoobj_text_center = Align.center(pescolhanovoobj_text)
                        c.print(pescolhanovoobj_text_center)
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()

                    else:
                        Utils.mensagem_erro_centralizada("Opção inválida!")
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal()
                    
                elif campo == '5':
                    Utils.spinner_centralizado("Voltando...", tempo = 2)
                    Utils.limpar_tela_universal()
                    break
                    
                else:
                    Utils.mensagem_centralizada("Opção inválida! digite uma opção disponível.")
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal()
                    
            except ValueError:
                Utils.mensagem_centralizada("Valor inválido! Digite números válidos.")
                Utils.aguardar_volta()
                Utils.limpar_tela_universal()
        return self.usuarios, self.usuario_logado

    def deletar_usuario(self):
        """
        Deleta o usuário cadastrado,
        apaga todos os dados inseridos e salvos.
        """

        if self.usuario_logado is None:
            Utils.mensagem_erro_centralizada("Faça login primeiro.")
            return
        
        while True:
            Utils.limpar_tela_universal()
            c.rule('[i][blue]VitalTrack[/][/i]')
            print(" ")

            deletarconta_text = Text()
            deletarconta_text.append('\n')
            deletarconta_text.append("Seção de Exclusão de Conta – Cuidado! Esta ação é permanente.\n", style="bold yellow")
            deletarconta_text.append("Esta ação não pode ser desfeita. Confirme se deseja deletar sua conta.", style="dim")
            deletarconta_text.append('\n')

            deletarconta_panel = Panel(deletarconta_text,border_style="blue",expand=False)
            c.print(Align.center(deletarconta_panel))


            deletarconta_text = Text()
            deletarconta_text.append("Tem certeza que deseja deletar sua conta? 😕 (s/n):")
            pdeletarconta_text = Panel(deletarconta_text, expand = False, border_style = "bold yellow", style = "bold yellow")
            pdeletarconta_text_center = Align.center(pdeletarconta_text)
            c.print(pdeletarconta_text_center)
        
            confirmaçao = input('💬 : ').lower()

            if confirmaçao == 's':
                del self.usuarios[self.usuario_logado]
                self.gerenciador.salvar_dadosjson(self.usuarios)
                self.usuario_logado = None
                contadeletada_text = Text()
                contadeletada_text.append('✅ Conta deletada com sucesso. Até logo...')
                pcontadeletadaa_text = Panel(contadeletada_text, expand = False, border_style = 'cyan')
                pcontadeletadaa_text_center = Align.center(pcontadeletadaa_text)
                c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                print(' ')
                c.print(pcontadeletadaa_text_center)
                return True
            
            elif confirmaçao == 'n':
                naodeletada_text = Text()
                naodeletada_text.append('Que bom! Creio que ainda podemos te auxiliar em muitas coisas. 😉✨')
                pnaodeletada_text = Panel(naodeletada_text, expand = False, border_style = 'cyan')
                pnaodeletada_text_center = Align.center(pnaodeletada_text)
                c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                print(' ')
                c.print(pnaodeletada_text_center)
                Utils.aguardar_volta()
                Utils.limpar_tela_universal()
                return False

            else:
                Utils.mensagem_erro_centralizada('Digite "s" ou "n".')
                Utils.aguardar_volta()
                Utils.limpar_tela_universal()
            
