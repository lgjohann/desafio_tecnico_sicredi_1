RPA Sicredi

Projeto de automação (RPA) desenvolvido para o desafio técnico, responsável por extrair informações de produtos do site Sicredi Conexão e estruturá-las em um arquivo CSV.

# Pré-requisitos
Sistema Operacional: Windows 10/11

Python: Versão 3.12 ou superior.

Navegador: Google Chrome instalado.

Nota: Não é necessário baixar o ChromeDriver manualmente. O projeto gerencia isso automaticamente.

🚀 Instalação e Configuração
Siga os passos abaixo para configurar o ambiente de desenvolvimento no Windows.

1. Clonar o repositório
   Abra o terminal e clone o projeto (ou baixe e extraia o zip):

PowerShell
git clone <URL_DO_SEU_REPOSITORIO>
cd rpa_sicredi
2. Criar o Ambiente Virtual
   O ambiente virtual isola as bibliotecas do projeto para não conflitar com outras instalações do seu Python. Execute:

PowerShell
python -m venv .venv
3. Ativar o Ambiente Virtual
   Este passo é obrigatório toda vez que for rodar o projeto.

No PowerShell:

PowerShell
.\.venv\Scripts\Activate.ps1
Se receber um erro de permissão (vermelho), execute este comando para liberar a execução de scripts e tente ativar novamente:

PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
No CMD (Prompt de Comando):

DOS
.venv\Scripts\activate.bat
(Ao ativar, você verá (.venv) no início da linha do terminal)

4. Instalar Dependências
   Com o ambiente ativo, instale todas as bibliotecas necessárias (Selenium, Pandas, etc.):

PowerShell
pip install -r requirements.txt
▶️ Como Rodar
Com o ambiente virtual ativo (.venv), execute o arquivo principal:

PowerShell
python main.py
O que o robô fará?
Verificará se o arquivo CSV de destino existe. Se não, ele cria um novo com os cabeçalhos.

Abrirá o navegador controlado pelo sistema.

Navegará até o site do Sicredi e extrairá as categorias, itens e links.

Salvará os dados extraídos no arquivo .csv localmente.