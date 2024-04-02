from odoo import fields, models, api, _


class Owner(models.Model):
    _name = "owner"

    name = fields.Char(trim=False)
    phone = fields.Char()
    address = fields.Char()

