#include <stdio.h>

int main() {
    int numero;
    int soma = 0;

    printf("=== SOMADOR DE NUMEROS ===\n");
    printf("Digite numeros inteiros para somar.\n");
    printf("Digite 0 para encerrar.\n\n");

    while (1) {
        printf("Digite um numero: ");

        // Verifica se a entrada foi um número inteiro
        if (scanf("%d", &numero) != 1) {
            printf("Entrada invalida! Digite apenas numeros inteiros.\n");

            // Limpa o buffer de entrada
            while (getchar() != '\n')
                continue;

            continue;
        }

        // Condição de parada
        if (numero == 0) {
            break;
        }

        soma += numero;
    }

    printf("\nA soma total dos numeros inseridos e: %d\n", soma);
    return 0;
}
