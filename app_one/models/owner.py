from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class Owner(models.Model):
    _name = "owner"

    name = fields.Char(trim=False)
    phone = fields.Char()
    address = fields.Char()

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Name must be unique')
    ]

    @api.constrains('name')
    def _check_unique_name(self):
        for record in self:
            if self.search_count([('name', '=', record.name)]) > 1:
                raise ValidationError(_('Name must be unique'))