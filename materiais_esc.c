#include <stdio.h>

int main() {
    float lapis, caneta;

    printf("Digite o numero de lapis: ");
    scanf("%f", &lapis);

    printf("Digite o numero de canetas: ");
    scanf("%f", &caneta);

    if (lapis > 1 || caneta > 1) {
        printf("Voce pode emprestar seus materiais\n");
    } else {
        printf("Voce nao pode emprestar seus materiais\n");
    }

    return 0;
}
