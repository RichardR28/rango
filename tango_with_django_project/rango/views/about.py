from django.shortcuts import render


def about(request):
    context_dict = {'autor': 'Richard Alves Roling'}
    return render(request, 'rango/about.html', context=context_dict)
