# -*- coding: utf-8 -*-
# from odoo import http


# class TexmarCollected(http.Controller):
#     @http.route('/texmar_collected/texmar_collected/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/texmar_collected/texmar_collected/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('texmar_collected.listing', {
#             'root': '/texmar_collected/texmar_collected',
#             'objects': http.request.env['texmar_collected.texmar_collected'].search([]),
#         })

#     @http.route('/texmar_collected/texmar_collected/objects/<model("texmar_collected.texmar_collected"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('texmar_collected.object', {
#             'object': obj
#         })
