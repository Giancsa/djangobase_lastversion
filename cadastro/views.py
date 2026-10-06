from django.shortcuts import render


def index(request):

    contexto = {
        'nome': 'Gian',
        'idade': 30,
        'frutas': ['Maçã', 'Banana', 'Laranja', 'Uva', 'Cajá', 'Manga'],
    }

    return render(
        request,
        'cadastro/index.html',
        contexto
    )


def contato(request):

    contexto = {
        "nome": "Gian"
    }

    return render(
        request,
        'cadastro/contato.html',
        contexto
    )
