import flet as ft
from projeto import Hotel

hotel = Hotel()

def main (page: ft.Page ):
    page.title ="sistema de Hotel"

    nome = ft.TextField (label="Nome", width= 250)
    telefone = ft.TextField(label="Telefone", width =200)
    email = ft.TextField (label="E-mail", width=250)
    clientes_list = ft.Column(scroll="auto")

    def atualizar_clientes():
     clientes_list.controls.clear()
     for c in hotel.lista_de_clientes:
        clientes_list.controls.append(
        ft.Text(f"{c['ID']} - {c['Nome']} - {c['Telefone']} - {c['E-mail']}")
            )
     page.update()
    
    def adicionar_cliente(e):
        if nome.value and telefone.value and email.value:
            hotel.lista_de_clientes (nome.value and email.value)
            nome.value, telefone.value, email.value = "","",""
            atualizar_clientes()
            page.update()

    clientes_tab = ft.Column([
        ft.Row([nome, telefone,email, ft.ElevatedButton ("Adicionar", on_click= adicionar_cliente)]),
        ft.Text("Lista de Clientes", size = 18, weight="bold"),
        clientes_list
    ])

    tipo_quarto = ft.TextField(label="Tipo (single, double, suite)", width=250)
    preco_quarto = ft.TextField(label="preço", width=150)
    quarto_list = ft.Column(scroll="auto")

    def atualizar_quartos():
        for q in hotel.lista_de_quartos:
            status = "Disponivel" if q["Status"] else "ocupado"
            quarto_list.controls.append(ft.Text(f"{q['Numero']} - {q['Tipo']} - R${q['Preço']} - {status}"))
            page.update()

    def adicionar_quarto(e):
         if tipo_quarto.value and preco_quarto.value:
            try:
                hotel.adicionar_quarto(tipo_quarto,float(preco_quarto.value))
                tipo_quarto.value, preco_quarto.value = "",""
                atualizar_quartos()
                page.update()
            except ValueError:
                page.snack_bar = ft.SnackBar(ft.text("Preço inválido"))
                page.snack_bar.open_True
                page.update()

    quartos_tab = ft.Column([
          ft.Row([tipo_quarto, preco_quarto,ft.ElevatedButton("Adicionar", on_click = adicionar_quarto)]),
        ft.Text("Lista de Quartos", size = 18, weight="bold"),
        quarto_list
    ])
    
    id_cliente_reserva = ft.TextField(label="ID Client", width=150)
    numero_quarto_reserva = ft.TextField(label="Número Quarto", width= 150)
    checkin = ft.TextField (label="Check-in", width=150)
    checkout = ft.TextField(label = "Cheko-out", width=150)
    reservas_list = ft.Column(scroll="auto")

    def atualizar_Reservas():
        reservas_list.controls.clear()
        for r in hotel.lista_de_reservas:
            reservas_list.controls.append(ft.Text(
                f"{r['Id']} - cliente: {r['cliente']['Nome']} - Quartos: {r['Quarto'] ['Numero']}- {r['Chekin']} até {r['Chekout']} - {r['Status']}"
            ))
        page.update()
    
    def criar_reservas(e):
        if id_cliente_reserva.value and numero_quarto_reserva.value and checkin.value and checkout.value:
            try:
                hotel.criar_reservas(int(id_cliente_reserva.value), int(numero_quarto_reserva.value), checkout.value, checkout.value)
                id_cliente_reserva.value, numero_quarto_reserva.value, checkin.value,checkout.value ="", "","",""
                atualizar_Reservas()
                atualizar_quartos()
                page.update()
            except ValueError:
                page.snack_bar = ft.SnackBar(ft.Text("ID inválido"))
                page.snack_bar.open = True
                page.update()
    
    reservas_tab = ft.Column([
        ft.Row([id_cliente_reserva, numero_quarto_reserva,checkin,checkout,
                ft.ElevatedButton("Reservar", on_click=criar_reservas)]),
        ft.Text("LIsta de Reservas", size=18, weight="bold"),
        reservas_list
    ])
    
    
    tabs = ft.Tabs(
         selected_index=0,
         tabs=[
             ft.Tab(text="Clientes", content=clientes_tab),
             ft.Tab (text="Quartos", content=quartos_tab),
             ft.Tab(text="Reservas", content=reservas_tab),
        ],
        expand=1
    )  
 
    page.add(tabs)
    atualizar_clientes()
    atualizar_quartos()
    atualizar_Reservas()

ft.app(target=main)

    

    

