# -*- coding: utf-8 -*-
# from odoo import http


# class TokoKue(http.Controller):
#     @http.route('/toko_kue/toko_kue/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/toko_kue/toko_kue/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('toko_kue.listing', {
#             'root': '/toko_kue/toko_kue',
#             'objects': http.request.env['toko_kue.toko_kue'].search([]),
#         })

#     @http.route('/toko_kue/toko_kue/objects/<model("toko_kue.toko_kue"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('toko_kue.object', {
#             'object': obj
#         })
