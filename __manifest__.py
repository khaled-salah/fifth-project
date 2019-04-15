# -*- coding: utf-8 -*-
{
    'name': "TM Management",

    'summary': """Timesheet management System""",

    'description': """
         for managing:
            - resources
            - projects
            - workflows
            


    """,
    "license": "AGPL-3",
    'author': "BBI-Consultancy",
    'website': "http://www.bbi-consultancy.com",
    'category': 'Timesheet',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ["hr_timesheet",'mail',],
    'images': [
    ],

    'data': [
        "views/inherit_timesheet.xml",


    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
