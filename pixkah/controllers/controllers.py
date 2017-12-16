# -*- coding: utf-8 -*-
from odoo import http

# class Pixkah(http.Controller):
#     @http.route('/pixkah/pixkah/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pixkah/pixkah/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pixkah.listing', {
#             'root': '/pixkah/pixkah',
#             'objects': http.request.env['pixkah.pixkah'].search([]),
#         })

#     @http.route('/pixkah/pixkah/objects/<model("pixkah.pixkah"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pixkah.object', {
#             'object': obj
#         })