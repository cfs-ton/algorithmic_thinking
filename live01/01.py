nome = input("Digite seu nome: ")
idade = int(input("Quantos anos você tem: "))

ano_atual = 2026

ano_nacimento = ano_atual - idade

print ("#"*30)
print (f"{nome} você nasceu em: {ano_nacimento}")