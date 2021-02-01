from odoo import models, fields, api, exceptions


class Course(models.Model):
    _name = "openacademy.course"
    _description = "Open Academy Course Model"

    name = fields.Char(string="Nombre curso")
    description = fields.Char(string="Descripción curso")
    course_state = fields.Selection(string="Estado curso", selection=([
        ('toStart', 'Por empezar'),
        ('active', 'Activo'),
        ('finished', 'Finalizado'),
    ]), default='toStart')
    minimum_participants = fields.Integer(string="Cantidad mínima participantes")
    session_ids = fields.One2many(string="Sesiones", comodel_name='openacademy.session', inverse_name='course_id',
                                  readonly="true")

    # attendees_number = fields.Integer(related="session_ids.attendees_number")

    @api.depends("session_ids", "minimum_participants")
    def active_button(self):

        for obj in self:
            if not obj.session_ids:
                raise exceptions.Warning('No hay ninguna sesión creada.')
                # elif not obj.session_ids:
                # raise exceptions.Warning('Hay que crear al menos una sesión para que un curso se active.')
                # elif not self.env['openacademy.session'].search([]):
                # raise exceptions.Warning('Hay que crear al menos una sesión para que un curso se active.')
                # if not len(obj.session_ids):
                # raise exceptions.Warning('Hay que crear al menos una sesión para que un curso se active.')
            for session in obj.session_ids:
                if obj.minimum_participants >= session.attendees_number:
                    raise exceptions.Warning("No hay el número suficiente de asistentes")
                else:
                    obj.course_state = 'active'

    def finished_button(self):
        for obj in self:
            obj.course_state = 'finished'
