from odoo import models, fields


class SessionWizard(models.TransientModel):
    _name = 'openacademy.session.wizard'
    _description = "Open Academy session wizard"

    name = fields.Char(string="Nombre sesión")
    instructor = fields.Char(string="Nombre instructor")
    start_date = fields.Date(string="Fecha inicio")
    course_id = fields.Many2one(string="Curso", comodel_name='openacademy.course')
    available_places = fields.Integer(string="Sitios disponibles")
    attendees_number = fields.Integer(string="Número asistentes")
    duration = fields.Integer(string="Duración sesiones")

    def save_session(self):
        res = self.env['openacademy.session'].create(
            {
                'name': self.name,
                'instructor': self.instructor,
                'start_date': self.start_date,
                'course_id': self.course_id.id,
                'available_places': self.available_places,
                'attendees_number': self.attendees_number,
                'duration': self.attendees_number,
            }
        )

        return res
