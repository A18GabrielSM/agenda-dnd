# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _


logger = logging.getLogger(__name__)


class AgendaDND(models.Model):
    _name = 'agenda.campaign'
    _description = 'Campaña DND'

    name = fields.Char('Nombre de campaña', required=True)
    game_date = fields.Date('Fecha de partida', required=True)
    player_count = fields.Integer('Nº de jugadores', default=5)
    dm_ids = fields.Many2many('res.partner', string='Dungeon Master')
    play_mode = fields.Selection([
        ('online', 'Online'),
        ('presential', 'Presencial')],
        'play_mode', default='online')
    state = fields.Selection([
        ('pending', 'Pendiente'),
        ('finished', 'Terminada'),
        ('continued', 'Continuada'),
        ('canceled', 'Cancelada')],
        'State', default='pending')

    @api.model
    def is_allowed_transition(self, old_value, new_value):
        allowed = [('pending', 'finished'),
                   ('pending', 'canceled'),
                   ('canceled', 'pending'),
                   ('finished', 'continued'),
                   ('continued', 'finished')]
        return (old_value, new_value) in allowed

    @api.multi
    def change_state(self, new_state):
        for campaign in self:
            if campaign.is_allowed_transition(campaign.state, new_state):
                campaign.state = new_state
            else:
                message = _('No se puede pasar de %s a %s') % (campaign.state, new_state)
                raise UserError(message)

    def make_pending(self):
        self.change_state('pending')

    def make_finished(self):
        self.change_state('finished')

    def make_canceled(self):
        self.change_state('canceled')

    def make_continued(self):
        self.change_state('continued')

    def make_online(self):
        self.play_mode='online'

    def make_presential(self):
        self.play_mode='presential'

