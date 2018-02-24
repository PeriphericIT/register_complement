# -*- coding: utf-8 -*-

from odoo import models, fields, api
from ..lib import cnab_440_parser
import base64


class ResCNAB(models.Model):

    _name = 'res.cnab'

    name = fields.Char('Nome da Importação')

    data_file = fields.Binary(string='Arquivo de Importação CNAB', required=True,
                              help='Import o Cnab por aqui.')
    filename = fields.Char()

    state = fields.Selection([
        ('draft', 'Provisório'),
        ('imported', 'Importado'),
        ('pending', 'Pendente'),
        ('done', 'Confirmado')
    ], default='draft', string='Status')

    cnab_type = fields.Selection([
        ('440', '440'),
        ('400', '400'),
    ], default='440', string='Tipo de Cnab')

    date_import = fields.Date('Data de importação', default=fields.Datetime.now())
    block_ids = fields.One2many('res.cnab.block','cnab_id' ,string='Header')

    @api.multi
    def import_cnab_file(self):

        cnabs = []
        if not self.data_file:
            print('Sem arquivo para importar')
            return

        if self.data_file:
            file_cnab = base64.b64decode(self.data_file)
            final_cnab = cnab_440_parser.CNAB440()
            final_cnab.receive_cnab_from_string(str(file_cnab))
            cnab_block = self.env['res.cnab.block']
            cnab_header = self.env['res.cnab.header.import']
            cnab_line = self.env['res.cnab.import.line']
            cnab_trailler = self.env['res.cnab.trailler.import']
            for item in final_cnab.cnabs:
                block = cnab_block.create({
                    'cnab_id': self.id,
                    'name': 'Cnab importado'
                })

                header = item['header']
                block.header_id = cnab_header.create({
                    'cod_servico':header.cod_servico,
                    'codigo_originador':header.codigo_originador,
                    'nome_originador':header.nome_originador,
                    'nro_banco':header.nro_banco,
                    'nome_banco':header.nome_banco,
                    'data_grav_arquivo':header.data_grav_arquivo,
                    'block_id': block.id
                })

                trailler = item['trailler']
                block.trailler_id = cnab_trailler.create({
                    'trailler_id_registro': trailler.trailler_id_registro,
                    'trailler_nro_seq_reg': trailler.trailler_nro_seq_reg,
                    'block_id':block.id

                })

                lines = item['registro']
                for line in lines:
                    cnab_line.create({
                        'block_id':block.id,
                        'cnab_id_registro':line.cnab_id_registro,
                        'cnab_cnpj_cpf':line.cnab_cnpj_cpf,
                        'cnab_nome_sacado':line.cnab_nome_sacado,
                        'cnab_end_sacado':line.cnab_end_sacado,
                        'cnab_id_tipo_inscr_sacado':line.cnab_id_tipo_inscr_sacado,

                    })

        print('_________FINALIZADO__________')




class ResCnabBlock(models.Model):
    _name = 'res.cnab.block'

    name = fields.Char('Arquivo de Cnab')
    cnab_id = fields.Many2one('res.cnab', string='Cnab')
    header_id = fields.Many2one('res.cnab.header.import', string='Header')
    trailler_id = fields.Many2one('res.cnab.trailler.import', string='Trailer')
    cnab_lines_ids = fields.One2many('res.cnab.import.line','block_id' ,string='Linhas')
    date_import = fields.Date('Data de importação', default=fields.Datetime.now())


class ResCnabHeaderImport(models.Model):
    _name = 'res.cnab.header.import'

    cod_servico = fields.Char('Codigo de Serviço')
    codigo_originador = fields.Char('Codigo Originador')
    nome_originador = fields.Char('Nome do Originador')
    nro_banco = fields.Char('Nro do Banco')
    nome_banco = fields.Char('Nome do Banco')
    data_grav_arquivo = fields.Char('Data de Gravação do arquivo')
    block_id = fields.Many2one('res.cnab.block', string='Cnab')


class ResCnabImportLine(models.Model):
    _name = 'res.cnab.import.line'

    cnab_id_registro = fields.Char('Id Registro')
    cnab_cnpj_cpf = fields.Char('CNPJ/CPF')
    cnab_nome_sacado = fields.Char('Nome do Sacado')
    cnab_end_sacado = fields.Char('Endereço do Sacado')
    cnab_id_tipo_inscr_sacado = fields.Char('Tipo de Inscrição')
    block_id = fields.Many2one('res.cnab.block', string='Cnab')


class ResCnabTraillerImport(models.Model):
    _name = 'res.cnab.trailler.import'

    trailler_id_registro = fields.Char('Id Registro')
    trailler_nro_seq_reg = fields.Char('Nro Sequencial do Trailler')
    block_id = fields.Many2one('res.cnab.block', string='Cnab')
