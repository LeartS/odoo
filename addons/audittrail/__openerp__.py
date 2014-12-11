# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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


{
    'name': 'Audit Trail',
    'version': '1.0',
    'category': 'Tools',
    'description': """
This module lets administrator track every user operation on all the objects of the system.
===========================================================================================

The administrator can subscribe to rules for read, write and delete on objects 
and can check logs.
    """,
    'author': 'OpenERP SA',
    'website': 'http://www.openerp.com',
    'depends': ['base'],
    'data': [
        'wizard/audittrail_view_log_view.xml',
        'audittrail_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo': ['audittrail_demo.xml'],
    'installable': True,
    'auto_install': False,
    'images': ['images/audittrail1.jpeg','images/audittrail2.jpeg','images/audittrail3.jpeg'],
}
