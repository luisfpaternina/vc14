from odoo import fields, models, api, _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    charge = fields.Char(
        string="Charge",
        readonly=False,
        config_parameter='sat_companies.charge')
    show_technical = fields.Boolean(
        string="Enable technical",
        related="company_id.show_technical",
        readonly=False,
        config_parameter='sat_companies.show_technical')
    is_potencial_client = fields.Boolean(
        string="Is potencial client",
        related="company_id.is_potencial_client",
        readonly=False,
        config_parameter='sat_companies.is_potencial_client')
    
    
    def set_values(self):
        ##############################################
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('charge', self.charge)
        self.env['ir.config_parameter'].sudo().set_param('show_technical', self.show_technical)
        self.env['ir.config_parameter'].sudo().set_param('is_potencial_client', self.is_potencial_client)
        return res
