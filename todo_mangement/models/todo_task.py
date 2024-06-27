from odoo import _, api, fields, models
from datetime import datetime, date
from odoo.exceptions import ValidationError


class ToDoTask(models.Model):
    _name = 'todo.task'
    _description = 'todo.task'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Task Name', tracking=1)
    assign_to = fields.Many2one('res.partner', tracking=1)
    description = fields.Text()
    active = fields.Boolean(default=True)
    due_date = fields.Date(default=fields.Date.context_today, tracking=1)
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('closed', 'Closed'),
    ], tracking=1)
    estimated_time = fields.Float()
    line_ids = fields.One2many('todo.task.line', 'task_id')
    is_late = fields.Boolean(compute='_check_expected_due_date', store=True)
    total_hours = fields.Float(compute="_compute_total_hours", store=True)
    progress = fields.Integer(string="Progress", compute='_compute_progress')

    @api.constrains('total_hours','estimated_time')
    def check_task_time(self):
        for rec in self:
            if rec.estimated_time <= rec.total_hours:
                raise ValidationError("Total Time should not exceed The Estimated Time for the Task")

    # @api.constrains('status')
    # def check_project_complete(self):
    #     for rec in self:
    #         if rec.status != "Done":
    #             raise ValidationError("Please make sure that all tasks have been completed")

    @api.depends('due_date', 'state')
    def _check_expected_due_date(self):
        for task in self:
            task.is_late = (
                    task.due_date and task.due_date < fields.Date.context_today(task) and task.state != 'completed')

    def action_new(self):
        for rec in self:
            print("inside action_new ")
            rec.state = 'new'

    def action_in_progress(self):
        for rec in self:
            print("inside action_in_progress ")
            rec.state = 'in_progress'

    def action_completed(self):
        for rec in self:
            print("inside action_completed ")
            rec.state = 'completed'

    def action_closed(self):
        for rec in self:
            rec.state = 'closed'

    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = _("%s (copyyy)") % self.name
        return super(ToDoTask, self).copy(default=default)

    def name_get(self):
        return [(rec.id, "%s [%s]" % (rec.name, str(rec.due_date))) for rec in self]

    @api.model
    def default_get(self, vals):
        res = super(ToDoTask, self).default_get(vals)
        res['due_date'] = date.today()
        return res

    @api.depends('line_ids.user_taken_time')
    def _compute_total_hours(self):
        for task in self:
            task.total_hours = sum(task.line_ids.mapped('user_taken_time'))

    @api.depends('total_hours', 'estimated_time')
    def _compute_progress(self):
        for rec in self:
            if rec.total_hours and rec.estimated_time:
                total_to_estimated = rec.total_hours / rec.estimated_time
                if 0.1 <= total_to_estimated <= 0.25:
                    rec.progress = 25
                elif 0.25 < total_to_estimated <= 0.5:
                    rec.progress = 50
                elif 0.5 < total_to_estimated <= 0.75:
                    rec.progress = 75
                elif 0.75 < total_to_estimated <= 1:
                    rec.progress = 100
                else:
                    rec.progress = 0
            else:
                rec.progress = 0


class ToDoTaskLine(models.Model):
    _name = 'todo.task.line'

    task_id = fields.Many2one('todo.task')
    date = fields.Date(string="Day", default=date.today())
    user_input = fields.Text(string="Task")
    user_taken_time = fields.Float(string="Taken Time")
