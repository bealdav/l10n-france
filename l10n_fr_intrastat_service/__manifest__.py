# Copyright 2010-2019 Akretion France (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'France Intrastat Service (DES)',
    'version': '12.0.1.0.0',
    'category': 'Localisation/Report Intrastat',
    'license': 'AGPL-3',
    'summary': 'Module for Intrastat service reporting (DES) for France',
    'author': 'Akretion,Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/l10n-france',
    'depends': ['intrastat_base'],
    'data': [
        'security/ir.model.access.csv',
        'views/intrastat_service_view.xml',
        'data/intrastat_service_reminder.xml',
        'security/intrastat_service_security.xml',
    ],
    'installable': True,
    'application': True,
}
