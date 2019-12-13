from django.shortcuts import render


# from django.http import HttpResponse


def main(request):
    return render(
        request,
        'myApp/main.html')


def lottery(request):
    return render(
        request,
        'myApp/lottery.html'
    )


def about(request):
    return render(
        request,
        'myApp/about.html'
    )


def contact(request):
    return render(
        request,
        'myApp/contact.html'
    )


def news(request):
    return render(
        request,
        'myApp/news.html'
    )
