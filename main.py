import busca_aleatoria
import busca_media
import insercao_aleatoria

      
def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Realizar buscas(80%), insercoes(10%) e remocoes(10%) aleatoriamente")
    print("2. Realizar buscas e insercoes. Sendo as buscas realizadas na metade dos vetores e listas encadeadas")
    print("3. Realizar buscas(20%), insercoes(40%) e remocoes(40%) aleatoriamente")
    print("4. Sair")
    print(67 * "-")
  


if __name__ == '__main__':
    loop=True
    
    while loop:
        print_menu()
        choice = input("Entre sua opcao [1-4]: ")
        if choice=='1':     
            print("Opcao 1 foi escolhida")
            busca_aleatoria.main() 
        elif choice=='2':
            print("Opcao 2 foi escolhida")
            busca_media.main()
        elif choice=='3':
            print("Opcao 3 foi escolhida")
            insercao_aleatoria.main()
        elif choice=='4':
            print("Opcao 4 foi escolhida")
            print('Saindo....')
            loop=False
        else:
            input("Opcao incorreta. Aperte qualquer tecla para tentar novamente..")
