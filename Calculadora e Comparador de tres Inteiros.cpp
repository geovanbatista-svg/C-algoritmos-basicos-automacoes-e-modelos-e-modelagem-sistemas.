#include <stdio.h>

int main() {
    int num1, num2, num3;

    // Entrada de dados
    printf("Digite o primeiro numero inteiro: ");
    scanf("%d", &num1);
    printf("Digite o segundo numero inteiro: ");
    scanf("%d", &num2);
    printf("Digite o terceiro numero inteiro: ");
    scanf("%d", &num3);

    // Operadores aritmeticos
    int soma = num1 + num2 + num3;
    int subtracao = num1 - num2 - num3;
    int multiplicacao = num1 * num2 * num3;
    float divisao = (float) num1 / num2 / num3; // Uso de casting para divisao real

    printf("\n--- Resultados Aritmeticos ---\n");
    printf("Soma: %d\n", soma);
    printf("Subtracao: %d\n", subtracao);
    printf("Multiplicacao: %d\n", multiplicacao);
    printf("Divisao: %.2f\n", divisao);

    // Operadores relacionais
    printf("\n--- Resultados Relacionais ---\n");
    if (num1 > num2) {
        printf("O primeiro numero (%d) e maior que o segundo (%d)\n", num1, num2);
    } else {
        printf("O primeiro numero (%d) NAO e maior que o segundo (%d)\n", num1, num2);
    }

    if (num2 < num3) {
        printf("O segundo numero (%d) e menor que o terceiro (%d)\n", num2, num3);
    } else {
        printf("O segundo numero (%d) NAO e menor que o terceiro (%d)\n", num2, num3);
    }

    // Operadores logicos
    printf("\n--- Resultados Logicos ---\n");
    if ((num1 > 0) && (num2 % 2 == 0)) {
        printf("O primeiro numero e positivo E o segundo numero e par.\n");
    } else {
        printf("As condicoes logicas NAO foram satisfeitas.\n");
    }

    return 0;
}