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
            adicona = input('escreva o que quer adicionar')
            materials.append(adicona)
            print(materials)
        case '3':
            tira = input('escreva oque quer tirar')
             materials.remove(tira)
            print(materials)
materiais()

def fucionarios():
    print('acesso liberado a lista de serventes')
    FuncoesServents = input("ajusta a lista:\n1 - lista de empregados\n2 - contradas\n3 - tirar materias\n")
    match FuncoesServents:
        case "1":
            print (servant)
        case '2':
            adicona = input('escreva o que quer adicionar')
            servant.append(adicona)
            print(servant)
        case '3':
            tira = input('escreva oque quer tirar')
            servant.remove(tira)
            print(servant)
servant()
