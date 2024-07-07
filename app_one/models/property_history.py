from odoo.exceptions import ValidationError
from datetime import date, datetime
from odoo import fields, models, api, _


class PropertyHistory(models.Model):
    _name = "property.history"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # user_id = fields.Many2one('res.users')
    # property_id = fields.Many2one('property')
    # old_state = fields.Char()
    # new_state = fields.Char()
    # reason = fields.Char()
    line_ids = fields.Many2many('property.history.line', 'history_id')

    property_id = fields.Many2one('property', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('closed', 'Closed'),
    ], required=True)
    reason = fields.Text()
    changed_by = fields.Many2one('res.users', string='Changed By', required=True)
    changed_on = fields.Datetime(string='Changed On', default=fields.Datetime.now)


class PropertyHistoryLine(models.Model):
    _name = "property.history.line"

    history_id = fields.Many2one('property.history')
    area = fields.Float()
    description = fields.Char()
