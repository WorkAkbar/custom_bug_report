{
    'name': 'Bug Report Module',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Pelaporan Bug, Keluhan, dan Permintaan Fitur',
    'author': 'Akbar',
    'depends': ['base'],  # Modul bawaan Odoo yang digunakan
    'data': [
        'views/bug_report_view.xml',  # File XML untuk tampilan
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

