"""
Password Strength Checker

Copyright (c) 2026 Gabriel Silva Bastos

Licensed under the MIT License.
See the LICENSE file in the project root for full license information.
"""

import string




import string


def carregar_senhas_comuns(filepath):
    """
    Carrega uma lista de senhas comuns a partir de um arquivo de texto.
    """
    common = []

    try:
        with open(filepath, "r", encoding="utf-8") as arquivo:
            for line in arquivo:
                senha = line.strip().lower()

                if senha:
                    common.append(senha)

    except FileNotFoundError:
        print(
            f"Aviso: o arquivo '{filepath}' não foi encontrado. "
            "Nenhuma senha comum será carregada."
        )

    return common


def verificar_senha(password, senhas_comuns):
    """
    Verifica a força da senha e retorna uma tupla:
    (pontuação, lista_de_feedbacks)
    """

    score = 0
    feedback = []

    # Número de caracteres
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("A senha deve ter pelo menos 8 caracteres.")

    if len(password) >= 12:
        score += 1
    else:
        feedback.append(
            "Para uma senha mais forte, utilize pelo menos 12 caracteres."
        )

    # Letra maiúscula
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append(
            "A senha deve conter pelo menos uma letra maiúscula."
        )

    # Número
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("A senha deve conter pelo menos um número.")

    # Caractere especial
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append(
            "A senha deve conter pelo menos um caractere especial."
        )

    # Senha comum anula a pontuação
    if password.lower() in senhas_comuns:
        score = 0
        feedback = [
            "A senha é muito comum e fácil de adivinhar. "
            "Escolha uma senha mais forte."
        ]

    return score, feedback


def main():
    strength_labels = {
        0: "Muito fraca",
        1: "Fraca",
        2: "Fraca",
        3: "Média",
        4: "Forte",
        5: "Muito forte",
    }

    senhas_comuns = carregar_senhas_comuns("common_passwords.txt")

    while True:
        password = input(
            "\nDigite a senha para verificar ou 'sair' para encerrar: "
        )

        if password.lower() == "sair":
            print("Programa encerrado.")
            break

        score, feedback = verificar_senha(password, senhas_comuns)

        print(
            f"Pontuação da senha: {score}/5 "
            f"({strength_labels[score]})"
        )

        if feedback:
            print("Feedback:")

            for mensagem in feedback:
                print(f"  - {mensagem}")
        else:
            print("A senha atende a todos os critérios.")

        # Registra apenas a quantidade de caracteres, não a senha real
        with open(
            "password_log.txt",
            "a",
            encoding="utf-8"
        ) as log_file:
            log_file.write(
                f"Senha: {'*' * len(password)}, "
                f"Pontuação: {score}, "
                f"Feedback: {'; '.join(feedback)}\n"
            )


if __name__ == "__main__":
    main()