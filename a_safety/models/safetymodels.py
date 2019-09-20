# -*- coding: utf-8 -*-
from reportlab.platypus.tableofcontents import delta
from odoo import models, fields, api

class RamakModule(models.Model):
    _name = 'rapor_modul'

    employee_id = fields.Many2one("hr.employee")
    name = fields.Char(related="employee_id.name")
    department_name = fields.Char(related="employee_id.department_id.name")

    work_email = fields.Char(related="employee_id.work_email")
    work_phone = fields.Char(related="employee_id.work_phone")
    birthday = fields.Date(related="employee_id.birthday")
    employee_image= fields.Binary(related="employee_id.image")

    started_job = fields.Date(related="employee_id.started_job")
    age = fields.Char(related="employee_id.age", compute="_compute_state")


    olay_kategorisi = fields.Selection(
        [('rk', 'Ramak Kala'), ('gdu', 'Güvensiz Durum'), ('gda', 'Güvensiz Davranış ')],
        'Olay Bildirim Kategorisi', requried=True)

    bildirim_no = fields.Integer(string='Bildirim No: ')

    rk_binasi = fields.Selection(
        [('10PD', '10 Numaralı Piro Depo'), ('200D', '200 Depo'), ('810US', '810 Uset Binası')],
        'RK. Binası', requried=True)

    rk_tarihi = fields.Datetime(string="RK. Tarihi: ", default=lambda s: fields.Datetime.now(), help="Olay tarihi ve saati")
    rk_yeri = fields.Char(string='RK. Yeri: ')

    olaydaki_kisiler = fields.Char(string='Olayda bulunan kişi(ler): ')
    arac_plakasi = fields.Integer(string='Araç (bisiklet, araba vs.) plakası: ')
    olay_sekli = fields.Text(string='Olayın Oluş Şekli: ')

    kaza_rapor_no = fields.Integer(string='Rapor No: ')
    kaza_tarihi = fields.Datetime(string='Kaza Tarihi: ')
    kaza_durumu = fields.Text(string='Kazanın Tarifi: ')

    @api.onchange('birthday')
    def _compute_state(self):
        time_age = (fields.datetime.now() - self.birthday).day
        self.age = str(time_age.years)

