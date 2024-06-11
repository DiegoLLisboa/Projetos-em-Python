import random

def escolher_palavra():
    palavras = ['Computador', 'Internet', 'Rede', 'Software', 'Hardware',
                'Programacao', 'Algoritmo', 'Dados', 'Nuvem', 'Seguranca',
                'Criptografia', 'Ciberseguranca', 'Firewall', 'Hackers',
                'Bluetooth', 'Realidade', 'Virtual', 'Aumentada', 'Inteligencia',
                'Artificial', 'Criptomoeda', 'Bitcoin', 'Inovação', 'Automacao',
                'Robotica', 'Dispositivos', 'Vestiveis', 'Impressao', 'Mistura',
                'Sistemas', 'Operacionais', 'Android', 'Windows', 'Linux',
                'Interface', 'Desenvolvimento', 'Codificacao', 'Prototipagem',
                'Gamificacao', 'Tecnologia']
    return random.choice(palavras).lower()

def exibir_forca(tentativas):
    estagios_forca = [
        """
        --------
        |      |
        |
        |
        |
        |
        |
        |
        |
        ----------
        """,
        """
        --------
        |      |
        |      O
        |
        |
        |
        |
        |
        |
        ----------
        """,
        """
        --------
        |      |
        |      O
        |      |
        |
        |
        |
        |
        |
        ----------
        """,
        """
        --------
        |      |
        |      O
        |     /|
        |
        |
        |
        |
        |
        ----------
        """,
        """
        --------
        |      |
        |      O
        |     /|\\
        |
        |
        |
        |
        |
        ----------
        """,
        """
        --------
        |      |
        |      O
        |     /|\\
        |     /
        |
        |
        |
        |
        ----------
        """,
        """
        --------
        |      |
        |      O
        |     /|\\
        |     / \\
        |
        |
        |
        |
        ----------
        """
    ]
    print(estagios_forca[tentativas])

def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ['_'] * len(palavra)
    tentativas = 0
    letras_tentadas = []

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra secreta.")
    print(" ".join(palavra_oculta))

    while tentativas < 6:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_tentadas.append(letra)

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            tentativas += 1

        exibir_forca(tentativas)
        print(" ".join(palavra_oculta))

        if '_' not in palavra_oculta:
            print("Parabéns! Você ganhou!")
            break
    else:
        print("Você perdeu! A palavra correta era:", palavra)

    print("Obrigado por jogar!")
    
    while True:
        resposta = input("Deseja jogar novamente? (sim/nao): ").lower()
        if resposta == 'sim':
            jogar()
            break
        elif resposta == 'nao':
            print("Até a próxima!")
            break
        else:
            print("Resposta inválida. Digite 'sim' ou 'nao'.")

jogar()
