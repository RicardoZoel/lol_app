# -*- coding: utf-8 -*-
from datetime import datetime
import this
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class gamesModel(models.Model): 
    _name = 'lol_app.games_model'
    _description = 'Game model'

    data = fields.Date("Date", default=datetime.now(),required=True)
    team1=fields.Many2one("lol_app.team_model",string="Team 1",required = True)
    team2=fields.Many2one("lol_app.team_model",string="Team 2",required = True)
    state = fields.Selection(string="Status",selection=[('P','Played'),('NP','NoPlayed'),('C','Canceled')], default="NP")
    # true=team1 / false team2
    selecwinner = fields.Selection(string="Winner",selection=[('T1','tema1'),('NP','NoPlayed'),('T2','tema2'),('C','Canceled')], default="NP")
    winner=fields.Char(readonly=True, compute="_check")

    
    def cancelGame(self):
          self.search([('data', '<', datetime.now() )])
          self._cr.autocommit(False)
          if self.state == "NP" and self.data<datetime.now():
               self.state = "C"
          self._cr.commit()
          self._cr.autocommit(True)
          return True

    def confirmGame(self):
          self.ensure_one()
          self._cr.autocommit(False)
          if self.state == "NP" or self.state=="C":
               self.state = "P"
          else:
            self._cr.rollback()
            self._cr.autocommit(True)
            raise ValidationError("This Game is alredy played!")          
          self._cr.commit()
          self._cr.autocommit(True)
          return True

    @api.depends("selecwinner")
    def _check(self):
        if self.selecwinner=="T1":
            self.winner=self.team1.name
        elif self.selecwinner=="T2":
            self.winner=self.team2.name
        else:
            self.winner=self.selecwinner
