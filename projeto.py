materials = ['cimento','brita','areia','tijolos']
enginner = ['carmen']
servant = ['joaõ','carlos','tobias']
MasterBuilde = ['robson']

def materiais():
    print('opçoes de maeriais')
    print('modificação na lista de materias liberados')
    funcoesMaterias = input("ajusta a lista:\n1 - Lista da obra\n2 - adicionar materias\n3 - tirar materias\n")
    match funcoesMaterias:
        case "1":
            print (materials)
            
        case '2':
            adicona = input('escreva o que quer adicionar       ')
            materials.append(adicona)
            print(materials)
            
        case '3':
            print(materials)
            tira = input('escreva oque quer tirar     ')
            materials.remove(tira)
            print('lista atualizada')
            print(materials)

def fucionarios():
    print('acesso liberado a lista de serventes')
    FuncoesServents = input("ajusta a lista:\n1 - lista de funcionarios\n2 - novos funcionarios\n3 - remover funcionarios\n")
    match FuncoesServents:
        case "1":
            print (servant)
            
        case '2':
            adicona = input('escreva o o nome do novo contratado      ')
            servant.append(adicona)
            print(servant)
            
        case '3':
            print(servant)
            tira = input('escreva o nome de quem saíra       ')
            servant.remove(tira)
            print('funcionarios atualizados')
            print(servant)

def Mbuilder():
    print('acesso liberado a lista de mestres de obras')
    FuncoesMestres = input("ajusta a lista:\n1 - mestre(s) atual\n2 - novo mestre\n3 - demitir mestre(s) \n")
    match FuncoesMestres:
        case "1":
            print (MasterBuilde)
            
        case '2':
            adicona = input('escreva quem é o novo mestre de obras       ')
            MasterBuilde.append(adicona)
            print(MasterBuilde)
            
        case '3':
            print(MasterBuilde)
            tira = input('escreva o nome do mestre de obras que saíra       ')
            MasterBuilde.remove(tira)
            print('mestre atualizado')
            print(MasterBuilde)
            
def interface_inicial():
    print(' ')
    acesso = input('quem esta acessando?: \n1 - servente - \n2 engenheiro - \n3 mestre de obra')
    match acesso:
         case '1':
             print('\n lista de materiais')
             print(materials) 
             
         case '2':
             print('\n acesso de engenheiro')
             escolha = input ('\n1 - materias \n2 - mestres de obras \n')
             match escolha: 
                 case '1':
                    materiais()
                    
                 case '2':
                    Mbuilder()

         case '3':
            print('\n acesso ou mestre de obras')
            escolha = input ('\n1 - materias \n2 - serventes \n')
            match escolha:
                 case '1':
                         materiais()
                 case '2':
                        fucionarios() 

         case _:
             print('acesso invalido' )
interface_inicial()



























    

          












