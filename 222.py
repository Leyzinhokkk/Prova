import random 

def lancar_dados():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    soma = dado1 + dado2
    return soma

resultado = lancar_dados()
print(f"o resultado do lançamento foi: {resultado}")