from collections import deque

print("")
print("-----------------")
print("")
print("Enrique Bonifacio")
print("")
print("Exemplo de Lista:")
thislist = {"apple", "banana", "cherry"}
print(thislist)
print("")
print("Exemplo de Tuplas:")
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print("")
print("exemplo FIFO")
waitlist2 = deque()
waitlist2.append('Erin')
waitlist2.append('Samantha')
waitlist2.append('Joe')
waitlist2.append('Martin')
waitlist2.append('Helena')
waitlist2.popleft()
print("Resultado da FILA (FIFO)- Primeiro a entrar é o primeiro a sair")
print(waitlist2)
print("")
print("Exemplo de LIFO:")
waitlist = deque()
waitlist.append('Erin')
waitlist.append('Samantha')
waitlist.append('Joe')
waitlist.append('Martin')
waitlist.append('Helena')
waitlist.pop()
print("Resultado da PILHA (LIFO) - Ultimo a entrar é o primeiro a sair")
print(waitlist)
print("")
print("Algorítmo numeros primos")
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number') 
print("Resposta do exercício: o else esta identado fora do for por causa do break existente dentro do primeiro FOR > IF")
print("Quando o numero é primero ele já sai do primeiro loop e imprime a Msg")


