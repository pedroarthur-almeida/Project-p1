# VitalTrack
- Projeto do primeiro período do Bacherelado em Sistemas de Informação.

# Descrição: 
- VitalTrack é um sistema desenvolvido em Python que oferece uma interface interativa no terminal, com foco no acompanhamento da saúde e na promoção de hábitos saudáveis. O programa conta com funcionalidades como registro de calorias, cálculo do Índice de Massa Corporal (IMC) e da Taxa Metabólica Basal (TMB). Um dos principais diferenciais do VitalTrack é seu caráter inclusivo: o sistema foi projetado para considerar informações específicas de pessoas trans no cálculo da TMB, promovendo um acompanhamento mais justo e personalizado. Com isso, o projeto busca unir tecnologia, saúde e inclusão em uma ferramenta acessível e eficiente.

# Tecnologias utilizadas:
- Python 3.13.3

# Bibliotecas Python utilizadas:
- rich – Para formatação avançada no terminal (cores, painéis, textos estilizados, etc.).
- datetime – Para manipulação de datas (registro de calorias por dia).
- json – Para salvar e carregar dados dos usuários em arquivos .json.
- time – Para pausas (time.sleep) e efeitos de carregamento.
- random – Para selecionar mensagens motivacionais aleatórias.
- prompt_toolkit – Para entrada de senha oculta (segurança no login).

# Funcionalidades principais:
- ✅ Cadastro/login de usuários, com CRUD completo, fluxos de erros e validações.
- 📊 Cálculo de IMC e TMB (com suporte a pessoas trans) e feedback relativo ao objetivo do usuário.
- 🔥 Registro diário de calorias, também integrado ao sistema de objetivos.
- 📅 Histórico de consumo de calorias, referente ao dia.
- 💡 Feedback personalizado (ganho de massa, perda de peso ou manutenção).

# Instalação
1. Clone o repositório:
```
git clone https://github.com/pedroarthur-almeida/projetop1.git
```
2. Instale as dependências:
```
pip install -r requirements.txt
```
3. Execute:
```
python project1.py
```

# Crie um ambiente virtual (recomendado):
- No Windows:
```
python -m venv venv
venv\Scripts\activate
```
- No Mac/Linux:
```
python -m venv venv
source venv/bin/activate
```
# Destaques e diferenciais do VitalTrack:
- Inclusivo: Cálculos adaptados para pessoas trans em terapia hormonal.
- Offline: Dados salvos localmente em usuarios.json.
- Feedback inteligente: Dicas personalizadas por objetivo.

# Screenshots do VitalTrack:
- Menu logado
![Menu logado](imgs/menulogado.png)






  
