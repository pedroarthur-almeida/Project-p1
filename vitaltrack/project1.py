usuarios = {} #criando um dicionário vazio para armazenar os dados. é como um banco de dados em formato de dicionário.
usuario_logado = None #variavel que guarda quem está logado no momento.
from datetime import datetime #importando biblioteca para utilizar datas.

def cadastro_de_usuario(): #criando a função de cadastro.
    global usuarios,usuario_logado #garantindo o acesso as variáveis globais, para poder adicionar os dados e etc.
    print('\n(Cadastro)')

    while True:
        email = input('\nDigite o seu email: ').strip().lower() #.strip() para ignorar espaços e .lower() para manter as letras minusculas.
        #verificando se o email está nos padrões corretos
        if email in usuarios:
            print('|Este email já foi cadastrado!|')
            print('|Insira um email ainda não cadastrado.|')
            continue #para pedir o email novamente caso ocorra o erro.
        
        elif '@' not in email or '.com' not in email:
            print('\n|O email precisa estar em um formato válido.|')
            print('|O email precisa ter ".com" e "@".|')
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
            continue #para continuar pedindo a senha caso ocorra o erro
            
        confirmaçao_de_senha = input('\nConfirme sua senha: ')

        if senha != confirmaçao_de_senha:
            print('\n|As senhas não coinscidem.|')
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


def calcular_imc():
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
        calcularimc_visualizarimc = input('\nDeseja visualizar o seu IMC (1) ou calcular outro qualquer? (2) ')

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
            pesoimc = float(input('\nDigite o seu peso em kg: '))
            alturaimc = float(input('Digite a sua altura em m: '))
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

#função para calcular a taxa metabólica basal.
def calcular_taxametabolicabasal():
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

    dados = user['dados']
    altura = dados['altura']
    peso = dados['peso']
    idade = dados['idade']
    sexo = dados['sexo']
    altura_cm = altura * 100  # Transforma altura de metros para cm, pois é necessário que a altura esteja em cm para realizar o cálculo da TMB.


    while True:
        try:
            print('\n-----TAXA METABÓLICA BASAL (TMB)-----')

            print('\nInformação: Taxa Metabólica Basal (TMB) é a quantidade mínima de calorias que seu corpo precisa para manter funções vitais (como respiração, circulação e temperatura) em repouso completo.')

            calculartmb_visualizartmb = input('\nDeseja visualizar sua taxa metabólica basal (1), ou calcular outra qualquer (2)?').strip()

            if calculartmb_visualizartmb == '1':
            
            #o cálculo da tmb é difirente dependo do sexo da pessoa.
                if sexo == 'm':
                    TMB = (10 * peso) + (6.25 * altura_cm) - (5 * idade) + 5
                    
                else:
                    TMB = (10 * peso) + (6.25 * altura_cm) - (5 * idade) - 161
                

                #salva a tmb em usuários.
                usuarios[usuario_logado]['TMB'] = TMB
                
                print('\n-----------------------------')
                print(f'-----Sua TMB é :({TMB:.2f})----')
                print('-----------------------------')
                aguardar_volta()
                return TMB
            
            elif calculartmb_visualizartmb == '2':
                pesoex = float(input('Digite o peso (em kg): '))
                alturaex = float(input('Digite a altura (em cm): '))
                idadeex = int(input('Digite a idade: '))
                sexoex = input('Digite o sexo (m(asculino)/f(eminino))').lower() #para ficar minusculo 

                if sexoex == 'm':
                    TMB = (10 * pesoex) + (6.25 * alturaex) - (5 * idadeex) + 5
                else:
                    TMB = (10 * pesoex) + (6.25 * alturaex) - (5 * idadeex) - 161

                print(f'\nSua TMB é :({TMB:.2f})')
                aguardar_volta()
                break

            else:
                print('|Opção inválida! Digite 1 ou 2.|')
                
        except ValueError:
            print('|Valor inválido! Use números.|')


def registrar_calorias():
    global usuarios, usuario_logado

    if usuario_logado is None:
        print('|Faça login primeiro!|')
        aguardar_volta() #função que retorna ao menu. 
        return
    
    user = usuarios[usuario_logado]

    if 'TMB' not in user:
        print('|Você precisa calcular sua taxa metabólica basal primeiro!|')
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
                cal = input('Quantas calorias você consumiu em sua última refeição? ')
                cal = int(cal)
                user['calorias_hoje'] += cal  # Acumula as calorias
                print(f'\nVocê consumiu {cal} calorias.')
                print(f'Total hoje: {user["calorias_hoje"]}/{TMB:.0f}')

            elif opcao == '2':
                    if data_atual not in user['historico_dias']:
                        user['historico_dias'][data_atual] = user['calorias_hoje']
                        print(f'\nDia finalizado com sucesso! Total salvo: {user["calorias_hoje"]} calorias')
                        user['calorias_hoje'] = 0  # Reseta para o próximo dia
                        
                        # Análise do dia que está sendo finalizado
                        diferenca = user['historico_dias'][data_atual] - TMB  # Usamos o valor salvo no histórico
                        
                        if diferenca > 0:
                            print(f'\nVocê está {diferenca:.0f} calorias acima da sua TMB.')
                        elif diferenca < 0:
                            print(f'\nVocê está {abs(diferenca):.0f} calorias abaixo da sua TMB.')
                        else:
                            print('\nVocê consumiu exatamente sua TMB!')
                        
                        # Dicas personalizadas por objetivo
                        print('\n--- ANÁLISE DO SEU OBJETIVO ---')
                        
                        if objetivo == '1':  # Ganho de massa
                            if diferenca > 0:
                                print('Ótimo! Superávit calórico ajuda no ganho de massa. MANTÉM! 😎')
                            else:
                                print('Atenção! Para ganhar massa, você precisa consumir mais que sua TMB.')
                                
                        elif objetivo == '2':  # Perda de peso
                            if diferenca < 0:
                                print('Perfeito! Déficit calórico é essencial para perda de peso. Continua assim! 👊') 
                            else:
                                print('Cuidado! Para perder peso, você precisa consumir menos que sua TMB.')
                                
                        else:  # Manutenção
                            if abs(diferenca) < (TMB * 0.1):  # 10% de margem
                                print('Excelente! Você está mantendo um bom equilíbrio. ✍')
                            else:
                                print('Para manutenção, tente ficar próximo da sua TMB.')
                    else:
                        print('\nVocê já finalizou o dia hoje!')
                    aguardar_volta()
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
            print('Digite um valor válido ou "sair".')


def aguardar_volta():
    input('\nPressione Enter para voltar ao menu...')

#Essa é a parte de escolha de objetivo, ocorre após o cadastro.
def escolher_objetivo():
    global usuario_logado, usuarios

    while True:

        print('\n(Qual é o seu objetivo? 🤔)')
        print('\nAntes de começarmos, é importante entender qual é o seu foco atual em relação à sua saúde. o VitalTrack foi pensado para se adaptar as suas necesssidades e objetivos. ✍')
        print('\nÉ como uma parceria, entendeu? 👊🤝')
        print('\nVocê pode escolher entre três caminhos:')
        print('\n1. Ganho de massa (Foco em ganho de peso e aumento da massa muscular.🏋️ 💪)')
        print('2. Perda de peso (ideal para quem deseja reduzir o percentual de gordura corporal de forma saudável.)🏃')
        print('3. Manutenção da saúde (Para quem quer manter o equilíbrio, hábitos saudáveis e o bem-estar geral.)❤')
        print(' ')

        objetivo = input('Agora é com você! 🕺 Escolha um objetivo (1-3): ')

        if objetivo not in ['1', '2', '3']:
            print('\n|Opção inválida! Escolha 1, 2 ou 3.|')
            continue 

        # Mensagem personalizada de acordo com o objetivo que o usuário escolher.
        objetivos = {
            '1': 'GANHO DE MASSA',
            '2': 'PERDA DE PESO', 
            '3': 'MANUTENÇÃO DA SAÚDE' }
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

                dados = { #aqui eu crio um dicionário, que se chama "dados" para coletar os dados do usuário, e insiro esse dicionário no dicionário "usuarios"
                    'objetivo': objetivo,
                    'idade': int(input('\nIdade: ')),
                    'peso': float(input('Peso (kg): ')),
                    'altura': float(input('Altura (m): ')),
                    'sexo': input('Sexo (m/f): ').lower()
                }
                if dados['idade'] > 100 or dados['peso'] > 350.0 or dados['altura'] > 2.2:
                    print('\n|Digite valores válidos.|' )
                    continue
                if dados['idade'] <= 0 or dados['peso'] <= 0 or dados['altura'] <= 0:
                    raise ValueError
                if dados['sexo'] not in ['m', 'f']:
                    raise ValueError
                
                # Salvando todos os dados no usuário
                usuarios[usuario_logado]['dados'] = dados
                usuarios[usuario_logado]['objetivo'] = objetivo
                return True
                
            except ValueError:
                print('\n|Valores inválidos! Digite novamente.|')
                

def fazer_login(): #criando a função de login.
  
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

def deletar_usuario():
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
    global usuario_logado #declarando novamente como global
 
    while True:
        
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

def menu_logado():
    global usuario_logado, usuarios 

    while True:
        
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
            escolher_objetivo()
            aguardar_volta()
        elif opcao == '7':
            usuario_logado = None
            print('Deslogado com sucesso!')
            break
        elif opcao == '8':
            if deletar_usuario():
                break
        
        else:
            print('Opção inválida! Digite um número de 1 a 8.')

#inicia o programa. 
if __name__ == "__main__":
    menu_principal() 

           
     
       
















  


  









  












    


    

