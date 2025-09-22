from projeto import Hotel



hotel = Hotel()

while True:
    menu = input("""
    Escolha uma opçao:
    1 - Gerenciar Clientes
    2 - Gerencair Quartos
    3 - Gerenciar Reservas
    4 - Sair
    """)

    match menu:
        case "1":
            while True:
                menu_clientes = input("""
                Escolha uma opçao:
                1 - Adicionar Cliente
                2 - Ver todos os Cliente
                3 - Modicar Cliente
                4 - Excluir Cliente
                0 - Voltar
                """)

                match menu_clientes:
                    case "1":
                        print(hotel.adicionarCliente())
                    case "2":
                        hotel.verTodosClientes()
                    case "3":
                        print(hotel.modificarCliente())
                    case "4":
                        print(hotel.excluirCliente())
                    case "0":
                        break
                    case _:
                        print("Opção inválida")
        
        case "2":
            while True:
                menu_quartos = input("""
                Escolha uma opçao:
                1 - Adicionar Quarto
                2 - Ver todos os Quarto
                3 - Modicar Quarto
                4 - Excluir Quarto
                5 - Ver Quartos Disponíveis
                0 - Voltar
                """)

                match menu_quartos:
                    case "1":
                        print(hotel.adicionarQuarto())
                    case "2":
                        hotel.verTodosQuartos()
                    case "3":
                        print(hotel.modificarQuarto())
                    case "4":
                        print(hotel.excluirQuarto())
                    case "5":
                        hotel.verificarQuartosDisponiveis()
                    case "0":
                        break
                    case _:
                        print("Opção inválida")


        case "3":
            while True:
                menu_reservas = input("""
                Escolha uma opção:
                1 - Adicionar Reserva
                2 - Ver todos os Reserva
                3 - Modicar Reserva
                4 - Excluir Reserva
                0 - Voltar
                """)

                match menu_reservas:
                    case "1":
                        print(hotel.adicionarReserva())
                    case "2":
                        hotel.verTodasReservas()
                    case "3":
                        print(hotel.modificarReserva())
                    case "4":
                        print(hotel.excluirReserva())
                    case "0":
                        break
                    case _:
                        print("Opção inválida")
        case "4":
            print("Fim do progama")
            break
        case _:
            print("Opção inválida")
