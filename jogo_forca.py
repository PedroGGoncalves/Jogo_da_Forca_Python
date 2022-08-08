def welcome(erro):
    print('-----------------------------------------------------')
    print('Seja Bem-Vindo ao Jogo da Forca !!! \nVocê tem ',6-erro,' chances para acertar a fruta.\nVamos lá!!!')
  
def palavra():
    import random

    arquivo =open("palavras.txt", encoding="utf8")
    linhas = arquivo.readlines()
    
    cont=0
    for linha in linhas:
        cont=cont+1
    cont=cont-1

    x = random.randint(1,cont)
    #print(x,linhas[x])

    return linhas[x]

def desenha_forca(erro):
    print(' ___\n|   |')
    if(erro==0):
        print('|\n|')
    if(erro==1):
        print('|   o\n|')
    if(erro==2):
        print('|   o\n|   |')
    if(erro==3):
        print('|   o\n|  \|')
    if(erro==4):
        print('|   o\n|  \|/')
    if(erro==5):
        print('|   o\n|  \|/\n     \\')
    if(erro==6):
        print('|   o\n|  \|/\n    |\\') #melhorar desenho
    print('\n')
    
def resultado(condd,erro,auxilia_linhas):
    if(condd==0):
        print('\n\nVoce venceu a resposta era:',auxilia_linhas)
        return 0
    if(erro==6):
        condicao=0
        print('\n\nVoce perdeu a resposta era:',auxilia_linhas)
        return 0
    return 1

def faca(erro):
    welcome(erro)
    desenha_forca(erro)
    
def repeticao(n,m,linhas):
    if(n==m):
        return 1
    else:
        if(linhas[m]=='-'):
            print(' ',end="")
        print(' _ ',end="")
        return repeticao(n+1,m,linhas)

def repeticao_2(n,m,linhas,save,teste,auxilia,aux_letra):
    if(n==m):
        return 1
    else:
        if(linhas[n]=='-'):
            print(' ',end="")
            teste=0
        if(save[n]==1 and teste==1):
            print('',auxilia[n],'',end="")
            teste=0
        if(linhas[n].upper() == aux_letra.upper() and teste==1):
            print('',auxilia[n],'',end="")
            contador2=1
            save[n]=1
            teste=0
        if(teste==1):
            print(' _ ',end="")
        return repeticao_2(n+1,m,linhas,save,1,auxilia,aux_letra)
        
def principal():
    linhas =palavra()
    auxilia_linhas=linhas
    save=[len(linhas)]
    
    linhas = linhas.replace('.', '').replace('ç', 'c').replace('ô', 'o').replace('ó', 'o').replace('õ', 'o').replace('é', 'e').replace('ê', 'e').replace('ê', 'e').replace('á', 'a').replace('ã', 'a').replace('â', 'a').replace('à', 'a').replace('í', 'i').replace('ú', 'u')

    erro=0
    contador=0
    
    welcome(erro)    
    desenha_forca(erro)

    save[0]=0
    while contador <(len(linhas)):
        save.append(0)
        if(linhas[contador]=='-'):
            save[contador]=1
        contador=contador+1

    repeticao(0,len(linhas)-1,linhas)
    
    condicao=1
    while condicao != 0:
        print('\n')
        letra = input('\nDigite uma letra:')
        print('\n')
            
        contador=0
        contador2=0

        while contador <(len(linhas)):
            aux_letra=letra
            if(linhas[contador].upper() == aux_letra.upper()):
                contador2=1
                break
            contador+=1
            
        if(contador2 ==1):
            faca(erro)       
        else:
            erro=erro+1
            faca(erro)
        
        repeticao_2(0,len(linhas)-1,linhas,save,1,auxilia_linhas,aux_letra)
        
        contador=0
        condicao=0
        
        while contador <(len(linhas))-1:
            if(save[contador]==0):
                condicao=1
            contador=contador+1
        condicao = resultado(condicao,erro,auxilia_linhas)

principal()






    
