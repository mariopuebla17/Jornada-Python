"""
Frontend -> parte visual
Backend -> lógica por trás do site

Frameworks:
- Django
- Flask
- Flet (usaremos esse) -> pip install flet
    > sites
    > programas de computador
    > aplicativos de celular
"""

""" passo a passo
Título
Botão iniciar o chat
    > popup
        > bem vindo
        > escreva seu nome
        > botão entrar
Abriu o chat
Mensagem: Usuário entrou no chat
Mensagens do chat
No fim do chat, campo de texto para enviar mensagem e botão enviar
"""

import flet as ft

def main(page):
    title = ft.Text("Hashzap")

    username = ft.TextField(label="Digite o nome de usuário")

    chat = ft.Column()

    def send_message_online(message_received):
        chat.controls.append(ft.Text(message_received))
        page.update()

    # criar túnel para envio de mensagem
    page.pubsub.subscribe(send_message_online)

    message_field = ft.TextField(label="Escreva sua mensagem aqui")

    def send_message(event):
        message_field_value = f"{username.value}: {message_field.value}"
        #enviar tudo para o túnel
        page.pubsub.send_all(message_field_value)
        message_field.value=""
        page.update()

    send_button = ft.ElevatedButton("Enviar", on_click=send_message)

    def enter_chat(event):
        # fechar popup
        popup.open=False
        # limpe a tela
        page.remove(start_button)
        # adicionar chat
        page.add(chat)
        # criar campo e botão de enviar mensagem
        linha_mensagem = ft.Row(
            [message_field, send_button]
        )
        page.add(linha_mensagem)
        text = f"{username.value} entrou no chat"
        chat.controls.append(ft.Text(text))
        page.update()

    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=ft.Text("Bem-vindo ao Hashzap"),
        content=username,
        actions=[
            ft.ElevatedButton("Entrar", on_click=enter_chat)
            ]
        )

    def start_chat(event):
        page.dialog = popup
        popup.open = True
        page.update()

    start_button = ft.ElevatedButton("Iniciar chat", on_click=start_chat)

    page.add(title)
    page.add(start_button)
# ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)