from odoo import api, fields, models


class SaleOrderLineInherit(models.Model):

    _inherit = 'sale.order.line'

    lot_id = fields.Many2one(
        comodel_name='stock.production.lot',
        domain="[('product_id', '=', product_id), ('company_id', '=', company_id)]",
        string='Product lot',
        required=False)



    #
    def _prepare_procurement_values(self, group_id=False):
        vals = super()._prepare_procurement_values(group_id=group_id)
        if self.lot_id:
            vals["new_lot_id"] = self.lot_id.id
        return vals

    # @api.onchange("product_id")
    # def product_id_change(self):
    #     super().product_id_change()
    #     self.lot_id = False
    #
    # @api.onchange("product_id")
    # def _onchange_product_id_set_lot_domain(self):
    #     return {"domain": {"lot_id": [("product_id", "=", self.product_id.id)]}}

    # def _prepare_procurement_values(self, group_id=False):
    #     vals = super()._prepare_procurement_values(group_id=group_id)
    #     if self.lot_id:
    #         vals["lot_id"] = self.lot_id.id
    #     return vals

    #
    # def _prepare_procurement_values(self, group_id=False):
    #     res = super(SaleOrderLineInherit, self)._prepare_procurement_values(group_id)
    #     # I am assuming field name in both sale.order.line and in stock.move are same and called 'YourField'
    #     if self.lot_id:
    #         res["restrict_lot_id"] = self.lot_id.id
    #     return res
# #
# class StockRuleInherit(models.Model):
#     _inherit = 'stock.rule'
#
#     def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, values, group_id):
#         res = super(StockRuleInherit, self)._get_stock_move_values(product_id, product_qty, product_uom, location_id,
#                                                                    name, origin, values, group_id)
#
#         return res


    # @api.depends('product_id')
    # def trigger_this_method(self):
    #  self.env['stock.move'].write({'lot_id':self.lot_id.id})




    # def _prepare_procurement_values(self, group_id=False):
    #     vals = super()._prepare_procurement_values(group_id=group_id)
    #     if self.lot_id:
    #         vals["restrict_lot_id"] = self.lot_id.id
    #     return vals
    #
    # @api.onchange("product_id")
    # def product_id_change(self):
    #     res = super().product_id_change()
    #     self.lot_id = False
    #     return res
    #
    # @api.onchange("product_id")
    # def _onchange_product_id_set_lot_domain(self):
    #     return {"domain": {"lot_id": [("product_id", "=", self.product_id.id)]}}




    # # @api.model
    # def create(self,vals):
    #     vals = self.env['stock.move.line'].write({'lot_id':self.product_lot_id})
    #     return super(SaleOrderLineInherit, self).create(vals)

    #
    # @api.onchange("product_id")
    # def product_id_change(self):
    #     res = super().product_id_change()
    #     self.product_lot_id= False
    #     return res
    # @api.model
    # def create(self,vals):
    #     print('created-------------------------->')
    #     self.env['stock.move.line'].write({'lot_id':self.product_lot_id.id,'company_id':self.company_id.id})
    #     rtn = super(SaleOrderLineInherit, self).create(vals)
    #     return rtn

