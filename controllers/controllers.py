# -*- coding: utf-8 -*-
from odoo import http

# class Proyectosge(http.Controller):
#     @http.route('/proyectosge/proyectosge/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyectosge/proyectosge/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyectosge.listing', {
#             'root': '/proyectosge/proyectosge',
#             'objects': http.request.env['proyectosge.proyectosge'].search([]),
#         })

#     @http.route('/proyectosge/proyectosge/objects/<model("proyectosge.proyectosge"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyectosge.object', {
#             'object': obj
#         })