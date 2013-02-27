# -*- encoding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

{
    "name" : "Taxes included in expense",
    "version" : "1.1",
    "author" : "Savoir-faire Linux",
    "category" : "Account",
    "website": "http://wwww.savoirfairelinux.com",
    "license": "GPL-3",
    "description": """
        This module adds a checkbox to tax to include tax in expense invoices.
        It is useful if your taxes are not included in the price, but you
        want to ease the life of your employees by allowing them to enter 
        their expenses with the taxes included.
        
        The tax calculation doesn't work in v7 for an expense. The expense now 
        create a voucher that only has one tax rate by voucher and we can't 
        safely select one tax rate per expense form. To fix this situation the
        expense form should suport the taxes like a supplier invoice form and a 
        the end of the workflow produce a voucher and the journal entries like
        what is done when a supplier invoice is open.
    """,
    "depends" : ["base", "account"],
    "init_xml" : [],
    "update_xml" : [
        "account_tax_expense_include_view.xml"
    ],
    "active": False,
    "installable": False
}
