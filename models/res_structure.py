
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResStructure(models.Model):
    _name = 'res.structure'

    partner_id = fields.Many2one('res.partner', 'Empresa Referente')
    name = fields.Char('Nome da estrutura')
    structure_line_ids = fields.One2many('res.structure.line', 'structure_id', string="Linhas de estrutura")

class ResStructureLine(models.Model):
    _name = 'res.structure.line'

    name = fields.Char('Nome da estrutura', related='structure_type_id.name', store=True)
    partner_id = fields.Many2one('res.partner', 'Contato relacionado')
    parent_partner_id = fields.Many2one('res.partner', 'Empresa relacionada', related='partner_id.parent_id', store=True)
    position = fields.Char('Posição', related='partner_id.function', store=True)
    structure_id = fields.Many2one('res.structure', 'Estrutura relacionada')
    structure_type_id = fields.Many2one('res.structure.type', 'Tipo de Estrutura')


class ResStructureType(models.Model):
    _name = 'res.structure.type'

    name = fields.Char('Tipo de Estrutura')

