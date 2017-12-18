# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Tasca(models.Model):
    _name = 'todo.task' #nom de referència de la classe
    name = fields.Char('Descripció', required = True)
    isDone = fields.Boolean('Feta?')
    isActive = fields.Boolean('Activa?', default = True)

    @api.one
    def do_toggle_done(self):
        self.isDone = not self.isDone
        return True

    @api.multi
    def do_clear_done(self):
        done_recs = self.search([('isDone', '=', True)])
        done_recs.write({'isActive': False})
        return True