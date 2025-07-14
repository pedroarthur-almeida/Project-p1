from gerenciar_usuario import *
from menus import *
m = Menus(cadastro)
          
if __name__ == "__main__":
    cadastro = GerenciarUsuario()  
    m.exibir_menu_inicial(cadastro)