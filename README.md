🌿 EcoSystem - Sistema de Gestão de Coletas

O EcoSystem é uma plataforma web desenvolvida para modernizar a gestão de solicitações de coleta de resíduos. O sistema conecta uma interface web moderna a um banco de dados corporativo pré-existente, permitindo que empresas abram e gerenciem chamados de forma ágil e segura.

🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando uma stack robusta para garantir integridade de dados e uma boa experiência de usuário:

Linguagem: Python 3.11+

Back-end Framework: Django 5.x (MVT Architecture)

Banco de Dados: PostgreSQL

Front-end: HTML5, CSS3, Bootstrap 5 (Design Responsivo)

Controle de Versão: Git & GitHub

🏛️ Banco de Dados e Modelagem

O diferencial deste projeto é a integração com uma estrutura de dados legada. O desenvolvimento não partiu de um banco vazio, mas sim da necessidade de conectar uma aplicação nova a tabelas que já continham histórico e regras de negócio.

1. Importação e Mapeamento dos Models

A camada de dados (Models) do sistema foi construída através do mapeamento direto das tabelas existentes no PostgreSQL.

O sistema espelha a estrutura exata do banco de dados original (nomes de tabelas e colunas).

Isso permite que a aplicação leia e grave dados sem a necessidade de migração de dados ou alteração na estrutura física das tabelas principais, garantindo que outros sistemas que usam o mesmo banco continuem funcionando.

2. Relacionamento entre Entidades

A lógica de negócio do sistema depende estritamente das Chaves Estrangeiras (Foreign Keys) definidas no banco:

Autenticação e Perfil:

A tabela Usuario contém as credenciais de acesso.

A tabela Empresa possui uma chave estrangeira apontando para Usuario.

A tabela Funcionario também aponta para Usuario.

No Login: O sistema verifica se o ID do usuário autenticado existe na tabela de Empresas ou de Funcionários para definir as permissões de acesso.

Fluxo de Solicitação:

Empresa -> Solicitação: Cada registro na tabela Solicitacoleta é vinculado obrigatoriamente ao ID da Empresa logada na sessão. Isso garante o isolamento dos dados (uma empresa não vê os chamados da outra).

Integridade em Cascata: O sistema respeita a cadeia de dependência: Solicitacoleta -> gera Coleta -> gera Autorizacao.

⚙️ Funcionalidades do Sistema

O módulo principal foca no Ciclo de Vida da Solicitação de Coleta:

Abertura de Chamado:

Interface simplificada onde a empresa informa apenas a descrição e o tipo de resíduo.

O sistema preenche automaticamente a data e vincula o cliente.

Monitoramento (Listagem):

Visualização clara dos chamados com indicadores visuais de status (Aberto, Em Andamento, Concluído).

Segurança na Exclusão (Regras de Negócio):

O sistema impede a exclusão de solicitações que já avançaram no fluxo de trabalho.

Se uma solicitação já possui registros filhos (como uma coleta agendada), o sistema intercepta o erro de integridade do banco e avisa o usuário que a exclusão não é permitida, preservando o histórico.

🚀 Como Rodar o Projeto

Siga os passos abaixo para executar o ambiente de desenvolvimento:

Clone o repositório:

git clone [https://github.com/SEU-USUARIO/ecosystem.git](https://github.com/SEU-USUARIO/ecosystem.git)
cd ecosystem


Crie e ative o ambiente virtual:

python -m venv venv

# Windows:
.\venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate


Instale as dependências:

pip install -r requirements.txt


Configure o Banco de Dados:
Certifique-se de que o PostgreSQL está rodando e configure as credenciais no arquivo settings.py.

Execute o servidor:

python manage.py runserver


Acesse em seu navegador: http://127.0.0.1:8000/
