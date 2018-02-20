# -*- coding: utf-8 -*-

from odoo import models, fields, api,exceptions

     
class Usuario(models.Model):
    _inherit = 'res.users'

    isPupil = fields.Boolean("isPupil",default=False)
    isTutor = fields.Boolean("isTutor",default=False)

    activities = fields.One2many('proyectosge.activity','owner', string="Activities")
    
    tutor = fields.Many2one('res.users',string="Tutor")
    pupils = fields.One2many('res.users','tutor',string = "Pupils")
 
    company = fields.Many2one('res.partner' , string="Compañy")

    @api.constrains('isPupil','isTutor')
    def _check_pupil_not_tutor(self):
        for r in self:
            if r.isPupil == True & r.isTutor == True:
                raise exceptions.ValidationError("A user can't be alumn and pupil")