# -*- coding: utf-8 -*-
from odoo import models, fields, api


class elosModel(models.Model): 
    _name = 'lol_app.elos_model'
    _description = 'Elo Subcategory'

    name = fields.Char()
    elo=fields.Many2one("lol_app.elo_model")
    eloP=fields.Integer()