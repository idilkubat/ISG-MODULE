from dateutil.relativedelta import relativedelta
from reportlab.platypus.tableofcontents import delta
import datetime
from odoo import fields, models, api
from odoo.fields import Date


class Employee(models.Model):
    _inherit = 'hr.employee'

    age = fields.Char(string='Age')
    started_job = fields.Date(string='İşe Giriş Tarihi')

    @api.onchange('birthday')
    def _compute_state(self):
        time_age = (fields.Date.today() - self.birthday).days
        years_age = fields.Integer(time_age / 365)
        self.age = str(years_age)


