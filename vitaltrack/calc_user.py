from utils import Utils
from rich.panel import Panel
from rich.console import Console 
from rich.text import Text 
from user_management import Cadastro
import time
from datetime import datetime 
c = Console()
cadastro = Cadastro()

def calcular_imc(usuarios, usuario_logado):
    """
    Calcula o IMC (índice de massa corporal) do usuário,
    O usuário pode calcular o seu próprio IMC (com seus dados salvos),
    ou pode optar por calcular outro IMC qualquer,
    a função retorna o status após calcular o valor do imc, em ambos os casos.
    """
    Utils.limpar_tela_universal()

    if usuario_logado is None:
        c.print(Panel('Faça login primeiro!', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
        Utils.aguardar_volta()
        return usuarios, usuario_logado
    
    user = cadastro.usuarios[usuario_logado]
    if not user.get('dados'):
        c.print(Panel('Complete seus dados primeiro!', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
        usuarios = cadastro.escolher_objetivo(usuarios, usuario_logado) 
        return usuarios, usuario_logado
    
    dados = user['dados']
    imc = dados['peso'] / (dados['altura'] ** 2)

    while True:
        Utils.limpar_tela_universal()
        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
        print(' ')
        imc_text = Text('CALCULADORA DE IMC (ÍNDICE DE MASSA CORPORAL)', justify = 'center')
        p_imctext = Panel(imc_text, title="[i][cyan]IMC[/cyan][/i]",title_align="center",border_style="cyan",expand=True)
        c.print(p_imctext)
        c.print(Panel('Deseja calcular o [u]seu IMC[/u] (1), calcular [u]outro qualquer[/u] (2), ou voltar (3)?', expand = False, border_style = 'yellow'))
        calcularimc_visualizarimc = input('>>> ')

        if calcularimc_visualizarimc not in ['1','2','3']:
            c.print(Panel('Digite "1", "2" ou "3".', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
            Utils.aguardar_volta()
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
    
            Utils.aguardar_volta()
            continue
    
        elif calcularimc_visualizarimc == '2':

            while True:
                    
                    try:
                        c.print(Panel('Digite o seu [green][u]peso[/u][/] em kg:', expand = False, border_style = 'yellow'))
                        pesoimc = float(input('>>> '))
                        if pesoimc > 350 or pesoimc <= 0:
                            c.print(Panel('Digite um peso válido.', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                            Utils.aguardar_volta()
                            continue
                    except ValueError:
                        c.print(Panel('Digite apenas números', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                        Utils.aguardar_volta()
                        continue
                    break
            
            while True:
                    
                    try:
                        c.print(Panel('Digite a sua [green][u]altura[/u][/] em m:', expand = False, border_style = 'yellow'))
                        alturaimc = float(input('>>> '))
                        if alturaimc > 2.2 or alturaimc <= 0:
                            c.print(Panel('Digite uma altura válida', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                            Utils.aguardar_volta()
                            continue
                    except ValueError:
                        c.print(Panel('Digite apenas números', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                        Utils.aguardar_volta()
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
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal()
                    break
                
        elif calcularimc_visualizarimc == '3':
            with c.status("[red]S[/red][magenta]a[/magenta][yellow]i[/yellow]"
                "[green]n[/green][cyan]d[/cyan][blue]o[/blue]", spinner = 'hearts'):  
                time.sleep(2)
                Utils.limpar_tela_universal()
            break
    return usuarios, usuario_logado
        
def calcular_taxametabolicabasal(usuarios, usuario_logado):
    """
    Calcula a tmb (Taxa metabólica basal) do usuário,
    o usuário pode escolher entre calcular sua TBM (com seus dados salvos),
    ou pode optar por calcular outra qualquer"""
    Utils.limpar_tela_universal()

    if usuario_logado is None:
        c.print(Panel('Faça login primeiro!', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
        Utils.aguardar_volta()  
        return usuarios, usuario_logado

    user = usuarios[usuario_logado]

    if not user.get('dados'):
        c.print(Panel('Complete seus dados primeiro!', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
        usuarios = cadastro.escolher_objetivo(usuarios, usuario_logado)
        return usuarios, usuario_logado

    while True:
        Utils.limpar_tela_universal()
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
            sexo_uso = dados['sexo']
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
                        cadastro.salvar_dadosjson()

                        c.print(Panel(f'Sua TMB é :({TMB:.2f})',expand = False, border_style = 'cyan'))
                        retornotmb1_text = Text()
                        retornotmb1_text.append('O cálculo foi feito com base no seu sexo de identidade, pois você informou que está em transição hormonal há mais de 12 meses.')
                        retornotmb1_text.append('\nApós esse tempo, a terapia hormonal tende a modificar significativamente o metabolismo, e por isso essa abordagem é mais precisa.')
                        pretornotmb1 = Panel(retornotmb1_text, expand = False, border_style = 'cyan', title = '[blue]INFO[/]')
                        c.print(pretornotmb1)
                        Utils.aguardar_volta()
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
                        cadastro.salvar_dadosjson()
                        Utils.aguardar_volta()
                        continue

                else:
                    #não usa hormônios -> usa sexo biológico
                    sexo_uso = dados.get('sexo_biologico', dados['sexo'])  #se por acaso sexo_biologico for None, usa sexo identidade

                if sexo_uso == 'm':
                    TMB = (10 * peso) + (6.25 * altura_cm) - (5 * idade) + 5
                    
                else:
                    TMB = (10 * peso) + (6.25 * altura_cm) - (5 * idade) - 161

                usuarios[usuario_logado]['TMB'] = TMB
                cadastro.salvar_dadosjson()
                
                c.print(Panel(f'Sua TMB é :({TMB:.2f})', expand = False, border_style = 'cyan'))
                retornotmb3_text = Text()
                retornotmb3_text.append('O cálculo foi feito com base no seu sexo biológico, pois você indicou que não faz uso de terapia hormonal.')
                retornotmb3_text.append('\nIsso é importante porque, sem o uso de hormônios, seu metabolismo segue padrões fisiológicos relacionados ao sexo biológico.')
                pretornotmb3 = Panel(retornotmb3_text, expand = False, border_style = 'cyan', title = '[blue]INFO[/]')
                c.print(pretornotmb3)
                Utils.aguardar_volta()
                continue
        
            else:

                sexo_uso = dados.get('sexo', '').lower()

                if sexo_uso == 'm':
                    TMB = (10 * peso) + (6.25 * altura_cm) - (5 * idade) + 5
                else:
                    TMB = (10 * peso) + (6.25 * altura_cm) - (5 * idade) - 161

                usuarios[usuario_logado]['TMB'] = TMB
                cadastro.salvar_dadosjson()

                c.print(Panel(f'Sua TMB é :({TMB:.2f})', expand = False, border_style = 'cyan'))
                c.print(Panel('O cálculo foi feito com base no sexo informado no seu cadastro.', expand = False, border_style = 'cyan', title = '[blue]INFO[/]'))
                Utils.aguardar_volta()
                continue

        elif calculartmb_visualizartmb == '2':

            while True:
                Utils.limpar_tela_universal()
                try:
                    c.print(Panel('Digite o [u][green]peso[/][/u] em quilogramas:', expand = False, border_style = 'yellow'))
                    pesoex = float(input('>>> '))
                    if pesoex > 350 or pesoex <= 0:
                        c.print(Panel('Digite um peso válido.',expand = False, border_style = 'red', title = '[b]ERRO[/b]', title_align = 'center'))
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()
                        continue
                except ValueError:
                        c.print(Panel('Digite apenas números', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()
                        continue
                break
            
            while True:
                    
                    try:
                        c.print(Panel('Digite a [green][u]altura[/u][/] em centímetros:', expand = False, border_style = 'yellow'))
                        alturaex = float(input('>>> '))
                        if alturaex > 220 or alturaex <= 100:
                            c.print(Panel('Digite uma altura válida, em centímetros.', expand = False, border_style = 'red', title = '[b]ERRO[/b]', title_align = 'center'))
                            Utils.aguardar_volta()
                            Utils.limpar_tela_universal()
                            continue
                    except ValueError:
                        c.print(Panel('Digite apenas números', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()
                        continue
                    break
                    
            while True:

                    try:            
                        c.print(Panel('Digite a [green][u]idade:[/u][/]', expand = False, border_style = 'yellow'))
                        idadeex = int(input('>>> '))
                        if idadeex > 100 or idadeex <= 0:
                            c.print(Panel('Digite uma idade válida.', expand = False, border_style = 'red', title = '[b]ERRO[/b]', title_align = 'center'))
                            Utils.aguardar_volta()
                            Utils.limpar_tela_universal()
                            continue
                    except ValueError:
                        c.print(Panel('Digite apenas números', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()
                        continue
                    break
            
            resposta = 'n'
            
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
                            Utils.aguardar_volta()
                            Utils.limpar_tela_universal()
                            continue
                    except ValueError:
                        c.print(Panel('Digite apenas números', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()
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
                                Utils.aguardar_volta()
                                Utils.limpar_tela_universal()
                                continue 
                    except ValueError:
                        c.print(Panel('Digite apenas números', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()
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
                            Utils.aguardar_volta()
                            Utils.limpar_tela_universal()
                            continue
                except ValueError:
                        c.print(Panel('Digite um número válido.', expand = False, border_style = 'red', title = '[b]ERRO[/b]', title_align = 'center'))
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()
                        continue
                
                tmb_m = (10 * pesoex) + (6.25 * alturaex) - (5 * idadeex) + 5
                tmb_f = (10 * pesoex) + (6.25 * alturaex) - (5 * idadeex) - 161
            
                if sexo_opcao == '1':  
                    Utils.limpar_tela_universal()
                    TMB = tmb_m
                    c.print(Panel(f'Sua TMB é: {TMB:.2f}', expand = False, border_style = 'cyan'))
                    
                elif sexo_opcao == '2':  
                    Utils.limpar_tela_universal()
                    TMB = tmb_f
                    c.print(Panel(f'Sua TMB é: {TMB:.2f}', expand = False, border_style = 'cyan'))
                    
                elif sexo_opcao == '3':  
                    
                    if em_transicao and tempo_transicao >= 12:
                        Utils.limpar_tela_universal()
                        TMB = tmb_m  
                        c.print(Panel(f'\nSua TMB é: {TMB:.2f}', expand = False, border_style = 'cyan'))
                        c.print(Panel('✅ Cálculo feito com base no seu sexo atual, conforme sua identidade de gênero.', expand = False, border_style = 'cyan', title = '[blue]INFO[/]', title_align = 'center'))

                    elif em_transicao:
                        Utils.limpar_tela_universal()
                        TMB = (tmb_m + tmb_f) / 2  
                        c.print(Panel(f'Sua TMB é: {TMB:.2f}', expand = False, border_style = 'cyan'))
                        c.print(Panel('Como sua transição é recente, usamos uma média para tornar o cálculo mais preciso.', expand = False, border_style = 'cyan', title = '[blue]INFO[/]', title_align = 'center'))

                    else:
                        Utils.limpar_tela_universal()
                        TMB = tmb_f  
                        c.print(Panel(f'Sua TMB é: {TMB:.2f}', expand = False, border_style = 'cyan'))
                        c.print(Panel('Como não há uso de hormônios, o cálculo foi feito com base no sexo biológico.', expand = False, border_style = 'cyan', title = '[blue]INFO[/]', title_align = 'center'))
                        
                elif sexo_opcao == '4':  
                    
                    if em_transicao and tempo_transicao >= 12:
                        Utils.limpar_tela_universal()
                        TMB = tmb_f  
                        c.print(Panel(f'Sua TMB é: {TMB:.2f}', expand = False, border_style = 'cyan'))
                        c.print(Panel('✅ Cálculo feito com base no seu sexo atual, conforme sua identidade de gênero.', expand = False, border_style = 'cyan', title = '[blue]INFO[/]', title_align = 'center'))

                    elif em_transicao:
                        Utils.limpar_tela_universal()
                        TMB = (tmb_m + tmb_f) / 2  
                        c.print(Panel(f'Sua TMB é: {TMB:.2f}', expand = False, border_style = 'cyan'))
                        c.print(Panel('Como sua transição é recente, usamos uma média para tornar o cálculo mais preciso.', expand = False, border_style = 'cyan', title = '[blue]INFO[/]', title_align = 'center'))

                    else:
                        Utils.limpar_tela_universal()
                        TMB = tmb_m  
                        c.print(Panel(f'Sua TMB é: {TMB:.2f}', expand = False, border_style = 'cyan'))
                        c.print(Panel('Como não há uso de hormônios, o cálculo foi feito com base no sexo biológico.', expand = False, border_style = 'cyan', title = '[blue]INFO[/]', title_align = 'center'))
                
                Utils.aguardar_volta()
                Utils.limpar_tela_universal()
                break
                    
        elif calculartmb_visualizartmb == '3':
            with c.status("[red]S[/red][magenta]a[/magenta][yellow]i[/yellow]"
                "[green]n[/green][cyan]d[/cyan][blue]o[/blue]", spinner = 'hearts'):  
                time.sleep(2)
                Utils.limpar_tela_universal()
            break

        else:
            c.print(Panel('Opção inválida! Digite 1, 2 ou 3.', expand = False, border_style = 'red', title = '[b]ERRO[/b]', title_align = 'center'))
            Utils.aguardar_volta()
            continue
    return usuarios, usuario_logado
        
def registrar_calorias(usuarios, usuario_logado):
    """
    Registra as calorias consumidas pelo usuário durante o dia,
    usuário digita suas calorias, o função salva ao lado de sua TBM,
    usuário tem a opção de "finalizar dia",
    após isso, recebe um feedback e pode verificar o histórico de consumo de acordo com o dia.
    """
    Utils.limpar_tela_universal()

    if usuario_logado is None:
        c.print(Panel('Faça login primeiro!', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
        Utils.aguardar_volta()  
        return usuarios, usuario_logado
    
    user = usuarios[usuario_logado]

    if 'TMB' not in user or not user.get('dados'):
        c.print(Panel('Você precisa calcular sua taxa metabólica basal primeiro!', expand = False, border_style = 'red', title = '❗AVISO❗', title_align = 'center'))
        Utils.aguardar_volta()
        if not calcular_taxametabolicabasal(usuarios, usuario_logado):  
            return usuarios, usuario_logado
    
    if 'historico_dias' not in user:
        user['historico_dias'] = {}

    data_atual = datetime.now().strftime('%d/%m/%Y') 

    TMB = user['TMB']
    objetivo = user['objetivo']
    
    calorias_hoje = 0

    if 'calorias_hoje' not in user:
        user['calorias_hoje'] = 0

    while True:
        Utils.limpar_tela_universal()
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
                Utils.limpar_tela_universal()
                c.print(Panel(f'Total de calorias hoje: {user["calorias_hoje"]}/{TMB:.0f}', expand = False, border_style = 'cyan'))
                c.print(Panel('Quantas calorias você consumiu em sua última refeição?', expand = False, border_style = 'yellow'))
                cal = input('>>> ')
                cal = int(cal)

                if cal <= 0:
                    c.print(Panel('Ops, este não é um valor válido. Caso queira registrar suas calorias, digite um valor válido.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal()
                    continue

                user['calorias_hoje'] += cal  #aqui, as calorias são acumuladas.
                cadastro.salvar_dadosjson()
                feedbackcal_text = Text()
                feedbackcal_text.append(f'Você consumiu {cal} calorias.')
                feedbackcal_text.append(f'\nTotal hoje: {user["calorias_hoje"]}/{TMB:.0f}')
                pfeedbackcal = Panel(feedbackcal_text, expand = False, border_style = 'cyan', title = 'FEEDBACK', title_align = 'center')
                c.print(pfeedbackcal)
                Utils.aguardar_volta()
                Utils.limpar_tela_universal()

            elif opcao == '2':
                    Utils.limpar_tela_universal()
                    c.print(Panel('Deseja finalizar o seu dia ? Não poderá mais adicionar calorias ao dia de hoje. (s/n):', expand = False, border_style = 'yellow'))
                    es = input('>>> ').strip().lower()

                    if es == 's':
                        if data_atual not in user['historico_dias']:
                            user['historico_dias'][data_atual] = user['calorias_hoje']
                            cadastro.salvar_dadosjson()
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
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()

                    elif es == 'n':
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()

                    else:
                        c.print(Panel('Digite (s) ou (n).', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                        Utils.aguardar_volta()
                        Utils.limpar_tela_universal()
                        continue

            elif opcao == '3':
                Utils.limpar_tela_universal()
                c.print(Panel('📅 HISTÓRICO DE CONSUMO:', expand = False, border_style = 'cyan'))

                if not user['historico_dias']:
                    c.print(Panel('Nenhum registro encontrado.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))

                else:
                    for data, total in user['historico_dias'].items():
                        c.print(Panel(f'{data}: {total} calorias', expand = False, border_style = 'cyan'))

                Utils.aguardar_volta()
            elif opcao == '4':
                with c.status("[red]S[/red][magenta]a[/magenta][yellow]i[/yellow]"
                    "[green]n[/green][cyan]d[/cyan][blue]o[/blue]", spinner = 'hearts'):  
                    time.sleep(2)
                    Utils.limpar_tela_universal()
                break

            else:
                c.print(Panel('Opção inválida!', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                Utils.aguardar_volta()
                Utils.limpar_tela_universal()

        except Exception as e:
            c.print(Panel(f'Ocorreu um erro: {e}', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
            Utils.aguardar_volta()
            Utils.limpar_tela_universal()

    return usuarios, usuario_logado