from django.shortcuts import render


def login(req):
    # POST -> login / GET -> login Form  제공
    if req.method == 'POST':
        pass
    else:
        return render(req, 'login.html')