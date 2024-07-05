from odoo.exceptions import ValidationError
from datetime import date
from odoo import fields, models, api, _


class Property(models.Model):
    _name = "property"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=1, default='New', size=30, tracking=1)
    active = fields.Boolean(default=True)
    description = fields.Text()
    postcode = fields.Char(required=1, )
    date_availability = fields.Date(default=date.today())
    # expected_price = fields.Float(digits=(0, 5))
    expected_price = fields.Float()
    selling_price = fields.Float(tracking=2)
    diff = fields.Float(compute='_compute_diff', store=1, inverse='_inverse_compute_diff')
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ], default='north')
    owner_id = fields.Many2one('owner')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('closed', 'Closed'),
    ], default="draft", tracking=1)

    _sql_constraints = [
        ('unique_name', 'unique("name")', 'Name must be unique')
    ]

    # It is not working why!
    # _sql_constraints = [
    #     ('constraint_name', 'constraint_logic', 'constraint_message'),
    # ]

    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for rec in self:
            if rec.bedrooms == 0:
                print('not valid')
                raise ValidationError('Please add valid number to bedrooms')

    # CRUD Methods
    @api.model_create_multi
    def create(self, vals):
        res = super(Property, self).create(vals)
        print("inside create method")
        return res

    @api.model
    def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
        print("inside _search/read method")
        res = super(Property, self)._search(domain, offset=offset, limit=limit, order=order,
                                            access_rights_uid=access_rights_uid)
        return res

    # No decorators needed for update(write) method
    def write(self, vals):
        res = super(Property, self).write(vals)
        print("inside write/update method")
        return res

    # No decorators needed for delete(unlink) method
    def unlink(self):
        res = super(Property, self).unlink()
        print("inside unlink/delete method")
        return res

    def action_draft(self):
        for rec in self:
            print("inside action_draft ")
            rec.state = 'draft'

    def action_pending(self):
        for rec in self:
            print("inside action_pending ")
            rec.state = 'pending'

    def action_sold(self):
        for rec in self:
            print("inside action_sold ")
            rec.state = 'sold'

    def action_closed(self):
        for rec in self:
            print("inside action_closed ")
            rec.state = 'closed'

    @api.depends('expected_price', 'selling_price')
    def _compute_diff(self):
        for rec in self:
            if rec.expected_price and rec.selling_price:
                rec.diff = rec.expected_price - rec.selling_price

    @api.depends('diff')
    def _inverse_compute_diff(self):
        for rec in self:
            if rec.diff and rec.expected_price and rec.selling_price == 0:
                rec.selling_price = rec.expected_price - rec.diff
            if rec.diff and rec.selling_price and rec.expected_price == 0:
                rec.expected_price = rec.selling_price + rec.diff

    @api.onchange('state')
    def _onchange_state(self):
        for rec in self:
            print("inside _onchange_state ")

    @api.onchange('name')
    def _onchange_name(self):
        for rec in self:
            if rec.name.isalpha():
                return {
                    'warning': {
                        'title': 'warning',
                        'message': 'Name should be only letters! ',
                        'type': 'notification',
                    }
                }

    # def action_open_related_owner(self):
    #     action = self.env['ir.actions.actions']._for_xml_id('app_one.owner_action')
    #     view_id =self.env.ref('app_one.owner_view_form')
    #     action['res_id'] = self.owner_id.id
    #     action['views'] = [[view_id, 'form']]
    #     return action

    def action_open_related_owner(self):
        action = self.env['ir.actions.actions']._for_xml_id('app_one.owner_action')

        view_id = self.env.ref('app_one.owner_view_form')
        if not view_id:
            raise ValueError("View not found or incorrectly referenced")

        if len(self.owner_id) != 1:
            raise ValueError("Expected singleton for owner_id, found multiple records")

        action['res_id'] = self.owner_id.id
        action['views'] = [[view_id.id, 'form']]
        return action

