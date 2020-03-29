# -*- coding: utf-8 -*-
{
    'name': "Agenda D&D",  # Module title
    'summary': "Recuerda que dias tienes partida",  # Module subtitle phrase
    'description': """Long description""",  # You can also rst format
    'author': "Gabriel Sanchez",
    'website': "http://www.example.com",
    'category': 'Uncategorized',
    'version': '12.0.1',
    'depends': ['base'],
    # This data files will be loaded at the installation (commented becaues file is not added in this example)
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/agenda_dnd.xml'
    ],
    # This demo data files will be loaded if db initialize with demo data (commented becaues file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
}
