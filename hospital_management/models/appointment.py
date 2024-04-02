from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime, date
import re


class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Apply patient appointment'

    appointment_sequence = fields.Char(string='Appointment Sequence')
    # patient = fields.Many2one('hospital.patient', string='Patient')
    reference = fields.Char(string='Reference')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    # doctor = fields.Many2one('hospital.doctor', string='Doctor')
    appointment_time = fields.Datetime(string='Appointment Time')
    # appointment_time = fields.Time()
    booking_date = fields.Date()
    # appointment_time = fields.DateTime()
    activities = fields.Char()
    # status = fields.Selection()
