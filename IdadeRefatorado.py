# Recebe idade digitada

idade = int(input ("Entrada de idade.:  "))


# Criacao de funcao para validacao de categoria idade

def verificaCategoriaIdade (numero) :
    if idade < 13 :
        return "Criança"
    elif idade >= 13 and idade < 18 :
        return "Jovem"
    else:
        return "Adulto"
# Apresenta idade

print(verificaCategoriaIdade(idade)) 