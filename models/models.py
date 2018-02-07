# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

   
class Activity(models.Model):
    _name = "proyectosge.activity"
    
    date = fields.Date(default=fields.Date.today)
    description = fields.Char(required=True)
    duration = fields.Float(digits=(2,1), help="Duration in hours")
    remarks = fields.Text(required=True)
    
    owner = fields.Many2one('res.users', string="Pupil",default=lambda self: self.env.user,readonly=True)
   

    @api.constrains('duration')
    def _check_duration_not_too_long(self):
        for r in self:
            if r.duration > 8:
                raise exceptions.ValidationError("A activity can´t be more than 8 hours")
            
    @api.constrains('duration')
    def _check_duration_not_too_short(self):
        for r in self:
            if r.duration < 0:
                raise exceptions.ValidationError("A activity can´t be less than 0 hours ")
            
    
            


