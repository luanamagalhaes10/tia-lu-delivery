
itens = []
pedidos = []
codigoI = 101   
CodigoP = 1

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

                item = [codigoI, nome, descricao, preco, estoque]
                itens.append(item)
                codigoI += 1  # pro codigo ficar sempre subindo um numero

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
    elif opcao == "2":
        while True:
            print("\n>>>> Menu de Pedidos <<<<\n")
            print("1 - Criar pedido")
            print("2 - Processar pedidos pendentes")
            print("3 - Atualizar status de pedido")
            print("4 - Cancelar pedido")
            print("5 - Consultar pedidos")
            print("6 - Voltar")

            opcaoPedido = input("\nEscolha uma opção para prosseguir >> ")

            if opcaoPedido == "1":
                if not itens:
                    print("\nNão há itens cadastrados no sistema")
                else:
                    PedidoItem = []
                    total = 0

                    while True:
                        print("\n      Cardapio     \n")
                        print(f"Código: {item[0]} \nNome: {item[1]} \nDescrição: {item[2]} \nPreço: {item[3]} \nEstoque: {item[4]}\n")

                        codigoI = int(input("\nDigite o código do item que deseja adicionar: \n"))
                        if codigoI == 0:
                            break

                        qtt = int(input(f"Digite a quantidade que deseja: "))

                        for item in itens: 
                            if item[0] == codigoI: 
                                if qtt <= item[4]:
                                    PedidoItem.append([item[1], qtt, item[3]])
                                    total += item[3] * qtt
                                    item[4] -= qtt
                                    print(f"{qtt}x {item[1]} adicionado ao pedido\n")

                                else:
                                    print("Estoque insuficiente")
                                    break
                            else:
                                print("Item não encontrado")

                    if PedidoItem:
                        #conferir este calculo depois
                        usarCupom = input("\nCupom de desconto:")
                        if usarCupom == "TIALUSP":
                            total *= 0.9

                        pedido = [CodigoP, PedidoItem, total, "AGUARDANDO APROVAÇÃO"]
                        pedidos.append(pedido)
                        print("\nPedido {CodigoP} criado com sucesso!\n Total: R${total:.2f}")
                        CodigoP += 1

                    else:
                        print("\nPedido não pode ser vazio")
            elif opcaoPedido == "2":
                pendentes = [p for p in pedidos if p[3] == "AGUARDANDO APROVAÇÃO"]
                if not pendentes: 
                    print("\nNenhum pedido pendente.")
                else:
                    for pedido in pendentes: 
                        print("\nPedido {pedido[0]}|Total: R${pedido[2]:.2f}")
                        escolha = input("Aceitar (a) ou Rejeitar (r)? ") 
                        if escolha.lower() == "a": 
                            pedido[3] = "ACEITO" 
                            print(f"Pedido {pedido[0]} ACEITO.") 
                        
                        else: 
                            pedido[3] = "REJEITADO" 
                            print(f"Pedido {pedido[0]} REJEITADO.")
