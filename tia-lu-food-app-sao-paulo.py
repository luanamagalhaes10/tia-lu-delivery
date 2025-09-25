
itens = []
pedidos = []
codigoP = 101   

while True:
    print("\n=== Bem-vindo ===")
    print("1 - Gerenciar menu de itens")
    print("2 - Gerenciar menu de pedidos")  
    print("3 - Sair")
    
    opcao = input("\nEscolha uma opção para prosseguir >> ")

   
    if opcao == "1":
        while True:   
            print("\n>>>> Menu de Itens <<<<")
            print("1 - Cadastrar item")
            print("2 - Listar itens")
            print("3 - Atualizar item")
            print("4 - Voltar")
            
            opcaoItem = input("\nEscolha uma opção>>")

            
            if opcaoItem == "1":
                nome = input("\nNome do item: ")
                descricao = input("Descrição: ")
                preco = float(input(f"Preço: "))
                estoque = int(input("Quantidade em estoque: "))

                item = [codigoP, nome, descricao, preco, estoque]
                itens.append(item)
                codigoP += 1  # pro codigo ficar sempre subindo um numero

                print("\nItem cadastrado com sucesso!")

          
            elif opcaoItem == "2":
                if not itens:
                    print("\n Nenhum item cadastrado.")
                else: 
                    print("\n>>>> Itens cadastrados <<<<\n")
                    for item in itens: 
                        print(f"Código: {item[0]} \nNome: {item[1]} \nDescrição: {item[2]} \nPreço: {item[3]} \nEstoque: {item[4]}\n")
                       

            
            elif opcaoItem == "3":
                if not itens:
                    print("\n Ainda não há itens cadastrados para atualizar.")
                else: 
                    codigo_id = int(input("\nDigite o código do item: "))
                    encontrado = False

                    for item in itens: 
                        if item[0] == codigo_id: 
                            print(f"\nAtualizando o item: {item[1]}")

                            novoNome = input("Novo nome: ")
                            if novoNome != "":
                                item[1] = novoNome          

                            novaDesc = input("Nova descrição: ")
                            if novaDesc != "":
                                item[2] = novaDesc

                            novoPreco = input("Novo preço: ")
                            if novoPreco != "":
                                item[3] = float(novoPreco)

                            novoEstoque = input("Novo estoque: ")
                            if novoEstoque != "":
                                item[4] = int(novoEstoque)
                                print("\n Item atualizado com sucesso!")
                                
                                encontrado = True
                                break
                                
                        if not encontrado:
                            print("\n Item não encontrado.")

            elif opcaoItem == "4":
                break  

            else:
                print("\nOpção inválida.")

    # MENU DOS PEDIDOS 
   