# -*- coding: utf-8 -*-
from odoo import models, fields, api


class rolModel(models.Model): 
    _name = 'lol_app.rol_model'
    _description = 'Rol Model'

    name = fields.Char("Rol Name")
    photo = fields.Image('IMG')
    description = fields.Html('Description')
    Rol=fields.Many2one("lol_app.player_model",string="Players",readonly=True)
