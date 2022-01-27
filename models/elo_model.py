# -*- coding: utf-8 -*-
from odoo import models, fields, api


class eloModel(models.Model): 
    _name = 'lol_app.elo_model'
    _description = 'Elo Category'

    name = fields.Char()
    eloS=fields.One2many("lol_app.elos_model","elo")
