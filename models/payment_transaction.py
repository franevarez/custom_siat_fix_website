from odoo import models

class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _finalize_post_processing(self):
        # Antes de reconciliar/invocación de SIAT, fuerza integer
        for tx in self:
            for inv in tx.invoice_ids:
                for line in inv.line_ids:
                    val = line.product_id.actividad_economica
                    if isinstance(val, str) and val.isdigit():
                        line.product_id.actividad_economica = int(val)
        return super()._finalize_post_processing()
