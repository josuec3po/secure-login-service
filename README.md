# Secure Auth Logic (Bcrypt + SQLite)

### Sobre o Projeto

Este é um projeto de estudo focado nos fundamentos de segurança e persistência de dados para sistemas de autenticação. O objetivo foi evoluir de uma lógica simples de comparação de strings para um sistema robusto, modularizado e que utiliza técnicas reais de mercado para proteger as credenciais dos utilizadores.

---

### Tecnologias e Ferramentas

* **Python 3.x**: Linguagem principal.
* **Bcrypt**: Biblioteca de hashing para proteção de palavras-passe.
* **SQLite3**: Base de dados relacional para persistência de dados.

---

### Funcionalidades Atuais

* [x] Conexão e criação automatizada de tabelas em base de dados SQLite.
* [x] Geração de Hash de senhas (`bcrypt_hash`) com fator de custo (rounds=12) e encoding UTF-8.
* [x] Verificação segura de senhas (`verify_password`) comparando o input do utilizador com o hash.
* [x] Arquitetura modularizada usando funções para facilitar a manutenção e leitura do código.

---

### Diário de Desenvolvimento (DevLog)

Nesta secção, documento a evolução do projeto e os desafios superados:

#### **Dia 1: O Mínimo Produto Viável (MVP)**

* Comecei com uma estrutura básica de `if/else` usando listas estáticas para validar login e senha.
* **Aprendizado:** Entendi que listas na memória perdem os dados ao fechar o programa.

#### **Dia 2: Segurança e Hashing**

* Implementei a biblioteca `bcrypt`.
* **Desafio:** Enfrentei um `TypeError` porque o bcrypt exige dados em `bytes` e não `strings`. Resolvi utilizando o método `.encode('utf-8')`.
* **Porquê Bcrypt?** Aprendi que o hashing é uma via de mão única, tornando o sistema seguro mesmo em caso de fuga de dados.

#### **Dia 3: Persistência com SQLite**

* Migrei os dados para um ficheiro `.db`.
* Aprendi a criar tabelas usando comandos SQL via Python.
* **Correção técnica:** Ajustei um erro de sintaxe na criação da tabela causado por uma vírgula extra no comando `CREATE TABLE`.

#### **Dia 4: Modularização e Encoding**

* Refatorei o código para utilizar funções (`def`), separando a lógica de gerar o hash, verificar a senha e efetuar o login.
* Aprofundei os meus conhecimentos sobre encoding de caracteres, compreendendo como o **UTF-8** atua mapeando os caracteres em bytes (essencial para o funcionamento do `bcrypt`).

#### **Dia 5: Integração Dinâmica e Persistência de Dados**
* Login Dinâmico: Refatorei a lógica de autenticação para consultar o banco de dados em tempo real. Agora, o sistema utiliza o comando SQL `SELECT` para buscar o hash da senha associado ao  usuario em questão, eliminando o uso de variáveis fixas (hardcoded) como havia no código anterior.

* Fluxo de Registro: Criei uma função de registro que captura o input do usuario, gera o hash via `bcrypt` e salva os dados de forma segura no SQLite usando o comando `INSERT`.

* Segurança na Consulta (**Aprendizado**): Implementei o uso de Placeholders (`?`) nas consultas SQL para poder referenciar as minhas variáveis de input e eventualmente descobri que para proteger o sistema contra ataques de SQL Injection, uma das vulnerabilidades mais comuns em sistemas web, é essencial o uso dos Placeholders.

---

### 🔧 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/teu-usuario/secure-auth-logic.git

```


2. Instale as dependências:
```bash
pip install bcrypt

```


3. Execute o script principal:
```bash
python login.py

```



---

### 📈 Próximos Passos

* [ ] Tratamento de Exceções: Implementar blocos try/except para lidar com erros de conexão à base de dados ou ficheiro corrompido e erros de usuário.

* [ ] Interface de Menu: Criar um menu principal que permita ao utilizador escolher entre (1) Login, (2) Registo ou (3) Sair, usando um loop while.

* [ ] Validação de Força de Senha: Adicionar uma lógica que obrigue o novo utilizador a criar uma senha com pelo menos 8 caracteres e alguns caractéres especiais.

---
