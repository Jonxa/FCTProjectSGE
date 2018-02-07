# -*- coding: utf-8 -*-

from odoo import models, fields

class FCTPartner(models.Model):
    _inherit = 'res.partner'
    
    isFCTPartner = fields.Boolean("FCTPartner",default=False)

    pupils = fields.One2many('res.users','company', string="Pupils")