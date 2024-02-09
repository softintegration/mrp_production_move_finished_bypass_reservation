# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, Command, fields, models, _
from odoo.osv import expression
from odoo.tools import float_compare, float_round, float_is_zero, OrderedSet


class StockMove(models.Model):
    _inherit = 'stock.move'

    def _should_bypass_reservation(self, forced_location=False):
        self.ensure_one()
        location = forced_location or self.location_id
        return location.should_bypass_reservation() or self.product_id.type != 'product'