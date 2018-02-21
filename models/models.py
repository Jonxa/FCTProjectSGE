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
                 
    @api.constrains('duration')
    def _check_total_duration(self):
        total_duration = 0
        for activity in self.search([('owner','=',self.owner.id)]):
            total_duration = total_duration + activity.duration
            if total_duration > 350:
               raise exceptions.ValidationError('Maximum duration of all the activities can´t be more than 350 hours.')
            
    @api.constrains('duration')
    def _check_day_duration(self):
        day_duration = 0
        for activity in self.search([('date','=',self.date)]):
            day_duration = day_duration + activity.duration
            if day_duration > 8:
                raise exceptions.ValidationError('Maximum duration per day can´t be more than 8 hours.')
#            
    
            


