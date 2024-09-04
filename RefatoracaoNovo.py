# Variavel de preco

precosProdutos = [100 , 200, 300] 


# Soma Valor de produto

totalProduto = sum(precosProdutos)

# Iniciando valor de desconto com zero
desconto = 0

# criando calculo de desconto

if totalProduto > 500:
    desconto = totalProduto * 0.1

totalcomDesconto  = totalProduto - desconto

# Apresentando valor com desconto incluido

print(f"Valor com desconto é : {totalcomDesconto}")

