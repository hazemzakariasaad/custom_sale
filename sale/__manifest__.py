{
    'name': 'Custom Sales Enhancements',
    'version': '1.0',
    'summary': 'Add custom fields to Sale Order',
    'category': 'Sales',
    'depends':  ['sale_management'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,

}