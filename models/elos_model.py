# -*- coding: utf-8 -*-
from odoo import models, fields, api


class elosModel(models.Model): 
    _name = 'lol_app.elos_model'
    _description = 'Elo Subcategory'

    name = fields.Char()
    elo=fields.Many2many("lol_app.elo_model",relation="lol_app_elo_model2elos_model")
    eloP=fields.Integer()
    value=fields.Integer()
