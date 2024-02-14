# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_compare, float_is_zero, float_round


class MrpProduction(models.Model):
    """ Manufacturing Orders """
    _inherit = 'mrp.production'

    def action_confirm(self):
        res = super(MrpProduction,self).action_confirm()
        for each in self:
            self.move_finished_ids._set_quantity_done(each.product_qty)
        return res





