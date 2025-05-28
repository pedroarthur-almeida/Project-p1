usuarios = {} 
usuario_logado = None 
from datetime import datetime 
import json
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import random
from prompt_toolkit import prompt
from rich.align import Align            
from rich.columns import Columns

c = Console()

def salvar_dadosjson():
    """Salva os dados em um arquivo .json"""
    with open('usuarios.json', 'w') as arquivo:
        json.dump(usuarios, arquivo, indent=4)

def carregar_dadosjson():
    """Carrega os dados salvos no arquivo .json"""
    global usuarios
    try:
        with open('usuarios.json', 'r') as arquivo:
            usuarios = json.load(arquivo)
    except FileNotFoundError:
        return {}

def aguardar_volta():
    """Pausa a execução do programa até que o usuário tecle "enter".""" 
    input('\nPressione "Enter" para voltar...')
    
def cadastro_de_usuario(): 
    """Cadastra o usuário e salva seus dados em um dicionário,
       em que a chave é o email.
    """
    c.clear()
    global usuarios,usuario_logado 
    c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
    print(' ')
    conteudo = Text("Siga as instruções para um cadastro bem sucedido.", justify="center")
    textcadastro = Panel(conteudo,title="[i][cyan]CADASTRO[/cyan][/i]",title_align="center",border_style="cyan",expand=True)
    c.print(textcadastro)

    while True:
        c.print(Panel('Digite o seu [green][b][u]email[/u][/b][/]: ', expand = False, border_style = 'yellow'))
        email = input('>>> ').strip().lower()
        
        if email in usuarios:
            erroremail_text = Text()
            erroremail_text.append('Este email já foi cadastrado!')
            erroremail_text.append('\nInsira um email ainda não cadastrado.')
            perroremail = Panel(erroremail_text, border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center")
            c.print(perroremail)
            aguardar_volta()
            continue 
        
        elif '@' not in email or '.com' not in email:
            erroremail_text2 = Text()
            erroremail_text2.append('O email precisa estar em um formato válido.')
            erroremail_text2.append('\nO email precisa ter ".com" e "@".')
            perroremail2 = Panel(erroremail_text2, border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center")
            c.print(perroremail2)
            aguardar_volta()
            continue 

        dominios_validos = ['gmail.com', 'outlook.com', 'hotmail.com', 'yahoo.com', 'icloud.com'] #criando essa lista pra salvar os dominios validos.
        
        if not any(email.endswith(dominio) for dominio in dominios_validos): #o comando endswith vai verficiar se o email termina com o domínio de forma correta, para evitar falsos positivos e emails no formato errado, ex: arthur@xcsgmail.com
            erroremail_text3 = Text()
            erroremail_text3.append('Domínio inválido! Use: Gmail, Outlook, Hotmail, Yahoo ou iCloud.')
            perroremail3 = Panel(erroremail_text3, border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center")
            c.print(perroremail3)
            aguardar_volta()
            continue

        break
    
    while True:
        c.print(Panel('Digite sua [green][u][b]senha[/u][/b][/](mínimo 6 caracteres): ', expand = False, border_style = 'yellow'))
        senha = prompt('>>> ', is_password = True)

        if len(senha) < 6:
            errorsenha_text = Text()
            errorsenha_text.append('Senha muito curta, a sua senha precisa ter, no mínimo, 6 caracteres.')
            perrorsenha = Panel(errorsenha_text, border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center")
            c.print(perrorsenha)
            aguardar_volta()
            continue 
            
        c.print(Panel('Confirme sua [green][u][b]senha[/b][/u][/]: ', expand = False, border_style = 'yellow'))
        confirmaçao_de_senha = prompt('>>> ', is_password = True)

        if senha != confirmaçao_de_senha:
            errorsenha_text2 = Text()
            errorsenha_text2.append('As senhas não coinscidem.')
            perrorsenha2 = Panel(errorsenha_text2, border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center")
            c.print(perrorsenha2)
            aguardar_volta()
            continue 
        else:
            break
    
    c.print(Panel('Digite seu [green][u][b]nome[/b][/u][/]: (Será seu nome de usuário)', expand = False, border_style = 'yellow'))
    nome = input('>>> ').strip()
    with c.status("[red]G[/red][magenta]u[/magenta][yellow]a[/yellow][green]r[/green]"
        "[cyan]d[/cyan][blue]a[/blue][red]n[/red][magenta]d[/magenta][yellow]o[/yellow] "
        "[green]o[/green][cyan]s[/cyan] "
        "[blue]d[/blue][red]a[/red][magenta]d[/magenta][yellow]o[/yellow][green]s[/green]", spinner = 'hearts'):  
        time.sleep(2)
    
    usuarios[email] = {
        'senha': senha,
        'nome': nome,
        'objetivo': None,
        'dados': None,
        'calorias_hoje': 0,          
        'historico_dias': {} 
    }

    usuario_logado = email
    c.rule('[i][blue]VitalTrack[/][/i]')
    print(' ')
    c.print(Panel('Agora vamos definir o [green][u]seu[/u][/] objetivo! 👇', expand = False, border_style = 'cyan'))

    escolher_objetivo()
    
    print('\nUsuário Cadastrado com sucesso! ✔')

    print('Seja bem vindo ao VITALTRACK! 😉')
    salvar_dadosjson()
    return True

def escolher_objetivo():
    """
    Escolha de objetivo (parte do cadastro),
    Usuário escolhe seu objetivo e fornece seus dados,
    armazena os dados do usuário em um outro dicionário "dados".
    """
    c.clear()
    global usuario_logado, usuarios

    while True:

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

        c.print(painelescolhadeobj)

        c.print(Panel('Agora é com [u][green][b]você![/b][/][/u] 🕺 Escolha um objetivo (1-3): ', border_style = 'yellow', expand = False))
        objetivo = input('>>> ').strip()

        if objetivo not in ['1', '2', '3']:
            errorescolhaobj_text = Text()
            errorescolhaobj_text.append('Opção inválida! Escolha 1, 2 ou 3.')
            perrorescolhaobjt = Panel(errorescolhaobj_text, border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center")
            c.print(perrorescolhaobjt)
            aguardar_volta()
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
        c.print(Panel(f'Você escolheu: {objetivos[objetivo]}', border_style = 'cyan', expand = False))
        
        if objetivo == '1':
            textoescolhaobj_text2 = Text()
            textoescolhaobj_text2.append('Boa! Você deseja aumentar sua massa corporal, tô contigo nessa! 😎 💪')
            textoescolhaobj_text2.append('\nUma dica: é importante que você consuma uma quantidade de calorias maior que a sua TMB.')
            textoescolhaobj_text2.append('\nNão sabe o que é TMB? não se preocupe! mais na frente eu te explico. 😉')
            textoescolha2 = Panel(textoescolhaobj_text2, border_style="cyan", expand = False,title="[bold cyan]Feedback[/bold cyan]",
                title_align="center")
            c.print(textoescolha2)

        elif objetivo == '2':
            textoescolhaobj_text3 = Text()
            textoescolhaobj_text3.append('Você escolheu perder peso, que legal! Tamo junto nessa jornada. 👊')
            textoescolhaobj_text3.append('\nCom foco e disciplina, qualquer objetivo pode se concretizar, vai dar tudo certo!')
            textoescolhaobj_text3.append('\nDica: é importante que você consuma uma quantidade de calorias inferior a sua TMB.')
            textoescolhaobj_text3.append('\nNão sabe o que é TMB? não se preocupe! mais na frente eu te explico. 😉')
            textoescolha3 = Panel(textoescolhaobj_text3, border_style="cyan", expand = False,title="[bold cyan]Feedback[/bold cyan]",
                title_align="center")
            c.print(textoescolha3)
            
        else:
            textoescolhaobj_text4 = Text()
            textoescolhaobj_text4.append('É isso ai! Você optou por manter-se saudável, conte comigo pra te auxiliar! ✋')
            textoescolhaobj_text4.append('\nÉ extremamente importante acompanhar a própria saúde, isso vale para pessoas de qualquer faixa etária. 🧒👨👴')
            textoescolhaobj_text4.append('\nDica: mantenha seu consumo de calorias em um valor próximo a sua TMB.')
            textoescolhaobj_text4.append('\nNão sabe o que é TMB? não se preocupe! mais na frente eu te explico. 😉')
            textoescolha4 = Panel(textoescolhaobj_text4, border_style="cyan", expand = False,title="[bold cyan]Feedback[/bold cyan]",
                title_align="center")
            c.print(textoescolha4)
        aguardar_volta()
        
        c.rule('[b][i][blue]VitalTrack[/][/i][/b]')
        print(' ')
        c.print(Panel('Beleza! Agora vamos coletar algumas informações sobre [green][u]você.[/u][/]', border_style = 'cyan', expand = False))

        try:
            while True:
                try:
                    c.print(Panel('Para que os cálculos de saúde e metabolismo sejam mais precisos, gostaríamos de saber sua identidade de gênero. Essa informação nos ajuda a oferecer resultados mais adequados para você.', border_style = 'cyan', expand = False))
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
                    c.print(painelidentidade)

                    c.print(Panel('Digite [green][u][b]sua[/b][/u][/] opção: ', expand = False, border_style = 'yellow'))
                    sexo_escolha = input('>>> ').strip()

                    if sexo_escolha not in ['1','2','3','4']:
                        erroridentidade_text = Text()
                        erroridentidade_text.append('Escolha uma opção disponível (1-4).')
                        perroridentidade = Panel(erroridentidade_text, border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center")
                        c.print(perroridentidade)
                        aguardar_volta()
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
                            textoterapiahormonal = Text()
                            textoterapiahormonal.append('\n')
                            textoterapiahormonal.append('Para adaptar melhor os cálculos às mudanças metabólicas:')
                            textoterapiahormonal.append('\n')
                            ptextoterapiahormonal = Panel(textoterapiahormonal, border_style="cyan", expand = False,title="[bold cyan]Sua identidade[/bold cyan]",title_align="center")
                            c.print(ptextoterapiahormonal)
                            c.print(Panel('Você já fez uso de terapia hormonal? (s/n):', expand = False, border_style = 'yellow'))
                            resposta = input('>>> ').lower().strip()
                            if resposta not in ['s','n']:
                                errorterapiahormonal_text = Text()
                                errorterapiahormonal_text.append('Digite (s) ou (n).')
                                perrorterapiahormonal = Panel(errorterapiahormonal_text, border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center")
                                c.print(perrorterapiahormonal)
                                aguardar_volta()
                                continue 
                            em_transicao = resposta == 's'
                            break
                        
                        if em_transicao:
                            while True:
                                try:
                                    c.print(Panel('Há quanto tempo (em meses) você faz uso de hormônios?', expand = False, border_style = 'yellow'))
                                    tempo_transicao = int(input('>>> '))
                                    
                                    if tempo_transicao <= 0:
                                        c.print(Panel('Digite um valor válido.', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                                        aguardar_volta()
                                        continue
                                    break
                                except ValueError:
                                    c.print(Panel('Digite somente números.', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                                    aguardar_volta()
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
                        c.print(Panel('Preciso de mais alguns de [green][b][u]seus[/u][/b][/] dados.', expand = False, border_style = 'cyan'))
                        c.print(Panel('Digite sua [u][green][b]idade[/b][/][/u]: ', expand = False, border_style = 'yellow'))
                        idade = int(input('>>> ').strip())
                        c.print(Panel('Digite o seu [u][green][b]peso[/b][/][/u] em quilogramas: ', expand = False, border_style = 'yellow'))
                        peso = float(input('>>> ').strip())
                        c.print(Panel('Digite sua [u][green][b]altura[/b][/][/u] em metros: ', expand = False, border_style = 'yellow'))
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
                            aguardar_volta()
                            continue
                        if idade > 100 or peso > 350 or altura > 2.5:
                            c.print(Panel('Valores fora do intervalo estimado.', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                            aguardar_volta()
                            continue

                        dados = {
                            'objetivo': objetivo,
                            'idade': idade,
                            'peso': peso,
                            'altura': altura,
                            'sexo': sexo,
                            'sexo_biologico': sexo_biologico if sexo_escolha in ['3', '4'] else None,
                            'em_transicao': em_transicao if sexo_escolha in ['3', '4'] else None,
                            'tempo_transicao': tempo_transicao if (sexo_escolha in ['3', '4'] and em_transicao) else None,
                            'sexo_escolha': sexo_escolha
                        }
                        
                        usuarios[usuario_logado]['dados'] = dados
                        usuarios[usuario_logado]['objetivo'] = objetivo
                        time.sleep(0.05)
                        
                        return True
                        
                    except ValueError:
                        c.print(Panel('Valores inválidos! Digite dados válidos para cada solicitação.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                        aguardar_volta()
                        continue

        except ValueError:
            c.print(Panel('Valores inválidos! Digite números válidos.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
            aguardar_volta()

def fazer_login(): #criando a função de login.
    """
    Função responsável pelo login do usuário,
    O usuário digita seu email e sua senha,
    caso estejam corretos, libera o acesso ao "menu logado".
    """
    c.clear()
    global usuario_logado, usuarios
    c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
    print(' ') 
    conteudo1 = Text('Seja bem vindo(a) a etapa de login', justify = 'center')
    textlogin = Panel(conteudo1,title="[i][cyan]LOGIN[/cyan][/i]",title_align="center",border_style="cyan",expand=True)
    c.print(textlogin)

    while True:
        c.print(Panel('Digite o seu [u][b][green]email[/][/b][/] cadastrado: ',expand = False, border_style = 'yellow' ))
        email = input('>>> ').lower().strip()
        
        if email not in usuarios:
            c.print(Panel('Email não cadastrado.', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
            aguardar_volta()
            continue
        break

    while True:
        c.print(Panel('Digite sua [u][b][green]senha:[/][/b][/] ',expand = False, border_style = 'yellow'))
        senha = prompt('>>> ', is_password = True).strip()

        if usuarios[email]["senha"] != senha:
            c.print(Panel('Senha incorreta.', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
            aguardar_volta()
            continue
    
        else:
            usuario_logado = email 
            with c.status("[red]V[/red][magenta]a[/magenta][yellow]l[/yellow][green]i[/green]"
              "[cyan]d[/cyan][blue]a[/blue][red]n[/red][magenta]d[/magenta][yellow]o[/yellow]", spinner='hearts'):
                time.sleep(2)
            print(' ')
            c.print(Panel(f'Bem-vindo(a), {usuarios[email]["nome"]}!', expand = False, border_style = 'cyan', style = 'cyan'))
            print(' ')
            return True

def atualizar_usuario(): 
    """
    Atualiza os dados do usuário,
    o usuário escolhe o que deseja atualizar,
    é permitido atualizar email, nome ou senha,
    os novos dados são salvos após mudanças.
    """
    c.clear()
    global usuario_logado, usuarios
    if usuario_logado is None: 
        c.print(Panel('Faça login primeiro!',expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
        return
    
    while True:
        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
        print(' ')
        atualizarperfil_text = Text()
        atualizarperfil_text.append('\n')
        atualizarperfil_text.append('ATUALIZAR PERFIL', style = 'blue')
        atualizarperfil_text.append('\n')

        atualizarperfil_text.append('\n1. ', style = 'red')
        atualizarperfil_text.append(f'Alterar nome. (nome atual:{usuarios[usuario_logado]["nome"]})')

        atualizarperfil_text.append('\n2. ', style = 'red')
        atualizarperfil_text.append('Alterar senha.')

        atualizarperfil_text.append('\n3. ', style = 'red')
        atualizarperfil_text.append(f'Alterar email. (email atual:{usuario_logado})')

        atualizarperfil_text.append('\n4. ', style = 'red')
        atualizarperfil_text.append('Voltar')

        patualizarperfil = Panel(atualizarperfil_text, expand = False, border_style = 'cyan', title = '🔹')
        c.print(patualizarperfil)

        c.print(Panel('O que deseja atualizar? (1-4):', expand = False, border_style = 'yellow'))
        opçao3 = input('>>> ').strip()

        if opçao3 == '1':
            c.print(Panel(f'Digite o novo nome (atual: {usuarios[usuario_logado]["nome"]}):',expand = False, border_style = 'yellow'))
            novo_nome = input('>>> ').strip()
            if novo_nome:
                usuarios[usuario_logado]["nome"] = novo_nome
                salvar_dadosjson()
                c.print(Panel('Nome atualizado com sucesso!', expand = False, border_style = 'cyan'))
                aguardar_volta()
                c.clear()

        elif opçao3 == '2':
            c.print(Panel('Digite uma nova senha (mínimo 6 caracteres):', expand = False, border_style = 'yellow'))
            nova_senha = input('>>> ')
            if len(nova_senha) >=6:
                usuarios[usuario_logado]["senha"] = nova_senha
                salvar_dadosjson()
                c.print(Panel('Senha atualizada com sucesso!', expand = False, border_style = 'cyan'))
                aguardar_volta()
                c.clear()

            else:
                c.print(Panel('Senha muito curta.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                aguardar_volta()
                c.clear() 

        elif opçao3 == '3':
            c.print(Panel(f'Digite seu novo email (atual: {usuario_logado}):', expand = False, border_style = 'yellow'))
            novo_email = input('>>> ').strip().lower()  
            if not novo_email:
                continue

            if novo_email == usuario_logado:
                c.print(Panel('O novo email é igual ao atual.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                aguardar_volta()
                c.clear()   

            elif '@' not in novo_email or '.com' not in novo_email:
                c.print(Panel("Formato inválido (use '@' e '.com').", expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                aguardar_volta()
                c.clear()

            elif novo_email in usuarios:
                c.print(Panel('Email já cadastrado.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center')) 
                aguardar_volta()
                c.clear()

            else:
                
                usuarios[novo_email] = usuarios[usuario_logado]
                del usuarios[usuario_logado]
                usuario_logado = novo_email
                salvar_dadosjson()
                c.print(Panel("Email atualizado com sucesso!", expand = False, border_style = 'cyan'))
                aguardar_volta()
                c.clear() 

        elif opçao3 == '4':
            with c.status("[red]G[/red][magenta]u[/magenta][yellow]a[/yellow][green]r[/green]"
                "[cyan]d[/cyan][blue]a[/blue][red]n[/red][magenta]d[/magenta][yellow]o[/yellow] "
                "[green]o[/green][cyan]s[/cyan] "
                "[blue]d[/blue][red]a[/red][magenta]d[/magenta][yellow]o[/yellow][green]s[/green]", spinner = 'hearts'):  
                time.sleep(2)
                c.clear()
            break

        else:
            c.print(Panel('Opção inválida. Digite uma opção disponível (1-4)', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
            aguardar_volta()
            c.clear()

def atualizar_dados():
    """
    Atualiza os dados físicos do usuário,
    usuário decide o que deseja atualizar.
    """
    c.clear()
    global usuario_logado, usuarios

    if usuario_logado is None:
        c.print(Panel('Faça login primeiro!', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
        aguardar_volta()
        return
    
    user = usuarios[usuario_logado]
    
    if not user.get('dados'):
        c.print(Panel('Complete seus dados primeiro!', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
        escolher_objetivo()
        return
    
    objetivos = {
            '1': 'GANHO DE MASSA',
            '2': 'PERDA DE PESO', 
            '3': 'MANUTENÇÃO DA SAÚDE' }
    
    while True:

        try:
            dados = user['dados']
            objetivo_atual = user['objetivo']
            c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
            print(' ')
            atualizarusuario_text = Text()
            atualizarusuario_text.append('\n')
            atualizarusuario_text.append('ATUALIZAR DADOS PESSOAIS', style = 'blue')
            atualizarusuario_text.append('\n')

            atualizarusuario_text.append('\n1. ', style = 'red')
            atualizarusuario_text.append(f'Idade: {dados["idade"]} anos')

            atualizarusuario_text.append('\n2. ', style = 'red')
            atualizarusuario_text.append(f'Peso: {dados["peso"]} kg')

            atualizarusuario_text.append('\n3. ', style = 'red')
            atualizarusuario_text.append(f'Altura: {dados["altura"]} m')

            atualizarusuario_text.append('\n4. ', style = 'red')
            atualizarusuario_text.append(f'Objetivo: {objetivos[objetivo_atual]}')

            atualizarusuario_text.append('\n5. ', style = 'red')
            atualizarusuario_text.append('Voltar')

            patualizarusuario = Panel(atualizarusuario_text, expand = False, border_style = 'cyan', title = '🔹', title_align = 'center')
            c.print(patualizarusuario)
            
            c.print(Panel('Qual dado deseja alterar? (1-5):', expand = False, border_style = 'yellow'))
            campo = input('>>> ').strip()
            
            if campo == '1':
                c.print(Panel('Nova idade:', expand = False, border_style = 'yellow'))
                nova_idade = int(input('>>> '))
                if 0 < nova_idade <= 100:
                    dados['idade'] = nova_idade
                    salvar_dadosjson()
                    c.print(Panel('Idade atualizada com sucesso!', expand = False, border_style = 'cyan'))
                    aguardar_volta()
                    c.clear()

                else:
                    c.print(Panel('Idade deve ser entre 1 e 100 anos', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                    aguardar_volta()
                    c.clear()
                
            elif campo == '2':
                c.print(Panel('Novo peso, em quilogramas:', expand = False, border_style = 'yellow'))
                novo_peso = float(input('>>> '))
                if 0 < novo_peso <= 350:
                    dados['peso'] = novo_peso
                    salvar_dadosjson()
                    c.print(Panel('Peso atualizado com sucesso!', expand = False, border_style = 'cyan'))
                    aguardar_volta()
                    c.clear()

                else:
                    c.print(Panel('Peso deve ser entre 0.1 e 350 kg', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                    aguardar_volta()
                    c.clear()
                
            elif campo == '3':
                c.print(Panel('Nova altura, em metros:', expand = False, border_style = 'yellow'))
                nova_altura = float(input('>>> '))
                if 0 < nova_altura <= 2.5:
                    dados['altura'] = nova_altura
                    salvar_dadosjson()
                    c.print(Panel('Altura atualizada com sucesso!', expand = False, border_style = 'cyan'))
                    aguardar_volta()
                    c.clear()

                else:
                    c.print(Panel('Altura deve ser entre 0.1 e 2.5 metros', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                    aguardar_volta()
                    c.clear()
                
            elif campo == '4':
                mudandoobj_text = Text()
                mudandoobj_text.append('\n')
                mudandoobj_text.append('Objetivos disponíveis:')
                mudandoobj_text.append('\n')

                mudandoobj_text.append('\n1. ', style = 'red')
                mudandoobj_text.append('Ganho de massa')

                mudandoobj_text.append('\n2. ', style = 'red')
                mudandoobj_text.append('Perda de peso')

                mudandoobj_text.append('\n3. ', style = 'red')
                mudandoobj_text.append('Manutenção da saúde')

                pmudandoobjt = Panel(mudandoobj_text, expand = False, border_style = 'cyan', title = 'Novo objetivo', title_align = 'center')
                c.print(pmudandoobjt)
                
                c.print(Panel('Novo objetivo (1-3):', expand = False, border_style = 'yellow'))
                novo_objetivo = input('>>> ').strip()
                if novo_objetivo in ['1', '2', '3']:
                    user['objetivo'] = novo_objetivo
                    salvar_dadosjson()
                    c.print(Panel(f'Objetivo atualizado para: {objetivos[novo_objetivo]}', expand = False, border_style = 'cyan'))
                    aguardar_volta()
                    c.clear()

                else:
                    c.print(Panel('Opção inválida!', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                aguardar_volta()
                c.clear()
                
            elif campo == '5':
                with c.status("[red]S[/red][magenta]a[/magenta][yellow]i[/yellow]"
                    "[green]n[/green][cyan]d[/cyan][blue]o[/blue]", spinner = 'hearts'):  
                    time.sleep(2)
                    c.clear()
                break
                
            else:
                c.print(Panel('Opção inválida! digite uma opção disponível.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                aguardar_volta()
                c.clear()
                
        except ValueError:
            c.print(Panel('Valor inválido! Digite números válidos.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
            aguardar_volta()
            c.clear()

def deletar_usuario():
    """
    Deleta o usuário cadastrado,
    apaga todos os dados inseridos e salvos.
    """
    global usuario_logado,usuarios

    if usuario_logado is None:
        c.print(Panel('Faça login primeiro.', expand = False, border_style = 'ERRO', title = 'ERRO', title_align = 'center'))
        return
    
    while True:

        c.print(Panel('Tem certeza que deseja deletar sua conta? 😕 (s/n):', expand = False, border_style = 'yellow'))
        confirmaçao = input('>>> ').lower()

        if confirmaçao == 's':
            del usuarios[usuario_logado]
            salvar_dadosjson()
            usuario_logado = None
            c.print(Panel('Conta [u][b][red]deletada[/][/b][/u] com sucesso. Até logo...', expand = False, border_style = 'cyan'))
            return True
        
        elif confirmaçao == 'n':
            c.print(Panel('Que bom! Creio que ainda podemos te auxiliar em muitas coisas. 😉✨', expand = False, border_style = 'cyan'))
            aguardar_volta()
            c.clear()
            return False

        else:
            c.print(Panel('Digite "s" ou "n".', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
            aguardar_volta()
            c.clear()
        
carregar_dadosjson()

def menu_principal():
    """
    Menu inicial,
    é exibido logo após iniciar o programa,
    abre ao usuário as opções de cadastro e login.
    """
    c.clear()
    global usuario_logado 
 
    while True:
        
        c.rule('[blue][i][b]Boas vindas ao VitalTrack![/b][/i][/]')

        textomenuprincipal_text = Text()

        textomenuprincipal_text.append('\n')
        textomenuprincipal_text.append('Seja bem vindo(a) ao menu inicial!\n', style = 'blue')
        textomenuprincipal_text.append('\nEscolha uma opção dentre as disponíveis.\n')

        textomenuprincipal_text.append('\n1 ', style = 'red')
        textomenuprincipal_text.append('Cadastro\n')

        textomenuprincipal_text.append('2 ', style = 'red')
        textomenuprincipal_text.append('Login\n')

        textomenuprincipal_text.append('3 ', style = 'red')
        textomenuprincipal_text.append('Sair\n')

        panel = Panel(textomenuprincipal_text, border_style="cyan", expand = False,title="[bold cyan]Menu Inicial[/bold cyan]",
    title_align="center")

        c.print(panel)

        c.print(Panel('Digite [green][u][b]sua[/b][/u][/] opção: ', expand = False, border_style = 'yellow'))
        opçao1 = input('>>> ')

        if opçao1 == '1':
            with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
    "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner = 'hearts'):  
                    time.sleep(2)
            if cadastro_de_usuario():
                menu_logado()
                     
        elif opçao1 == '2':
            with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
    "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner = 'hearts'):  
                    time.sleep(2)
            if fazer_login():
                with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
    "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner = 'hearts'):  
                    time.sleep(2)
                menu_logado()
                
        elif opçao1 == '3':
            with c.status("[red]S[/red][magenta]a[/magenta][yellow]i[/yellow]"
    "[green]n[/green][cyan]d[/cyan][blue]o[/blue]", spinner = 'hearts'):  
                    time.sleep(2)
            c.print(Panel('até logo! 👋', expand = False, border_style = 'cyan'))
            break

        else:
            errormenuprincipal_text = Text()
            errormenuprincipal_text.append('Opção inválida!')
            errormenuprincipal_text.append('Digite uma opção presente no MENU.')
            perrormenuprincipal = Panel(errormenuprincipal_text, border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center")
            c.print(perrormenuprincipal)
            aguardar_volta()

def calcular_imc():
    """
    Calcula o IMC (índice de massa corporal) do usuário,
    O usuário pode calcular o seu próprio IMC (com seus dados salvos),
    ou pode optar por calcular outro IMC qualquer,
    a função retorna o status após calcular o valor do imc, em ambos os casos.
    """
    c.clear()
    global usuarios,usuario_logado

    if usuario_logado is None:
        c.print(Panel('Faça login primeiro!', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
        aguardar_volta()
        return
    
    user = usuarios[usuario_logado]
    if not user.get('dados'):
        c.print(Panel('Complete seus dados primeiro!', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
        escolher_objetivo()
        return
    
    dados = user['dados']
    imc = dados['peso'] / (dados['altura'] ** 2)

    while True:
        c.clear()
        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
        print(' ')
        imc_text = Text('CALCULADORA DE IMC (ÍNDICE DE MASSA CORPORAL)', justify = 'center')
        p_imctext = Panel(imc_text, title="[i][cyan]IMC[/cyan][/i]",title_align="center",border_style="cyan",expand=True)
        c.print(p_imctext)
        c.print(Panel('Deseja calcular o [u]seu IMC[/u] (1), calcular [u]outro qualquer[/u] (2), ou voltar (3)?', expand = False, border_style = 'yellow'))
        calcularimc_visualizarimc = input('>>> ')

        if calcularimc_visualizarimc not in ['1','2','3']:
            c.print(Panel('Digite "1", "2" ou "3".', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
            aguardar_volta()
            continue

        if calcularimc_visualizarimc == '1':
            calcularimc1_text = Text()
            calcularimc1_text.append(f'SEU IMC: {imc:.2f}')
            
            if imc < 18.5:
                status = 'Abaixo do peso'
            elif 18.5 <= imc < 25:
                status = 'Peso normal'
            elif 25 <= imc < 30:
                status = 'Sobrepeso'
            else:
                status = 'Obesidade'
            calcularimc1_text.append(f'\nStatus: {status}')
            pcalcularimc1 = Panel(calcularimc1_text, expand = False, border_style = 'cyan')
            with c.status("[red]C[/red][magenta]a[/magenta][yellow]l[/yellow][green]c[/green]"
                "[cyan]u[/cyan][blue]l[/blue][red]a[/red][magenta]n[/magenta]"
                "[yellow]d[/yellow][green]o[/green]", spinner="hearts"):
                time.sleep(2)
            c.print(pcalcularimc1)

            objetivo = user['objetivo']
            if objetivo == '1':
                    feedbackobj1_text = Text()
                    feedbackobj1_text.append('Dica: Aumente a ingestão de proteínas e calorias saudáveis')  
                    feedbackobj1_text.append('\nAlém disso, Foque em treinos de força e superávit calórico')
                    feedbackobj1_text.append('\nConsuma alimentos com alta quantidade de proteínas e carboidratos.')
                    pfeedbackobj1 = Panel(feedbackobj1_text, border_style="cyan", expand = False,title="[bold cyan]Feedback[/bold cyan]",
                title_align="center")
                    c.print(pfeedbackobj1)
                    
            elif objetivo == '2':
                    feedbackobj2_text = Text()
                    feedbackobj2_text.append('Dica: Combine dieta balanceada com exercícios aeróbicos')
                    feedbackobj2_text.append('\nUtilize alimentos com baixa quantidade de carboidratos e alta quantidade de proteínas.')
                    pfeedbackobj2 = Panel(feedbackobj2_text, border_style="cyan", expand = False,title="[bold cyan]Feedback[/bold cyan]",
                title_align="center")
                    c.print(pfeedbackobj2)
                    
            else:
                    feedbackobj3_text = Text()
                    feedbackobj3_text.append('Dica: Mantenha hábitos equilibrados e pratique atividades físicas')  
                    feedbackobj3_text.append('\nExistem diversos tipos de atividades físicas que podem te auxiliar.')
                    feedbackobj3_text.append('\nAté mesmo uma caminhada de 40/50 minutos, acelera seu metabolismo, e melhora sua saúde.')
                    pfeedbackobj3 = Panel(feedbackobj3_text, border_style="cyan", expand = False,title="[bold cyan]Feedback[/bold cyan]",
                title_align="center")
                    c.print(pfeedbackobj3)
    
            aguardar_volta()
            continue
    
        elif calcularimc_visualizarimc == '2':

            while True:
                    
                    try:
                        c.print(Panel('Digite o seu [green][u]peso[/u][/] em kg:', expand = False, border_style = 'yellow'))
                        pesoimc = float(input('>>> '))
                        if pesoimc > 350 or pesoimc <= 0:
                            c.print(Panel('Digite um peso válido.', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                            aguardar_volta()
                            continue
                    except ValueError:
                        c.print(Panel('Digite apenas números', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                        aguardar_volta()
                        continue
                    break
            
            while True:
                    
                    try:
                        c.print(Panel('Digite a sua [green][u]altura[/u][/] em m:', expand = False, border_style = 'yellow'))
                        alturaimc = float(input('>>> '))
                        if alturaimc > 2.2 or alturaimc <= 0:
                            c.print(Panel('Digite uma altura válida', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                            aguardar_volta()
                            continue
                    except ValueError:
                        c.print(Panel('Digite apenas números', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                        aguardar_volta()
                        continue
                    
                    imc = (pesoimc/alturaimc**2)
                    with c.status("[red]C[/red][magenta]a[/magenta][yellow]l[/yellow][green]c[/green]"
                        "[cyan]u[/cyan][blue]l[/blue][red]a[/red][magenta]n[/magenta]"
                        "[yellow]d[/yellow][green]o[/green]", spinner="hearts"):
                        time.sleep(2)
                    c.print(Panel(f'O IMC é {imc:.2f}', expand = False, border_style = 'cyan'))

                    if imc < 18.5:
                        status = 'Abaixo do peso'
                    elif 18.5 <= imc < 25:
                        status = 'Peso normal'
                    elif 25 <= imc < 30:
                        status = 'Sobrepeso'
                    else:
                        status = 'Obesidade'
                    c.print(Panel(f'Status: {status}', expand = False, border_style = 'cyan'))
                    aguardar_volta()
                    c.clear()
                    break
                
        elif calcularimc_visualizarimc == '3':
            with c.status("[red]S[/red][magenta]a[/magenta][yellow]i[/yellow]"
                "[green]n[/green][cyan]d[/cyan][blue]o[/blue]", spinner = 'hearts'):  
                time.sleep(2)
                c.clear()
            break
        
def calcular_taxametabolicabasal():
    """
    Calcula a tmb (Taxa metabólica basal) do usuário,
    o usuário pode escolher entre calcular sua TBM (com seus dados salvos),
    ou pode optar por calcular outra qualquer"""
    c.clear()
    global usuarios, usuario_logado 

    if usuario_logado is None:
        c.print(Panel('Faça login primeiro!', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
        aguardar_volta()  
        return

    user = usuarios[usuario_logado]

    if not user.get('dados'):
        c.print(Panel('Complete seus dados primeiro!', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
        escolher_objetivo()
        return

    while True:
        c.clear()
        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
        print(' ')
        tmb_text = Text('TAXA METABÓLICA BASAL (TMB)', justify = 'center')
        p_tmbtext = Panel(tmb_text, title="[i][cyan]TMB[/cyan][/i]",title_align="center",border_style="cyan",expand=True)
        c.print(p_tmbtext)    

        c.print(Panel('[violet]Informação:[/] Taxa Metabólica Basal (TMB) é a quantidade [red]mínima[/] de calorias que seu corpo precisa para manter funções vitais (como [chartreuse2]respiração[/], [chartreuse2]circulação[/] e [chartreuse2]temperatura[/]) em repouso completo.', expand = False, border_style = 'cyan'))

        c.print(Panel('Deseja calcular [u]sua taxa metabólica basal[/u] (1), calcular [u]outra qualquer[/u] (2), ou voltar (3)?', expand = False, border_style = 'yellow'))
        calculartmb_visualizartmb = input('>>> ').strip()

        if calculartmb_visualizartmb == '1':

            with c.status("[red]C[/red][magenta]a[/magenta][yellow]l[/yellow][green]c[/green]"
                "[cyan]u[/cyan][blue]l[/blue][red]a[/red][magenta]n[/magenta]"
                "[yellow]d[/yellow][green]o[/green]", spinner="hearts"):
                time.sleep(2)

            dados = user['dados']
            altura = dados['altura']
            peso = dados['peso']
            idade = dados['idade']
            sexo = dados['sexo']
            altura_cm = altura * 100  

            if 'sexo_escolha' in dados and dados['sexo_escolha'] in ['3', '4']:  

                if dados.get('em_transicao'):

                    if dados.get('tempo_transicao', 0) >= 12:
                        #uso de hormônios > 12 meses -> usa sexo identidade
                        sexo_uso = dados['sexo']  #sexo de identidade

                        if sexo_uso == 'm':
                            TMB = (10 * peso) + (6.25 * altura_cm) - (5 * idade) + 5
                        else:
                            TMB = (10 * peso) + (6.25 * altura_cm) - (5 * idade) - 161

                        usuarios[usuario_logado]['TMB'] = TMB
                        salvar_dadosjson()

                        c.print(Panel(f'Sua TMB é :({TMB:.2f})',expand = False, border_style = 'cyan'))
                        retornotmb1_text = Text()
                        retornotmb1_text.append('O cálculo foi feito com base no seu sexo de identidade, pois você informou que está em transição hormonal há mais de 12 meses.')
                        retornotmb1_text.append('\nApós esse tempo, a terapia hormonal tende a modificar significativamente o metabolismo, e por isso essa abordagem é mais precisa.')
                        pretornotmb1 = Panel(retornotmb1_text, expand = False, border_style = 'cyan', title = '[blue]INFO[/]')
                        c.print(pretornotmb1)
                        aguardar_volta()
                        continue

                    elif dados.get('tempo_transicao', 0) < 12:

                        tmb_m = (10 * peso) + (6.25 * altura_cm) - (5 * idade) + 5
                        tmb_f = (10 * peso) + (6.25 * altura_cm) - (5 * idade) - 161
                        TMB = (tmb_m + tmb_f) / 2
                        c.print(Panel(f'Sua TMB é: {TMB:.2f} calorias (Resultado baseado na média entre os cálculos masculino e feminino.)', expand = False, border_style = 'cyan'))
                        retornotmb2_text = Text()
                        retornotmb2_text.append('Utilizamos essa maneira, pois como você está em transição, seu corpo, fisiologicamente falando, está mudando gradualmente.')
                        retornotmb2_text.append('\nA média entre TMB masculina e feminina representa um ponto intermediário mais realista para estimar a sua necessidade calórica durante essa fase.')
                        pretornotmb2 = Panel(retornotmb2_text, expand = False, border_style = 'cyan', title = '[blue]INFO[/]')
                        c.print(pretornotmb2)
                        usuarios[usuario_logado]['TMB'] = TMB
                        salvar_dadosjson()
                        aguardar_volta()
                        continue

                else:
                    #não usa hormônios -> usa sexo biológico
                    sexo_uso = dados.get('sexo_biologico', dados['sexo'])  #se por acaso sexo_biologico for None, usa sexo identidade

                if sexo_uso == 'm':
                    TMB = (10 * peso) + (6.25 * altura_cm) - (5 * idade) + 5
                    
                else:
                    TMB = (10 * peso) + (6.25 * altura_cm) - (5 * idade) - 161

                usuarios[usuario_logado]['TMB'] = TMB
                salvar_dadosjson()
                
                c.print(Panel(f'Sua TMB é :({TMB:.2f})', expand = False, border_style = 'cyan'))
                retornotmb3_text = Text()
                retornotmb3_text.append('O cálculo foi feito com base no seu sexo biológico, pois você indicou que não faz uso de terapia hormonal.')
                retornotmb3_text.append('\nIsso é importante porque, sem o uso de hormônios, seu metabolismo segue padrões fisiológicos relacionados ao sexo biológico.')
                pretornotmb3 = Panel(retornotmb3_text, expand = False, border_style = 'cyan', title = '[blue]INFO[/]')
                c.print(pretornotmb3)
                aguardar_volta()
                continue
        
            else:

                sexo_uso = dados.get('sexo', '').lower()

                if sexo_uso == 'm':
                    TMB = (10 * peso) + (6.25 * altura_cm) - (5 * idade) + 5
                else:
                    TMB = (10 * peso) + (6.25 * altura_cm) - (5 * idade) - 161

                usuarios[usuario_logado]['TMB'] = TMB
                salvar_dadosjson()

                c.print(Panel(f'Sua TMB é :({TMB:.2f})', expand = False, border_style = 'cyan'))
                c.print(Panel('O cálculo foi feito com base no sexo informado no seu cadastro.', expand = False, border_style = 'cyan', title = '[blue]INFO[/]'))
                aguardar_volta()
                continue

        elif calculartmb_visualizartmb == '2':

            while True:
                c.clear()
                try:
                    c.print(Panel('Digite o [u][green]peso[/][/u] em quilogramas:', expand = False, border_style = 'yellow'))
                    pesoex = float(input('>>> '))
                    if pesoex > 350 or pesoex <= 0:
                        c.print(Panel('Digite um peso válido.',expand = False, border_style = 'red', title = '[b]ERRO[/b]', title_align = 'center'))
                        aguardar_volta()
                        c.clear()
                        continue
                except ValueError:
                        c.print(Panel('Digite apenas números', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                        aguardar_volta()
                        c.clear()
                        continue
                break
            
            while True:
                    
                    try:
                        c.print(Panel('Digite a [green][u]altura[/u][/] em centímetros:', expand = False, border_style = 'yellow'))
                        alturaex = float(input('>>> '))
                        if alturaex > 220 or alturaex <= 100:
                            c.print(Panel('Digite uma altura válida, em centímetros.', expand = False, border_style = 'red', title = '[b]ERRO[/b]', title_align = 'center'))
                            aguardar_volta()
                            c.clear()
                            continue
                    except ValueError:
                        c.print(Panel('Digite apenas números', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                        aguardar_volta()
                        c.clear()
                        continue
                    break
                    
            while True:

                    try:            
                        c.print(Panel('Digite a [green][u]idade:[/u][/]', expand = False, border_style = 'yellow'))
                        idadeex = int(input('>>> '))
                        if idadeex > 100 or idadeex <= 0:
                            c.print(Panel('Digite uma idade válida.', expand = False, border_style = 'red', title = '[b]ERRO[/b]', title_align = 'center'))
                            aguardar_volta()
                            c.clear()
                            continue
                    except ValueError:
                        c.print(Panel('Digite apenas números', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                        aguardar_volta()
                        c.clear()
                        continue
                    break

            while True:
                    try: 
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
                        c.print(painelidentidade)
                        
                        c.print(Panel('Digite [green][u][b]sua[/b][/u][/] opção: ', expand = False, border_style = 'yellow'))
                        sexo_opcao = input('>>> ').strip()
            
                        if sexo_opcao not in ['1', '2', '3', '4']:
                            c.print(Panel('Opção inválida! Escolha 1-4', expand = False, border_style = 'red', title = '[b]ERRO[/b]', title_align = 'center'))
                            aguardar_volta()
                            c.clear()
                            continue
                    except ValueError:
                        c.print(Panel('Digite apenas números', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                        aguardar_volta()
                        c.clear()
                        continue
                    break
            
            while True:
                    try:
                    
                        em_transicao = False
                        tempo_transicao = 0
                        
                        if sexo_opcao in ['3', '4']:
                            c.print(Panel('Você já fez uso de terapia hormonal? (s/n):', expand = False, border_style = 'yellow'))
                            resposta = input('>>> ').lower().strip()
                            if resposta not in ['s','n']:
                                c.print(Panel('Digite (s) ou (n).', expand = False, border_style = 'red', title = '[b]ERRO[/b]', title_align = 'center'))
                                aguardar_volta()
                                c.clear()
                                continue 
                    except ValueError:
                        c.print(Panel('Digite apenas números', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                        aguardar_volta()
                        c.clear()
                        continue
                    break
            
            while True:
                try:
                    em_transicao = resposta == 's'    
                    if em_transicao:
                        c.print(Panel('Há quantos meses você faz uso?', expand = False, border_style = 'yellow'))
                        tempo_transicao = int(input('>>> '))
                        if tempo_transicao <= 0:
                            c.print(Panel('Digite um valor válido.', expand = False, border_style = 'red', title = '[b]ERRO[/b]', title_align = 'center'))
                            aguardar_volta()
                            c.clear()
                            continue
                except ValueError:
                        c.print(Panel('Digite um número válido.', expand = False, border_style = 'red', title = '[b]ERRO[/b]', title_align = 'center'))
                        aguardar_volta()
                        c.clear()
                        continue
                
                tmb_m = (10 * pesoex) + (6.25 * alturaex) - (5 * idadeex) + 5
                tmb_f = (10 * pesoex) + (6.25 * alturaex) - (5 * idadeex) - 161
            
                if sexo_opcao == '1':  
                    c.clear()
                    TMB = tmb_m
                    c.print(Panel(f'Sua TMB é: {TMB:.2f}', expand = False, border_style = 'cyan'))
                    
                elif sexo_opcao == '2':  
                    c.clear()
                    TMB = tmb_f
                    c.print(Panel(f'Sua TMB é: {TMB:.2f}', expand = False, border_style = 'cyan'))
                    
                elif sexo_opcao == '3':  
                    
                    if em_transicao and tempo_transicao >= 12:
                        c.clear()
                        TMB = tmb_m  
                        c.print(Panel(f'\nSua TMB é: {TMB:.2f}', expand = False, border_style = 'cyan'))
                        c.print(Panel('✅ Cálculo feito com base no seu sexo atual, conforme sua identidade de gênero.', expand = False, border_style = 'cyan', title = '[blue]INFO[/]', title_align = 'center'))

                    elif em_transicao:
                        c.clear()
                        TMB = (tmb_m + tmb_f) / 2  
                        c.print(Panel(f'Sua TMB é: {TMB:.2f}', expand = False, border_style = 'cyan'))
                        c.print(Panel('Como sua transição é recente, usamos uma média para tornar o cálculo mais preciso.', expand = False, border_style = 'cyan', title = '[blue]INFO[/]', title_align = 'center'))

                    else:
                        c.clear()
                        TMB = tmb_f  
                        c.print(Panel(f'Sua TMB é: {TMB:.2f}', expand = False, border_style = 'cyan'))
                        c.print(Panel('Como não há uso de hormônios, o cálculo foi feito com base no sexo biológico.', expand = False, border_style = 'cyan', title = '[blue]INFO[/]', title_align = 'center'))
                        
                elif sexo_opcao == '4':  
                    
                    if em_transicao and tempo_transicao >= 12:
                        c.clear()
                        TMB = tmb_f  
                        c.print(Panel(f'Sua TMB é: {TMB:.2f}', expand = False, border_style = 'cyan'))
                        c.print(Panel('✅ Cálculo feito com base no seu sexo atual, conforme sua identidade de gênero.', expand = False, border_style = 'cyan', title = '[blue]INFO[/]', title_align = 'center'))

                    elif em_transicao:
                        c.clear()
                        TMB = (tmb_m + tmb_f) / 2  
                        c.print(Panel(f'Sua TMB é: {TMB:.2f}', expand = False, border_style = 'cyan'))
                        c.print(Panel('Como sua transição é recente, usamos uma média para tornar o cálculo mais preciso.', expand = False, border_style = 'cyan', title = '[blue]INFO[/]', title_align = 'center'))

                    else:
                        c.clear()
                        TMB = tmb_m  
                        c.print(Panel(f'Sua TMB é: {TMB:.2f}', expand = False, border_style = 'cyan'))
                        c.print(Panel('Como não há uso de hormônios, o cálculo foi feito com base no sexo biológico.', expand = False, border_style = 'cyan', title = '[blue]INFO[/]', title_align = 'center'))
                
                aguardar_volta()
                c.clear()
                break
                    
        elif calculartmb_visualizartmb == '3':
            with c.status("[red]S[/red][magenta]a[/magenta][yellow]i[/yellow]"
                "[green]n[/green][cyan]d[/cyan][blue]o[/blue]", spinner = 'hearts'):  
                time.sleep(2)
                c.clear()
            break

        else:
            c.print(Panel('Opção inválida! Digite 1, 2 ou 3.', expand = False, border_style = 'red', title = '[b]ERRO[/b]', title_align = 'center'))
            aguardar_volta()
            continue
        
def registrar_calorias():
    """
    Registra as calorias consumidas pelo usuário durante o dia,
    usuário digita suas calorias, o função salva ao lado de sua TBM,
    usuário tem a opção de "finalizar dia",
    após isso, recebe um feedback e pode verificar o histórico de consumo de acordo com o dia.
    """
    c.clear()
    global usuarios, usuario_logado

    if usuario_logado is None:
        c.print(Panel('Faça login primeiro!', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
        aguardar_volta()  
        return
    
    user = usuarios[usuario_logado]

    if 'TMB' not in user or not user.get('dados'):
        c.print(Panel('Você precisa calcular sua taxa metabólica basal primeiro!', expand = False, border_style = 'red', title = '❗AVISO❗', title_align = 'center'))
        aguardar_volta()
        if not calcular_taxametabolicabasal():  
            return  
    
    if 'historico_dias' not in user:
        user['historico_dias'] = {}

    data_atual = datetime.now().strftime('%d/%m/%Y') 

    TMB = user['TMB']
    objetivo = user['objetivo']
    
    calorias_hoje = 0

    if 'calorias_hoje' not in user:
        user['calorias_hoje'] = 0

    while True:
        c.clear()
        try:
            c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
            print(' ')
            registrodecal_text = Text()
            registrodecal_text.append('\n')
            registrodecal_text.append('REGISTRO DE CALORIAS\n', style = 'blue')
            registrodecal_text.append('\n')
            registrodecal_text.append(f'Data: {data_atual}')
            registrodecal_text.append('\n')

            registrodecal_text.append('\n1. ', style = 'red')
            registrodecal_text.append('Adicionar calorias ao seu dia\n')

            registrodecal_text.append('2. ', style = 'red')
            registrodecal_text.append('Finalizar o dia\n')

            registrodecal_text.append('3. ', style = 'red')
            registrodecal_text.append('Ver histórico\n')

            registrodecal_text.append('4. ', style = 'red')
            registrodecal_text.append('Voltar')

            pregistrodecal = Panel(registrodecal_text, border_style="cyan", expand = False,title="[bold cyan]🍽[/bold cyan]",
    title_align="center")
            c.print(pregistrodecal)

            c.print(Panel('Digite uma opção (1-4):', expand = False, border_style = 'yellow'))
            opcao = input('>>> ').strip()

            if opcao == '1':
                c.clear()
                c.print(Panel(f'Total de calorias hoje: {user["calorias_hoje"]}/{TMB:.0f}', expand = False, border_style = 'cyan'))
                c.print(Panel('Quantas calorias você consumiu em sua última refeição?', expand = False, border_style = 'yellow'))
                cal = input('>>> ')
                cal = int(cal)

                if cal <= 0:
                    c.print(Panel('Ops, este não é um valor válido. Caso queira registrar suas calorias, digite um valor válido.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                    aguardar_volta()
                    c.clear()
                    continue

                user['calorias_hoje'] += cal  #aqui, as calorias são acumuladas.
                salvar_dadosjson()
                feedbackcal_text = Text()
                feedbackcal_text.append(f'Você consumiu {cal} calorias.')
                feedbackcal_text.append(f'\nTotal hoje: {user["calorias_hoje"]}/{TMB:.0f}')
                pfeedbackcal = Panel(feedbackcal_text, expand = False, border_style = 'cyan', title = 'FEEDBACK', title_align = 'center')
                c.print(pfeedbackcal)
                aguardar_volta()
                c.clear()

            elif opcao == '2':
                    c.clear()
                    c.print(Panel('Deseja finalizar o seu dia ? Não poderá mais adicionar calorias ao dia de hoje. (s/n):', expand = False, border_style = 'yellow'))
                    es = input('>>> ').strip().lower()

                    if es == 's':
                        if data_atual not in user['historico_dias']:
                            user['historico_dias'][data_atual] = user['calorias_hoje']
                            salvar_dadosjson()
                            c.print(Panel(f'Dia finalizado com sucesso! Total salvo: {user["calorias_hoje"]} calorias', expand = False, border_style = 'cyan'))
                            user['calorias_hoje'] = 0  #zerando a contagem para o próximo dia
                            
                            diferenca = user['historico_dias'][data_atual] - TMB  # Usamos o valor salvo no histórico
                            
                            if diferenca > 0:
                                c.print(Panel(f'Você está {diferenca:.0f} calorias acima da sua TMB.', expand = False, title = 'INFO', title_align = 'center', border_style = 'cyan'))

                            elif diferenca < 0:
                                c.print(Panel(f'Você está {abs(diferenca):.0f} calorias abaixo da sua TMB.', expand = False, title = 'INFO', title_align = 'center', border_style = 'cyan'))

                            else:
                                c.print(Panel('Você consumiu exatamente sua TMB!', expand = False, title = 'INFO', title_align = 'center', border_style = 'cyan'))
                            
                            #dicas personalizadas de acordo com o objetivo do usuário.
                        
                            print('ANÁLISE DO SEU OBJETIVO')
                            
                            if objetivo == '1':  #ganho de massa
                                if diferenca > 0:
                                    analiseobj1_text = Text()
                                    analiseobj1_text.append('\n')
                                    analiseobj1_text.append('Análise do seu objetivo:', style = 'blue')
                                    analiseobj1_text.append('\n')
                                    analiseobj1_text.append('\nÓtimo! Superávit calórico ajuda no ganho de massa. MANTÉM! 😎')
                                    analiseobj1_text.append('\n💪 Alimente-se bem: priorize proteínas (frango, ovos, peixe), carboidratos complexos (arroz, batata-doce) e gorduras boas (azeite, castanhas)')
                                    analiseobj1_text.append('\n🛌 Descanse de verdade: dormir 7–9 horas por noite e ter dias de descanso são tão importantes quanto o treino e alimentação.')
                                    panaliseobj1 = Panel(analiseobj1_text, expand = False, border_style = 'cyan', title = '🤓', title_align = 'center')
                                    c.print(panaliseobj1)
                                    
                                else:
                                    analiseobj12_text = Text()
                                    analiseobj12_text.append('\n')
                                    analiseobj12_text.append('Análise do seu objetivo:', style = 'blue')
                                    analiseobj12_text.append('\n')
                                    analiseobj12_text.append('\nAtenção! Para ganhar massa, você precisa consumir mais que sua TMB.')
                                    analiseobj12_text.append('\n📅 Seja consistente: resultados vêm com treino e alimentação regulares, mantenha a disciplina.')
                                    panaliseobj12 = Panel(analiseobj12_text, expand = False, border_style = 'cyan', title = '🤓', title_align = 'center')
                                    c.print(panaliseobj12)
                                              
                            elif objetivo == '2':  #perda de peso
                                if diferenca < 0:
                                    analiseobj2_text = Text()
                                    analiseobj2_text.append('\n')
                                    analiseobj2_text.append('Análise do seu objetivo:', style = 'blue')
                                    analiseobj2_text.append('\n')
                                    analiseobj2_text.append('\nPerfeito! Déficit calórico é essencial para perda de peso. Continua assim! 👊')
                                    analiseobj2_text.append('\n🥗 Prefira alimentos naturais: invista em frutas, verduras, proteínas magras e evite ultraprocessados.')
                                    analiseobj2_text.append('\n🚶 Mexa-se regularmente: além da dieta, exercícios ajudam a acelerar o metabolismo e manter a massa magra.')
                                    panaliseobj2 = Panel(analiseobj2_text, expand = False, border_style = 'cyan', title = '🤓', title_align = 'center')
                                    c.print(panaliseobj2)

                                else:
                                    analiseobj22_text = Text()
                                    analiseobj22_text.append('\n')
                                    analiseobj22_text.append('Análise do seu objetivo:', style = 'blue')
                                    analiseobj22_text.append('\n')
                                    analiseobj22_text.append('\nCuidado! Para perder peso, você precisa consumir menos que sua TMB.')
                                    analiseobj22_text.append('\n🧐 Reavalie a alimentação: às vezes, pequenas “fugas” na dieta ou subestimativa das calorias podem impedir o progresso.')
                                    analiseobj22_text.append('\n⏳ Tenha paciência: perda de peso nem sempre é linear, o corpo pode demorar para responder — persistência é chave.')
                                    panaliseobj22 = Panel(analiseobj22_text, expand = False, border_style = 'cyan', title = '🤓', title_align = 'center')
                                    c.print(panaliseobj22)

                            else:  
                                if abs(diferenca) < (TMB * 0.1):  
                                    analiseobj3_text = Text()
                                    analiseobj3_text.append('\n')
                                    analiseobj3_text.append('Análise do seu objetivo:', style = 'blue')
                                    analiseobj3_text.append('\n')
                                    analiseobj3_text.append('\nExcelente! Você está mantendo um bom equilíbrio. ✍')
                                    analiseobj3_text.append('\n🔄 Mantenha a rotina saudável: hábitos consistentes geram resultados duradouros, então não deixe a disciplina cair.')
                                    panaliseobj3 = Panel(analiseobj3_text, expand = False, border_style = 'cyan', title = '🤓', title_align = 'center')
                                    c.print(panaliseobj3)

                                else:
                                    analiseobj32_text = Text()
                                    analiseobj32_text.append('\n')
                                    analiseobj32_text.append('Análise do seu objetivo:', style = 'blue')
                                    analiseobj32_text.append('\n')
                                    analiseobj32_text.append('\nPara manutenção de sua sáude, tente ficar próximo da sua TMB.')
                                    analiseobj32_text.append('\n📅 Faça exames periódicos: prevenção é sempre o melhor remédio, mantenha suas consultas em dia.')
                                    analiseobj32_text.append('\n🚭 Evite hábitos nocivos: reduza ou elimine álcool, cigarro e outras substâncias que prejudicam a saúde.')
                                    panaliseobj32 = Panel(analiseobj32_text, expand = False, border_style = 'cyan', title = '🤓', title_align = 'center')
                                    c.print(panaliseobj32)

                        else:
                            c.print(Panel('Você já finalizou o dia hoje!', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                        aguardar_volta()
                        c.clear()

                    elif es == 'n':
                        aguardar_volta()
                        c.clear()

                    else:
                        c.print(Panel('Digite (s) ou (n).', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                        aguardar_volta()
                        c.clear()
                        continue

            elif opcao == '3':
                c.clear()
                c.print(Panel('📅 HISTÓRICO DE CONSUMO:', expand = False, border_style = 'cyan'))

                if not user['historico_dias']:
                    c.print(Panel('Nenhum registro encontrado.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))

                else:
                    for data, total in user['historico_dias'].items():
                        c.print(Panel(f'{data}: {total} calorias', expand = False, border_style = 'cyan'))

                aguardar_volta()
            elif opcao == '4':
                with c.status("[red]S[/red][magenta]a[/magenta][yellow]i[/yellow]"
                    "[green]n[/green][cyan]d[/cyan][blue]o[/blue]", spinner = 'hearts'):  
                    time.sleep(2)
                    c.clear()
                break

            else:
                c.print(Panel('Opção inválida!', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                aguardar_volta()
                c.clear()

        except:
            c.print(Panel('Digite apenas números.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
            aguardar_volta()
            c.clear()
        
def menu_logado():
    """
    Menu onde o usuário tem acesso as funcionalidades do programa,
    só é possível ter acesso a esse menu após o login.
    """
    c.clear()
    global usuario_logado, usuarios 

    while True:
        c.clear()
        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
        print(' ')

        nome = usuarios[usuario_logado]["nome"]

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
        parte1.append("\n[1] Ver perfil completo\n", style="cyan")
        parte1.append("[2] Calcular IMC\n", style="cyan")
        parte1.append("[3] Calcular TMB\n", style="cyan")
        parte1.append("[4] Registro de calorias", style="cyan")
        painel1 = Panel(parte1, title="Vital", border_style="cyan", width=38)

        parte2 = Text()
        parte2.append('\n')
        parte2.append('No VitalTrack, o foco é você.')
        parte2.append('\n')
        parte2.append("\n[5] Atualizar perfil\n", style="cyan")
        parte2.append("[6] Atualizar objetivo/dados\n", style="cyan")
        parte2.append("[7] Deslogar\n", style="cyan")
        parte2.append("[8] Deletar conta", style="red")
        painel2 = Panel(parte2, title="Track", border_style="cyan", width=38)

        inspiracao = Panel(Text(mensagem, justify="center", style="magenta"), title="Seja bem vindo(a)!", border_style="magenta", width=80)

        footer = Panel(Text("Digite a opção desejada.", justify="center", style="yellow"), width=80, style="grey37")

        c.print(Align.center(header))
        c.print(Align.center(Columns([painel1, painel2], expand=False)))
        c.print(Align.center(inspiracao))
        c.print(Align.center(footer))
        
        opcao = input('>>> ').strip()
        
        if opcao == '1':
            with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
                "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner = 'hearts'):  
                time.sleep(2)
            c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
            print(' ')
            verpefil_text = Text()
            verpefil_text.append('\n')
            verpefil_text.append('SEU PERFIL', style = 'blue')
            verpefil_text.append('\n')
            verpefil_text.append(f'\nNome: {usuarios[usuario_logado]["nome"]}')
            verpefil_text.append(f'\nEmail: {usuario_logado}')
        
            if usuarios[usuario_logado]["dados"]:
                dados = usuarios[usuario_logado]["dados"]
                verpefil_text.append(f'\nObjetivo: {["Ganho de massa", "Perda de peso", "Manutenção"][int(dados["objetivo"])-1]}')
                verpefil_text.append(f'\nIdade: {dados["idade"]} anos')
                verpefil_text.append(f'\nPeso: {dados["peso"]} kg')
                verpefil_text.append(f'\nAltura: {dados["altura"]} m')
                
                pverperfil = Panel(verpefil_text, border_style="cyan", expand = False,title="[bold cyan]Seu perfil[/bold cyan]",
    title_align="center")
                
                sexo_escolha = dados.get('sexo_escolha', None)

                if sexo_escolha in ['1', '3']:  # homem cis ou homem trans
                    sexo_exibicao = 'Masculino'

                elif sexo_escolha in ['2', '4']:  # mulher cis ou mulher trans
                    sexo_exibicao = 'Feminino'

                else:
                    sexo_exibicao = 'Não informado'
            verpefil_text.append(f'\nSexo: {sexo_exibicao}')        
            c.print(pverperfil)    
            aguardar_volta()
            with c.status("[red]S[/red][magenta]a[/magenta][yellow]i[/yellow]"
                "[green]n[/green][cyan]d[/cyan][blue]o[/blue]", spinner = 'hearts'):  
                time.sleep(2)
                c.clear()

        elif opcao == '2':
            with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
                "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner = 'hearts'):  
                time.sleep(2)
            calcular_imc()

        elif opcao == '3':
            with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
                "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner = 'hearts'):  
                time.sleep(2)
            calcular_taxametabolicabasal()

        elif opcao == '4':
            with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
                "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner = 'hearts'):  
                time.sleep(2)
            registrar_calorias()

        elif opcao == '5':
            with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
                "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner = 'hearts'):  
                time.sleep(2)
            atualizar_usuario()

        elif opcao == '6':
            with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
                 "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner = 'hearts'):  
                time.sleep(2)
            print('\nAtualizando dados...')
            atualizar_dados()

        elif opcao == '7':
            with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
                "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner = 'hearts'):  
                time.sleep(2)

            while True:

                c.print(Panel('Deseja mesmo deslogar? (s/n)', expand = False, border_style = 'yellow'))
                deslog = input('>>> ').strip()

                if deslog == 's':
                    usuario_logado = None
                    c.print(Panel('[b][u][red]Deslogado[/][/u][/b] com sucesso!', expand = False, border_style = 'cyan', style = 'cyan'))
                    aguardar_volta()
                    return
                
                elif deslog == 'n':
                    c.print(Panel('Você permanece [green][u][b]logado.[/b][/u][/]', expand = False, border_style = 'cyan', style = 'cyan')) 
                    aguardar_volta()
                    c.clear()
                    break
                
                else:
                    c.print(Panel('Digite "s" ou "n".', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                    aguardar_volta()
                   
        elif opcao == '8':
            with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
                "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner = 'hearts'):  
                time.sleep(2)
            if deletar_usuario():
                aguardar_volta()
                c.clear()
                return
        else:
            c.print(Panel('Opção inválida! Digite um número de 1 a 8.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
            aguardar_volta()
            c.clear()

if __name__ == "__main__":
    menu_principal() 
