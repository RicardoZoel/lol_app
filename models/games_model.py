# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import models, fields, api


class playerModel(models.Model): 
    _name = 'lol_app.player_model'
    _description = 'Task Category'

    data = fields.Date("Date", default=datetime.now(),required=True)
    team1=fields.Many2one("lol_app.team_model",string="Team 1",Required = True)
    team2=fields.Many2one("lol_app.team_model",string="Team 2",Required = True)
