from odoo import fields, models, _, api


class SalesOrder(models.Model):
    _inherit = 'sale.order'

    chosen_products = fields.Many2many('product.template', compute='_compute_chosen_products')

    @api.depends('order_line', 'order_line.product_template_id')
    def _compute_chosen_products(self):
        for rec in self:
            rec.chosen_products = rec.order_line.mapped('product_template_id').ids if rec.order_line else False


class SalesOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_template_id = fields.Many2one(domain=False)
