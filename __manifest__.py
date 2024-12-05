{
    'name': 'Bug Report Module',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Pelaporan Bug, Keluhan, dan Permintaan Penambahan Fitur',
    'author': 'Akbar',
    'website': 'https://https://maesindo.com',  # Tambahkan website perusahaan Anda
    'depends': [
        'base',  # Modul bawaan Odoo yang diperlukan
    ],
    'data': [
        'views/bug_report_view.xml',  # File XML untuk tampilan
    ],
    'installable': True,  # Modul dapat diinstal
    'application': True,  # Modul dianggap aplikasi
    'auto_install': False,  # Modul tidak terinstal otomatis
    'license': 'LGPL-3',  # Lisensi yang digunakan
}

