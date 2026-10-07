# Sistema de Cadastro via Terminal com Validação e Persistência de Dados

Este é um sistema de cadastro interativo desenvolvido em **Python** que roda diretamente na linha de comando (CLI). O projeto foi construído para praticar conceitos fundamentais de lógica de programação, manipulação de arquivos locais e validação de dados de entrada do usuário.

## 🚀 Funcionalidades

- **Questionário Interativo:** Coleta de informações básicas (Nome, Idade, Endereço, E-mail e Celular).
- **Validação de CPF:** Loop interno que garante que o CPF contenha exatamente 11 dígitos e seja composto apenas por números.
- **Confirmação de Dados:** Exibe um resumo estruturado para o usuário validar as informações antes de salvar.
- **Fluxo de Repetição:** Se o usuário notar algum erro e responder "Não" na confirmação, o sistema reinicia o questionário automaticamente.
- **Persistência em Arquivo:** Salva os dados confirmados em um arquivo de texto local (`usuarios_cadastrados.txt`) usando o modo *append* (não sobrescreve cadastros anteriores).

## 🛠️ Tecnologias e Conceitos Aplicados

- **Linguagem:** Python 3
- **Estruturas de Repetição:** Loops aninhados (`while True`) para controle de fluxo e validação contínua.
- **Manipulação de Arquivos (I/O):** Uso do gerenciador de contexto `with open()` para escrita segura de dados.
- **Tratamento de Strings:** Métodos como `.strip()` para remover espaços em branco e `.upper()` para padronizar respostas.

## 📁 Como Executar o Projeto

1. Certifique-se de ter o Python instalado em sua máquina (preferencialmente Python 3.x).
2. Clone este repositório ou baixe o arquivo do script:
   ```bash
   git clone https://github.com
   ```
3. Navegue até a pasta do projeto e execute o script no terminal:
   ```bash
   python nome_do_arquivo.py
   ```
4. Siga as instruções exibidas na tela do terminal. Após a confirmação positiva (`S`), o arquivo `usuarios_cadastrados.txt` será criado na mesma pasta com os dados salvos.

## 📝 Exemplo de Saída no Arquivo
```text
Nome: João Silva | Idade: 25 | CPF: 12345678901 | Celular: 11999999999 | Email: joao@email.com | Endereço: Rua Flores, 123
```

---
Desenvolvido como parte dos meus estudos em Engenharia de Software e Programação com Python 🚀
