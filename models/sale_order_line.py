# -*- coding: utf-8 -*-

from odoo import models,fields,api,_
from odoo.exceptions import UserError

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    product_type = fields.Selection(related='product_id.type',store=True)

