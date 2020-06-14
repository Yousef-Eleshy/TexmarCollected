# -*- coding: utf-8 -*-
{
    'name': "texmar_collected",

    'summary': """
         Includes: Size of Pieces - Customer Order - Purchase Order Cancel""",

    'description': """
         Includes: Size of Pieces - Customer Order - Purchase Order Cancel
    """,

    'author': "EgyMentors",
    'website': "http://www.egymentors.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mrp', 'sale_management', 'stock', 'purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/inv_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
