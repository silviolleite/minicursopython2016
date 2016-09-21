#declaração da lista vazia
lista = []
#for para ler os 5 números
for i in range(5):
       #armazenamos o valor digitado no teclado
       num = int(input("Digite o {}º número: ".format(i+1)))
       #adiciona o número digitado a lista com a função append
       lista.append(num)
#termina o laço e imprime o maior número
print("{} é o maior número".format(max(lista)))
