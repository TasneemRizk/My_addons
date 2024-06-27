""" Initialize Calendar Event """

from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError, Warning


class CalendarEvent(models.Model):
    """
        Inherit Calendar Event:
         -
    """
    _inherit = 'calendar.event'



