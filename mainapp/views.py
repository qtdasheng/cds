import json

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from common import md5_
from .models import TSysUser, TUser, TSysRole, TMessage, TGoods, TCaipu

from chidiansha import settings


# Create your views here.
def login(request):
    # 分两种用户，一个是会员，一个管理员（系统）
    print('--->', request.method)
    if request.method == 'POST':
        print(request.POST)

        error = None

        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        remeber = request.POST.get('remeber', '')  # checkbox

        password_ = md5_.hash_encode(password)  # 转成md5后的密文

        # 验证用户名和口令是否为空
        if not all((username, password)):
            error = f'用户名或口令不能为空！'

        login_user = TSysUser.objects.filter(username=username, auth_string=password_).first()
        if login_user:
            # 系统管理员
            role_ = login_user.role
            login_info = {
                '_id': login_user.id,
                'name': role_.name,
                'code': role_.code
            }

        else:
            login_user = TUser.objects.filter(name=username, auth_string=password).first()
            if login_user:
                # 会员
                login_info = {
                    '_id': login_user.user_id,
                    'name': login_user.name,
                    'code': '',
                    'head': login_user.head,
                    'email': login_user.mail,
                    'phone': login_user.phone
                }
            else:
                error = f'{username} 用户名或口令错误！'

        if not error:
            request.session['login_user'] = login_info
            return redirect('/')

    return render(request, 'login.html', locals())


def logout(request):
    del request.session['login_user']
    return redirect('/login/')


def user(request):
    users = TUser.objects.all()

    return render(request, 'user.html', locals())


def goods(request):
    goods = TGoods.objects.all()

    return render(request, 'good.html', locals())


def caipus(request):
    caipus = TCaipu.objects.all()

    return render(request, 'caipu.html', locals())


def index(request):
    return render(request, 'dashboard.html')


def message(request):
    objs = TMessage.objects.all()
    action = request.GET.get('action', '')
    if action == 'del':
        TMessage.objects.get(pk=request.GET.get('id_')).delete()

    return render(request, 'message/list.html', locals())


def role(request):
    action = request.GET.get('action', '')
    if action == 'del':
        TSysRole.objects.get(pk=request.GET.get('role_id')).delete()

    roles = TSysRole.objects.all()
    return render(request, 'role/list.html', locals())


def list_sys_user(request):
    action = request.GET.get('action', '')
    if action == 'del':
        TSysUser.objects.get(pk=request.GET.get('id_')).delete()

    # 查询系统时，除去超级管理员的用户
    users = TSysUser.objects.filter(~Q(pk=request.session['login_user']['_id'])).all()
    return render(request, 'sys_user/list.html', locals())


class EditRoleView(View):
    def get(self, request):
        role_id = request.GET.get('role_id', '')
        if role_id:
            role = TSysRole.objects.get(pk=role_id)
        return render(request, 'role/edit.html', locals())

    def post(self, request):
        from .forms import RoleForm
        role_id = request.POST.get('id', '')
        if role_id:
            form = RoleForm(request.POST, instance=TSysRole.objects.get(pk=role_id))
        else:
            form = RoleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/role/')

        errors = json.loads(form.errors.as_json())
        return render(request, 'role/edit.html', locals())


class EditSysUserView(View):
    def get(self, request):
        id_ = request.GET.get('id_', '')
        if id_:
            obj = TSysUser.objects.get(pk=id_)

        roles = TSysRole.objects.filter(~Q(code='admin'))
        return render(request, 'sys_user/edit.html', locals())

    def post(self, request):
        from .forms import SysUserForm
        id_ = request.POST.get('id', '')
        if id_:
            form = SysUserForm(request.POST, instance=TSysUser.objects.get(pk=id_))
        else:
            form = SysUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/list_sysuser/')

        errors = json.loads(form.errors.as_json())

        roles = TSysRole.objects.filter(~Q(code='admin'))

        return render(request, 'sys_user/edit.html', locals())


class EditMessageView(View):
    def get(self, request):
        id_ = request.GET.get('id_', '')
        if id_:
            obj = TMessage.objects.get(pk=id_)

        return render(request, 'message/edit.html', locals())

    def post(self, request):
        from .forms import MessageForm
        id_ = request.POST.get('id_', '')
        if id_:
            form = MessageForm(request.POST, instance=TMessage.objects.get(pk=id_))
        else:
            form = MessageForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/message/')

        errors = json.loads(form.errors.as_json())
        return render(request, 'message/edit.html', locals())


class AuditMessage(View):
    def get(self, request):
        action = request.GET.get('action', '')
        if action:
            obj = TMessage.objects.get(pk=request.GET.get('id_'))
            if action == 'yes':
                obj.state = 1
            elif action == 'no':
                obj.state = 2
                obj.note = request.GET.get('note', '')
            obj.save()
            obj.full_clean()

        objs = TMessage.objects.filter(state=0).all()
        return render(request, 'message/list_audit.html', locals())
