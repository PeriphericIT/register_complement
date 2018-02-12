
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):

    _inherit = 'res.partner'

    register_type = fields.Selection([('invest','Investidor'),
                                        ('fundo','Fundo'),
                                        ('gest','Gestor'),
                                        ('clear','Clearing'),
                                        ],string="Tipo de Cadastro")
