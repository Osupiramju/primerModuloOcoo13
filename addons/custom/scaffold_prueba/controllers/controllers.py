# -*- coding: utf-8 -*-
# from odoo import http


# class ScaffoldPrueba(http.Controller):
#     @http.route('/scaffold_prueba/scaffold_prueba/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/scaffold_prueba/scaffold_prueba/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('scaffold_prueba.listing', {
#             'root': '/scaffold_prueba/scaffold_prueba',
#             'objects': http.request.env['scaffold_prueba.scaffold_prueba'].search([]),
#         })

#     @http.route('/scaffold_prueba/scaffold_prueba/objects/<model("scaffold_prueba.scaffold_prueba"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('scaffold_prueba.object', {
#             'object': obj
#         })
