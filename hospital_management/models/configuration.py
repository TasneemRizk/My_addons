from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime, date
import re


class Configuration(models.Model):
    _name = 'hospital.configuration'
    _description = 'Apply patient configuration'

    name = fields.Char(string="Name")
    active = fields.Boolean(string="Active", default=True)
    # color = fields.Char(string='Color')
    color = fields.Integer(string='Color')

