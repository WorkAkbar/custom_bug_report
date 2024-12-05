from odoo import models, fields, api

class BugReport(models.Model):
    _name = 'bug.report'
    _description = 'Bug Report'

    # Field untuk judul laporan
    name = fields.Char(
        string="Title",
        required=True
    )

    # Field untuk deskripsi laporan
    description = fields.Text(
        string="Description"
    )

    # Field untuk jenis laporan
    report_type = fields.Selection(
        [
            ('bug', 'Bug'),
            ('complaint', 'Complaint'),
            ('feature', 'Feature Request')
        ],
        string="Report Type",
        required=True,
    )

    # Field untuk prioritas laporan
    priority = fields.Selection(
        [
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High')
        ],
        string="Priority",
        default='medium',  # Default priority adalah 'medium'
    )

    # Field untuk pengguna yang melaporkan bug
    user_id = fields.Many2one(
        'res.users',
        string="Reported By",
        default=lambda self: self.env.user,
        readonly=True,  # Field ini hanya baca
    )

    # Field untuk status laporan
    status = fields.Selection(
        [
            ('new', 'New'),
            ('in_progress', 'In Progress'),
            ('resolved', 'Resolved'),
            ('closed', 'Closed')
        ],
        string="Status",
        default='new',  # Default status adalah 'new'
        tracking=True,  # Melacak perubahan status
    )

    # Tanggal laporan dibuat
    created_date = fields.Datetime(
        string="Created Date",
        default=fields.Datetime.now,
        readonly=True
    )

    # Tanggal laporan diperbarui terakhir kali
    updated_date = fields.Datetime(
        string="Last Updated",
        readonly=True
    )

    @api.onchange('report_type')
    def _onchange_report_type(self):
        """
        Fungsi onchange untuk mengubah prioritas secara otomatis
        berdasarkan jenis laporan.
        """
        if self.report_type == 'bug':
            self.priority = 'high'
        elif self.report_type == 'complaint':
            self.priority = 'medium'
        elif self.report_type == 'feature':
            self.priority = 'low'

    @api.model
    def create(self, vals):
        """
        Override method create untuk menambahkan logika tambahan
        saat membuat laporan baru.
        """
        vals['created_date'] = fields.Datetime.now()
        res = super(BugReport, self).create(vals)
        return res

    def write(self, vals):
        """
        Override method write untuk logika tambahan saat
        memperbarui laporan bug.
        """
        vals['updated_date'] = fields.Datetime.now()
        res = super(BugReport, self).write(vals)
        return res

    def action_set_in_progress(self):
        """
        Fungsi untuk mengubah status laporan menjadi 'In Progress'.
        """
        self.status = 'in_progress'

    def action_resolve(self):
        """
        Fungsi untuk mengubah status laporan menjadi 'Resolved'.
        """
        self.status = 'resolved'

    def action_close(self):
        """
        Fungsi untuk mengubah status laporan menjadi 'Closed'.
        """
        self.status = 'closed'
