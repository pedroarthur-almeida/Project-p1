import json
from usuario import Usuario

class GerenciarJson:
    def salvar_dadosjson(self, dados):
        dados_convertidos = {}
        for email, usuario in dados.items():
            if isinstance(usuario, dict):
                # converte de dict para objeto antes de salvar
                usuario = Usuario.from_dict(usuario)
            dados_convertidos[email] = usuario.to_dict()

        with open('usuarios.json', 'w') as arquivo:
            json.dump(dados_convertidos, arquivo, indent=4)

    def carregar_dadosjson(self):
        try:
            with open('usuarios.json', 'r') as arquivo:
                dados = json.load(arquivo)
                return {email: Usuario.from_dict(info) for email, info in dados.items()}
        except FileNotFoundError:
            return {}
