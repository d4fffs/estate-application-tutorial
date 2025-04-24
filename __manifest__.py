{
    'name:': "estate",
    'version' : '1.0',
    'depends' : ['base'],
    'author' : 'Daffa Faiq',
    'category' : 'App', 
    'description' : """
    This Module is used to learn basic odoo 17 technical
    """,
     'application': True,
     'data': [
         'security/ir.model.access.csv',    
         'views/menu.xml',
         'views/estate_property.xml'
     ]
}