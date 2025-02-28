1) Valor da variável SOMA
O código percorre um loop de K = 1 até K = 13, somando cada valor de K a SOMA.
Soma = 91

2) Verificação de número na sequência de Fibonacci
Aqui está um programa em Python que verifica se um número pertence à sequência de Fibonacci:

def pertence_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or num == 0

num = int(input("Informe um número: "))
if pertence_fibonacci(num):
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")

3) Análise de faturamento diário
O programa abaixo lê um arquivo JSON e realiza as análises:

import json

with open("faturamento.json") as file:
    dados = json.load(file)

valores = [d['valor'] for d in dados if d['valor'] > 0]  # Ignorando dias sem faturamento
media_mensal = sum(valores) / len(valores)

menor = min(valores)
maior = max(valores)
dias_acima_media = sum(1 for valor in valores if valor > media_mensal)

print(f"Menor faturamento: R$ {menor:.2f}")
print(f"Maior faturamento: R$ {maior:.2f}")
print(f"Dias acima da média: {dias_acima_media}")

4) Percentual de faturamento por estado
Cálculo do percentual de faturamento de cada estado:

faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento.values())

for estado, valor in faturamento.items():
    percentual = (valor / total) * 100
    print(f"{estado}: {percentual:.2f}%")

5) Inverter string sem usar funções prontas
Código em Python para inverter uma string:

def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

texto = input("Digite uma string: ")
print(f"String invertida: {inverter_string(texto)}")

