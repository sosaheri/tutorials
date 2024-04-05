
{
    'name': "HS Real State",
    'version': "1.0",
    'category': 'DEV',
    'summary': """
        No hello world
    """,
    'description': """
        My first Odoo App, no hello world
    """,
    'author': "Heriberto Sosa",
    'email': "sosaheriberto2001@gmail.com",
    'depends': [
        'base',
    ],    
    'application': True,
    "data": [
        "models/data/security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_menus.xml"
    ],


}


