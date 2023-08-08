from odoo import api, models, fields


class Product(models.Model):
    _name = "block.block"

    extra_service = fields.Many2many("product.product", string="Select Products")

    quantity = fields.Integer(string="Quantity")

    client = fields.Many2one("res.partner", string="client", ondelete="Cascade")

    state = fields.Selection(
        [("draft", "Draft"), ("confirm", "Confirm")], default="draft"
    )

    def prepare_invoice_line(self):
        return {
            "name": self.client.name,
            "origin": self.client,
            # "discount_rate": "",
            # "discount_type": "amount",
            # 'type': 'out_invoice',
            # 'account_id': self.client.id,
            # 'partner_shipping_id': self.partner_shipping_id.id,
            # 'journal_id': journal_id,
            "currency_id": self.env.company.currency_id.id,
            # 'comment': self.note,
            "partner_id": self.client.id,
            # 'payment_term_id': self.payment_term_id.id,
            # 'fiscal_position_id': self.fiscal_position_id.id or self.partner_invoice_id.property_account_position_id.id,
            "company_id": self.env.company.id,
            "user_id": self.env.user.id,
            # 'team_id': self.team_id.id,
            # 'transaction_ids': [(6, 0, self.transaction_ids.ids)],
        }

    def sale_order(self):
        self.state = "confirm"

        if self.client:
            my_dict = self.prepare_invoice_line()
            inv_id = self.env["sale.order"].create(my_dict)
            for service in self.extra_service:
                service_dict = {
                    "product_id": service.id,
                    "order_id": inv_id.id,
                    "price_unit": service.lst_price,
                    "name": service.name,
                    "product_uom_qty": self.quantity,
                }
                self.env["sale.order.line"].create(service_dict)

            inv_id.supply_rate()
