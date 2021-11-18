N = 0
pico = 0
posicao = {}
k = 0
while True:
    N = int(input())    
    if N == 0:
        break
    if 2<= N <=10000:
        vetor = (input("insira a sequencia: ").split(' '))    
    if vetor[1]<vetor[0] and vetor[N]<vetor[0] or vetor[1]>vetor[0] and vetor[N]>vetor[0]:
        pico+=1
        posicao[k] = '0' 
        k+= 1
    for i in range(1,N+1):
        if vetor[i-1]>vetor[i] and vetor[i+1]>vetor[i] or vetor[i-1]<vetor[i] and vetor[i+1]<vetor[i] :
            pico+=1
            posicao[k] = i
            k+= 1
       # elif vetor[i-1]<vetor[i] and vetor[i+1]<vetor[i]:
print(vetor)
print(vetor[0]>vetor[1])
    


