// Nome: [Seu Nome]
// Disciplina: Algoritmos e Programação Estruturada
// Unidade 4 - Funções e Passagem de Parâmetros
// Aula 1 - Funções
// Ferramenta: OnlineGDB (https://www.onlinegdb.com/)

#include <stdio.h>

// Função que calcula o salário bruto
float calcular_salario_bruto(float valor_hora, float horas_trabalhadas) {
    return valor_hora * horas_trabalhadas;
}

// Função que calcula o desconto (9% sobre o salário bruto)
float calcular_desconto(float salario_bruto) {
    return salario_bruto * 0.09;
}

// Função que calcula o salário líquido
float calcular_salario_liquido(float salario_bruto, float desconto) {
    return salario_bruto - desconto;
}

// Função principal
int main() {
    float valor_hora, horas_trabalhadas;
    float salario_bruto, desconto, salario_liquido;

    printf("=== CALCULO DE SALARIO ===\n\n");

    // Entrada de dados
    printf("Informe o valor de hora trabalhada: R$ ");
    scanf("%f", &valor_hora);

    printf("Informe a quantidade de horas trabalhadas no MES: ");
    scanf("%f", &horas_trabalhadas);

    // Chamadas das funções
    salario_bruto = calcular_salario_bruto(valor_hora, horas_trabalhadas);
    desconto = calcular_desconto(salario_bruto);
    salario_liquido = calcular_salario_liquido(salario_bruto, desconto);

    // Saída dos resultados
    printf("\nSALARIO BRUTO: R$ %.2f", salario_bruto);
    printf("\nDESCONTO (9%%): R$ %.2f", desconto);
    printf("\nSALARIO LIQUIDO: R$ %.2f\n", salario_liquido);

    printf("\n=== FIM DO PROGRAMA ===\n");

    return 0;
}
