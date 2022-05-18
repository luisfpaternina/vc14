{
    'name': 'pc stock picking extend',

    "summary": """This module create stock.picking app for users: transfer request""",

    'version': '14.0.0.0',

    'author': "Process Control",

    'website': "www.processcontrol.es",

    'category': 'stock',

    'depends': [

        'base',
        'stock',
        'sat_companies_stock',
        'sat_companies_industry',

    ],

    'data': [

        'security/security.xml',  
        #'security/ir.model.access.csv',    
        'views/stock_picking.xml',
              
    ],
    
    "images": [
        'static/description/icon.png'
    ],
    

    "application": False,
    "installable": True,
    "auto_install": False,

}
