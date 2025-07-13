usuario_logado = None 
from user_management import *
from menus import *
          
if __name__ == "__main__":
    cadastro = GerenciarUsuario()  
    usuario_logado = None
    menu_principal(cadastro, usuario_logado)