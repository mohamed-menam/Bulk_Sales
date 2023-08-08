# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Bulk Sale",
    "version": "1.1",
    "summary": "MY First Model",
    "author": " ",
    "sequence": 1,
    "description": """sale""",
    "category": "Invoicing Management",
    "website": "https://www.odoo.com/page/billing",
    "license": "LGPL-3",
    "depends": [
        "sale_management",
        "sale_discount_total",
        "account",
        "l10n_generic_coa",
    ],
    "data": ["security/ir.model.access.csv", "views/blockproduct.xml"],
    "demo": [],
    "installable": True,
    "auto_install": False,
}
