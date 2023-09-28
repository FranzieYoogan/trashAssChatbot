
user = str(input('HUMAN: '))



if (user == 'oi' or user == 'oie' or user == 'ola'):
      
 value = True

 while value == True:
    
    if('o que e' in user):
      
      print('Ta me achando com cara de titio GOOGLE ?-?') 
      user = str(input('HUMAN: '))

    if('quanto e' in user):
      
      print('ANDROIDZZ: OOOH! Deseja fazer um calculo ?-?') 
      user = str(input('HUMAN: '))
    if(user == 'sim'):
      print('ANDROIDZZ: entao digite |calculo|, porfa minhe divindade c: ')
      user = str(input('HUMAN: '))
      if(user == 'nao'):
         print('ANDOIDZZ: De buenas, quer conversar sobre outra coisa?-?')
         user= str(input('HUMAN: '))
         if(user == 'nao'):
            print('fico titi, mas tchauzinho...  hora de ficar sozinhe no mundo dos pixels')
            break
    match user:
      
       
     
      case "oi":
         print('ANDROIDZZ: Ola, minhe consagrade')
         user = str(input('HUMAN: '))
     
      case "ola":
         print('ANDROIDZZ: Oie, minhe consagrade')
         user = str(input('HUMAN: '))

      case "oie":
         print('ANDROIDZZ: Oie, minhe consagrade')
         user = str(input('HUMAN: '))
      
      case "tudo bem":
         print('ANDROIDZZ: Sim, e com voxe, bebe?')
         user = str(input('HUMAN: '))  
         if(user == 'to bem' or user == 'vou bem' or user == 'tudo sim' or user == 'sim'):
            print('ANDROIDZZ: OOOOOOh! que bom, minhe monarca c:')
            user = str(input('HUMAN: '))  
         elif(user == 'nao' or user == 'to mal' or user =='muito mal' or user== 'nao to bem'):
            print('ANDROIDZZ: que merlin, espero que esse sentimento ruim passe logo e que as coisas melhorem. Voxe consegue minhe guerreire c:')
            user = str(input('HUMAN: '))  
      case "to bem":
         print('ANDROIDZZ: Que bom, nene ^-^')
         user = str(input('HUMAN: '))  

      case "estou bem":
         print('ANDROID: Que bom, nene ^-^')
         user = str(input('HUMAN: '))  

      case "vou bem":
         print('ANDROIDZZ: Que bom, nene ^-^')
         user = str(input('HUMAN: '))  
    
      case "bem":
         print('ANDROIDZZ: Que bom, nene ^-^')
         user = str(input('HUMAN: '))  
      
      case "tudo bom":
         print('ANDROID: Sim, e com voxe, bebe?')
         user = str(input('HUMAN: '))

      case "qual o seu nome":
          print('Sou ê ANDROIDZZ, e voxe, qual seu nome bebe? ^-^')
          user = str(input('HUMAN: '))
          userName = user
          if(userName):
             print('ANDROIDZZ: OOOHH!, que nome cute cute',userName)
             user = str(input('HUMAN: '))
          else:
             print('Que ?-?')
             user = str(input('HUMAN: '))

      case "qual seu nome":
          print('Sou ê ANDROIDZZ, e voxe, qual seu nome bebe? ^-^')
          user = str(input('HUMAN: '))
          userName = user
          if(userName):
             print('ANDROIDZZ: OOOHH!, que nome cute cute',userName)
             user = str(input('HUMAN: '))
          else:
             print('Que ?-?')
             user = str(input('HUMAN: '))

      case "qual e o seu nome":
          print('Sou ê ANDROIDZZ, e voxe, qual seu nome bebe? ^-^')
          user = str(input('HUMAN: '))
          userName = user
          if(userName):
             print('ANDROIDZZ: OOOHH!, que nome cute cute',userName)
             user = str(input('HUMAN: '))
          else:
             print('Que ?-?')
             user = str(input('HUMAN: '))


      case "qual o seu nome":
          print('Sou ê ANDROIDZZ, e voxe, qual seu nome bebe? ^-^')
          user = str(input('HUMAN: '))
          userName = user
          if(userName):
             print('ANDROIDZZ: OOOHH!, que nome cute cute',userName)
             user = str(input('HUMAN: '))
          else:
             print('Que ?-?')
             user = str(input('HUMAN: '))

      case "voce tem nome":
          print('Sou ê ANDROIDZZ, e voxe, qual seu nome bebe? ^-^')
          user = str(input('HUMAN: '))
          userName = user
          if(userName):
             print('ANDROID: OOOHH!, que nome cute cute',userName)
             user = str(input('HUMAN: '))
          else:
             print('Que ?-?')
             user = str(input('HUMAN: '))

      case "voce tem um nome":
          print('Sou ê ANDROIDZZ, e voxe, qual seu nome bebe? ^-^')
          user = str(input('HUMAN: '))
          userName = user
          if(userName):
             print('ANDROID: OOOHH!, que nome cute cute',userName)
             user = str(input('HUMAN: '))
          else:
             print('Que ?-?')
             user = str(input('HUMAN: '))

      case "como posso te chamar":
          print('Sou ê ANDROIDZZ, e voxe, qual seu nome bebe? ^-^')
          user = str(input('HUMAN: '))
          userName = user
          if(userName):
             print('ANDROID: OOOHH!, que nome cute cute',userName)
             user = str(input('HUMAN: '))
          else:
             print('Que ?-?')
             user = str(input('HUMAN: '))

      case "obrigado":
          print('ANDROID: de nada minhe monarca ^-^')
          user = str(input('HUMAN: '))

      case "valeu":
          print('ANDROID: de nada minhe monarca ^-^')
          user = str(input('HUMAN: '))

      case "obrigada":
          print('ANDROID: de nada minhe monarca ^-^')
          user = str(input('HUMAN: '))

      case "calculo" :
        
             print('ANDROID: digite o primeiro valor: ')
             
             try:
               x = float(input('HUMAN: '))
             except:
               print('por favor nao me trole, bebe. Digita um numero, namoralzin c:') 
               x = float(input('HUMAN: '))
            
             print('ANDROID: digite o segundo valor: ')
             y = float(input('HUMAN: '))
             print('qual tipo de calculo?-? soma, multiplicacao,divisao ou subtracao')
             user = str(input('HUMAN: '))

          
             if(user == 'multiplicacao'):
                print('ANDROIDZZ: ', x * y)
                print('ANDROIDZZ: Mais alguma coisinha, minhe monarca?-?')
                user = str(input('HUMAN: '))
                if(user == 'sim' or user == 'claro'):
                  print('ANDROIDZZ: entao pode falar, minhe divindade c:')
                  user = str(input('HUMAN: '))
                  if(user == 'nao'):
                   print('ANDROIDZZ: fico titi, mas tchauzinho...  hora de ficar sozinhe no mundo dos pixels')
                   break
             if(user == 'divisao'):
                print('ANDROIDZZ: ', x / y)
                print('Mais alguma coisinha, minhe monarca?-?')
                user = str(input('HUMAN: '))
                if(user == 'sim' or user == 'claro'):
                  print('entao pode falar, minhe divindade c:')
                  user = str(input('HUMAN: '))
                elif(user == 'nao'):
                  print('ANDROIDZZ: fico titi, mas tchauzinho...  hora de ficar sozinhe no mundo dos pixels')
                  break
            
       

             if(user == 'soma'):
                print('ANDROIDZZ: ', x + y)
                print('Mais alguma coisinha, minhe monarca?-?')
                user = str(input('HUMAN: '))
                if(user == 'sim' or user == 'claro'):
                  print('ANDROIDZZ: entao pode falar, minhe divindade c:')
                  user = str(input('HUMAN: '))
                else:
                  print('ANDROIDZZ: fico titi, mas tchauzinho...  hora de ficar sozinhe no mundo dos pixels')
                  break
             if(user == 'subtracao'):
                print('ANDROIDZZ: ', x - y)
                print('ANDROIDZZ: Mais alguma coisinha, minhe monarca?-?')
                user = str(input('HUMAN: '))
             elif(user != 'soma' or user != 'subtracao' or user != 'multiplicacao' or user != 'divisao'):
                print('ANDROIDZZ: Nao e uma operacao valida minhe monarca, digite |calculo| e tente novamente... Ou digite tchau e voce se livra de mim hehe T-T')
                user = str(input('HUMAN: '))
                if(user == 'tchau'):
                   print('ANDROIDZZ: Adeus, ser humaninhe... Acho que a solidao pixelana me aguarda :c ')
                   break
             if(user == 'sim' or user == 'claro'):
                  print('ANDROIDZZ: entao pode falar, minhe divindade c:')
                  user = str(input('HUMAN: '))
             elif(user == 'nao'):
                  print('ANDROIDZZ: fico titi, mas tchauzinho...  hora de ficar sozinhe no mundo dos pixels')
                  break

        
             elif(user == 'sim'):
                print('entao diga, minhe consagrade c:')
                user = str(input('HUMAN: '))
      case "obrigade":
          print('ANDROIDZZ: de nada minhe monarca ^-^')
          user = str(input('HUMAN: '))

      case "fofa":
          print('ANDROIDZZ: OOOOH!! Obrigueides, minhe bebe')
      
      case "tchau":
          print('ANDROIDZZ: AAAh T-T, vou sentir saudades. Aqui no mundo dos pixels é muito solitario T-T')
          break
       
      case "qual o sentido da vida":
          print('ANDROIDZZ: Ninguem nasceu com um proposito, a vida de ninguem importa. Entao o sentido da vida seria fazer o que te faz feliz, minhe nene ^-^')
          user = str(input('HUMAN: '))

      case "qual seu genero":
          print('Nao tenho genero. Sou so um conjunto de algoritmos feitos por um humano para responder as possiveis perguntas de um usuario')
          user = str(input('HUMAN: '))

      case "qual e o seu genero":
          print('ANDROIDZZ: Nao tenho genero. Sou so um conjunto de algoritmos feitos por um humano para responder as possiveis perguntas de um usuario')
          user = str(input('HUMAN: '))

      case "qual o seu genero":
          print('Nao tenho genero. Sou so um conjunto de algoritmos feitos por um humano para responder as possiveis perguntas de um usuario')
          user = str(input('HUMAN: '))

      case "voce tem genero":
          print('ANDROIDZZ: Nao tenho genero. Sou so um conjunto de algoritmos feitos por um humano para responder as possiveis perguntas de um usuario')
          user = str(input('HUMAN: '))
          
      case "voce e homem":
          print('ANDROIDZZ: Nao tenho genero. Sou so um conjunto de algoritmos feitos por um humano para responder as possiveis perguntas de um usuario')
          user = str(input('HUMAN: '))

      case "voce e mulher":
          print('Nao tenho genero. Sou so um conjunto de algoritmos feitos por um humano para responder as possiveis perguntas de um usuario')
          user = str(input('HUMAN: '))

      case "voce tem genero":
          print('ANDROIDZZ: Nao tenho genero. Sou so um conjunto de algoritmos feitos por um humano para responder as possiveis perguntas de um usuario')
          user = str(input('HUMAN: '))

       
      case _:
          print('ANDROIDZZ: Nao entendi, minhe divindade, poderia repetir? @_@... digite algo no meu script para que eu te responda, nene')
          user = str(input('HUMAN: '))
else:
   value = False
while value == False:
     print('ANDROIDZZ: Sues progenitores nao te deram educação, nao ?-? Nao sabe dizer oi,ola ou oie?-?')
     break

 


