# Desafios de Lógica de Programação

Este repositório contém soluções para cinco desafios de programação envolvendo lógica e manipulação de dados.

## Enunciados

### 1) Cálculo de Variável SOMA
Considere o seguinte trecho de código:
```c
int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça {
    K = K + 1;
    SOMA = SOMA + K;
}
Imprimir(SOMA);
```
Ao final do processamento, qual será o valor da variável SOMA?

---

### 2) Sequência de Fibonacci
Dada a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos dois valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa que, informado um número, verifique se ele pertence ou não à sequência.

**IMPORTANTE:** O número pode ser informado por qualquer método de entrada.

---

### 3) Análise de Faturamento Mensal
Dado um vetor contendo o faturamento diário de uma distribuidora, escreva um programa que calcule e retorne:
- O menor valor de faturamento ocorrido em um dia do mês;
- O maior valor de faturamento ocorrido em um dia do mês;
- O número de dias no mês em que o faturamento diário foi superior à média mensal.

**IMPORTANTE:**
- O faturamento estará disponível em um arquivo JSON ou XML.
- Dias sem faturamento (finais de semana e feriados) devem ser ignorados no cálculo da média.

---

### 4) Percentual de Faturamento por Estado
Dado o valor de faturamento mensal de uma distribuidora detalhado por estado:
```
SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53
```
Escreva um programa que calcule o percentual de representação de cada estado em relação ao faturamento total da distribuidora.

---

### 5) Inversão de String
Escreva um programa que inverta os caracteres de uma string sem utilizar funções prontas, como `reverse()`.

**IMPORTANTE:**
- A string pode ser informada por qualquer método de entrada.

---

## Como Executar os Códigos

1. Clone este repositório:
   ```sh
   git clone (https://github.com/Limaitalos/desafio_desenvolvedor_gupy)
   ```
2. Execute os scripts de acordo com a linguagem utilizada (exemplo em Python):
   ```sh
   python desafio1.py
   ```
3. Para os desafios que requerem entrada do usuário, siga as instruções exibidas no terminal.

## Tecnologias Utilizadas
- Python 3
- JSON (para leitura de dados no desafio 3)

---

Feito com ❤️ por [Ítalo Lima](https://github.com/Limaitalos).

