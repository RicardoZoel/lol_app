# -*- coding: utf-8 -*-
from odoo import models, fields, api


class eloModel(models.Model): 
    _name = 'lol_app.elo_model'
    _description = 'Elo Category'

    name = fields.Char(index=True)
    value=fields.Integer()
    eloS=fields.Many2many("lol_app.elos_model", relation="lol_app_elo_model2elos_model")
