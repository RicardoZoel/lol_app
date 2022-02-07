# -*- coding: utf-8 -*-
# from odoo import http


# class TaskApp(http.Controller):
#     @http.route('/task_app/task_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_app/task_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_app.listing', {
#             'root': '/task_app/task_app',
#             'objects': http.request.env['task_app.task_app'].search([]),
#         })

#     @http.route('/task_app/task_app/objects/<model("task_app.task_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_app.object', {
#             'object': obj
#         })
