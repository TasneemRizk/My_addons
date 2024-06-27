from odoo.exceptions import ValidationError
from datetime import date
from odoo import fields, models, api, _


class Building(models.Model):
    _name = "building"
    _description = "building"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'code'

    name = fields.Char()
    no = fields.Integer()
    code = fields.Char()
    description = fields.Text()
    active = fields.Boolean(drfault=True)
