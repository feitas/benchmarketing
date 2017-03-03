# -*- coding: utf-8 -*-
{
    'name': "Benchmarketing",

    'summary': """
        Benchmarketing，企业对标管理""",

    # 'description': """
    #     Long description of module's purpose
    # """,

    'author': "Tony",
    'website': "http://malijie.cc",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/benchmarketing_views.xml',
        'views/team_views.xml',
        'views/target_views.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}