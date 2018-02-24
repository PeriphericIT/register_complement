# -*- coding: utf-8 -*-
{
    'name': "Cadastro Complementar",

    'summary': """
        Modulo para o cadastro de Pessoas Fisicas, Juridicas, Fundos de investimentos, etc...""",

    'description': """
        Modulo para o cadastro de Pessoas Fisicas, Juridicas, Fundos de investimentos, etc...
    """,

    'author': "Peripheric IT",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','br_base'],

    # always loaded
    'data': [
        'views/res_partner_views.xml',
        'views/res_structure_views.xml',
        'views/res_cnab_views.xml',
        #'views/task.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [

    ],
}
