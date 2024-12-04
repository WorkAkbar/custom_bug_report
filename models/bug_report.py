
from odoo import models, fields

class BugReport(models.Model):
    _name = 'bug.report'
    _description = 'Bug Report'

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    report_type = fields.Selection(
        [
            ('bug', 'Bug'),
            ('complaint', 'Complaint'),
            ('feature', 'Feature Request')
        ],
        string="Report Type",
        required=True,
    )
    priority = fields.Selection(
        [
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High')
        ],
        string="Priority",
    )
    user_id = fields.Many2one('res.users', string="Reported By", default=lambda self: self.env.user)
