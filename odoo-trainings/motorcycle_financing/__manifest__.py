# -*- coding: utf-8 -*-
{
    "name": "Motorcycle Financing",
    "summary": "Streamlines the loan application process for dealerships.",
    "category": "Kawiil/Custom Modules",
    "version": "0.0.1",
    "website": "https://github.com/GimanthaP-OasisPro/kawiil-motors-odoo",
    "author": "Gimantha Pathirana",
    "license": "OPL-1",
    "application": True,
    "installable": True,
    "depends": ["base"],
    'data': [
    'security/motorcycle_financing_groups.xml',
    'security/ir.model.access.csv',
    'security/rules.xml',

    'views/loan_application_views.xml',
    'views/motorcycle_financing_menu.xml',
],
    'demo': [
    'data/loan_demo.xml',
],

}
