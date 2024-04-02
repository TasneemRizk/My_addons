from odoo import fields, models, api


class AddingMultiline(models.TransientModel):
    _name = 'adding.multiline'

    chosen_product = fields.Many2many('product.product', compute='_compute_chosen_product')
    product_ids = fields.Many2many('product.product', string='Selected Products',
                                   domain="[('id', 'not in', chosen_product)]")

    # @api.depends('product_ids')
    # def _compute_chosen_product(self):
    #     for record in self:
    #         record.chosen_product = [(6, 0, record.product_ids.ids)]

    @api.depends('product_ids')
    def _compute_chosen_product(self):
        for record in self:
            record.chosen_product = record.env['sale.order.line'].search([
                ('order_id', '=', record.env.context.get('active_id', False)),
            ]).mapped('product_id')


    # def default_get(self, fields):
    #     res = super(AddingMultiline, self).default_get(fields)
    #
    #     # Check if there are chosen products in the context
    #     chosen_products = self.env.context.get('chosen_products', [])
    #
    #     # If there are chosen products, add them to the wizard's default values
    #     if chosen_products:
    #         res['product_ids'] = [(6, 0, chosen_products)]
    #
    #     return res

    def action_confirm(self):
        active_id = self.env.context.get('active_id')
        get_active_id = self.env['sale.order'].browse(active_id)
        line_env = self.env['sale.order.line']
        if get_active_id.state == 'draft':
            for rec in self.product_ids:
                so_order_line = line_env.create({
                    'product_id': rec.id,
                    'order_id': get_active_id.id,
                })



# from odoo import fields, models, api, _


#
#
# class AddingMultiline(models.TransientModel):
#     _name = 'adding.multiline'
#
#     product_ids = fields.Many2many('product.product')
#
#     # def default_get(self, fields):
#     #     res = super(AddingMultiline, self).default_get(fields)
#     #     # Check if there are selected products in the context
#     #     selected_products = self.env.context.get('selected_products', [])
#     #     # If there are selected products, add them to the wizard's default values
#     #     if selected_products:
#     #         res['product_ids'] = [(6, 0, selected_products)]
#     #     return res
#
#     chosen_product = []
#
#     @api.depends('product_ids.rec.id')
#     def _compute_chosen_product(self):
#         for record in self:
#             record.chosen_product = ', '.join(record.product_ids.mapped('rec.id'))
#
#
#     def action_confirm(self):
#         active_id = self.env.context.get('active_id')
#         get_active_id = self.env['sale.order'].browse(active_id)
#         line_env = self.env['sale.order.line']
#         if get_active_id.state == 'draft':
#             for rec in self.product_ids:
#                 domain = [(rec.id, 'not in', 'chosen_product')]
#                 filtered_search = self.env['sale.order.line'].search(domain)
#                 if rec.domain:
#
#                     so_order_line = line_env.create({
#                         'product_id': rec.id,
#                         'order_id': get_active_id.id,
#                     })
#
#



    # def action_confirm(self):
    #     print("action_confirm!")
    #     active_id = self.env.context.get('active_id')
    #     print("active_id!: ", active_id)
    #     get_active_id = self.env['sale.order'].browse(active_id)
    #     print("get_active_id!: ", get_active_id)
    #     line_env = self.env['sale.order.line']
    #     print("line_env!: ", line_env)
    #     if get_active_id.state == 'draft':
    #         for rec in self.product_ids:
    #             so_order_line = line_env.create({
    #                 'product_id': rec.id,
    #                 'order_id': get_active_id.id,
    #             })
    #             print("rec.id!: ", rec.id)
    #             print("get_active_id.id!: ", get_active_id.id)
    #             print("so_order_line!: ", so_order_line)

    # default_code = fields.Char(string="Internal Reference", compute='_compute_default_code', store=True)
    # product_name = fields.Char(string="Name", compute='_compute_product_name', store=True)
    # product_variant = fields.Many2many('product.product', string="Product Variant", compute='_compute_product_variant', store=True)
    # product_variant = fields.Many2many(
    #     'product.product',
    #     string="Product Variant",
    #     compute='_compute_product_variant',
    #     store=True,
    #     order='name',  # Replace with the actual field you want to order by
    # )
    # @api.depends('product_ids.default_code')
    # def _compute_default_code(self):
    #     for record in self:
    #         record.default_code = ', '.join(record.product_ids.mapped('default_code'))
    #
    # @api.depends('product_ids.name')
    # def _compute_product_name(self):
    #     for record in self:
    #         record.product_name = ', '.join(record.product_ids.mapped('name'))

    # @api.depends('product_ids.product_template_variant_value_ids')
    # def _compute_product_variant(self):
    #     for record in self:
    #         record.product_variant = [(6, 0, record.product_ids.mapped('product_template_variant_value_ids').ids)]
