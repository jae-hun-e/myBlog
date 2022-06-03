from django.shortcuts import render, redirect
# DB에 있는 정보인지 아닌지 Django가 알아서 판단해줌
from django.contrib import auth


def login(req):
    # POST -> login / GET -> login Form  제공
    if req.method == 'POST':
        userid = req.POST['username']
        pwd = req.POST['password']
        # Django 안의 auth 안에 이미 user라는 DB가 만들어져있음 그래서 user라는 객체를 만들 수 있음
        user = auth.authenticate(req, username=userid, password=pwd)
        if user is not None:
            auth.login(req, user)  # user객체로 로그인 함
            return redirect('home')
        else:
            return render(req, 'login.html')
    else:
        return render(req, 'login.html')


def logout(req):
    auth.logout(req)
    return redirect('home')