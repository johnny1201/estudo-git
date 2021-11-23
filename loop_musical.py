N = 0

while True:
    pico = 0
    posicao = []
    vetor = []
    K = 0
    N = int(input())    
    if N == 0:
        break
    if 2<= N <=10000:
        vetorstr = (input("insira a sequencia: ").split(' ')) 
        print('seu vetor é {}'.format(vetorstr))
        while N != len(vetorstr):
            N = int(input('Defina o numero de amostras: ')) 
            vetorstr = (input("insira uma sequencia com o numero de amostras especificado: ").split(' ')) 
            print('sua amostra é {}'.format(vetorstr))
        for   vetornum in vetorstr:
            vetor.append(int(vetornum)) 
        print('amostra transformada em inteiro\n {}'.format(vetor))
    


    
    
    for i in range(0,N-1):
        print('vetor pos {} é {}'.format(i, vetor[i]))
        if i==0:
            if vetor[1]<vetor[i] and vetor[N-1]<vetor[i] or vetor[1]>vetor[i] and vetor[N-1]>vetor[i]:
                pico+=1
                print('pico if 1 = ',pico)
                #posicao.append(i)  
                K+= 1
        elif i==N-1:
            if vetor[N-1]>vetor[N-2] and vetor[N-1]>vetor[0] or vetor[N-2]>vetor[N-1] and vetor[N-1]<vetor[0]:
                pico+=1
                print('pico if 2 = ',pico)
        elif vetor[i-1]>vetor[i] and vetor[i+1]>vetor[i] or vetor[i-1]<vetor[i] and vetor[i+1]<vetor[i] :
            pico+=1
        #    posicao[k] = i
           

    print('picos ',pico)
       # elif vetor[i-1]<vetor[i] and vetor[i+1]<vetor[i]:
print('acabou o programa')
    


