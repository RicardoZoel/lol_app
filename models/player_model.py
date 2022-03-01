# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class playerModel(models.Model): 
    _name = 'lol_app.player_model'
    _description = 'Player Category'
    _sql_constraints = [ ('Player_unique_name','UNIQUE (name)','name must be unique!!'), ]

    name = fields.Char("Player name", required=True,index=True)
    elo=fields.Many2one("lol_app.elo_model",string="Elo",Required = True)
    eloS=fields.Many2one("lol_app.eloS_model",Required = True)
    rol=fields.Many2many("lol_app.rol_model", string="Rol",Required = True)
    team=fields.Many2one("lol_app.team_model",string="Team")

    @api.onchange('elo')
    def onchange_elo(self):
            self.eloS = ""
            elos_ids = self.env['lol_app.elos_model'].search([('elo','=',self.elo.id)])
            _logger.debug("----------------------->" + str(elos_ids))
            domain = {'eloS': [('eloS', '=', elos_ids)]}
            return {'domain': domain}