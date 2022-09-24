from odoo import api, fields, models


class StockmovelineInherit(models.Model):

    _inherit = 'stock.move'




    new_lot_id = fields.Many2one(
        comodel_name='stock.production.lot',
        string='New_lot_id',
        required=False)


    # @api.model
    # def _prepare_procurement_values(self):
    #     vals = super()._prepare_procurement_values()
    #     vals["new_lot_id"] = self.new_lot_id.id
    #     return vals

    def _prepare_move_line_vals(self, quantity=None, reserved_quant=None):
        vals = super()._prepare_move_line_vals(
            quantity=quantity, reserved_quant=reserved_quant
        )
        if self.new_lot_id:

            vals["lot_id"] = self.new_lot_id.id
        return vals

    class StockRule(models.Model):
        _inherit = "stock.rule"

        def _get_custom_move_fields(self):
            fields = super()._get_custom_move_fields()
            fields += ["new_lot_id"]
            return fields

    # def create(self,vals):
    #
    #
    #     vals={
    #         'lot_id'
    #     }
    #     res = super(StockmovelineInherit, self).create(vals)
    #
    #     return res
    # #
    # def _update_reserved_quantity(self, need, available_quantity, location_id, lot_id=None, package_id=None,
    #                               owner_id=None, strict=True):
    #     lot_id = '123'
    #
    #
    #
    #     return super(StockmovelineInherit, self)._update_reserved_quantity()



    #
    # lot_id = fields.Many2one(
    #     'stock.production.lot', 'Lot/Serial Number',
    #     related='move_id.sale_line_id.lot_id',
    #     domain="[('product_id', '=', product_id), ('company_id', '=', company_id)]", check_company=True)