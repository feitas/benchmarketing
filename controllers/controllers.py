# -*- coding: utf-8 -*-
from odoo import http

# class Benchmarketing(http.Controller):
#     @http.route('/benchmarketing/benchmarketing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/benchmarketing/benchmarketing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('benchmarketing.listing', {
#             'root': '/benchmarketing/benchmarketing',
#             'objects': http.request.env['benchmarketing.benchmarketing'].search([]),
#         })

#     @http.route('/benchmarketing/benchmarketing/objects/<model("benchmarketing.benchmarketing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('benchmarketing.object', {
#             'object': obj
#         })