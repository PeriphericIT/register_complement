# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
import requests
import re

class ResPartner(models.Model):

    _inherit = 'res.partner'

    register_type = fields.Selection([('invest','Investidor'),
                                        ('fundo','Fundo'),
                                        ],string="Tipo de Cadastro")

    structure_id = fields.Many2one('res.structure', string='Estrutura')

    social_capital = fields.Float('Capital Social')

    economic_group = fields.Char('Grupo Econômico')
    social_denomination = fields.Char('Denominação Social')
    comercial_denomination = fields.Char('Denominação Comercial')
    register_company_type = fields.Char('Tipo de Empresa')
    person_type = fields.Char('Tipo de Pessoa')
    registry_date = fields.Date('Data de Registro')
    entry_date = fields.Date('Data de Entrada')
    departure_date = fields.Date('Data de Saída')
    economic_activity = fields.Char('Atividade Econômica')
    legal_nature = fields.Char('Natureza Jurídica')
    industry = fields.Char('Ramo de Atividade')
    patrimony = fields.Char('Patrimônio')
    ranking = fields.Char('Ranking')
    shareholder_type = fields.Char('Tipo de Cotista')
    profession = fields.Char('Profissão')
    rg_number = fields.Char('Número do RG')
    marital_status = fields.Selection([
    ('single','Solteiro(a)'),
    ('married','Casado(a)'),
    ('divorced','Divorciado(a)'),
    ('widower','Viúvo(a)'),
    ('separate','Separado(a)'),
    ], 'Estado Civíl')

    #Booleans para checagem do tipo de Cadastro
    register_client = fields.Boolean("Cliente")
    register_quotaholder = fields.Boolean("Cotista")
    register_market_participant = fields.Boolean("Participante do Mercado")


    @api.multi
    def review_structure(self):
        tree_id = self.env.ref('register_complement.register_complement_res_structure_lines_tree').id
        form_id = self.env.ref('register_complement.register_complement_res_structure_lines_form').id

        domain = [('parent_partner_id','=', self.id)]
        return {'type': 'ir.actions.act_window',
                    'res_model': 'res.structure.line',
                    'view_mode': 'form',
                    'domain': domain,
                    'views': [(tree_id, 'tree'),(form_id,'form')],
                    'context':{'group_by':['structure_type_id','position']},
                    'target': 'current',
                    }


    @api.multi
    def check_cnpj(self):
        '''
        Checa no serviço receitaws pelo cnpj e, caso possua os dados, retorna a requisição e preenche alguns
        dos camos solicitados
        :return:
        '''
        if self.company_type == 'company':
            if self.cnpj_cpf:
                new_cnpj = re.sub(r'\D', "", self.cnpj_cpf)
                req = requests.get('https://www.receitaws.com.br/v1/cnpj/%s' % new_cnpj)
                # FIXME: Incluir novas checagens e criar retorno para cnpjs inexistentes....
                print(req.json())
                for k,v in req.json().items():
                    print(k)
                    print(v)
                self.name = req.json()['nome']
                self.street2 = "%s %s" % (req.json()['numero'], req.json()['complemento'])
                self.legal_name = req.json()['fantasia']
                self.zip = req.json()['cep']
                self.social_capital = req.json()['capital_social']
            else:
                print('Não há cnpj...')
