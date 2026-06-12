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
            tira = input('escreva oque quer tirar     ')
            materials.remove(tira)
            print(materials)
materiais()

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
            tira = input('escreva o nome de quem saíra       ')
            servant.remove(tira)
            print(servant)
 fucionarios()

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
            tira = input('escreva o nome do mestre de obras que saíra       ')
            MasterBuilde.remove(tira)
            print(MasterBuilde)
 Mbuilder()
