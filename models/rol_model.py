# -*- coding: utf-8 -*-
from odoo import models, fields, api


class rolModel(models.Model): 
    _name = 'lol_app.rol_model'
    _description = 'Rol Model'
    _sql_constraints = [ ('rol_unique_name','UNIQUE (name)','name must be unique!!'), ]

    name = fields.Char("Rol Name", index=True)
    photo = fields.Image()
    description = fields.Html('Description')
    Rol=fields.Many2many("lol_app.player_model",string="Players",readonly=True)
