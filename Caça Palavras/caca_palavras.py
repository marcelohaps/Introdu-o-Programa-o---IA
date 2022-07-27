import random
import numpy as np
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import time

def ptomm(mm): #Essa função converte o valor em pontos para milímetros, pois fica mais fácil de trabalhar com o formato A4 com as medidas em milímetros.
    return mm/0.352777

def gera_pdf(matrix, name_person, words):  #Essa função serve para gerar o pdf do meu caça-palavras.
    my_pdf = canvas.Canvas("caca_palavras.pdf", pagesize = A4)
    pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
    pdfmetrics.registerFont(TTFont('Impact', 'Impact.ttf'))
    pdfmetrics.registerFont(TTFont('Tahoma', 'Tahoma.ttf'))
    
    aux_column = 0
    aux_line = 0
    aux = 0
    aux2 = 0
    largura, altura = A4
    my_pdf.drawImage("borda.png", ptomm(0), ptomm(0), width = 595, height = 841) # Coloca essa borda personalizada no pdf.
    my_pdf.drawCentredString(ptomm(110), ptomm(276), "CAÇA-PALAVRAS - " +str(name_person))
    for i in range(len(matrix)): #(Linhas 26 a 31) - Coloca a matriz do caça-palavras no pdf.
        for j in range(len(matrix[i])):
            my_pdf.drawCentredString(ptomm(28)+aux_column, ptomm(240)-aux_line, matrix[i][j])
            aux_column += 15
        aux_line += 18
        aux_column = 0

    for i in range(len(words)): #Linhas (33 a 38) - Coloca as palavras que o usuário digitou abaixo do caça-palavras.
        my_pdf.drawCentredString(ptomm(70)+aux, ptomm(30)-aux2, words[i])
        aux2 -= 15
        if i % 2 != 0:
            aux2 = 0
            aux += 100
    my_pdf.save() #Salva o pdf no diretório do programa.
    return 0

def main():
    strings = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  #String com todas as letras do alfabeto que será útil para gerar a matriz aleatória.
    matriz = np.array([['']*30]*30)         #Inicializando a matriz do tipo 'char' vazia.
    palavras = []
    posicoes = []
    g = 0
    t = 0
    a = 1
    name = input("Digite o seu nome: ")
    name = name.title()

    for i in range(len(matriz)):                   #Linhas (51 a 54) - Percorro cada posição da matriz e a função random.choice coloca alguma letra do alfabeto lá.
        for j in range(len(matriz[i])):                                #LEMBRANDO QUE A FUNÇÃO random.choice IRÁ DISTRIBUIR AS LETRAS DE MANEIRA ALEATÓRIA. NÃO SEREI RESPONSÁVEL
            matriz[i][j] = random.choice(strings)          #            CASO ESSA ALEATORIEDADE GERE ALGUMA PALAVRA DE BAIXO CALÃO.  
    i = 0
    lista_linhas = random.sample(range(len(matriz)), 6) # lista_linhas é um vetor que recebe as linhas em que vou colocar as palavras. Usei a função random.sample pois não quero palavras na mesma linha, somente em linhas diferentes.
    print("Digite 6 palavras com menos de 30 letras: ") # Pedindo 6 palavras para o usuário
    while True:
        palavras_user = input(f"Digite a {a}º palavra: ")
        if len(palavras_user) > 10:                       #Linhas (61 a 63) - Como a matriz é 30x30, se o usuário digitar uma palavra com mais de 30 letras, eu peço para ele digitar outra.
            print("Essa palavra é muito grande, amigo! Digite outra ae!")
            continue
        palavras.append(palavras_user.upper())      #Armazena as palavras que o usuário digitou em uma lista.
        coluna = random.randint(0, 30-(len(palavras_user))) #A função random.randint gera em qual coluna a palavra vai começar.
        posicoes.append([lista_linhas[i], coluna, (coluna+len(palavras_user))-1]) #Adiciona a linha que a palavra vai estar, a coluna que ela vai começar e a coluna em que ela vai terminar em uma lista.
        i += 1                                                                    #Essa lista de posições é muito importante!
        a += 1
        if i == 6:
            break
        

    for x in range(len(posicoes)):      #Linhas (75 a 80) - Nessa parte, o programa adiciona as palavras na matriz.
        linha = posicoes[x][0]
        g = 0
        for y in range(posicoes[x][1], posicoes[x][2]+1):
            matriz[linha][y] = palavras[x][g]
            g += 1
    
    print("Iremos mostrar como ficou seu caça-palavras aqui no terminal, mas não se preocupe; iremos gerar o PDF dele!!")
    time.sleep(4)
    for x in range(len(matriz)):        #Linhas (82 a 85) - Essa parte serve para mostrar o caça-palavras no terminal. Mas não é necessário, pois estou gerando o pdf dele.
        for y in range(len(matriz[x])):
            print(matriz[x][y], end = ' ')
        print('')
    
    print(f"Aguarde 5 segundos que irei gerar o PDF do seu caça-palavras, {name}.")
    for timer in range(5, -1, -1):
        print(timer)
        time.sleep(1)
    
    print("PDF GERADO! CHEQUE A PASTA EM QUE O PROGRAMA ESTÁ ARMAZENADO.")
    

    gera_pdf(matriz, name.upper(), palavras) #Chamando a função que gera o pdf. Ela tem como parâmetros a matriz, o nome do usuário e as palavras que ele digitou.
if __name__ == '__main__':
    main()
   
    



