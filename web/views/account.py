from django.shortcuts import render, HttpResponse, redirect
from rbac.models import UserInfo
from rbac.service.init_permissions import init_permissions


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    current_user = UserInfo.objects.filter(name=user, password=pwd).first()
    if not current_user:
        return render(request, 'login.html', {'msg': '用户名或密码错误'})
    init_permissions(request, current_user)
    return redirect(to='list')