from odoo import fields, models, api, _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    charge = fields.Char(
        string="Charge",
        readonly=False,
        config_parameter='sat_companies.charge')
    
    
    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('charge', self.charge)
        return res
