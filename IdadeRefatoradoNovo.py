# Recebe idade digitada

idade = int(input ("Entrada de idade.:  "))


# Criacao de funcao para validacao de categoria idade

def verificaCategoriaIdade (idade) :
    if idade < 13 :
        return "Criança"
    elif idade >= 13 and idade < 18 :
        return "Jovem"
    else:
        return "Adulto"

categoriaIdade = verificaCategoriaIdade(idade)

# Apresenta idade com a variavel global categoriaIdade que é boa pratica mais usada

print(f"A pessoa é :  {categoriaIdade}") 