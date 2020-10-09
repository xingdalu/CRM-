from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.shortcuts import HttpResponse
import re


class RbacMiddleware(MiddlewareMixin):

    def process_request(self, request):
        current_path = request.path_info
        for path in settings.VALID_URL_LIST:
            if re.match(path, current_path):
                return None
        permissions_url = request.session.get(settings.PERMISSION_SESSION_KEY)
        if not permissions_url:
            return HttpResponse('无法获得当前权限信息，请登录')
        flag = False
        for url in permissions_url:
            reg = '^%s$' % url
            if re.match(reg, current_path):
                flag = True
        if not flag:
            return HttpResponse('无权访问')


