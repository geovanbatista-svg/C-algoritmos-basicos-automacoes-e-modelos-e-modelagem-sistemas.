#include <stdio.h>

int main() {
    float vetor[5];     // Agora o vetor armazena números decimais
    float soma = 0;
    int i;
    
    printf("=== SISTEMA DE VENDAS - SOMA DE VALORES ===\n");
    
    for(i = 0; i < 5; i++) {
        printf("Digite o valor do dia %d: ", i + 1);
        scanf("%f", &vetor[i]);   // Usa %f para float 
        soma +=  vetor[i];
    }
    
    printf("\n Valores inseridos:\n");
    for(i = 0; i < 5; i++) {
        printf("Dia %d: %.2f\n", i + 1, vetor[i]); // %.2f = 2 casas decimais
    }

    printf("\nSoma total das vendas: %.2f\n", soma);
    
    return 0;
}