# 🧑‍💻 Sistema Login em Backend
##Sistema de login em backend para desenvolvimento de conhecimento e absorção de práticas funcionais

Este projeto tem por finalidade a pratica de fundamentos procedurais e logica de programação usando funções basicas da linguagem escolhida para este fim.

Objetivo: Dominar os conceitos procedurais e logica, utilizando como desafios apenas os seguintes Tópicos:
-	Variáveis, Tipos de Dados, Operadores
-	Estruturas de Controle (if, for, while)
-	Funções e Módulos
-	Listas, Tuplas, Dicionários e Conjuntos
-	Manipulação de Arquivos JSON
-	Tratamento de Exceções

# 🚀 Tecnologias Utilizadas
- **Python**
- **Bibliotecas:** Hashlib, json, getpass, os, time
- **Outros Ferramentas:**
  - **Draw.io - app.diagrams.net** (Ferrameta criação de design de UML e diagramas)
  - **Frontend:** Utilize o prompt da sua escolha para executar o sistema no windows: powershell/CMD e Linux use terminal de sua escolha.
    Obs: Devido a utilização da função **getpass** que oculta preencimento de senha, pode ocorre de não funcionar em alguns prompts exemplo de IDEs como pycharm, ja no Windows funcionou de boa.
    
# 🗺️Arquitetura e Design do projeto, regras de negocios
## Sistema em backend, com estrutura de monolito, com base para persistir dados em arquivo JSON
![Arquitetura e Diagramas](Login_x_Diagrama.drawio.png)

# 🎲 Como usar o sistema
## 1. Clone o repositório:
```bash
git clone https://github.com/zantech-pro/sistema_login_backend.git
```
## 2. Execute o Sistema:
```bash
python login.py
```
# 🖥️ Capturas de Tela
**Menu Inicial**<br/>
![tela de Menu](prints/tela_login.png)

**Tela de Autenticação**<br/>
![tela de autenticação](prints/area_autenticacao.png)

**Tela de Visualização do sistema**<br/>
![Tela Recuperação](prints/area_de_recuperar.png)

**Após rodar o sistema aparecera a base JSON (Exemplo abaixo, ela ja com cadastros de usuarios)**<br/>
```json
[
    {
        "user": "joaostartup",
        "password": "15e2b0d3c33891ebb0f1ef609ec419420c20e320ce94c65fbc8c3312448eb225",
        "email": "joao@startup.com.br",
        "palavra_secreta": "Startup na alta",
        "nome_full": "João Startup",
        "date_birth": "31/12/1999",
        "id": 1
    },
    {
        "user": "mariadevjava",
        "password": "8a9bcf1e51e812d0af8465a8dbcc9f741064bf0af3b3d08e6b0246437c19f7fb",
        "email": "maria.dev@devjava.com.br",
        "palavra_secreta": "Maria programa em java",
        "nome_full": "Maria dev Java",
        "date_birth": "22/09/1989",
        "id": 2
    },
    {
        "user": "enzonoob123",
        "password": "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9",
        "email": "juninho@jovemenrolado.com.br",
        "palavra_secreta": "Minha senha e admin123",
        "nome_full": "Enzo junior",
        "date_birth": "01/04/2015",
        "id": 3
    }
]
```

📌 Funcionalidades

✅ Tratamentos de validação por meio de if-else e time

✅ Manipulação de JSON para leitura, escrita e alteração (CRUD)

✅ Utilização de biblioteca hashlib para crião dos hash256. 

✅ Algoritimo para criação de IDs e tratamento de listas e dicionarios


📜 Licença
Este projeto foi feito com carinho e é de uso pessoal. Caso tenha interesse, entre em contato!

Meu telegram: [@zandermais](https://t.me/zandermais)

📧: dev@zantech.com.br


