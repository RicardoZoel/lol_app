# -*- coding: utf-8 -*-
from odoo import models, fields, api


class playerModel(models.Model): 
    _name = 'lol_app.player_model'
    _description = 'Task Category'

    name = fields.Char("Team name", required=True)
    ceo=fields.Char("CEO name", required=True)
    player=fields.One2many("lol_app.player_model","team", string="Players",Required = True)

