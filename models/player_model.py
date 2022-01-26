# -*- coding: utf-8 -*-
from odoo import models, fields, api


class playerModel(models.Model): 
    _name = 'lol_app.player_model'
    _description = 'Task Category'

    name = fields.Char("Player name", required=True)
    #elo=fields.Integer("Elo player")
    rol=fields.One2many("lol_app.rol_model","Rol", string="Rol",Required = True)
    team=fields.Many2one("lol_app.team_model",string="Team",readonly=True)
