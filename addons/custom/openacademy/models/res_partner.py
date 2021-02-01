from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_instructor = fields.Boolean(String="¿Es instructor?", default=False)
