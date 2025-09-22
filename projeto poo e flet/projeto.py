
class Cliente:
    def __init__(self, id:int, nome:str, telefone:str, email:str):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email


class Quarto:
    def __init__(self, n_quarto:int, tipo:str, preco:float, status_quarto:bool):
        self.n_quarto = n_quarto
        self.tipo = tipo
        self.preco = preco
        self.status_quarto = status_quarto


class Reserva:
    def __init__(self, dono:int, quarto:int, check_in:str, check_out:str, status_reserva):
        self.dono = dono
        self.quarto = quarto
        self.check_in = check_in
        self.check_out = check_out
        self.status_reserva = status_reserva

class Hotel:
    def __init__(self):
        self.lista_de_clientes = []
        self.id_cliente = 1
        self.lista_de_quartos = []
        self.numero_quarto = 1
        self.lista_de_reservas = []
        self.id_reserva = 1
    
    def adicionarCliente(self):
        nome = input("Digite o nome do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        email = input("Digite o email do cliente: ")

        novo_cliente = {
            "ID": self.id_cliente,
            "Nome": nome,
            "Telefone": telefone,
            "E-mail": email
        }

        self.id_cliente += 1

        self.lista_de_clientes.append(novo_cliente)
        return f"Cliente {nome} cadastrado com sucesso"

    def verTodosClientes(self):
        if len(self.lista_de_clientes) == 0:
            print("Lista Vazia")
        else:
            for cliente_da_vez in self.lista_de_clientes:
                print(f"""
                ID: {cliente_da_vez['ID']}
                Nome: {cliente_da_vez['Nome']}
                Telefone: {cliente_da_vez['Telefone']}
                E-mail: {cliente_da_vez['E-mail']}
                """)

    def modificarCliente(self):
        id_cliente = int(input("digite o id do cliente que quer modificar: "))
        for cliente in self.lista_de_clientes:
         if cliente["ID"] == id_cliente:
             cliente["Nome"] = input(f"Novo nome ({cliente['Nome']}): ") or cliente["Nome"]
             cliente ['Telefone'] = (input (f"Novo telefone {cliente['Telefone']}: ") or cliente["Telefone"]) 
             cliente ['E-mail' ] = input (f"Novo email{cliente['E-mail']}: ") or cliente ["E-mail"]
             print ("o cliente foi atualizado")
             
        else:
            print("cliente não encontrado")


    def excluirCliente(self):
     id_cliente = int(input("Digite o ID do cliente que deseja excluir: "))
     for cliente in self.lista_de_clientes:
        if cliente["ID"] == id_cliente:
           self.lista_de_clientes.remove(cliente)
           print("cliente excluido")
           return
        print("cliente não encontrado")
             





    def adicionarQuarto(self):
        tipo = input("Digite o tipo do quarto: ")
        preco = float(input("Digite o preço da diária do quarto: "))

        novo_quarto = {
            "Número": self.numero_quarto,
            "Tipo": tipo,
            "Preço": preco,
            "Status": True
        }

        self.numero_quarto += 1

        self.lista_de_quartos.append(novo_quarto)
        return f"Quarto {self.numero_quarto - 1} cadastrado com sucesso"

    def verTodosQuartos(self):
        if len(self.lista_de_quartos) == 0:
            print("Lista Vazia")
        else:
            for quarto_da_vez in self.lista_de_quartos:
                print(f"""
                Número: {quarto_da_vez['Número']}
                Tipo: {quarto_da_vez['Tipo']}
                Preço: {quarto_da_vez['Preço']}
                Status: {quarto_da_vez['Status']}
                """)

    def verificarQuartosDisponiveis(self):
        if len(self.lista_de_quartos) == 0:
            print("Lista Vazia")
        else:
            for quarto_da_vez in self.lista_de_quartos:
                if quarto_da_vez['Status'] == True:
                    print(f"""
                    Número: {quarto_da_vez['Número']}
                    Tipo: {quarto_da_vez['Tipo']}
                    Preço: {quarto_da_vez['Preço']}
                    Status: {quarto_da_vez['Status']}
                    """)

    def modificarQuarto(self):
        n_quarto = int(input("Digite o número do quarto que deseja modificar: "))
        for quarto in self.lista_de_quartos:
         if quarto["Número"] == n_quarto:
            quarto["Tipo"] = input(f"Novo tipo ({quarto['Tipo']}): ") or quarto["Tipo"]
            preco = input(f"Novo preço ({quarto['Preço']}): ")
            quarto["Preço"] = float(preco) if preco else quarto["Preço"]
            status = input(f"Disponível (s/n) ({quarto['Status']}): ")
         if status.lower() == "s":
                quarto["Status"] = True
         elif status.lower() == "n":
                quarto["Status"] = False
            

    def excluirQuarto(self):
        n_quarto = int(input("Digite o número do quarto que deseja excluir: "))
        for quarto in self.lista_de_quartos:
         if quarto["Número"] == n_quarto:

            self.lista_de_quartos.remove(quarto)
            return "Quarto excluído com sucesso!"
        return "Quarto não encontrado."




    def adicionarReserva(self):
        for cliente_da_vez in self.lista_de_clientes:
            print(f"ID: {cliente_da_vez['ID']} | Nome: {cliente_da_vez['Nome']}")             
        dono = int(input("Digite o ID cliente que está reservando o quarto: "))

        for quarto_da_vez in self.lista_de_quartos:
            print(f"Número: {quarto_da_vez['Número']} | Status: {quarto_da_vez['Status']}")
        n_quarto = int(input("Digite o número do quarto que será reservado: "))

        check_in = input("Digite a data de entrada: ")
        check_out = input("Digite a data de saída: ")


        nova_reserva = {
            "ID": self.id_reserva,
            "Dono": dono,
            "Número Quarto": n_quarto,
            "Check-In": check_in,
            "Check-Out": check_out,
            "Status Quarto": "Reservado" #Em Andamento ou Concluído
        }

        self.id_reserva += 1

        self.lista_de_reservas.append(nova_reserva)
        return f"Reserva de número {self.id_reserva - 1} cadastrado com sucesso"




    def verTodasReservas(self):
        if len(self.lista_de_reservas) == 0:
            print("Lista Vazia")
        else:
            for reserva_da_vez in self.lista_de_reservas:
                print(f"""
                ID: {reserva_da_vez['ID']}
                Dono: {reserva_da_vez['Dono']}
                Número Quarto: {reserva_da_vez['Número Quarto']}
                Check-In: {reserva_da_vez['Check-In']}
                Check-Out: {reserva_da_vez['Check-Out']}
                Status Quarto: {reserva_da_vez['Status Quarto']}
                """)

    
    def modificarReserva(self):
        id_reserva = int(input("Digite o ID da reserva que deseja modificar: "))
        for reserva in self.lista_de_reservas:
         if reserva["ID"] == id_reserva:
            reserva["Check-In"] = input(f"Novo Check-In ({reserva['Check-In']}): ") or reserva["Check-In"]
            reserva["Check-Out"] = input(f"Novo Check-Out ({reserva['Check-Out']}): ") or reserva["Check-Out"]
            status = input(f"Novo status (Reservado/Concluído/Cancelado) ({reserva['Status Quarto']}): ")
            reserva["Status Quarto"] = status or reserva["Status Quarto"]
           
        

    def excluirReserva(self):
        id_reserva = int(input("Digite o ID da reserva que deseja excluir: "))
        for reserva in self.lista_de_reservas:
         if reserva["ID"] == id_reserva:
            # liberar o quarto
            for quarto in self.lista_de_quartos:
                if quarto["Número"] == reserva["Número Quarto"]:
                    quarto["Status"] = True
            self.lista_de_reservas.remove(reserva)
            return "Reserva excluída com sucesso!"
        return "Reserva não encontrada."
        

if __name__ == "__main__":
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
