# 🔐 Password Strength Checker

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Cybersecurity](https://img.shields.io/badge/Área-Cybersecurity-red)
![Status](https://img.shields.io/badge/Status-Funcional-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

Um verificador de força de senhas desenvolvido em **Python**, capaz de analisar diferentes critérios de segurança, identificar senhas comuns e fornecer recomendações para melhorar a senha informada.

O projeto foi desenvolvido com fins educacionais para praticar conceitos de Python aplicados à segurança da informação.

---

## 📌 Funcionalidades

- Verificação do tamanho da senha;
- Detecção de letras maiúsculas;
- Detecção de números;
- Detecção de caracteres especiais;
- Comparação com uma lista de senhas comuns;
- Classificação da força da senha;
- Exibição de recomendações de segurança;
- Registro dos resultados em arquivo de log;
- Proteção da senha no log por meio de asteriscos;
- Execução contínua até o usuário solicitar o encerramento.

---

## 🧠 Critérios de pontuação

A senha pode receber uma pontuação de **0 a 5**.

| Critério | Pontuação |
|---|:---:|
| Possuir pelo menos 8 caracteres | +1 |
| Possuir pelo menos 12 caracteres | +1 |
| Possuir pelo menos uma letra maiúscula | +1 |
| Possuir pelo menos um número | +1 |
| Possuir pelo menos um caractere especial | +1 |

Caso a senha esteja presente no arquivo `common_passwords.txt`, sua pontuação será automaticamente definida como **0**.

### Classificação

| Pontuação | Classificação |
|:---:|---|
| 0 | Muito fraca |
| 1 | Fraca |
| 2 | Fraca |
| 3 | Média |
| 4 | Forte |
| 5 | Muito forte |

---

## 📁 Estrutura do projeto

```text
password-strength-checker/
├── password_checker.py
├── common_passwords.txt
├── .gitignore
├── LICENSE
└── README.md
```

O arquivo `password_log.txt` será criado automaticamente após a primeira verificação.

---

## ⚙️ Requisitos

- Python 3.10 ou superior;
- Nenhuma biblioteca externa é necessária.

O projeto utiliza apenas o módulo `string`, que já faz parte da biblioteca padrão do Python.

---

## 🚀 Como executar

Clone o repositório:

```bash
git clone https://github.com/outter1/password-strength-checker.git
```

Entre na pasta:

```bash
cd password-strength-checker
```

Execute o programa:

### Linux ou macOS

```bash
python3 password_checker.py
```

### Windows

```bash
python password_checker.py
```

---

## 📝 Lista de senhas comuns

Crie o arquivo `common_passwords.txt` na mesma pasta do programa.

Exemplo:

```text
123456
password
qwerty
admin
letmein
welcome
password123
```

Cada senha deve ocupar uma linha.

O programa converte todas as entradas para letras minúsculas antes de realizar a comparação. Dessa forma, `Password`, `PASSWORD` e `password` são tratados como a mesma senha.

---

## 💻 Exemplo de execução

```text
Digite a senha para verificar ou 'sair' para encerrar: Gabriel123

Pontuação da senha: 3/5 (Média)

Feedback:
  - Para uma senha mais forte, utilize pelo menos 12 caracteres.
  - A senha deve conter pelo menos um caractere especial.
```

Exemplo com uma senha mais forte:

```text
Digite a senha para verificar ou 'sair' para encerrar: TryHackMe!2025

Pontuação da senha: 5/5 (Muito forte)
A senha atende a todos os critérios.
```

---

## 📄 Registro de resultados

Após cada verificação, o programa adiciona o resultado ao arquivo:

```text
password_log.txt
```

Exemplo:

```text
Senha: **************, Pontuação: 5, Feedback:
```

A senha original não é armazenada. Ela é substituída por asteriscos de acordo com sua quantidade de caracteres.

---

## 🔎 Conceitos de Python utilizados

O projeto utiliza conceitos importantes da linguagem Python:

- Funções;
- Parâmetros e valores de retorno;
- Listas;
- Dicionários;
- Tuplas;
- Laços `for` e `while`;
- Estruturas condicionais;
- Tratamento de exceções;
- Leitura e escrita de arquivos;
- F-strings;
- Expressões geradoras;
- Funções `any()`, `len()` e `open()`;
- Métodos `isupper()`, `isdigit()`, `lower()`, `strip()` e `join()`.

---

## 🔒 Observações de segurança

Este projeto possui finalidade educacional e não substitui ferramentas profissionais de análise de senhas.

A pontuação representa apenas o cumprimento de critérios básicos. Uma senha pode cumprir todos os critérios e ainda ser previsível.

Boas práticas adicionais incluem:

- Utilizar frases-senha longas;
- Não reutilizar senhas;
- Evitar nomes, datas e informações pessoais;
- Utilizar um gerenciador de senhas;
- Ativar autenticação de dois fatores;
- Não registrar senhas em texto puro.

---

## 🛠️ Melhorias futuras

- Interface gráfica;
- Geração automática de senhas fortes;
- Verificação de letras minúsculas;
- Detecção de padrões previsíveis;
- Identificação de sequências como `123456` e `abcdef`;
- Cálculo aproximado de entropia;
- Testes automatizados com `pytest`;
- Exportação de relatórios;
- Argumentos via linha de comando;
- Verificação segura de senhas expostas em vazamentos.

---

## ⚠️ Aviso

Não utilize senhas reais ou sensíveis durante testes públicos, gravações ou demonstrações.

O projeto deve ser utilizado apenas para aprendizado e conscientização sobre segurança de senhas.

---

## 👨‍💻 Autor

Desenvolvido por **Gabriel Silva Bastos**.

- GitHub: [@outter1](https://github.com/outter1)
- Área de interesse: Cybersecurity e Desenvolvimento de Sistemas

---

## 📜 Licença

Este projeto está sob a licença MIT.

Consulte o arquivo `LICENSE` para mais informações.
