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
            final_cnab.print_cnabs()
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
                        'cnab_id_registro': line.cnab_id_registro,
                        'cnab_cnpj_cpf': line.cnab_cnpj_cpf,
                        'cnab_nome_sacado': line.cnab_nome_sacado,
                        'cnab_end_sacado': line.cnab_end_sacado,
                        'cnab_id_tipo_inscr_sacado': line.cnab_id_tipo_inscr_sacado,
                        'cnab_coobrigacao': line.cnab_coobrigacao,
                        'cnab_caract_especial': line.cnab_caract_especial,
                        'cnab_modalidade_operacao': line.cnab_modalidade_operacao,
                        'cnab_natureza_operacao': line.cnab_natureza_operacao,
                        'cnab_origem_recurso': line.cnab_origem_recurso,
                        'cnab_classe_risco_operacao': line.cnab_classe_risco_operacao,
                        'cnab_nro_controle_participante': line.cnab_nro_controle_participante,
                        'cnab_nro_banco': line.cnab_nro_banco,
                        'cnab_valor_pago': line.cnab_valor_pago,
                        'cnab_data_liquidacao': line.cnab_data_liquidacao,
                        'cnab_id_ocorrencia': line.cnab_id_ocorrencia,
                        'cnab_nro_documento': line.cnab_nro_documento,
                        'cnab_data_vencimento':line.cnab_data_vencimento,
                        'cnab_valor_titulo': line.cnab_valor_titulo,
                        'cnab_banco_encarregado_cobranca': line.cnab_banco_encarregado_cobranca,

                    })
            self.state = 'imported'


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

    name = fields.Char('Nome', default='Header')
    cod_servico = fields.Char('Codigo de Serviço')
    codigo_originador = fields.Char('Codigo Originador')
    nome_originador = fields.Char('Nome do Originador')
    nro_banco = fields.Char('Nro do Banco')
    nome_banco = fields.Char('Nome do Banco')
    data_grav_arquivo = fields.Char('Data de Gravação do arquivo')
    block_id = fields.Many2one('res.cnab.block', string='Cnab')


class ResCnabImportLine(models.Model):
    _name = 'res.cnab.import.line'

    name = fields.Char('Nome', default='Registro')
    block_id = fields.Many2one('res.cnab.block', string='Cnab')

    cnab_id_registro = fields.Char('Id Registro')
    cnab_cnpj_cpf = fields.Char('CNPJ/CPF')
    cnab_nome_sacado = fields.Char('Nome do Sacado')
    cnab_end_sacado = fields.Char('Endereço do Sacado')
    cnab_id_tipo_inscr_sacado = fields.Char('Tipo de Inscrição')
    cnab_coobrigacao = fields.Char('Coobrigação')
    cnab_caract_especial = fields.Char('Característica Especial')
    cnab_modalidade_operacao = fields.Char('Modalidade da Operação')
    cnab_natureza_operacao = fields.Char('Natureza da Operação')
    cnab_origem_recurso = fields.Char('Origem do recurso')
    cnab_classe_risco_operacao = fields.Char('Classe Risco da Operação')
    cnab_nro_controle_participante = fields.Char('No de Controle do Participante')
    cnab_nro_banco = fields.Char('Numero do Banco')
    cnab_valor_pago = fields.Char('Valor pago')
    cnab_data_liquidacao = fields.Char('Data da Liquidação')
    cnab_id_ocorrencia = fields.Char('Identificação Ocorrência')
    cnab_nro_documento = fields.Char('No do Documento')
    cnab_data_vencimento = fields.Char('Data do Vencimento do Título')
    cnab_valor_titulo = fields.Char('Valor do Título (Face)')
    cnab_banco_encarregado_cobranca = fields.Char('Banco Encarregado da Cobrança')

    # Falta mapear
    # cnab_agencia_depositaria = fields.Char('Endereço do Sacado')
    # cnab_especie_titulo = fields.Char('Endereço do Sacado')
    # cnab_data_emissao_titulo = fields.Char('Endereço do Sacado')
    # cnab_tipo_pessoa_cedente = fields.Char('Endereço do Sacado')
    # cnab_nro_termo_de_cessao = fields.Char('Endereço do Sacado')
    # cnab_valor_presente_parcela = fields.Char('Endereço do Sacado')
    # cnab_valor_abatimento = fields.Char('Endereço do Sacado')
    # cnab_nro_nf_duplicata = fields.Char('Endereço do Sacado')
    # cnab_nro_serie_nf_duplicata = fields.Char('Endereço do Sacado')
    # cnab_cep_sacado = fields.Char('Endereço do Sacado')
    # cnab_cedente = fields.Char('Endereço do Sacado')
    # cnab_chave_nota = fields.Char('Endereço do Sacado')
    # cnab_nro_sequencial_registro = fields.Char('Endereço do Sacado')


class ResCnabTraillerImport(models.Model):
    _name = 'res.cnab.trailler.import'

    name = fields.Char('Nome', default='Trailler')
    trailler_id_registro = fields.Char('Id Registro')
    trailler_nro_seq_reg = fields.Char('Nro Sequencial do Trailler')
    block_id = fields.Many2one('res.cnab.block', string='Cnab')
