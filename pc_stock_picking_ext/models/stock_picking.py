# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class StockPicking(models.Model):

    _inherit = 'stock.picking'

    task_id = fields.Many2one(
        'project.task',
        string="Task")
    gadget_id = fields.Many2one(
        'product.template',
        string="Gadget",
        related="task_id.product_id")
  