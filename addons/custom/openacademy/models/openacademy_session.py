from dateutil.relativedelta import relativedelta

from odoo import models, fields


class Session(models.Model):
    _name = 'openacademy.session'
    _description = "Open Academy session Model"

    name = fields.Char(string="Nombre sesion")
    instructor = fields.One2many(string="Nombre instructor", comodel_name="res.partner")
    start_date = fields.Date(string="Fecha inicio")
    course_id = fields.Many2one(string="Cursos", comodel_name='openacademy.course',
                                domain=[('course_state', '=', 'toStart')])
    available_places = fields.Integer(string="Sitios disponibles")
    attendees_number = fields.Integer(string="Número asistentes")
    duration = fields.Integer(string="Duración sesiones")
    assists_percent = fields.Float(string="Porcentaje asistentes", compute="compute_assists_percent")
    finish_date = fields.Date(string="Fecha fin", compute="compute_finish_date")

    def compute_finish_date(self):
        for obj in self:
            obj.finish_date = obj.start_date + relativedelta(days=+obj.duration)

    def compute_assists_percent(self):
        for obj in self:
            obj.assists_percent = (obj.attendees_number / obj.available_places) * 100
