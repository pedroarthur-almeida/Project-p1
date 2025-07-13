from rich.align import Align            
from rich.columns import Columns
import random
from calc_user import *


class Menus:
    pass

def menu_principal(usuarios, usuario_logado = None):
    """
    Menu inicial,
    é exibido logo após iniciar o programa,
    abre ao usuário as opções de cadastro e login.
    """
    Utils.limpar_tela_universal()
 
    while True:
        
        c.rule('[blue][i][b]Boas vindas ao VitalTrack![/b][/i][/]')
        print(' ')
        textomenuprincipal_text = Text()

        textomenuprincipal_text.append('\n')
        textomenuprincipal_text.append('Seja bem vindo(a) ao menu inicial!\n', style = 'bold yellow')
        textomenuprincipal_text.append('\nEscolha uma opção dentre as disponíveis.\n', style = 'dim')

        textomenuprincipal_text.append('\n1 ', style = 'red')
        textomenuprincipal_text.append('Cadastro\n')

        textomenuprincipal_text.append('2 ', style = 'red')
        textomenuprincipal_text.append('Login\n')

        textomenuprincipal_text.append('3 ', style = 'red')
        textomenuprincipal_text.append('Sair\n')

        panel = Panel(textomenuprincipal_text, border_style="bold blue", expand = False,title="[bold blue]Menu Inicial[/bold blue]",
    title_align="center")
        panel_centralizado = Align.center(panel)
        c.print(panel_centralizado)

        entradamenu_principal = Text()
        entradamenu_principal.append('Digite sua opção: ', style = 'yellow')

        pentradamenu_principal = Panel(entradamenu_principal, expand = False, border_style = 'yellow')
        pentradamenu_principal_center = Align.center(pentradamenu_principal)
        c.print(pentradamenu_principal_center)

        opçao1 = input('>>> ')

        if opçao1 == '1':
            with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
    "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner = 'hearts'):  
                    time.sleep(2)
            usuario_logado = cadastro.cadastro_de_usuario()
            if usuario_logado:
                menu_logado(cadastro, usuario_logado, usuarios)
                     
        elif opçao1 == '2':
            with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
    "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner = 'hearts'):  
                    time.sleep(2)
            usuario_logado = cadastro.fazer_login()
            if usuario_logado:  
                with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
                "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner='hearts'):  
                    time.sleep(3)
                menu_logado(cadastro, usuario_logado, usuarios)  
                
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
            Utils.aguardar_volta()
    return usuarios, usuario_logado

def menu_logado(cadastro, usuario_logado, usuarios):
    """
    Menu onde o usuário tem acesso as funcionalidades do programa,
    só é possível ter acesso a esse menu após o login.
    """
    while True:
        Utils.limpar_tela_universal()
        c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
        print(' ')

        nome = cadastro.usuarios[usuario_logado].nome
        saude = SaudeCorporal(usuarios, usuario_logado, cadastro)

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
            verpefil_text.append('Dados:')
            verpefil_text.append('\n')
            verpefil_text.append(f'\n👤 Nome: {cadastro.usuarios[usuario_logado].nome}',style='bold white')
            verpefil_text.append(f'\n📧 Email: {usuario_logado}',style='bold white')

            objetivos = {
                '1': 'GANHO DE MASSA',
                '2': 'PERDA DE PESO',
                '3': 'MANUTENÇÃO DA SAÚDE'
                                        }
            if cadastro.usuarios[usuario_logado].dados:
                dados = cadastro.usuarios[usuario_logado].dados
                objetivo_id = cadastro.usuarios[usuario_logado].objetivo 
                verpefil_text.append(f'\n🎯 Objetivo: {objetivos.get(objetivo_id, "Não definido")}',style='bold white')
                verpefil_text.append(f'\n🎂 Idade: {dados["idade"]} anos',style='bold white')
                verpefil_text.append(f'\n💪 Peso: {dados["peso"]} kg',style='bold white')
                verpefil_text.append(f'\n📏 Altura: {dados["altura"]} m',style='bold white')
                
                pverperfil = Panel(verpefil_text, border_style="bold blue", expand = False,title="📝 Perfil",
    title_align="center")
                
                sexo_escolha = dados.get('sexo_escolha', None)

                if sexo_escolha in ['1', '3']:  # homem cis ou homem trans
                    sexo_exibicao = 'Masculino'

                elif sexo_escolha in ['2', '4']:  # mulher cis ou mulher trans
                    sexo_exibicao = 'Feminino'

                else:
                    sexo_exibicao = 'Não informado'
            verpefil_text.append(f'\n⚪ Sexo: {sexo_exibicao}',style='bold white')  
            pverperfil_center = Align.center(pverperfil)      
            c.print(pverperfil_center)    
            Utils.aguardar_volta()
            with c.status("[red]S[/red][magenta]a[/magenta][yellow]i[/yellow]"
                "[green]n[/green][cyan]d[/cyan][blue]o[/blue]", spinner = 'hearts'):  
                time.sleep(2)
                Utils.limpar_tela_universal()

        elif opcao == '2':
            with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
                "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner = 'hearts'):  
                time.sleep(2)
            saude.calcular_imc(cadastro, usuario_logado)

        elif opcao == '3':
            with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
                "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner = 'hearts'):  
                time.sleep(2)
            saude.calcular_taxametabolicabasal(cadastro.usuarios, usuario_logado)

        elif opcao == '4':
            with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
                "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner = 'hearts'):  
                time.sleep(2)
            usuarios, usuario_logado = saude.registrar_calorias(cadastro.usuarios, usuario_logado)

        elif opcao == '5':
            with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
                "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner = 'hearts'):  
                time.sleep(2)
            usuarios, usuario_logado = cadastro.atualizar_usuario(cadastro.usuarios, usuario_logado)

        elif opcao == '6':
            with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
                 "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner = 'hearts'):  
                time.sleep(2)
            print('\nAtualizando dados...')
            usuarios, usuario_logado = cadastro.atualizar_dados(usuario_logado)
            cadastro.usuarios = usuarios

        elif opcao == '7':
            with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
                "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner = 'hearts'):  
                time.sleep(2)

            while True:
                c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                print(' ')
                c.print(Panel('[bold yellow]Deseja mesmo deslogar? (s/n)[/bold yellow]', expand = False, border_style = 'bold yellow'))
                deslog = input('>>> ').strip()

                if deslog == 's':
                    usuario_logado = None
                    deslogado_text = Text()
                    deslogado_text.append('Deslogado com sucesso!', style = 'bold white')
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
                    permanecelogado_text.append('Você permanece logado.', style = 'bold white')
                    painelpermanecelogado_text = Panel(permanecelogado_text, expand = False, border_style = 'bold blue')
                    painelpermanecelogado_text_center = Align.center(painelpermanecelogado_text)
                    c.rule('\n[blue][b][i]VitalTrack[/i][/][/]')
                    print(' ')
                    c.print(painelpermanecelogado_text_center) 
                    Utils.aguardar_volta()
                    Utils.limpar_tela_universal()
                    break
                
                else:
                    c.print(Panel('Digite "s" ou "n".', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
                    Utils.aguardar_volta()
                   
        elif opcao == '8':
            with c.status("[red]C[/red][magenta]a[/magenta][yellow]r[/yellow][green]r[/green]"
                "[cyan]e[/cyan][blue]g[/blue][red]a[/red][magenta]n[/magenta][yellow]d[/yellow][green]o[/green]", spinner = 'hearts'):  
                time.sleep(2)
            usuarios, usuario_logado = cadastro.deletar_usuario(usuario_logado, cadastro.usuarios)
            if usuario_logado is None:
                Utils.aguardar_volta()
                Utils.limpar_tela_universal()
                return 
        else:
            c.print(Panel('Opção inválida! Digite um número de 1 a 8.', expand = False, border_style = 'red', title = 'ERRO', title_align = 'center'))
            Utils.aguardar_volta()
            Utils.limpar_tela_universal()