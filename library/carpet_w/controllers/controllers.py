# -*- coding: utf-8 -*-
# from odoo import http


# class LibraryApp(http.Controller):
#     @http.route('/carpet_w/carpet_w', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/carpet_w/carpet_w/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('carpet_w.listing', {
#             'root': '/carpet_w/carpet_w',
#             'objects': http.request.env['carpet_w.carpet_w'].search([]),
#         })

#     @http.route('/carpet_w/carpet_w/objects/<model("carpet_w.carpet_w"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('carpet_w.object', {
#             'object': obj
#         })
