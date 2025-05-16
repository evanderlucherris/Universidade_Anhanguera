#include <stdio.h>

int main(){

  float num1, num2, media;

  printf("Digite o primeiro numero: ");

  scanf("%f", &num1);

  printf("Digite o segundo numero: ");

  scanf("%f", &num2);

  media = (num1 + num2)/2;

  printf("Media = %.2f", media);

  return 0;

}