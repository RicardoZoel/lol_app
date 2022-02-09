# -*- coding: utf-8 -*-
from odoo import models, fields, api


class teamModel(models.Model): 
    _name = 'lol_app.team_model'
    _description = 'Team Category'
    _sql_constraints = [ ('team_unique_name','UNIQUE (name)','name must be unique!!'),('team_unique_ceo','UNIQUE (ceo)','ceo must be unique!!'), ]

    name = fields.Char("Team name", required=True,index=True)
    ceo=fields.Char("CEO name", required=True,index=True)
    player=fields.One2many("lol_app.player_model","team", string="Players",Required = True)
    #mediaElo=fields.
