usuarios = {} #criando um dicionário vazio para armazenar os dados.
usuario_logado = None


def cadastro_de_usuario(): #criando a função de cadastro.
    global usuarios,usuario_logado #garantindo o acesso
    print('\n-----Cadastro-----')
    email = input('Digite o seu email: ').strip().lower() #.strip() para ignorar espaços e .lower() para manter as letras minusculas.

    #verificando se o email está nos padrões corretos
    if email in usuarios:
     print('Este email já foi cadastrado!')
     return False
    
    elif '@' not in email or '.com' not in email:
     print('Digite seu email em um formato válido.')
     print('O email precisa ter ".com" e "@".')
     return False
    
    senha = input('Digite sua senha(mínimo 6 caracteres): ')

    #verificando se a senha está nos padrões corretos.
    if len(senha) < 6:
        print('Senha muito curta. Mínimo 6 caracteres.')
        return False
         
    confirmaçao_de_senha = input('Confirme sua senha: ')

    if senha != confirmaçao_de_senha:
        print('As senhas não coinscidem.')
        return False
    
    nome = input('Digite seu nome: ').strip()

     # Criando o usuário
    usuarios[email] = {
        'senha': senha,
        'nome': nome,
        'objetivo': None,
        'dados': None
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
        print('Faça login primeiro!')
        aguardar_volta()
        return
    
    user = usuarios[usuario_logado]
    if not user.get('dados'):
        print('Complete seus dados primeiro!')
        escolher_objetivo()
        return
    
    dados = user['dados']
    imc = dados['peso'] / (dados['altura'] ** 2)

    while True:
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
        print('Faça login primeiro!')
        aguardar_volta() #função que retorna ao menu. 
        return

    user = usuarios[usuario_logado]

    if not user.get('dados'):
        print('Complete seus dados primeiro!')
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

            calculartmb_visualizartmb = input('\nDeseja visualizar sua taxa metabólica basal (1), ou calcular outra qualquer (2)?')

            if calculartmb_visualizartmb == '1':
            
            #o cálculo da tmb é difirente dependo do sexo da pessoa.
                if sexo == 'm':
                    TMB = (10 * peso) + (6.25 * altura_cm) - (5 * idade) + 5
                else:
                    TMB = (10 * peso) + (6.25 * altura_cm) - (5 * idade) - 161

                print(f'\nSua TMB é :({TMB:.2f})')
                aguardar_volta()
                break

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
                print('Opção inválida! Digite 1 ou 2.')
                
        except ValueError:
            print('Valor inválido! Use números.')



def aguardar_volta():
    input('\nPressione Enter para voltar ao menu...')

#Essa é a parte de escolha de objetivo, ocorre após o cadastro.
def escolher_objetivo():
    global usuario_logado, usuarios

    while True:

        print('(Qual é o seu objetivo? 🤔)')
        print('\nAntes de começarmos, é importante entender qual é o seu foco atual em relação à sua saúde. o VitalTrack foi pensado para se adaptar as suas necesssidades e objetivos. ✍')
        print('\nÉ como uma parceria, entendeu? 👊🤝')
        print('\nVocê pode escolher entre três caminhos:')
        print('\n1. Ganho de massa (Foco em ganho de peso e aumento da massa muscular.🏋️ 💪)')
        print('2. Perda de peso (ideal para quem deseja reduzir o percentual de gordura corporal de forma saudável.)🏃')
        print('3. Manutenção da saúde (Para quem quer manter o equilíbrio, hábitos saudáveis e o bem-estar geral.)❤')
        print(' ')

        objetivo = input('Agora é com você! 🕺 Escolha um objetivo (1-3): ')

        if objetivo not in ['1', '2', '3']:
            print('Opção inválida! Escolha 1, 2 ou 3.')
            continue 

        # Mensagem personalizada
        objetivos = {
            '1': 'GANHO DE MASSA',
            '2': 'PERDA DE PESO', 
            '3': 'MANUTENÇÃO DA SAÚDE' }
        print('\n-----------------------------')
        print(f'Você escolheu: {objetivos[objetivo]}')
        print('-----------------------------')
        if objetivo == '1':
            print('\nBoa! Você deseja aumentar sua massa corporal, tô contigo nessa! 😎 💪')
            print('\nUma dica: é importante que você consuma uma quantidade de calorias maior que a sua TMB.')
            print('\nNão sabe o que é TMB? não se preocupe! mais na frente eu te explico. 😉')
        elif objetivo == '2':
            print('\nVocê escolheu perder peso, que legal! Tamo junto nessa jornada. 👊')
            print('\nCom foco e disciplina, qualquer objetivo pode se concretizar, vai dar tudo certo!')
            print('\nDica: é importante que você consuma uma quantidade de calorias inferior a sua TMB.')
            print('\nNão sabe o que é TMB? não se preocupe! mais na frente eu te explico. 😉')
        else:
            print('\nÉ isso ai! Você optou por manter-se saudável, conte comigo pra te auxiliar! ✋')
            print('\nÉ extremamente importante acompanhar a própria saúde, isso vale para pessoas de qualquer faixa etária. 🧒👨👴')
            print('\nDica: mantenha seu consumo de calorias em um valor próximo a sua TMB.')
            print('\nNão sabe o que é TMB? não se preocupe! mais na frente eu te explico. 😉')

        print('Beleza! Agora vamos coletar algumas informações sobre você.')

        while True:
            try:

                dados = {
                    'objetivo': objetivo,
                    'idade': int(input('\nIdade: ')),
                    'peso': float(input('Peso (kg): ')),
                    'altura': float(input('Altura (m): ')),
                    'sexo': input('Sexo (m/f): ').lower()
                }
                
                if dados['idade'] <= 0 or dados['peso'] <= 0 or dados['altura'] <= 0:
                    raise ValueError
                if dados['sexo'] not in ['m', 'f']:
                    raise ValueError
                
                # Salvar todos os dados no usuário
                usuarios[usuario_logado]['dados'] = dados
                usuarios[usuario_logado]['objetivo'] = objetivo
                return True
                
            except ValueError:
                print('Valor inválido! Digite novamente.')
                

def fazer_login(): #criando a função de login.
  
    global usuario_logado, usuarios #declarando ambos como globais, para que possam ser utilizados e modificados.
    print('\n-----Login-----')
    email = input('Digite o seu email cadastrado: ').lower().strip()
    senha = input('Digite sua senha: ')

  #vamos verificar se o cadastro existe.
    if email not in usuarios:
        print('Email não cadastrado.')
        return False
    elif usuarios[email]["senha"] != senha:
        print('Senha incorreta.')
        return False
    else:
        usuario_logado = email
        print(f'Bem-vindo(a), {usuarios[email]["nome"]}!')
        return True

def atualizar_usuario(): #criando a função atualizar (parte do crud)
    global usuario_logado, usuarios
    if usuario_logado is None: #caso o usuario não esteja logado.
        print('Faça login primeiro!')
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
                print('Senha muito curta.') 
        elif opçao3 == '3':
            novo_email = input('Digite seu novo emai (atual: {usuario_logado}): ').strip().lower()  
            if not novo_email:
                continue
            if novo_email == usuario_logado:
                print('O novo email é igual ao atual.')   
            elif '@' not in novo_email or '.com' not in novo_email:
                print("Formato inválido (use '@' e '.com').")
            elif novo_email in usuarios:
                print('Email já cadastrado.') 
            else:
                # Transferir todos os dados para o novo email
                usuarios[novo_email] = usuarios[usuario_logado]
                del usuarios[usuario_logado]
                usuario_logado = novo_email
                print("Email atualizado com sucesso!") 
        elif opçao3 == '4':
            break
        else:
            print('Opção inválida. Digite uma opção disponível (1-4)') 

def deletar_usuario():
    global usuario_logado,usuarios
    if usuario_logado is None:
        print('Faça login primeiro.')
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
        print('\n=====VITALTRACK=====')
        print('\n-----MENU INICIAL-----\n') 
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
            print('Opção inválida! Digite uma opção presente no MENU.')

def menu_logado():
    global usuario_logado, usuarios 

    while True:

        print('\n===== VITALTRACK =====')
        print('\n----- MENU PRINCIPAL -----')
        print(f'Logado como: {usuarios[usuario_logado]["nome"]}')
        print('\n1. Ver perfil completo')
        print('2. Calcular IMC')
        print('3. Calcular TMB')
        print('4. Atualizar perfil')
        print('5. Atualizar objetivo/dados')
        print('6. Deslogar')
        print('7. Deletar conta')
        
        opcao = input('\nEscolha uma opção: ').strip()
        
        if opcao == '1':
            print('\n----- SEU PERFIL -----')
            print(f'Nome: {usuarios[usuario_logado]["nome"]}')
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
            atualizar_usuario()
        elif opcao == '5':
            print('\nAtualizando dados...')
            escolher_objetivo()
            aguardar_volta()
        elif opcao == '6':
            usuario_logado = None
            print('Deslogado com sucesso!')
            break
        elif opcao == '7':
            if deletar_usuario():
                break
        
        else:
            print('Opção inválida! Digite um número de 1 a 7.')

#inicia o programa. 
if __name__ == "__main__":
    menu_principal() 

           
     
       
















  


  









  












    


    

