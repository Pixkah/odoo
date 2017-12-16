# -*- coding: utf-8 -*-
{
    'name': "Pixkah",

    'summary': """
        Module for Pixkah business and operations""",

    'description': """
        Module for Pixkah business and operations
    """,

    'author': "Tecnología y Software Pixkah SC",
    'website': "http://www.pixkah.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'business',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}