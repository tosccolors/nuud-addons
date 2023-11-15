
{
    "name": "Nuud Reports",
    "version": "16.0.0.0",
    "author": "Deepa, The Open Source Company (TOSC)",
    "category": "Reports",
    'website': 'https://www.tosc.nl',
    'description': "Report Enhancements specific to Nuud",
    "depends": ["sale", "purchase_stock", "account"],
    "data": [
        "views/sale_report_template.xml",
        "views/purchase_report_template.xml",
        "views/account_report_template.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
    "application": False,
}
