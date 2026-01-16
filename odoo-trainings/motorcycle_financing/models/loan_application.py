from odoo import models, fields


class LoanApplication(models.Model):
    _name = "loan.application"
    _description = "Loan Application"

    name = fields.Char(
        string="Application Number",
        required=True,
    )

    currency_id = fields.Many2one(
        comodel_name="res.currency",
        string="Currency",
        default=lambda self: self.env.company.currency_id.id,
        required=True,
    )

    down_payment = fields.Monetary(
        string="Downpayment",
        currency_field="currency_id",
    )

    interest_rate = fields.Float(
        string="Interest Rate (%)",
        digits=(5, 4),
    )

    loan_amount = fields.Monetary(
        string="Loan Amount",
        currency_field="currency_id",
    )

    loan_term = fields.Integer(
        string="Loan Term (Months)",
        required=True,
        default=36,
    )

    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("sent", "Sent"),
            ("review", "Credit Check"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
            ("signed", "Signed"),
            ("cancel", "Canceled"),
        ],
        string="Status",
        default="draft",
    )

    notes = fields.Html(
        string="Notes",
    )
