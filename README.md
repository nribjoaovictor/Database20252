# 🌿 EcoSystem — Sistema de Gestão de Coletas
O **EcoSystem** é uma plataforma web desenvolvida para modernizar o processo de solicitações e gerenciamento de coletas de resíduos. A solução integra uma interface web moderna a um banco de dados corporativo **já existente**, permitindo que empresas registrem e acompanhem pedidos de coleta com agilidade e segurança.

## 🛠 Tecnologias Utilizadas
| Tecnologia | Descrição |
|----------|-----------|
| **Python 3.11+** | Linguagem principal |
| **Django 5.x** | Framework backend (Arquitetura MVT) |
| **PostgreSQL** | Banco de dados utilizado |
| **HTML5, CSS3, Bootstrap 5** | Interface responsiva |
| **Git & GitHub** | Versionamento do projeto |

## 🏛 Banco de Dados e Modelagem
O diferencial do projeto é a **integração direta com um banco legado**. Ao invés de criar uma nova base, o sistema foi desenvolvido para **consumir o banco já existente**, preservando dados históricos e garantindo compatibilidade com outros sistemas internos.

### 🔹 Importação e Mapeamento dos Models
- Models foram criados espelhando fielmente as tabelas do PostgreSQL.
- Estrutura e nomes originais foram preservados.
- Não houve necessidade de migração ou alteração do banco físico.
- O sistema consegue ler e gravar informações sem interromper aplicações externas.

### 🔹 Relacionamento entre Entidades
**Autenticação e Perfil**
- `Usuario` contém credenciais de login.
- `Empresa` e `Funcionario` possuem relacionamento com `Usuario`.
- Durante o login o sistema identifica o tipo de usuário e define permissões.

**Fluxo de Solicitação**
Empresa → Solicitação → Coleta → Autorização

- Cada solicitação pertence exclusivamente à empresa logada.
- Uma empresa **não visualiza solicitações de outra empresa**.
- Integridade garantida por relações em cascata.

## ⚙ Funcionalidades Principais
- **Abertura de Solicitação:** descrição e tipo do resíduo informados pelo usuário.
- **Monitoramento:** listagem com status (Aberto / Em andamento / Concluído).
- **Segurança na Exclusão:** solicitações com coletas vinculadas **não podem ser excluídas**.

## 🚀 Como Rodar o Projeto
### 1. Clonar o repositório
```bash
git clone https://github.com/SEU-USUARIO/ecosystem.git
cd ecosystem
```

### 2. Ambiente virtual
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar banco
Editar `settings.py` com as credenciais do PostgreSQL.

### 5. Iniciar servidor
```bash
python manage.py runserver
```

Acesse: **http://127.0.0.1:8000/**
