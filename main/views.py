from django.shortcuts import render


def index(request):
    data = {
        'title': 'Bereza index',
        'values': ['Some', 'Hello', 123, "54"],
        'object': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football',
        },
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html', {'title': 'Bereza about'})


def test(request):
    return render(request, 'main/test.html', {'title': 'Bereza test'})
