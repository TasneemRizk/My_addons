{
    'name':"App One",
    'author':"Tasneem Rezk",
    'category':"",
    'sequence': 1,
    'version':'17.0.0.1.0',
    'depends':['base',
               'account',
               'sale',
               'calendar',
               ],
    'data':[
        'security/ir.model.access.csv',
        'wizard/change_state_view.xml',
        'views/base_menu.xml',
        'views/property_view.xml',
        'views/owner_view.xml',
    ],
    # 'assets': {
    #     'web.assets_backend': ['app_one/static/src/property.css']
    # },
    'installable': True,
    'application': False,
    'auto_install': False,
}