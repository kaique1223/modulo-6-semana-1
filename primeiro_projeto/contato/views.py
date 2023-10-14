from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    resposta = HttpResponse('''
<!DOCTYPE html>
<html>
<head>
    <title>Contato</title>
</head>
<body>
    <h1>Entre em Contato</h1>
    <form method="post">
        <a href="{% url 'contato' %}">Entre em Contato</a>

        <label for="id_nome">Nome:</label>
        <input type="text" id="id_nome" name="nome"><br><br>

        <label for="id_email">Email:</label>
        <input type="email" id="id_email" name="email"><br><br>

        <label for="id_mensagem">Mensagem:</label><br>
        <textarea id="id_mensagem" name="mensagem" rows="4" cols="50"></textarea><br><br>

        <input type="submit" value="Enviar">
    </form>
</body>
</html>
''')
    return resposta