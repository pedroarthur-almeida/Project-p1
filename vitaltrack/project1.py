usuarios = {} #criando um dicionário vazio para armazenar os dados. é como um banco de dados em formato de dicionário.
usuario_logado = None #variavel que guarda quem está logado no momento.
from datetime import datetime #importando biblioteca para utilizar datas.
import os
import platform

def limpar_tela():

        if platform.system() == 'Windows':
            os.system('cls')

        else:
            os.system('clear')
        
def aguardar_volta():
    """Pausa a execução do programa até que o usuário tecle "enter".""" 
    input('\nPressione "Enter" para voltar...')
    limpar_tela()

def cadastro_de_usuario(): #criando a função de cadastro.
    """Cadastra o usuário e salva seus dados em um dicionário,
       em que a chave é o email.
    """
    limpar_tela()
    global usuarios,usuario_logado #garantindo o acesso as variáveis globais, para poder adicionar os dados e etc.
    print('\n(Cadastro)')

    while True:
        email = input('\nDigite o seu email: ').strip().lower() #.strip() para ignorar espaços e .lower() para manter as letras minusculas.
        #verificando se o email está nos padrões corretos
        if email in usuarios:
            print('|Este email já foi cadastrado!|')
            print('|Insira um email ainda não cadastrado.|')
            aguardar_volta()
            continue #para pedir o email novamente caso ocorra o erro.
        
        elif '@' not in email or '.com' not in email:
            print('\n|O email precisa estar em um formato válido.|')
            print('|O email precisa ter ".com" e "@".|')
            aguardar_volta()
            continue #para pedir o email novamente.

        dominios_validos = ['gmail.com', 'outlook.com', 'hotmail.com', 'yahoo.com', 'icloud.com'] #criando essa lista pra salvar os dominios validos.
        
        if not any(email.endswith(dominio) for dominio in dominios_validos): #o comando endswith vai verficiar se o email termina com o domínio de forma correta, para evitar falsos positivos e emails no formato errado, ex: arthur@xcsgmail.com
            print('\n|Domínio inválido! Use: Gmail, Outlook, Hotmail, Yahoo ou iCloud.|')
            continue

        break
    
    while True:
        senha = input('Digite sua senha(mínimo 6 caracteres): ')

        #verificando se a senha está nos padrões corretos.
        if len(senha) < 6:
            print('\n|Senha muito curta, a sua senha precisa ter, no mínimo, 6 caracteres.|')
            aguardar_volta()
            continue #para continuar pedindo a senha caso ocorra o erro
            
        confirmaçao_de_senha = input('\nConfirme sua senha: ').strip()

        if senha != confirmaçao_de_senha:
            print('\n|As senhas não coinscidem.|')
            aguardar_volta()
            continue #para continuar pedindo a senha caso ocorra o erro
        else:
            break
    
    nome = input('\nDigite seu nome: (Será seu nome de usuário) ').strip()
    
     # Criando o usuário
    usuarios[email] = {
        'senha': senha,
        'nome': nome,
        'objetivo': None,
        'dados': None,
        'calorias_hoje': 0,          
        'historico_dias': {} 
    }

    usuario_logado = email
    # chamando a escolha do objetivo, antes de ir para o menu logado.
    print('\nAgora vamos definir o seu objetivo! 👇')
    escolher_objetivo()
    
    print('\nUsuário Cadastrado com sucesso! ✔')

    print('Seja bem vindo ao VITALTRACK! 😉')
    
    return True

#Essa é a parte de escolha de objetivo, ocorre após o cadastro.
def escolher_objetivo():
    """
    Escolha de objetivo (parte do cadastro),
    Usuário escolhe seu objetivo e fornece seus dados,
    armazena os dados do usuário em um outro dicionário "dados".
    """
    limpar_tela()
    global usuario_logado, usuarios

    while True:

        print('\n(Qual é o seu objetivo? 🤔)')
        print('\nAntes de começarmos, é importante entender qual é o seu foco atual em relação à sua saúde. o VitalTrack foi pensado para se adaptar as suas necesssidades e objetivos. ✍')
        print('É como uma parceria, entendeu? 👊🤝')
        print('\nVocê pode escolher entre três caminhos:')
        print('\n1. Ganho de massa (Foco em ganho de peso e aumento da massa muscular.🏋️ 💪)')
        print('2. Perda de peso (ideal para quem deseja reduzir o percentual de gordura corporal de forma saudável.)🏃')
        print('3. Manutenção da saúde (Para quem quer manter o equilíbrio, hábitos saudáveis e o bem-estar geral.)❤')
        print(' ')

        objetivo = input('Agora é com você! 🕺 Escolha um objetivo (1-3): ')

        if objetivo not in ['1', '2', '3']:
            print('\n|Opção inválida! Escolha 1, 2 ou 3.|')
            aguardar_volta()
            continue 

        # Mensagem personalizada de acordo com o objetivo que o usuário escolher.
        objetivos = {
            '1': 'GANHO DE MASSA',
            '2': 'PERDA DE PESO', 
            '3': 'MANUTENÇÃO DA SAÚDE' }
        limpar_tela()
        print('\n-----------------------------')
        print(f'Você escolheu: {objetivos[objetivo]}')
        print('-----------------------------')
        if objetivo == '1':
            print('\nBoa! Você deseja aumentar sua massa corporal, tô contigo nessa! 😎 💪')
            print('Uma dica: é importante que você consuma uma quantidade de calorias maior que a sua TMB.')
            print('\nNão sabe o que é TMB? não se preocupe! mais na frente eu te explico. 😉')
        elif objetivo == '2':
            print('\nVocê escolheu perder peso, que legal! Tamo junto nessa jornada. 👊')
            print('Com foco e disciplina, qualquer objetivo pode se concretizar, vai dar tudo certo!')
            print('\nDica: é importante que você consuma uma quantidade de calorias inferior a sua TMB.')
            print('Não sabe o que é TMB? não se preocupe! mais na frente eu te explico. 😉')
        else:
            print('\nÉ isso ai! Você optou por manter-se saudável, conte comigo pra te auxiliar! ✋')
            print('É extremamente importante acompanhar a própria saúde, isso vale para pessoas de qualquer faixa etária. 🧒👨👴')
            print('\nDica: mantenha seu consumo de calorias em um valor próximo a sua TMB.')
            print('Não sabe o que é TMB? não se preocupe! mais na frente eu te explico. 😉')

        print('\nBeleza! Agora vamos coletar algumas informações sobre você.')

        while True:

            try:

                print('\nPara que os cálculos de saúde e metabolismo sejam mais precisos, gostaríamos de saber sua identidade de gênero. Essa informação nos ajuda a oferecer resultados mais adequados para você.')

                print('\nQual é a sua identidade de gênero?')
            
                print('\n1. Homem Cis')
                print('2. Mulher Cis')
                print('3. Homem Trans')
                print('4. Mulher Trans')

                sexo_escolha = input('\nEscolha a sua opção (1-4): ').strip()

                if sexo_escolha not in ['1','2','3','4']:
                    print('\nEscolha uma opção disponível (1-4).')
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

                        print('\nPara adaptar melhor os cálculos às mudanças metabólicas:')
                        resposta = input('Você já fez uso de terapia hormonal? (s/n): ').lower().strip()
                        if resposta not in ['s','n']:
                            print('\nDigite (s) ou (n).')
                            aguardar_volta()
                            continue 
                        em_transicao = resposta == 's'
                        break

                    if em_transicao:
                            
                        while True:
                        
                            try:

                                tempo_transicao = int(input('\nHá quanto tempo (em meses) você faz uso de hormônios?: '))
                                if tempo_transicao <= 0:
                                    print('\n|Digite um valor válido.|')
                                    aguardar_volta()
                                    continue
                                break

                            except ValueError:
                                print('\n|Digite somente números.|')
                                aguardar_volta()
                                continue

                sexo = 'm' if sexo_escolha == '3' else 'f'
                sexo_biologico = 'f' if sexo_escolha == '3' else 'm'

            except ValueError:
                print('\n|Valores inválidos! Digite números válidos.|')        

            while True:
                try:

                    idade = int(input('\nIdade: ').strip())
                    peso = float(input('Peso (kg): ').strip())
                    altura = float(input('Altura (m): ').strip())
                    limpar_tela()
                    

                    if idade <= 0 or peso <= 0 or altura <= 0:
                        print('\n|Valores inválidos! Digite números positivos.|')
                        continue
                    if idade > 100 or peso > 350 or altura > 2.5:
                        print('\n|Valores fora do intervalo estimado.|')
                        continue

                except ValueError:
                    print('\n|Valores inválidos! Digite dados válidos para cada solicitação.|')
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
                return True #vai retornar verdadeiro para a funçao que chamou essa, no caso, a de cadastro. assim a de cadastro entrará na condição de que foi concluido e retornará true para outra funçao que chamou ela, no caso, a menu principal.

def fazer_login(): #criando a função de login.
    """
    Função responsável pelo login do usuário,
    O usuário digita seu email e sua senha,
    caso estejam corretos, libera o acesso ao "menu logado".
    """
    limpar_tela()
  
    global usuario_logado, usuarios #declarando ambos como globais, para que possam ser utilizados e modificados.
    print('\n-----Login-----')
    email = input('Digite o seu email cadastrado: ').lower().strip()
    senha = input('Digite sua senha: ')

  #vamos verificar se o cadastro existe.
    if email not in usuarios:
        print('|Email não cadastrado.|')
        return False
    elif usuarios[email]["senha"] != senha:
        print('|Senha incorreta.|')
        return False
    else:
        usuario_logado = email #chave do dicionário principal.
        print(f'Bem-vindo(a), {usuarios[email]["nome"]}!')
        return True

def atualizar_usuario(): #criando a função atualizar (parte do crud)
    """
    Atualiza os dados do usuário,
    o usuário escolhe o que deseja atualizar,
    é permitido atualizar email, nome ou senha,
    os novos dados são salvos após mudanças.
    """
    limpar_tela()
    global usuario_logado, usuarios
    if usuario_logado is None: #caso o usuario não esteja logado.
        print('|Faça login primeiro!|')
        return
    
    while True:

        print('\n-----ATUALIZAR PERFIL-----')
        print(f'1.Alterar nome. (nome atual:{usuarios[usuario_logado]['nome']})')
        print('2.Alterar senha.')
        print(f'3.Alterar EMAIL. (email atual:{usuario_logado})')
        print('4.Voltar ao MENU anterior.')

        opçao3 = input('O que deseja atualizar? (1-4): ')

        if opçao3 == '1':
            novo_nome = input(f'Digite o novo nome (atual: {usuarios[usuario_logado]['nome']}):').strip()
            if novo_nome:
                usuarios[usuario_logado]["nome"] = novo_nome
                print('Nome atualizado com sucesso!')

        elif opçao3 == '2':
            nova_senha = input('Digite uma nova senha (mínimo 6 caracteres): ')
            if len(nova_senha) >=6:
                usuarios[usuario_logado]["senha"] = nova_senha
                print('Senha atualizada com sucesso!')

            else:
                print('|Senha muito curta.|') 

        elif opçao3 == '3':
            novo_email = input('Digite seu novo emai (atual: {usuario_logado}): ').strip().lower()  
            if not novo_email:
                continue

            if novo_email == usuario_logado:
                print('|O novo email é igual ao atual.|')   

            elif '@' not in novo_email or '.com' not in novo_email:
                print("|Formato inválido (use '@' e '.com').|")

            elif novo_email in usuarios:
                print('|Email já cadastrado.|') 

            else:
                # Transferir todos os dados para o novo email digitado pelo usuário
                usuarios[novo_email] = usuarios[usuario_logado]
                del usuarios[usuario_logado]
                usuario_logado = novo_email
                print("Email atualizado com sucesso!") 

        elif opçao3 == '4':
            break

        else:
            print('|Opção inválida. Digite uma opção disponível (1-4)|')

def atualizar_dados():
    limpar_tela()
    global usuario_logado, usuarios

    if usuario_logado is None:
        print('\n|Faça login primeiro!|')
        aguardar_volta()
        return
    
    user = usuarios[usuario_logado]
    
    if not user.get('dados'):
        print('\n|Complete seus dados primeiro!|')
        escolher_objetivo()
        return
    
    while True:

        try:

            print('\nATUALIZAR DADOS PESSOAIS')
            dados = user['dados']
            objetivo_atual = user['objetivo']

            objetivos = {
            '1': 'GANHO DE MASSA',
            '2': 'PERDA DE PESO', 
            '3': 'MANUTENÇÃO DA SAÚDE' }

            print(f'\nDados atuais:')
            print(f'\n1. Idade: {dados["idade"]} anos')
            print(f'2. Peso: {dados["peso"]} kg')
            print(f'3. Altura: {dados["altura"]} m')
            print(f'4. Objetivo: {objetivos[objetivo_atual]}')
            print('5. Voltar')
            
            campo = input('\nQual dado deseja alterar? (1-5): ').strip()
            
            if campo == '1':
                nova_idade = int(input('\nNova idade: '))
                if 0 < nova_idade <= 100:
                    dados['idade'] = nova_idade
                    print('Idade atualizada com sucesso!')

                else:
                    print('Idade deve ser entre 1 e 100 anos')
                aguardar_volta()
                
            elif campo == '2':
                novo_peso = float(input('\nNovo peso (kg): '))
                if 0 < novo_peso <= 350:
                    dados['peso'] = novo_peso
                    print('Peso atualizado com sucesso!')

                else:
                    print('Peso deve ser entre 0.1 e 350 kg')
                aguardar_volta()
                
            elif campo == '3':
                nova_altura = float(input('\nNova altura (m): '))
                if 0 < nova_altura <= 2.5:
                    dados['altura'] = nova_altura
                    print('Altura atualizada com sucesso!')

                else:
                    print('Altura deve ser entre 0.1 e 2.5 metros')
                aguardar_volta()
                
            elif campo == '4':
                
                print('\nObjetivos disponíveis:')
                print('1. Ganho de massa')
                print('2. Perda de peso')
                print('3. Manutenção da saúde')
                
                novo_objetivo = input('\nNovo objetivo (1-3): ').strip()
                if novo_objetivo in ['1', '2', '3']:
                    user['objetivo'] = novo_objetivo
                    print(f'\nObjetivo atualizado para: {objetivos[novo_objetivo]}')

                else:
                    print('\n|Opção inválida!|')
                aguardar_volta()
                
            elif campo == '5':
                aguardar_volta()
                return

            else:
                print('Opção inválida! digite uma opção disponível.')
                aguardar_volta()
                
        except ValueError:
            print('\n|Valor inválido! Digite números válidos.|')
            aguardar_volta()

def deletar_usuario():
    """
    Deleta o usuário cadastrado,
    apaga todos os dados inseridos e salvos.
    """
    limpar_tela()
    global usuario_logado,usuarios

    if usuario_logado is None:
        print('|Faça login primeiro.|')
        return
    confirmaçao = input('Tem certeza que deseja deletar sua conta? 😕 (s/n): ').lower()

    if confirmaçao == 's':
        del usuarios[usuario_logado]
        usuario_logado = None
        print('Conta deletada com sucesso. Até logo...')
        return True
    return False

def menu_principal():
    """
    Menu inicial,
    é exibido logo após iniciar o programa,
    abre ao usuário as opções de cadastro e login.
    """
    
    global usuario_logado #declarando novamente como global
 
    while True:
        limpar_tela()
        print('<<<VITALTRACK>>>')
        
        print('\n(MENU INICIAL)\n') 
        print('1.Cadastro')
        print('2.Fazer login')
        print('3.Sair')

        opçao1 = input('Digite sua opção: ')

        if opçao1 == '1':
            if cadastro_de_usuario():
                menu_logado()    
        elif opçao1 == '2':
            if fazer_login():
                menu_logado()
        elif opçao1 == '3':
            print('Saindo... até logo! 👋')
            break
        else:
            print('|Opção inválida! Digite uma opção presente no MENU.|')

def calcular_imc():
    """
    Calcula o IMC (índice de massa corporal) do usuário,
    O usuário pode calcular o seu próprio IMC (com seus dados salvos),
    ou pode optar por calcular outro IMC qualquer,
    a função retorna o status após calcular o valor do imc, em ambos os casos.
    """
    limpar_tela()
    global usuarios,usuario_logado

    if usuario_logado is None:
        print('|Faça login primeiro!|')
        aguardar_volta()
        return
    
    user = usuarios[usuario_logado]
    if not user.get('dados'):
        print('|Complete seus dados primeiro!|')
        escolher_objetivo()
        return
    
    dados = user['dados']
    imc = dados['peso'] / (dados['altura'] ** 2)

    while True:
        print('\nCALCULADORA DE IMC (ÍNDICE DE MASSA CORPORAL)')
        calcularimc_visualizarimc = input('\nDeseja calcular o seu IMC (1), calcular outro qualquer (2), ou voltar (3)? ')

        if calcularimc_visualizarimc == '1':
            print('\n-----------------------------')
            print(f'------ SEU IMC: {imc:.2f} -------')
            print('-----------------------------')

        # Classificação de acordo com o IMC do usuário
            if imc < 18.5:
                status = 'Abaixo do peso'
            elif 18.5 <= imc < 25:
                status = 'Peso normal'
            elif 25 <= imc < 30:
                status = 'Sobrepeso'
            else:
                status = 'Obesidade'
    
            print(f'\nStatus: {status}')

            # Dicas conforme objetivo do usuário
            objetivo = user['objetivo']
            if objetivo == '1':  # Ganho de massa
                    print('Dica: Aumente a ingestão de proteínas e calorias saudáveis')
                    print('Além disso, Foque em treinos de força e superávit calórico')
                    print('Consuma alimentos com alta quantidade de proteínas e carboidratos.')
            elif objetivo == '2':  # Perda de peso
                    print('Dica: Combine dieta balanceada com exercícios aeróbicos')
                    print('Utilize alimentos com baixa quantidade de carboidratos e alta quantidade de proteínas.')
            else:  # Manutenção
                    print('Dica: Mantenha hábitos equilibrados e pratique atividades físicas')
                    print('Existem diversos tipos de atividades físicas que podem te auxiliar.')
                    print('Até mesmo uma caminhada de 40/50 minutos, acelera seu metabolismo, e melhora sua saúde.')
    
            aguardar_volta()
            break
    #função auxiliar para incorporar em outras funções e voltar ao menu.

        elif calcularimc_visualizarimc == '2':

            while True:
                    
                    try:
                        pesoimc = float(input('\nDigite o seu peso em kg: '))
                        if pesoimc > 350 or pesoimc <= 0:
                            print('\nDigite um peso válido.')
                            continue
                    except ValueError:
                        print('\nDigite apenas números')
                        continue
                    break
            
            while True:
                    
                    try:

                        alturaimc = float(input('Digite a sua altura em m: '))
                        if alturaimc > 2.2 or alturaimc <= 0:
                            print('\nDigite uma altura válida')
                            continue
                    except ValueError:
                        print('\nDigite apenas números')
                        continue
                    
                        
                    imc = (pesoimc/alturaimc**2)
                    print(f'\nO IMC é {imc:.2f}')

                    if imc < 18.5:
                        status = 'Abaixo do peso'
                    elif 18.5 <= imc < 25:
                        status = 'Peso normal'
                    elif 25 <= imc < 30:
                        status = 'Sobrepeso'
                    else:
                        status = 'Obesidade'
                    print(f'Status: {status}')
                    aguardar_volta()
                    break
                
        elif calcularimc_visualizarimc == '3':
            aguardar_volta()
            break

#função para calcular a taxa metabólica basal.
def calcular_taxametabolicabasal():
    """
    Calcula a tmb (Taxa metabólica basal) do usuário,
    o usuário pode escolher entre calcular sua TBM (com seus dados salvos),
    ou pode optar por calcular outra qualquer"""
    limpar_tela()
    global usuarios, usuario_logado

    #verifica se o usuário está logado.
    if usuario_logado is None:
        print('|Faça login primeiro!|')
        aguardar_volta() #função que retorna ao menu. 
        return

    user = usuarios[usuario_logado]

    if not user.get('dados'):
        print('|Complete seus dados primeiro!|')
        escolher_objetivo()
        return

    while True:
            
            print('\n-----TAXA METABÓLICA BASAL (TMB)-----')

            print('\nInformação: Taxa Metabólica Basal (TMB) é a quantidade mínima de calorias que seu corpo precisa para manter funções vitais (como respiração, circulação e temperatura) em repouso completo.')

            calculartmb_visualizartmb = input('\nDeseja calcular sua taxa metabólica basal (1), calcular outra qualquer (2), ou voltar (3)? ').strip()

            if calculartmb_visualizartmb == '1':

                #calculando a TMB com os dados do usuário.

                dados = user['dados']
                altura = dados['altura']
                peso = dados['peso']
                idade = dados['idade']
                sexo = dados['sexo']
                altura_cm = altura * 100  #transforma altura de metros para cm, pois é necessário que a altura esteja em cm para realizar o cálculo da TMB.

                
                #para pessoas trans.
                if 'sexo_escolha' in dados and dados['sexo_escolha'] in ['3', '4']:  

                    if dados.get('em_transicao') and dados.get('tempo_transicao', 0) >= 12:
                        #usa sexo de identidade após 12+ meses de TH
                        sexo = dados['sexo']

                    elif dados.get('em_transicao'):
                        #calcula média se estiver em TH há menos de 12 meses
                        tmb_m = (10 * peso) + (6.25 * altura_cm) - (5 * idade) + 5
                        tmb_f = (10 * peso) + (6.25 * altura_cm) - (5 * idade) - 161
                        TMB = (tmb_m + tmb_f) / 2
                        print(f'\nSua TMB é: {TMB:.2f} calorias (Resultado baseado na média entre os cálculos masculino e feminino.)')
                        print('Utilizamos essa maneira, pois como você está em transição, seu corpo, fisiologicamente falando, está mudando gradualmente.')
                        print('A média entre TMB masculina e feminina representa um ponto intermediário mais realista para estimar a sua necessidade calórica durante essa fase.')
                        usuarios[usuario_logado]['TMB'] = TMB
                        aguardar_volta()
                        continue

                if sexo == 'm':
                    TMB = (10 * peso) + (6.25 * altura_cm) - (5 * idade) + 5
                    
                else:
                    TMB = (10 * peso) + (6.25 * altura_cm) - (5 * idade) - 161
                
                usuarios[usuario_logado]['TMB'] = TMB
                
                print('\n-----------------------------')
                print(f'-----Sua TMB é :({TMB:.2f})----')
                print('-----------------------------')
                aguardar_volta()
                break

            elif calculartmb_visualizartmb == '2':

                while True:

                    try:
                        pesoex = float(input('\nDigite o peso (em kg): '))
                        if pesoex > 350:
                            print('Digite um peso válido.')
                            continue
                        

                        alturaex = float(input('\nDigite a altura (em cm): '))
                        if alturaex > 220:
                            print('\nDigite uma altura válida, em centímetros.')
                            continue
                        
            
                        idadeex = int(input('\nDigite a idade: '))
                        if idadeex > 100:
                            print('\nDigite uma idade válida.')
                            continue
                    
                        print('\nQual é a sua identidade de gênero?')
                        print('\n1. Homem Cis')
                        print('2. Mulher Cis')
                        print('3. Homem Trans')
                        print('4. Mulher Trans')
            
                        sexo_opcao = input('\nEscolha a sua opção: (1-4): ').strip()
            
                        if sexo_opcao not in ['1', '2', '3', '4']:
                            print('\n|Opção inválida! Escolha 1-4|')
                            continue
                        
                        em_transicao = False
                        tempo_transicao = 0
                        
                        if sexo_opcao in ['3', '4']:
                            resposta = input('\nVocê já fez uso de terapia hormonal? (s/n): ').lower().strip()
                            if resposta not in ['s','n']:
                                print('\nDigite (s) ou (n).')
                                aguardar_volta()
                                continue 
                            em_transicao = resposta == 's'
                        
                            if em_transicao:

                                while True:

                                    try:

                                        tempo_transicao = int(input('\nHá quantos meses você faz uso? '))
                                        if tempo_transicao < 0:
                                            print('\n|Digite um valor válido.|')
                                            continue
                                        break
                                    except ValueError:
                                        print('\n|Digite um número válido.|')
                        
                        tmb_m = (10 * pesoex) + (6.25 * alturaex) - (5 * idadeex) + 5
                        tmb_f = (10 * pesoex) + (6.25 * alturaex) - (5 * idadeex) - 161
                    
                        if sexo_opcao == '1':  

                            TMB = tmb_m
                            print(f'\nSua TMB é: {TMB:.2f}')
                            
                        elif sexo_opcao == '2':  

                            TMB = tmb_f
                            print(f'\nSua TMB é: {TMB:.2f}')
                            
                        elif sexo_opcao == '3':  

                            if em_transicao and tempo_transicao >= 12:
                                TMB = tmb_m  
                                print(f'\nSua TMB é: {TMB:.2f}')
                                print('✅ Cálculo feito com base no seu sexo atual, conforme sua identidade de gênero.')

                            elif em_transicao:
                                TMB = (tmb_m + tmb_f) / 2  
                                print(f'\nSua TMB é: {TMB:.2f}')
                                print('Como sua transição é recente, usamos uma média para tornar o cálculo mais preciso.')

                            else:
                                TMB = tmb_f  
                                print(f'\nSua TMB é: {TMB:.2f}')
                                print('Como não há uso de hormônios, o cálculo foi feito com base no sexo biológico.')
                                
                        elif sexo_opcao == '4':  

                            if em_transicao and tempo_transicao >= 12:
                                TMB = tmb_f  
                                print(f'\nSua TMB é: {TMB:.2f}')
                                print('✅ Cálculo feito com base no seu sexo atual, conforme sua identidade de gênero.')

                            elif em_transicao:
                                TMB = (tmb_m + tmb_f) / 2  
                                print(f'\nSua TMB é: {TMB:.2f}')
                                print('Como sua transição é recente, usamos uma média para tornar o cálculo mais preciso.')

                            else:
                                TMB = tmb_m  
                                print(f'\nSua TMB é: {TMB:.2f}')
                                print('Como não há uso de hormônios, o cálculo foi feito com base no sexo biológico.')
                        
                        aguardar_volta()
                        break
                        
                    except ValueError:
                        print('\n|Valor inválido! Digite números válidos.|')
                    break

            elif calculartmb_visualizartmb == '3':
                aguardar_volta()
                break

            else:
                print('\n|Opção inválida! Digite 1, 2 ou 3.|')
                continue

def registrar_calorias():
    """
    Registra as calorias consumidas pelo usuário durante o dia,
    usuário digita suas calorias, o função salva ao lado de sua TBM,
    usuário tem a opção de "finalizar dia",
    após isso, recebe um feedback e pode verificar o histórico de consumo de acordo com o dia.
    """
    limpar_tela()
    global usuarios, usuario_logado

    if usuario_logado is None:
        print('|Faça login primeiro!|')
        aguardar_volta() #função que retorna ao menu. 
        return
    
    user = usuarios[usuario_logado]

    if 'TMB' not in user:
        print('\n|Você precisa calcular sua taxa metabólica basal primeiro!|')
        calcular_taxametabolicabasal()
    
    if 'historico_dias' not in user:
        user['historico_dias'] = {}

    data_atual = datetime.now().strftime('%d/%m/%Y') #pegando a data atual.

    TMB = user['TMB']
    objetivo = user['objetivo']
    
    calorias_hoje = 0

    if 'calorias_hoje' not in user:
        user['calorias_hoje'] = 0

    print('\n-----REGISTRO DE CALORIAS-----')
    print(f'Data: {data_atual}')

    while True:

        try:
            
            print('\n1. Adicionar calorias ao seu dia')
            print('2. Finalizar o dia')
            print('3. Ver histórico')
            print('4. Voltar')

            opcao = input('Digite uma opção (1-4): ').strip()

            if opcao == '1':
                print(f'\nTotal de calorias hoje: {user["calorias_hoje"]}/{TMB:.0f}')
                cal = input('\nQuantas calorias você consumiu em sua última refeição? ')
                cal = int(cal)

                if cal <= 0:
                    print('\nOps, este não é um valor válido. Caso queira registrar suas calorias, digite um valor válido.')
                    aguardar_volta()
                    continue

                user['calorias_hoje'] += cal  #aqui, as calorias são acumuladas.
                print(f'\nVocê consumiu {cal} calorias.')
                print(f'Total hoje: {user["calorias_hoje"]}/{TMB:.0f}')
                aguardar_volta()

            elif opcao == '2':
                    es = input('\nDeseja finalizar o seu dia ? Não poderá mais adicionar calorias ao dia de hoje. (s/n):  ').strip().lower()

                    if es == 's':
                        if data_atual not in user['historico_dias']:
                            user['historico_dias'][data_atual] = user['calorias_hoje']
                            print(f'\nDia finalizado com sucesso! Total salvo: {user["calorias_hoje"]} calorias')
                            user['calorias_hoje'] = 0  #zerando a contagem para o próximo dia
                            
                            diferenca = user['historico_dias'][data_atual] - TMB  # Usamos o valor salvo no histórico
                            
                            if diferenca > 0:
                                print(f'\nVocê está {diferenca:.0f} calorias acima da sua TMB.')

                            elif diferenca < 0:
                                print(f'\nVocê está {abs(diferenca):.0f} calorias abaixo da sua TMB.')

                            else:
                                print('\nVocê consumiu exatamente sua TMB!')
                            
                            #dicas personalizadas de acordo com o objetivo do usuário.
                            print('\n--- ANÁLISE DO SEU OBJETIVO ---')
                            
                            if objetivo == '1':  #ganho de massa
                                if diferenca > 0:
                                    print('\nÓtimo! Superávit calórico ajuda no ganho de massa. MANTÉM! 😎')

                                else:
                                    print('\nAtenção! Para ganhar massa, você precisa consumir mais que sua TMB.')
                                    
                            elif objetivo == '2':  #perda de peso
                                if diferenca < 0:
                                    print('\nPerfeito! Déficit calórico é essencial para perda de peso. Continua assim! 👊') 

                                else:
                                    print('\nCuidado! Para perder peso, você precisa consumir menos que sua TMB.')
                                    
                            else:  
                                if abs(diferenca) < (TMB * 0.1):  
                                    print('\nExcelente! Você está mantendo um bom equilíbrio. ✍')

                                else:
                                    print('\nPara manutenção, tente ficar próximo da sua TMB.')

                        else:
                            print('\nVocê já finalizou o dia hoje!')
                        aguardar_volta()

                    elif es == 'n':
                        aguardar_volta()

                    else:
                        print('Digite (s) ou (n).')
                        continue
            elif opcao == '3':
                print('\n📅 HISTÓRICO DE CONSUMO:')

                if not user['historico_dias']:
                    print('Nenhum registro encontrado.')

                else:
                    for data, total in user['historico_dias'].items():
                        print(f'{data}: {total} calorias')

                aguardar_volta()
            elif opcao == '4':
                break

            else:
                print('|Opção inválida!|')
                aguardar_volta()

        except:
            print('\nDigite apenas números.')

def menu_logado():
    """
    Menu onde o usuário tem acesso as funcionalidades do programa,
    só é possível ter acesso a esse menu após o login.
    """
    
    global usuario_logado, usuarios 

    while True:
        limpar_tela()
        print('\n(VITALTRACK)')
        
        print('\n(MENU PRINCIPAL)')
        print(f'Logado como: {usuarios[usuario_logado]["nome"]}')
        print('\n1. Ver perfil completo')
        print('2. Calcular IMC')
        print('3. Calcular TMB')
        print('4. Registro de calorias')
        print('5. Atualizar perfil')
        print('6. Atualizar objetivo/dados')
        print('7. Deslogar')
        print('8. Deletar conta')
        
        opcao = input('\nEscolha uma opção: ').strip()
        
        if opcao == '1':
            limpar_tela()
            print('\n(SEU PERFIL)')
            print(f'\nNome: {usuarios[usuario_logado]["nome"]}')
            print(f'Email: {usuario_logado}')
            if usuarios[usuario_logado]["dados"]:
                dados = usuarios[usuario_logado]["dados"]
                print(f'Objetivo: {["Ganho de massa", "Perda de peso", "Manutenção"][int(dados["objetivo"])-1]}')
                print(f'Idade: {dados["idade"]} anos')
                print(f'Peso: {dados["peso"]} kg')
                print(f'Altura: {dados["altura"]} m')
                print(f'Sexo: {"Masculino" if dados["sexo"] == "m" else "Feminino"}')
            aguardar_volta()

        elif opcao == '2':
            calcular_imc()

        elif opcao == '3':
            calcular_taxametabolicabasal()

        elif opcao == '4':
            registrar_calorias()

        elif opcao == '5':
            atualizar_usuario()

        elif opcao == '6':
            print('\nAtualizando dados...')
            atualizar_dados()

        elif opcao == '7':
            usuario_logado = None
            print('Deslogado com sucesso!')
            break
        
        elif opcao == '8':
            if deletar_usuario():
                break
        
        else:
            print('Opção inválida! Digite um número de 1 a 8.')

if __name__ == "__main__":
    menu_principal() 
