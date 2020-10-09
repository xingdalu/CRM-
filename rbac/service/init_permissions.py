from rbac.models import Permission
from django.conf import settings


def init_permissions(request, current_user):
    permissions_queryset = current_user.roles.filter(permissions__isnull=False).values('permissions__id',
                                                                                      'permissions__title',
                                                                                      'permissions__url',
                                                                                      'permissions__menu_id',
                                                                                      'permissions__menu__title',
                                                                                      'permissions__menu__icon').distinct()
    permissions_list = []
    menu_dict = {}
    for permission in permissions_queryset:
        permissions_list.append(permission['permissions__url'])
        if not permission['permissions__menu_id']:
            continue
        menu_id = permission['permissions__menu_id']
        node = {'title': permission['permissions__title'], 'url': permission['permissions__url']}
        if menu_id in menu_dict:
            menu_dict[menu_id]['children'].append(node)
        else:
            menu_dict[menu_id] = {'title': permission['permissions__menu__title'],
                                  'icon': permission['permissions__menu__icon'],
                                  'children': [node, ]}
    print(menu_dict)
    request.session[settings.PERMISSION_SESSION_KEY] = permissions_list
    request.session[settings.MENU_SESSION_KEY] = menu_dict
