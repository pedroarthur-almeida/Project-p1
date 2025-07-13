import os
import platform

class Utils:
    @staticmethod
    def limpar_tela_universal():
        sistema_operacional = platform.system()
        if sistema_operacional == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    @staticmethod
    def aguardar_volta():
        """Pausa a execução do programa até que o usuário tecle "enter".""" 
        input('\nPressione a tecla "enter" para continuar...')

    