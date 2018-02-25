# -*- coding: utf-8 -*-

# Parser do Cnab 440

class CNAB440():

    def __init__(self):
        self.cnabs = []

    def print_cnabs(self):
        for item in self.cnabs:
            for k,v in item.items():
                if k == 'header' or k == 'trailler':
                    print(v.__dict__)
                else:
                    for val in v:
                        print(val.__dict__)


    def receive_cnab_from_string(self, cnab_string):
        cnab_file = cnab_string.split('\\n')
        counter = 1
        self.cnab = {'header':'',
                     'registro':[],
                     'trailler':''}

        for line in cnab_file:
            if line[0] == '0' or line[0] == 'b':
                header = CNAB440_Header(line)
                self.cnab.update({'header':header})

            if line[0] == '1':
                registro = CNAB440_Registro(line)
                self.cnab['registro'].append(registro)

            if line[0] == '9':
                trailler = CNAB440_Trailler(line)
                self.cnab.update({'trailler':trailler})
                self.cnabs.append(self.cnab)
                self.cnab = {'header':'',
                     'registro':[],
                     'trailler':''}
                counter += 1

    def receive_cnab(self, cnab_file):
        self.file = cnab_file
        counter = 1
        self.cnab = {'header': '',
                     'registro': [],
                     'trailler': ''}

        for line in cnab_file:
            if line[0] == '0':
                header = CNAB440_Header(line)
                self.cnab.update({'header': header})

            if line[0] == '1':
                registro = CNAB440_Registro(line)
                self.cnab['registro'].append(registro)

            if line[0] == '9':
                trailler = CNAB440_Trailler(line)
                self.cnab.update({'trailler': trailler})
                self.cnabs.append(self.cnab)
                self.cnab = {'header': '',
                             'registro': [],
                             'trailler': ''}
                counter += 1


class CNAB440_Header():

    def __init__(self, line):
        id_registro = [0, 1]
        id_arquivo_remessa = [1, 2]
        literal_remessa = [2, 9]
        cod_servico = [9, 11]
        literal_servico = [11,26]
        codigo_originador = [26,46]
        nome_originador = [46,76]
        nro_banco = [76,79]
        nome_banco = [79,94]
        data_grav_arquivo = [94,100]
        id_sistema = [108,110]
        nro_sequencial_arquivo = [110,117]
        nro_sequencial_registro = [394,400]

        self.id_registro = line[id_registro[0]:id_registro[1]]
        self.id_arquivo_remessa = line[id_arquivo_remessa[0]:id_arquivo_remessa[1]]
        self.literal_remessa = line[literal_remessa[0]:literal_remessa[1]]
        self.cod_servico = line[cod_servico[0]:cod_servico[1]]
        self.literal_servico = line[literal_servico[0]:literal_servico[1]]
        self.codigo_originador = line[codigo_originador[0]:codigo_originador[1]]
        self.nome_originador = line[nome_originador[0]:nome_originador[1]]
        self.nro_banco = line[nro_banco[0]:nro_banco[1]]
        self.nome_banco = line[nome_banco[0]:nome_banco[1]]
        self.data_grav_arquivo = line[data_grav_arquivo[0]:data_grav_arquivo[1]]
        self.id_sistema = line[id_sistema[0]:id_sistema[1]]
        self.nro_sequencial_arquivo = line[nro_sequencial_arquivo[0]:nro_sequencial_arquivo[1]]
        self.nro_sequencial_registro = line[nro_sequencial_registro[0]:nro_sequencial_registro[1]]

class CNAB440_Registro():

    def __init__(self, line):
        cnab_id_registro = [0, 1]
        cnab_coobrigacao = [20, 22]
        cnab_caract_especial = [22, 24]
        cnab_modalidade_operacao = [24,28]
        cnab_natureza_operacao = [28,30]
        cnab_origem_recurso = [30,34]
        cnab_classe_risco_operacao =[34,36]
        cnab_nro_controle_participante = [37,62]
        cnab_nro_banco = [62,65]
        cnab_valor_pago = [82,92]
        cnab_data_liquidacao = [94,100]
        cnab_id_ocorrencia = [108,110]
        cnab_nro_documento = [110,120]
        cnab_data_vencimento = [120,126]
        cnab_valor_titulo = [126,139]
        cnab_banco_encarregado_cobranca = [139,142]
        cnab_agencia_depositaria = [142,147]
        cnab_especie_titulo = [147,149]
        cnab_data_emissao_titulo = [150,156]
        cnab_tipo_pessoa_cedente = [159,161]
        cnab_nro_termo_de_cessao = [173,192]
        cnab_valor_presente_parcela = [192,205]
        cnab_valor_abatimento = [205,218]
        cnab_id_tipo_inscr_sacado = [218,220]
        cnab_cnpj_cpf = [220,234]
        cnab_nome_sacado = [234,274]
        cnab_end_sacado = [274,314]
        cnab_nro_nf_duplicata = [314,323]
        cnab_nro_serie_nf_duplicata = [323,326]
        cnab_cep_sacado = [326,334]
        cnab_cedente = [334,394]
        cnab_chave_nota = [394,438]
        cnab_nro_sequencial_registro = [438,444]

        self.cnab_id_registro = line[cnab_id_registro[0]:cnab_id_registro[1]]
        self.cnab_coobrigacao = line[cnab_coobrigacao[0]:cnab_coobrigacao[1]]
        self.cnab_caract_especial = line[cnab_caract_especial[0]:cnab_caract_especial[1]]
        self.cnab_modalidade_operacao = line[cnab_modalidade_operacao[0]:cnab_modalidade_operacao[1]]
        self.cnab_natureza_operacao = line[cnab_natureza_operacao[0]:cnab_natureza_operacao[1]]
        self.cnab_origem_recurso = line[cnab_origem_recurso[0]:cnab_origem_recurso[1]]
        self.cnab_classe_risco_operacao = line[cnab_classe_risco_operacao[0]:cnab_classe_risco_operacao[1]]
        self.cnab_nro_controle_participante = line[cnab_nro_controle_participante[0]:cnab_nro_controle_participante[1]]
        self.cnab_nro_banco = line[cnab_nro_banco[0]:cnab_nro_banco[1]]
        self.cnab_valor_pago = line[cnab_valor_pago[0]:cnab_valor_pago[1]]
        self.cnab_data_liquidacao = line[cnab_data_liquidacao[0]:cnab_data_liquidacao[1]]
        self.cnab_id_ocorrencia = line[cnab_id_ocorrencia[0]:cnab_id_ocorrencia[1]]
        self.cnab_nro_documento = line[cnab_nro_documento[0]:cnab_nro_documento[1]]
        self.cnab_data_vencimento = line[cnab_data_vencimento[0]:cnab_data_vencimento[1]]
        self.cnab_valor_titulo = line[cnab_valor_titulo[0]:cnab_valor_titulo[1]]
        self.cnab_banco_encarregado_cobranca = line[cnab_banco_encarregado_cobranca[0]:cnab_banco_encarregado_cobranca[1]]
        self.cnab_agencia_depositaria = line[cnab_agencia_depositaria[0]:cnab_agencia_depositaria[1]]
        self.cnab_especie_titulo = line[cnab_especie_titulo[0]:cnab_especie_titulo[1]]
        self.cnab_data_emissao_titulo = line[cnab_data_emissao_titulo[0]:cnab_data_emissao_titulo[1]]
        self.cnab_tipo_pessoa_cedente = line[cnab_tipo_pessoa_cedente[0]:cnab_tipo_pessoa_cedente[1]]
        self.cnab_nro_termo_de_cessao = line[cnab_nro_termo_de_cessao[0]:cnab_nro_termo_de_cessao[1]]
        self.cnab_valor_presente_parcela = line[cnab_valor_presente_parcela[0]:cnab_valor_presente_parcela[1]]
        self.cnab_valor_abatimento = line[cnab_valor_abatimento[0]:cnab_valor_abatimento[1]]
        self.cnab_id_tipo_inscr_sacado = line[cnab_id_tipo_inscr_sacado[0]:cnab_id_tipo_inscr_sacado[1]]
        self.cnab_cnpj_cpf = line[cnab_cnpj_cpf[0]:cnab_cnpj_cpf[1]]
        self.cnab_nome_sacado = line[cnab_nome_sacado[0]:cnab_nome_sacado[1]]
        self.cnab_end_sacado = line[cnab_end_sacado[0]:cnab_end_sacado[1]]
        self.cnab_nro_nf_duplicata = line[cnab_nro_nf_duplicata[0]:cnab_nro_nf_duplicata[1]]
        self.cnab_nro_serie_nf_duplicata = line[cnab_nro_serie_nf_duplicata[0]:cnab_nro_serie_nf_duplicata[1]]
        self.cnab_cep_sacado = line[cnab_cep_sacado[0]:cnab_cep_sacado[1]]
        self.cnab_cedente = line[cnab_cedente[0]:cnab_cedente[1]]
        self.cnab_chave_nota = line[cnab_chave_nota[0]:cnab_chave_nota[1]]
        self.cnab_nro_sequencial_registro = line[cnab_nro_sequencial_registro[0]:cnab_nro_sequencial_registro[1]]


        # Printa todos os campos da classe..
        # print(self.__dict__)

class CNAB440_Trailler():

    def __init__(self, line):

        # Definições de posição
        trailler_id_registro = [0, 1]
        trailler_nro_seq_reg = [394,400]

        # Definição de estrutura
        self.trailler_id_registro = line[trailler_id_registro[0]:trailler_id_registro[1]]
        self.trailler_nro_seq_reg = line[trailler_nro_seq_reg[0]:trailler_nro_seq_reg[1]]


if __name__ == '__main__':
    print('Hello Gays')

    file_cnab = open('CNAB440.txt', 'r')
    new_cnab = CNAB440()
    new_cnab.receive_cnab(file_cnab)
    new_cnab.print_cnabs()