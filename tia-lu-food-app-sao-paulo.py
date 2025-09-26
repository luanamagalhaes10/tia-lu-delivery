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
                preco = float(input("Preço: "))
                estoque = int(input("Quantidade em estoque: "))

                item = [codigoI, nome, descricao, preco, estoque]
                itens.append(item)
                codigoI += 1  

                print("\nItem cadastrado com sucesso!")

            elif opcaoItem == "2":
                if not itens:
                    print("\n Nenhum item cadastrado.")
                else: 
                    print("\n>>>> Itens cadastrados <<<<\n")
                    for item in itens: 
                        print(f"Código: {item[0]} \nNome: {item[1]} \nDescrição: {item[2]} \nPreço: R${item[3]:.2f} \nEstoque: {item[4]}\n")

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
                        for item in itens:
                            print(f"Código: {item[0]} \nNome: {item[1]} \nDescrição: {item[2]} \nPreço: R${item[3]:.2f} \nEstoque: {item[4]}\n")

                        codigoEscolhido = int(input("\nDigite o código do item que deseja adicionar: "))
                        encontrado = False  

                        for item in itens: 
                            if item[0] == codigoEscolhido: 
                                encontrado = True
                                qtt = int(input("Digite a quantidade que deseja: "))
                                if qtt <= item[4]:
                                    PedidoItem.append([item[1], qtt, item[3]])
                                    total += item[3] * qtt
                                    item[4] -= qtt
                                    print(f"{qtt}x {item[1]} adicionado ao pedido\n")
                                else:
                                    print("Estoque insuficiente")
                                break  

                        if not encontrado:
                            print("Item não encontrado")

                        continuar = input("Deseja adicionar outro item? \n [1] Sim \n [2] Não:\n")
                           
                        if continuar == "1":
                            continue
                        else: 
                            break

                    if PedidoItem:
                        usarCupom = input("\nTem cupom de desconto? ")
                        if usarCupom == "TIALUSP":
                            total *= 0.9
                            print("Cupom aplicado! Desconto de 10%")
                        elif usarCupom.strip() != "":
                            print("\nCupom inválido, prosseguindo sem desconto.\n")

                        pedido = [CodigoP, PedidoItem, total, "AGUARDANDO APROVAÇÃO"]
                        pedidos.append(pedido)
                        print(f"\nPedido {CodigoP} criado com sucesso!\nTotal: R${total:.2f}")
                        CodigoP += 1

                    else:
                        print("\nPedido não pode ser vazio")

            elif opcaoPedido == "2":
                pendentes = [p for p in pedidos if p[3] == "AGUARDANDO APROVAÇÃO"]
                if not pendentes: 
                    print("\nNenhum pedido pendente.")
                else:
                    for pedido in pendentes: 
                        print(f"\nPedido {pedido[0]} | Total: R${pedido[2]:.2f}")
                        escolha = input("Aceitar (1) ou Rejeitar (2)? ") 
                        if escolha == "1": 
                            pedido[3] = "FAZENDO" 
                            print(f"Pedido {pedido[0]} ACEITO e agora está FAZENDO.") 
                        else: 
                            pedido[3] = "REJEITADO" 
                            print(f"Pedido {pedido[0]} REJEITADO.")

            elif opcaoPedido == "3":
                codigo_id = int(input("Digite o código do pedido: "))
                encontrado = False
                for pedido in pedidos:
                    if pedido[0] == codigo_id:
                        encontrado = True
                        print(f"Status atual: {pedido[3]}")
                        print("1 - FAZENDO")
                        print("2 - FEITO")
                        print("3 - ESPERANDO ENTREGADOR")
                        print("4 - SAIU PARA ENTREGA")
                        print("5 - ENTREGUE")
                        op = input("Escolha o novo status: ")

                        if op == "1": pedido[3] = "FAZENDO"
                        elif op == "2": pedido[3] = "FEITO"
                        elif op == "3": pedido[3] = "ESPERANDO ENTREGADOR"
                        elif op == "4": pedido[3] = "SAIU PARA ENTREGA"
                        elif op == "5": pedido[3] = "ENTREGUE"
                        else: print("Opção inválida.")
                        print(f"Status do pedido {pedido[0]} atualizado para {pedido[3]}.")
                        break
                if not encontrado:
                    print("Pedido não encontrado.")

            elif opcaoPedido == "4":
                codigo_id = int(input("Digite o código do pedido: "))
                for pedido in pedidos:
                    if pedido[0] == codigo_id:
                        if pedido[3] in ["AGUARDANDO APROVAÇÃO", "ACEITO", "FAZENDO"]:
                            pedido[3] = "CANCELADO"
                            print(f"Pedido {codigo_id} foi CANCELADO.")
                        else:
                            print("Esse pedido não pode ser cancelado.")
                        break
                else:
                    print("Pedido não encontrado.")

            elif opcaoPedido == "5":
                if not pedidos:
                    print("\nNenhum pedido registrado.")
                else:
                    print("\n>>>> Todos os pedidos <<<<")
                    for pedido in pedidos:
                        print(f"\nCódigo: {pedido[0]}")
                        print("Itens:")
                        for item in pedido[1]:
                            subtotal = item[1] * item[2]
                            print(f" - {item[0]} x{item[1]} (R${item[2]:.2f} cada) = R${subtotal:.2f}")

                        print(f"Total: R${pedido[2]:.2f}")
                        print(f"Status: {pedido[3]}")

            elif opcaoPedido == "6":
                break

            else:
                print("\nOpção inválida.")

    elif opcao == "3":
        print("Saindo do sistema...")
        break
