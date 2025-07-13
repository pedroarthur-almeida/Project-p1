class Usuario:
    def __init__(self, email, senha, nome, objetivo = None, dados = None, calorias_hoje = 0, historico_dias = None):
        self.email = email
        self.senha = senha
        self.nome = nome
        self.objetivo = objetivo
        self.dados = dados
        self.calorias_hoje = calorias_hoje
        self.historico_dias = historico_dias
        self.TMB = None
        
    @classmethod
    def from_dict(cls, dados_usuario):
        obj = cls(
            email=dados_usuario.get("email"),
            senha=dados_usuario.get("senha"),
            nome=dados_usuario.get("nome"),
            objetivo=dados_usuario.get("objetivo"),
            dados=dados_usuario.get("dados"),
            calorias_hoje=dados_usuario.get("calorias_hoje", 0),
            historico_dias=dados_usuario.get("historico_dias", {})
        )
        obj.TMB = dados_usuario.get("TMB")
        return obj
    
    def to_dict(self):
        return {
            "email": self.email,
            "senha": self.senha,
            "nome": self.nome,
            "objetivo": self.objetivo,
            "dados": self.dados,
            "calorias_hoje": self.calorias_hoje,
            "historico_dias": self.historico_dias,
            "TMB": self.TMB,
        }