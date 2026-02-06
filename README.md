RPA Sicredi

Projeto de automação (RPA) desenvolvido para o desafio técnico, responsável por extrair informações da aba produtos do site **Sicredi Conexão** e estruturá-las em um arquivo CSV.

## Pré-requisitos

- **Python:** Versão **3.12** ou superior.
- **Navegador:** Google Chrome instalado.

---

## Instalação e Configuração

Siga os passos abaixo para configurar o ambiente de desenvolvimento no Windows.

### 1. Clonar o repositório

Abra o terminal e clone o projeto:

```bash
git clone git@github.com:lgjohann/desafio_tecnico_sicredi_1.git
cd rpa_sicredi
```

### 2. Criar o Ambiente Virtual

```bash
python -m venv .venv
```

### 3. Ativar o Ambiente Virtual


**No PowerShell:**

```bash
.\.venv\Scripts\Activate.ps1
```

**No CMD:**

```bash
.\.venv\Scripts\Activate.bat
```


_Em caso de erro de permissão para execução de scripts, execute este comando para liberar a execução e tente novamente:_
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```


### 4. Instalar Dependências

```
pip install -r requirements.txt
```

---

## Como Rodar

Com o ambiente virtual ativo (`.venv`), execute o arquivo principal:


```bash
python main.py
```

### O que o robô fará?

1. Verificará se o arquivo CSV de destino existe. Se não exitir, ele criará um novo com os cabeçalhos.

2. Abrirá o navegador Chrome controlado pelo sistema.

3. Navegará até o site do Sicredi Conexão e extrairá os itens e respectivos links de cada uma das três categorias da aba Produtos.

4. Salvará os dados extraídos no arquivo `.csv` localmente.


---
