from odoo import fields, models, _, api


class SalesOrder(models.Model):
    """
    Inherit Sale Order
    """
    _inherit = 'sale.order'

    order_ids = fields.Many2many('product.product', domain="[('id', 'not in', chosen_product)]")
    chosen_product = fields.Many2many('product.product', compute='_compute_chosen_product')

    # product_ids = fields.Many2many('product.product', compute='_compute_product_ids')
    #
    # @api.depends('order_line', 'order_line.product_id')
    # def _compute_product_ids(self):
    #     for rec in self:
    #         rec.product_ids = rec.order_line.mapped('product_id').ids if rec.order_line else False


    # @api.depends('product_ids')
    # def _compute_chosen_product(self):
    #     for record in self:
    #         record.chosen_product = record.product_ids


    @api.depends('order_line.product_id')
    def _compute_chosen_product(self):
        for record in self:
            record.chosen_product = record.order_line.mapped('product_id')


    # @api.depends('order_line.product_id')
    # def _compute_chosen_product(self):
    #     for record in self:
    #         record.chosen_product = record.env['sale.order.line'].search([
    #             ('order_id', '=', record.env.context.get('active_id', False)),
    #         ]).mapped('product_id')
    #

    # @api.depends('order_ids')
    # def _compute_chosen_product(self):
    #     for record in self:
    #         record.chosen_product = record.env['sale.order.line'].search([
    #             ('order_id', '=', record.id),
    #         ]).mapped('product_id')

    # @api.depends('order_ids')
    # def _compute_chosen_product(self):
    #     for record in self:
    #         record.chosen_product = [(6, 0, record.order_ids.ids)]


    # def default_get(self, fields):
    #     res = super(SalesOrder, self).default_get(fields)
    #
    #     # Check if there are chosen products in the context
    #     chosen_products = self.env.context.get('chosen_products', [])
    #
    #     # If there are chosen products, add them to the wizard's default values
    #     if chosen_products:
    #         res['order_ids'] = [(6, 0, chosen_products)]
    #
    #     return res

    def multi_order_action(self):
        print("multi_order_action!")
        action = self.env['ir.actions.act_window']._for_xml_id('app_one.adding_multiline_wizard_action')
        if self.id:
            action['context'] = {
                'default_order_ids': [(6, 0, self.order_ids.ids)],
            }
        return action


