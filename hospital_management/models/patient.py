from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime, date
import re


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Gathering patient information'
    # _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    ref = fields.Char(string='Reference', )
    birth_date = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute="_compute_age", readonly=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    active = fields.Boolean(string="Active", default=True)
    image = fields.Image()

    tag_ids = fields.Many2many('hospital.configuration', string='Tags')

    appointment_count = fields.Integer()
    # appointment_ids = fields.One2many('hospital.appointment')
    parent = fields.Char(string="Parent's name: ", )
    marital_status = fields.Selection([('single', 'Single'), ('married', 'Married')])
    partner_name = fields.Char(string="Partner: ")

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.birth_date:
                rec.age = today.year - rec.birth_date.year
            else:
                rec.age = 0

    @api.onchange('age')
    def _parent_wanted(self):
        for rec in self:
            if rec.age > 18:
                rec.parent = False

    # @api.constrains('name', 'partner_name')
    # def _name_validation(self):
    #     for rec in self:
    #         if (not rec.name
    #                 or not re.match("^[A-Za-z]*$", rec.name)
    #                 or not re.match("^[A-Za-z]*$", rec.partner_name)
    #                 or not re.match("^[A-Za-z]*$", rec.parent)):
    #             raise ValidationError(
    #                 "Patient's name, Partner's name or Parent's name  should contain only alphabetic characters.")
    #             # raise ValueError("Name should contain only alphabetic characters.")
    #             # Note that we use ValidationError to check constrains values NOT ValueError

    @api.model
    def create(self, record):
        record['ref'] = self.env['ir.sequence'].next_by_code('patients.sequence')
        return super(HospitalPatient, self).create(record)
