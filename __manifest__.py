# -*- coding: utf-8 -*-
{
    'name': "lol_app",

    'summary': """
        Application for managini different task""",

    'description': """
        In this aplication can hadd different tasks to do it Also tou can modigy different things!
    """,

    'author': "Ricardo Zoel Molina gandia",
    'website': "http://www.RicardoZ.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/games_views.xml',
        'views/team_views.xml',
        'views/player_views.xml',
        'views/elos_views.xml',
        'views/rol_views.xml',
        'views/menu.xml',
    #    'views/templates.xml',
        'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
