class Usuario:
    def __init__(self, email, senha, nome, objetivo = None, dados = None, calorias_hoje = 0, historico_dias = None,agua_hoje=0,
        meta_agua=0, historico_agua=None, quiz_progresso=None):
        self.email = email
        self.senha = senha
        self.nome = nome
        self.objetivo = objetivo
        self.dados = dados
        self.calorias_hoje = calorias_hoje
        self.historico_dias = historico_dias
        self.TMB = None
        self.agua_hoje = agua_hoje
        self.meta_agua = meta_agua
        self.historico_agua = historico_agua or {}
        self.quiz_progresso = quiz_progresso or {}

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
        obj.agua_hoje = dados_usuario.get("agua_hoje", 0)
        obj.meta_agua = dados_usuario.get("meta_agua", 0)
        obj.historico_agua = dados_usuario.get("historico_agua", {})
        obj.quiz_progresso = dados_usuario.get("quiz_progresso", {})
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
            "agua_hoje": self.agua_hoje,
            "meta_agua": self.meta_agua,
            "historico_agua": self.historico_agua,
            "quiz_progresso": getattr(self, "quiz_progresso", {})
        }