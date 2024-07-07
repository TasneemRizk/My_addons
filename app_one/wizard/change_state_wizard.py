from odoo import fields, models, api

class ChangeState(models.TransientModel):
    _name = 'change.state'

    property_id = fields.Many2one('property')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('closed', 'Closed'),
    ], default="closed", tracking=1)
    reason = fields.Char()

    def action_confirm(self):
        self.ensure_one()  # تأكد من وجود سجل واحد فقط
        # تحديث حالة العقار
        self.property_id.write({
            'state': self.state,
            'change_reason': self.reason,
        })

        # تسجيل في السجل (log) لتتبع التغييرات
        self.env['property.history'].create({
            'property_id': self.property_id.id,
            'state': self.state,
            'reason': self.reason,
            'changed_by': self.env.uid,
        })

        # عرض رسالة تأكيد للمستخدم
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Confirmation',
                'message': 'The property state has been updated successfully.',
                'sticky': False,
            }
        }
    @api.model
    def action_open_change_state_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Change State Wizard',
            'res_model': 'change.state',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_property_id': self.env.context.get('active_id'),
            },
        }

# from odoo import fields, models
#
# class ChangeState(models.TransientModel):
#     _name = 'change.state'
#
#     property_id = fields.Many2one('property')
#     state = fields.Selection([
#         ('draft', 'Draft'),
#         ('pending', 'Pending'),
#     ], default='draft')
#     reason = fields.Char()
#
#     def action_confirm(self):
#         print('confirm')
