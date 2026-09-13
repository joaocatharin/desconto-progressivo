# Programa de descontos progressivos

# Solicita o valor total da compra
valor_compra = float(input("Digite o valor total da compra (R$): "))

# Determina o percentual de desconto de acordo com as regras
if valor_compra < 200:
    percentual = 0.05          # 5%
elif valor_compra < 300:
    percentual = 0.10          # 10%
else:
    percentual = 0.15          # 15%

# Calcula o valor do desconto e o valor final a pagar
desconto = valor_compra * percentual
valor_final = valor_compra - desconto

# Exibe os resultados formatados
print(f"\nValor original da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado ({percentual*100:.0f}%): R$ {desconto:.2f}")
print(f"Valor total a pagar: R$ {valor_final:.2f}")