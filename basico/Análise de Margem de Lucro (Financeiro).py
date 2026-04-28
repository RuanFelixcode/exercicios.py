'''Exercício 4: Análise de Margem de Lucro (Financeiro)
Cenário: Uma consultoria faturou R$ 15.000,00 em um projeto. Os custos fixos foram de R$
5.000,00 e o imposto sobre o faturamento é de 15%. Objetivo: Calcule o imposto, o lucro
líquido e a margem de lucro (Lucro / Faturamento). No final, crie uma variável booleana
chamada meta_atingida que verifica se a margem de lucro é superior a 0.30 (30%).'''

consultoria_fatura = 15000.00
custos_fixos = 5000.00
imposto = consultoria_fatura * 0.15
lucro = consultoria_fatura - custos_fixos - imposto
margem = lucro / consultoria_fatura
meta_atingida = margem > 0.30
print(f"Imposto: R${imposto:.2f}")
print(f"Lucro líquido: R${lucro:.2f}")
print(f"Margem de lucro: {margem:.2%}")
print(f"Meta atingida? {meta_atingida}")
