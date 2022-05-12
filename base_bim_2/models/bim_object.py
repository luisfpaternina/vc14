# -*- coding: utf-8 -*-
# Part of Ynext. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _
from datetime import datetime

class BimObject(models.Model):
    _description = "BIM Object"
    _name = 'bim.object'
    _order = "id desc"
    _rec_name = 'desc'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']

    name = fields.Char('Code', default="New")
    desc = fields.Char('Description')
    project_id = fields.Many2one('bim.project', 'Project', ondelete="cascade", domain="[('company_id','=',company_id)]")
    user_id = fields.Many2one('res.users', string='Responsable', tracking=True,
        default=lambda self: self.env.user)
    company_id = fields.Many2one(comodel_name="res.company", string="Company", default=lambda self: self.env.company,
                                 required=True)
    image_medium = fields.Binary("Image Size")

    def _set_image_medium(self):
        self._set_image_value(self.image_medium)

    @api.model
    def create(self, vals):
        if vals.get('name', "New") == "New":
            vals['name'] = self.env['ir.sequence'].next_by_code('bim.object') or "New"
        return super(BimObject, self).create(vals)

    def name_get(self):
        res = super(BimObject, self).name_get()
        result = []
        for element in res:
            project_id = element[0]
            cod = self.browse(project_id).name
            desc = self.browse(project_id).desc
            name = cod and '[%s] %s' % (cod, desc) or '%s' % desc
            result.append((project_id, name))
        return result
