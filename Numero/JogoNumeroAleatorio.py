import random

NIVEIS = {
    "1": ("Fácil", 50, 10),
    "2": ("Médio", 100, 7),
    "3": ("Difícil", 500, 9),
}

def escolher_nivel():
    while True:
        print("\nEscolha o nível:")
        for chave, (nome, maximo, tentativas) in NIVEIS.items():
            print(f"{chave} - {nome} (1 a {maximo}, {tentativas} tentativas)")
        opcao = input("Nível: ")
        if opcao in NIVEIS:
            return NIVEIS[opcao]
        print("Opção inválida!")

def ler_palpite(maximo):
    while True:
        try:
            palpite = int(input(f"Digite um palpite (1 a {maximo}): "))
            if 1 <= palpite <= maximo:
                return palpite
            print(f"Digite um número entre 1 e {maximo}.")
        except ValueError:
            print("Isso não é um número válido!")

def jogar(recorde):
    nome, maximo, limite = escolher_nivel()
    secreto = random.randint(1, maximo)

    for tentativa in range(1, limite + 1):
        print(f"\nTentativa {tentativa}/{limite}")
        palpite = ler_palpite(maximo)

        if palpite < secreto:
            print("É mais que isso! ⬆️")
        elif palpite > secreto:
            print("É menos que isso! ⬇️")
        else:
            print(f"🎉 Parabéns! Você acertou em {tentativa} tentativa(s)!")
            if recorde is None or tentativa < recorde:
                print("🏆 Novo recorde!")
                return tentativa
            return recorde

    print(f"😢 Acabaram as tentativas! O número era {secreto}.")
    return recorde

def main():
    recorde = None
    print("=== JOGO DA ADIVINHAÇÃO ===")
    while True:
        recorde = jogar(recorde)
        if input("\nJogar de novo? (s/n): ").lower() != "s":
            print("Obrigado por jogar!")
            break

if __name__ == "__main__":
    main()