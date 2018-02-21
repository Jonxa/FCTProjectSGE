# -*- coding: utf-8 -*-
{
    'name': "Proyecto SGE",

    'summary': """" Make the tracing of FTC students.""",

    'description': """
            Proyecto SGE module for tracing students:
            -
            -
            -
            -
    """,

    'author': "Jon Xabier Gimenez",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','report'],

    # always loaded
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/proyectosge.xml',
        'views/fctpartner.xml',
        'views/rules.xml',
        'views/usuario.xml',
        'views/reportActivity.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}