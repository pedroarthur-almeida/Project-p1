from utils import Utils
from rich.panel import Panel
from rich.console import Console 
from rich.text import Text 
from user_management import Cadastro
import time
from datetime import datetime
from rich.align import Align 
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
        imc_text = Text()
        imc_text.append('\n')
        imc_text.append('Calculadora de IMC (Índice de massa corporal)\n', style = 'bold yellow')
        imc_text.append('Digite sua opção e escolha como seguir.', style = 'dim')
        imc_text.append('\n')
        p_imctext = Panel(imc_text, title="[bold blue]IMC[/bold blue]",title_align="center",border_style="blue",expand=False)
        p_imctext_center = Align.center(p_imctext)
        c.print(p_imctext_center)
        c.print(Panel('Deseja calcular o seu IMC (1), calcular outro qualquer (2), ou voltar (3)?', expand = False, border_style = 'bold yellow', style = 'bold yellow'))
        calcularimc_visualizarimc = input('>>> ')

        if calcularimc_visualizarimc not in ['1','2','3']:
            c.print(Panel('Digite "1", "2" ou "3".', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
            Utils.aguardar_volta()
            continue

        if calcularimc_visualizarimc == '1':
            calcularimc1_text = Text()
            calcularimc1_text.append(f'SEU IMC: {imc:.2f}', style = 'bold white')
            
            if imc < 18.5:
                status = 'Abaixo do peso'
            elif 18.5 <= imc < 25:
                status = 'Peso normal'
            elif 25 <= imc < 30:
                status = 'Sobrepeso'
            else:
                status = 'Obesidade'
            calcularimc1_text.append(f'\nStatus: {status}', style = 'dim')
            pcalcularimc1 = Panel(calcularimc1_text, expand = False, border_style = 'cyan')
            pcacularimc1_center = Align.center(pcalcularimc1)
            with c.status("[red]C[/red][magenta]a[/magenta][yellow]l[/yellow][green]c[/green]"
                "[cyan]u[/cyan][blue]l[/blue][red]a[/red][magenta]n[/magenta]"
                "[yellow]d[/yellow][green]o[/green]", spinner="hearts"):
                time.sleep(2)
            c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
            print(' ')
            c.print(pcacularimc1_center)

            objetivo = user['objetivo']
            if objetivo == '1':
                    feedbackobj1_text = Text()
                    feedbackobj1_text.append('Dica: Aumente a ingestão de proteínas e calorias saudáveis.')  
                    feedbackobj1_text.append('\nAlém disso, Foque em treinos de força e superávit calórico.')
                    feedbackobj1_text.append('\nConsuma alimentos com alta quantidade de proteínas e carboidratos.')
                    pfeedbackobj1 = Panel(feedbackobj1_text, border_style="cyan", expand = False,title="[bold cyan]Feedback[/bold cyan]",title_align="center")
                    pfeedbackobj1_center = Align.center(pfeedbackobj1)
                    c.print(pfeedbackobj1_center)
                    
            elif objetivo == '2':
                    feedbackobj2_text = Text()
                    feedbackobj2_text.append('Dica: Combine dieta balanceada com exercícios aeróbicos.')
                    feedbackobj2_text.append('\nUtilize alimentos com baixa quantidade de carboidratos e alta quantidade de proteínas.')
                    pfeedbackobj2 = Panel(feedbackobj2_text, border_style="cyan", expand = False,title="[bold cyan]Feedback[/bold cyan]",title_align="center")
                    pfeedbackobj2_center = Align.center(pfeedbackobj2)
                    c.print(pfeedbackobj2_center)
                    
            else:
                    feedbackobj3_text = Text()
                    feedbackobj3_text.append('Dica: Mantenha hábitos equilibrados e pratique atividades físicas')  
                    feedbackobj3_text.append('\nExistem diversos tipos de atividades físicas que podem te auxiliar.')
                    feedbackobj3_text.append('\nAté mesmo uma caminhada de 40/50 minutos, acelera seu metabolismo, e melhora sua saúde.')
                    pfeedbackobj3 = Panel(feedbackobj3_text, border_style="cyan", expand = False,title="[bold cyan]Feedback[/bold cyan]",title_align="center")
                    pfeedbackobj3_center = Align.center(pfeedbackobj3)
                    c.print(pfeedbackobj3_center)
    
            Utils.aguardar_volta()
            continue
    
        elif calcularimc_visualizarimc == '2':

            while True:
                    
                    try:
                        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                        print(' ')
                        c.print(Panel('Digite o seu peso em kg:', expand = False, border_style = 'bold yellow', style = 'bold yellow'))
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
                        c.print(Panel('Digite a sua altura em m:', expand = False, border_style = 'bold yellow', style = 'bold yellow'))
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
                    c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                    print(' ')
                    resultimc_text = Text()
                    resultimc_text.append('\n')
                    resultimc_text.append(f'O IMC calculado é {imc:.2f}\n', style = 'bold white')

                    if imc < 18.5:
                        status = 'Abaixo do peso'
                    elif 18.5 <= imc < 25:
                        status = 'Peso normal'
                    elif 25 <= imc < 30:
                        status = 'Sobrepeso'
                    else:
                        status = 'Obesidade'
                    
                    resultimc_text.append(f'Status: {status}', style = 'dim')
                    resultimc_text.append('\n')
                    painelresultimc_text = Panel(resultimc_text, expand = False, border_style = 'bold blue',title = '📊 Resultado')
                    painelresultimc_text_center = Align.center(painelresultimc_text)
                    c.print(painelresultimc_text_center)
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
        tmb_text = Text()
        tmb_text.append('\n')
        tmb_text.append('Calculadora de TMB (Taxa Metabólica Basal)',style = 'bold yellow')
        tmb_text.append('\nTaxa Metabólica Basal é o mínimo de calorias que seu corpo precisa em repouso.', style='dim')
        tmb_text.append('\n')
        p_tmbtext = Panel(tmb_text, title="TMB",title_align="center",border_style="bold blue",expand=False)
        p_tmbtext_center = Align.center(p_tmbtext)
        c.print(p_tmbtext_center)    

        c.print(Panel('Deseja calcular sua taxa metabólica basal (1), calcular outra qualquer (2), ou voltar (3)?', expand = False, border_style = 'bold yellow', style = 'bold yellow'))
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
                        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                        print(' ')
                        retornotmb1_text = Text()
                        
                        retornotmb1_text.append(f'Sua TMB é :({TMB:.2f})\n', style = 'bold white')
                        retornotmb1_text.append('O cálculo foi feito com base no seu sexo de identidade, pois você informou que está em transição hormonal há mais de 12 meses.',style = 'dim')
                        retornotmb1_text.append('\nApós esse tempo, a terapia hormonal tende a modificar significativamente o metabolismo, e por isso essa abordagem é mais precisa.',style = 'dim')
                        
                        pretornotmb1 = Panel(retornotmb1_text, expand = False, border_style = 'bold blue', title = 'Info')
                        pretornotmb1_center = Align.center(pretornotmb1)
                        c.print(pretornotmb1_center)
                        Utils.aguardar_volta()
                        continue

                    elif dados.get('tempo_transicao', 0) < 12:

                        tmb_m = (10 * peso) + (6.25 * altura_cm) - (5 * idade) + 5
                        tmb_f = (10 * peso) + (6.25 * altura_cm) - (5 * idade) - 161
                        TMB = (tmb_m + tmb_f) / 2
                        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                        print(' ')
                        retornotmb2_text = Text()
                        retornotmb2_text.append(f'Sua TMB é: {TMB:.2f} calorias (Resultado baseado na média entre os cálculos masculino e feminino.)\n',style = 'bold white')
                        retornotmb2_text.append('Utilizamos essa maneira, pois como você está em transição, seu corpo, fisiologicamente falando, está mudando gradualmente.',style = 'dim')
                        retornotmb2_text.append('\nA média entre TMB masculina e feminina representa um ponto intermediário mais realista para estimar a sua necessidade calórica durante essa fase.',style = 'dim')
                        pretornotmb2 = Panel(retornotmb2_text, expand = False, border_style = 'bold blue', title = 'Info')
                        pretornotmb2_center = Align.center(pretornotmb2)
                        c.print(pretornotmb2_center)
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
                c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                print(' ')
                retornotmb3_text = Text()
                retornotmb3_text.append(f'Sua TMB é :({TMB:.2f})\n', style = 'bold white')
                retornotmb3_text.append('O cálculo foi feito com base no seu sexo biológico, pois você indicou que não faz uso de terapia hormonal.',style = 'dim')
                retornotmb3_text.append('\nIsso é importante porque, sem o uso de hormônios, seu metabolismo segue padrões fisiológicos relacionados ao sexo biológico.', style = 'dim')
                pretornotmb3 = Panel(retornotmb3_text, expand = False, border_style = 'bold blue', title = 'Info')
                pretornotmb3_center = Align.center(pretornotmb3)
                c.print(pretornotmb3_center)
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
                c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                print(' ')
                retornotmb4_text = Text()
                retornotmb4_text.append(f'Sua TMB é :({TMB:.2f})\n', style = 'bold white')
                retornotmb4_text.append('O cálculo foi feito com base no sexo informado no seu cadastro.', style = 'dim')
                pretornotmb4_text = Panel(retornotmb4_text, expand = False, border_style = 'bold blue', title = 'Info')
                pretornotmb4_text_center = Align.center(pretornotmb4_text)
                c.print(pretornotmb4_text_center)
                Utils.aguardar_volta()
                continue

        elif calculartmb_visualizartmb == '2':

            while True:
                c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                print(' ')
                try:
                    c.print(Panel('[bold yellow]Digite o peso em quilogramas:[/bold yellow]', expand = False, border_style = 'bold yellow'))
                    pesoex = float(input('>>> '))
                    if pesoex > 350 or pesoex <= 0:
                        c.print(Panel('Digite um peso válido.',expand = False, border_style = 'red', title = '[b]ERRO[/b]', title_align = 'center'))
                        Utils.aguardar_volta()
                        continue
                except ValueError:
                        c.print(Panel('Digite apenas números', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                        Utils.aguardar_volta()
                        continue
                break
            
            while True:
                    
                    try:
                        c.print(Panel('[bold yellow]Digite a altura em centímetros:[/bold yellow]', expand = False, border_style = 'bold yellow'))
                        alturaex = float(input('>>> '))
                        if alturaex > 220 or alturaex <= 100:
                            c.print(Panel('Digite uma altura válida, em centímetros.', expand = False, border_style = 'red', title = '[b]ERRO[/b]', title_align = 'center'))
                            Utils.aguardar_volta()
                            continue
                    except ValueError:
                        c.print(Panel('Digite apenas números', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                        Utils.aguardar_volta()
                        continue
                    break
                    
            while True:

                    try:            
                        c.print(Panel('[bold yellow]Digite a idade:[/bold yellow]', expand = False, border_style = 'bold yellow'))
                        idadeex = int(input('>>> '))
                        if idadeex > 100 or idadeex <= 0:
                            c.print(Panel('Digite uma idade válida.', expand = False, border_style = 'red', title = '[b]ERRO[/b]', title_align = 'center'))
                            Utils.aguardar_volta()
                            continue
                    except ValueError:
                        c.print(Panel('Digite apenas números', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                        Utils.aguardar_volta()
                        continue
                    break
            
            resposta = 'n'
            
            while True:
                    try:
                        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                        print(' ') 
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
                        
                        opcaotextoidentidade = Text()
                        opcaotextoidentidade.append('Digite sua opção: ', style = 'bold yellow')
                        popcaotextoidentidade = Panel(opcaotextoidentidade, expand = False, border_style = 'bold yellow')
                        popcaotextoidentidade_center = Align.center(popcaotextoidentidade)
                        c.print(popcaotextoidentidade_center)
                        sexo_opcao = input('>>> ').strip()
            
                        if sexo_opcao not in ['1', '2', '3', '4']:
                            c.print(Panel('Opção inválida! Escolha 1-4', expand = False, border_style = 'red', title = '[b]ERRO[/b]', title_align = 'center'))
                            Utils.aguardar_volta()
                            continue
                    except ValueError:
                        c.print(Panel('Digite apenas números', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                        Utils.aguardar_volta()
                        continue
                    break
            
            while True:
                    try:
                    
                        em_transicao = False
                        tempo_transicao = 0
                        
                        if sexo_opcao in ['3', '4']:
                            c.print(Panel('[bold yellow]Você já fez uso de terapia hormonal? (s/n):[/bold yellow]', expand = False, border_style = 'bold yellow'))
                            resposta = input('>>> ').lower().strip()
                            if resposta not in ['s','n']:
                                c.print(Panel('Digite (s) ou (n).', expand = False, border_style = 'red', title = '[b]ERRO[/b]', title_align = 'center'))
                                Utils.aguardar_volta()
                                continue 
                    except ValueError:
                        c.print(Panel('Digite apenas números', border_style = "red", expand = False, title = "[b]ERRO[/b]", title_align="center"))
                        Utils.aguardar_volta()
                        continue
                    break
            
            while True:
                try:
                    em_transicao = resposta == 's'    
                    if em_transicao:
                        c.print(Panel('[bold yellow]Há quantos meses você faz uso?[/bold yellow]', expand = False, border_style = 'bold yellow'))
                        tempo_transicao = int(input('>>> '))
                        if tempo_transicao <= 0:
                            c.print(Panel('Digite um valor válido.', expand = False, border_style = 'red', title = '[b]ERRO[/b]', title_align = 'center'))
                            Utils.aguardar_volta()
                            continue
                except ValueError:
                        c.print(Panel('Digite um número válido.', expand = False, border_style = 'red', title = '[b]ERRO[/b]', title_align = 'center'))
                        Utils.aguardar_volta()
                        continue
                
                tmb_m = (10 * pesoex) + (6.25 * alturaex) - (5 * idadeex) + 5
                tmb_f = (10 * pesoex) + (6.25 * alturaex) - (5 * idadeex) - 161
            
                if sexo_opcao == '1':  
                    c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                    print(' ')
                    TMB = tmb_m
                    resultadotmbop1_text = Text()
                    resultadotmbop1_text.append(f'Sua TMB é: {TMB:.2f}')
                    painelresultadotmbop1_text = Panel(resultadotmbop1_text, expand = False, border_style = 'bold blue')
                    painelresultadotmbop1_text_center = Align.center(painelresultadotmbop1_text)
                    c.printt(painelresultadotmbop1_text_center)
                    
                elif sexo_opcao == '2':  
                    c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                    print(' ')
                    TMB = tmb_f
                    resultadotmbop2_text = Text()
                    resultadotmbop2_text.append(f'Sua TMB é: {TMB:.2f}')
                    painelresultadotmbop2_text = Panel(resultadotmbop2_text, expand = False, border_style = 'bold blue')
                    painelresultadotmbop2_text_center = Align.center(painelresultadotmbop2_text)
                    c.print(painelresultadotmbop2_text_center)
                    
                elif sexo_opcao == '3':  
                    if em_transicao and tempo_transicao >= 12:
                        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                        print(' ')
                        TMB = tmb_m  
                        resultadotmbop3_text = Text()
                        resultadotmbop3_text.append(f'Sua TMB é: {TMB:.2f}')
                        resultadotmbop3_text.append('\n✅ Cálculo feito com base no seu sexo atual, conforme sua identidade de gênero.', style = 'dim')
                        painelresultadotmbop3_text = Panel(resultadotmbop3_text, expand = False, border_style = 'bold blue')
                        painelresultadotmbop3_text_center = Align.center(painelresultadotmbop3_text)
                        c.print(painelresultadotmbop3_text_center)

                    elif em_transicao:
                        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                        print(' ')
                        TMB = (tmb_m + tmb_f) / 2  
                        resultadotmbop32_text = Text()
                        resultadotmbop32_text.append(f'Sua TMB é: {TMB:.2f}')
                        resultadotmbop32_text.append('\nComo sua transição é recente, usamos uma média para tornar o cálculo mais preciso.', style = 'dim')
                        painelresultadotmbop32_text = Panel(resultadotmbop32_text, expand = False, border_style = 'bold blue')
                        painelresultadotmbop32_text_center = Align.center(painelresultadotmbop32_text)
                        c.print(painelresultadotmbop32_text_center)

                    else:
                        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                        print(' ')
                        TMB = tmb_f  
                        resultadotmbop33_text = Text()
                        resultadotmbop33_text.append(f'Sua TMB é: {TMB:.2f}')
                        resultadotmbop33_text.append('\nComo não há uso de hormônios, o cálculo foi feito com base no sexo biológico.', style = 'dim')
                        painelresultadotmbop33_text = Panel(resultadotmbop33_text, expand = False, border_style = 'bold blue')
                        painelresultadotmbop33_text_center = Align.center(painelresultadotmbop33_text)
                        c.print(painelresultadotmbop33_text_center)
                        
                elif sexo_opcao == '4':  
                    
                    if em_transicao and tempo_transicao >= 12:
                        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                        print(' ')
                        TMB = tmb_f
                        resultadotmbop4_text = Text()
                        resultadotmbop4_text.append(f'Sua TMB é: {TMB:.2f}')
                        resultadotmbop4_text.append('\n✅ Cálculo feito com base no seu sexo atual, conforme sua identidade de gênero.',style = 'dim')  
                        painelresultadotmbop4_text = Panel(resultadotmbop4_text, expand = False, border_style = 'bold blue')
                        painelresultadotmbop4_text_center = Align.center(painelresultadotmbop4_text)
                        c.print(painelresultadotmbop4_text_center)

                    elif em_transicao:
                        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                        print(' ')
                        TMB = (tmb_m + tmb_f) / 2 
                        resultadotmbop41_text = Text()
                        resultadotmbop41_text.append(f'Sua TMB é: {TMB:.2f}') 
                        resultadotmbop41_text.append('\nComo sua transição é recente, usamos uma média para tornar o cálculo mais preciso.',style = 'dim')
                        painelresultadotmbop41_text = Panel(resultadotmbop41_text, expand = False, border_style = 'bold blue')
                        painelresultadotmbop41_text_center = Align.center(painelresultadotmbop41_text)
                        c.print(painelresultadotmbop41_text_center)

                    else:
                        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                        print(' ')
                        TMB = tmb_m
                        resultadotmbop42_text = Text()
                        resultadotmbop42_text.append(f'Sua TMB é: {TMB:.2f}')  
                        resultadotmbop42_text.append('\nComo não há uso de hormônios, o cálculo foi feito com base no sexo biológico.', style = 'dim')
                        painelresultadotmbop42_text = Panel(resultadotmbop42_text, expand = False, border_style = 'bold blue')
                        painelresultadotmbop42_text_center = Align.center(painelresultadotmbop42_text)
                        c.print(painelresultadotmbop42_text_center)
                
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
            registrodecal_text.append('Registro de calorias\n', style = 'bold blue')
            
            registrodecal_text.append(f'Data: {data_atual}', style = 'dim')
            registrodecal_text.append('\n')

            registrodecal_text.append('\n1. ', style = 'red')
            registrodecal_text.append('Adicionar calorias ao seu dia\n', style = 'bold white')

            registrodecal_text.append('2. ', style = 'red')
            registrodecal_text.append('Finalizar o dia\n', style = 'bold white')

            registrodecal_text.append('3. ', style = 'red')
            registrodecal_text.append('Ver histórico\n', style = 'bold white')

            registrodecal_text.append('4. ', style = 'red')
            registrodecal_text.append('Voltar', style = 'bold white')
            registrodecal_text.append('\n')

            pregistrodecal = Panel(registrodecal_text, border_style="bold blue", expand = False,title="[bold blue]🍽[/bold blue]",title_align="center")
            pregistrodecal_center = Align.center(pregistrodecal)
            c.print(pregistrodecal_center)

            opcaoregistrocal_text = Text()
            opcaoregistrocal_text.append('Digite uma opção (1-4):',style = 'bold yellow')
            painelopcaoregistrocal_text = Panel(opcaoregistrocal_text, expand = False, border_style = 'bold yellow')
            painelopcaoregistrocal_text_center = Align.center(painelopcaoregistrocal_text)
            c.print(painelopcaoregistrocal_text_center)
            opcao = input('>>> ').strip()

            if opcao == '1':
                c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                print(' ')
                perguntaadicaocalorias_text = Text()
                perguntaadicaocalorias_text.append(f'Total de calorias hoje: {user["calorias_hoje"]}/{TMB:.0f}')
                painelperguntaadicaocalorias_text = Panel(perguntaadicaocalorias_text, expand = False, border_style = 'bold blue')
                painelperguntaadicaocalorias_text_center = Align.center(painelperguntaadicaocalorias_text)
                c.print(painelperguntaadicaocalorias_text_center)

                c.print(Panel('[bold yellow]Quantas calorias você consumiu em sua última refeição?[/bold yellow]', expand = False, border_style = 'bold yellow'))
                cal = input('>>> ')
                cal = int(cal)

                if cal <= 0:
                    c.print(Panel('Ops, este não é um valor válido. Caso queira registrar suas calorias, digite um valor válido.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                    Utils.aguardar_volta()
                    continue

                user['calorias_hoje'] += cal  #aqui, as calorias são acumuladas.
                cadastro.salvar_dadosjson()
                feedbackcal_text = Text()
                feedbackcal_text.append(f'Você consumiu {cal} calorias.',style = 'bold white')
                feedbackcal_text.append(f'\nTotal hoje: {user["calorias_hoje"]}/{TMB:.0f}',style = 'bold white')
                pfeedbackcal = Panel(feedbackcal_text, expand = False, border_style = 'bold blue', title = 'FEEDBACK', title_align = 'center')
                pfeedbackcal_center = Align.center(pfeedbackcal)
                c.print(pfeedbackcal_center)
                Utils.aguardar_volta()
                Utils.limpar_tela_universal()

            elif opcao == '2':
                    c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                    print(' ')
                    c.print(Panel('[bold yellow]Deseja finalizar o seu dia ? Não poderá mais adicionar calorias ao dia de hoje. (s/n):[/bold yellow]', expand = False, border_style = 'bold yellow'))
                    es = input('>>> ').strip().lower()

                    if es == 's':
                        if data_atual not in user['historico_dias']:
                            user['historico_dias'][data_atual] = user['calorias_hoje']
                            cadastro.salvar_dadosjson()
                            c.print(Panel(f'Dia finalizado com sucesso! Total salvo: {user["calorias_hoje"]} calorias', expand = False, border_style = 'cyan'))
                            user['calorias_hoje'] = 0  #zerando a contagem para o próximo dia
                            
                            diferenca = user['historico_dias'][data_atual] - TMB  # Usamos o valor salvo no histórico
                            
                            if diferenca > 0:
                                respostadiferenca1 = Text()
                                respostadiferenca1.append(f'Você está {diferenca:.0f} calorias acima da sua TMB.')
                                painelrespostadiferenca1 = Panel(respostadiferenca1, expand = False, border_style = 'bold blue')
                                painelrespostadiferenca1_center = Align.center(painelrespostadiferenca1)
                                c.print(painelrespostadiferenca1_center)

                            elif diferenca < 0:
                                respostadiferenca2 = Text()
                                respostadiferenca2.append(f'Você está {abs(diferenca):.0f} calorias abaixo da sua TMB.')
                                painelrespostadiferenca2 = Panel(respostadiferenca2, expand = False, border_style = 'bold blue')
                                painelrespostadiferenca2_center = Align.center(painelrespostadiferenca2)
                                c.print(painelrespostadiferenca2_center)

                            else:
                                respostadiferenca3 = Text()
                                respostadiferenca3.append('Você consumiu exatamente sua TMB!')
                                painelrespostadiferenca3 = Panel(respostadiferenca3, expand = False, border_style = 'bold blue')
                                painelrespostadiferenca3_center = Align.center(painelrespostadiferenca3)
                                c.print(painelrespostadiferenca3_center)
                            
                            #dicas personalizadas de acordo com o objetivo do usuário.
                        
                            if objetivo == '1':  #ganho de massa
                                if diferenca > 0:
                                    analiseobj1_text = Text()
                                    analiseobj1_text.append('\n')
                                    analiseobj1_text.append('Análise do seu objetivo:', style = 'bold blue')
                                    analiseobj1_text.append('\n')
                                    analiseobj1_text.append('\nÓtimo! Superávit calórico ajuda no ganho de massa. MANTÉM! 😎')
                                    analiseobj1_text.append('\n💪 Alimente-se bem: priorize proteínas (frango, ovos, peixe), carboidratos complexos (arroz, batata-doce) e gorduras boas (azeite, castanhas)')
                                    analiseobj1_text.append('\n🛌 Descanse de verdade: dormir 7–9 horas por noite e ter dias de descanso são tão importantes quanto o treino e alimentação.')
                                    analiseobj1_text.append('\n')
                                    panaliseobj1 = Panel(analiseobj1_text, expand = False, border_style = 'bold blue', title = '🤓', title_align = 'center')
                                    panaliseobj1_center = Align.center(panaliseobj1)
                                    c.print(panaliseobj1_center)
                                    
                                else:
                                    analiseobj12_text = Text()
                                    analiseobj12_text.append('\n')
                                    analiseobj12_text.append('Análise do seu objetivo:', style = 'bold blue')
                                    analiseobj12_text.append('\n')
                                    analiseobj12_text.append('\nAtenção! Para ganhar massa, você precisa consumir mais que sua TMB.')
                                    analiseobj12_text.append('\n📅 Seja consistente: resultados vêm com treino e alimentação regulares, mantenha a disciplina.')
                                    analiseobj12_text.append('\n')
                                    panaliseobj12 = Panel(analiseobj12_text, expand = False, border_style = 'bold blue', title = '🤓', title_align = 'center')
                                    panaliseobj12_center = Align.center(panaliseobj12)
                                    c.print(panaliseobj12_center)
                                              
                            elif objetivo == '2':  #perda de peso
                                if diferenca < 0:
                                    analiseobj2_text = Text()
                                    analiseobj2_text.append('\n')
                                    analiseobj2_text.append('Análise do seu objetivo:', style = 'bold blue')
                                    analiseobj2_text.append('\n')
                                    analiseobj2_text.append('\nPerfeito! Déficit calórico é essencial para perda de peso. Continua assim! 👊')
                                    analiseobj2_text.append('\n🥗 Prefira alimentos naturais: invista em frutas, verduras, proteínas magras e evite ultraprocessados.')
                                    analiseobj2_text.append('\n🚶 Mexa-se regularmente: além da dieta, exercícios ajudam a acelerar o metabolismo e manter a massa magra.')
                                    analiseobj2_text.append('\n')
                                    panaliseobj2 = Panel(analiseobj2_text, expand = False, border_style = 'bold blue', title = '🤓', title_align = 'center')
                                    panaliseobj2_center = Align.center(panaliseobj2)
                                    c.print(panaliseobj2_center)

                                else:
                                    analiseobj22_text = Text()
                                    analiseobj22_text.append('\n')
                                    analiseobj22_text.append('Análise do seu objetivo:', style = 'bold blue')
                                    analiseobj22_text.append('\n')
                                    analiseobj22_text.append('\nCuidado! Para perder peso, você precisa consumir menos que sua TMB.')
                                    analiseobj22_text.append('\n🧐 Reavalie a alimentação: às vezes, pequenas “fugas” na dieta ou subestimativa das calorias podem impedir o progresso.')
                                    analiseobj22_text.append('\n⏳ Tenha paciência: perda de peso nem sempre é linear, o corpo pode demorar para responder — persistência é chave.')
                                    analiseobj22_text.append('\n')
                                    panaliseobj22 = Panel(analiseobj22_text, expand = False, border_style = 'bold blue', title = '🤓', title_align = 'center')
                                    panaliseobj22_center = Align.center(panaliseobj22)
                                    c.print(panaliseobj22_center)

                            else:  
                                if abs(diferenca) < (TMB * 0.1):  
                                    analiseobj3_text = Text()
                                    analiseobj3_text.append('\n')
                                    analiseobj3_text.append('Análise do seu objetivo:', style = 'bold blue')
                                    analiseobj3_text.append('\n')
                                    analiseobj3_text.append('\nExcelente! Você está mantendo um bom equilíbrio. ✍')
                                    analiseobj3_text.append('\n🔄 Mantenha a rotina saudável: hábitos consistentes geram resultados duradouros, então não deixe a disciplina cair.')
                                    analiseobj3_text.append('\n')
                                    panaliseobj3 = Panel(analiseobj3_text, expand = False, border_style = 'bold blue', title = '🤓', title_align = 'center')
                                    panaliseobj3_center = Align.center(panaliseobj3)
                                    c.print(panaliseobj3_center)

                                else:
                                    analiseobj32_text = Text()
                                    analiseobj32_text.append('\n')
                                    analiseobj32_text.append('Análise do seu objetivo:', style = 'bold blue')
                                    analiseobj32_text.append('\n')
                                    analiseobj32_text.append('\nPara manutenção de sua sáude, tente ficar próximo da sua TMB.')
                                    analiseobj32_text.append('\n📅 Faça exames periódicos: prevenção é sempre o melhor remédio, mantenha suas consultas em dia.')
                                    analiseobj32_text.append('\n🚭 Evite hábitos nocivos: reduza ou elimine álcool, cigarro e outras substâncias que prejudicam a saúde.')
                                    analiseobj32_text.append('\n')
                                    panaliseobj32 = Panel(analiseobj32_text, expand = False, border_style = 'bold blue', title = '🤓', title_align = 'center')
                                    panaliseobj32_center = Align.center(panaliseobj32)
                                    c.print(panaliseobj32_center)

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
                        continue

            elif opcao == '3':
                c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                print(' ')
                historico_text = Text()
                historico_text.append('\n')
                historico_text.append('📅 HISTÓRICO DE CONSUMO:\n', style = 'bold white')
                historico_text.append('\n')

                if not user['historico_dias']:
                    c.print(Panel('Nenhum registro encontrado.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))

                else:
                    for data, total in user['historico_dias'].items():
                        historico_text.append(f'{data}: {total} calorias', style = 'dim')
                        historico_text.append('\n')
                        painelhistorico_text = Panel(historico_text, expand = False, border_style = 'bold blue')
                        painelhistorico_text_center = Align.center(painelhistorico_text)
                        c.print(painelhistorico_text_center)

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