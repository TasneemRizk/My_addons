# -*- coding: utf-8 -*-
{
    'name': 'To Do List',
    'summary': 'To Do List',
    'author': "Tasneem Rezk",
    'version': '17.0.0.1.0',
    'category': "Tasneem's practise",
    'sequence': 1,
    'depends': [
        'base',
        'account',
        'sale',
        'calendar',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/to_do.xml',
        'views/all_tasks.xml',
        'views/base_menu.xml',
        'reports/tasks_report.xml',
    ],
    # 'assets':{
    #     'web.assets_backend':['todo_management/static/src/css/todo.css']
    # },
    'installable': True,
    'application': True,
    'auto_install': False,
}
