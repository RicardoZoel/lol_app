# -*- coding: utf-8 -*-
from odoo import models, fields, api


class playerModel(models.Model): 
    _name = 'lol_app.player_model'
    _description = 'Player Category'

    name = fields.Char("Player name", required=True)
    elo=fields.Many2one("lol_app.elo_model",string="Elo",Required = True)
    eloS=fields.Many2one("lol_app.eloS_model",Required = True)
    rol=fields.Many2many("lol_app.rol_model", string="Rol",Required = True)
    team=fields.Many2one("lol_app.team_model",string="Team")

    @api.onchange('elo')
    def onchange_category(self):
            self.eloS = ""
            domain = {'eloS': [('elo', '=', self.elo.name)]}
            return {'domain': domain}