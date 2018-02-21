# -*- coding: utf-8 -*-

# Parser do Cnab 440

class CNAB440():

    def __init__(self, cnab_file):
        self.file = cnab_file
        self.cnabs = []
        counter = 1
        self.cnab = []

        for line in cnab_file:

            if line[0] == '0':
                header = CNAB440_Header(line)
                self.cnab.append(header)

            if line[0] == '1':
                registro = CNAB440_Registro(line)
                self.cnab.append(registro)

            if line[0] == '9':
                trailler = CNAB440_Trailler(line)
                self.cnab.append(trailler)

                self.cnabs.append(self.cnab)
                self.cnab = []
                counter += 1

    def print_cnabs(self):
        for item in self.cnabs:
            for i in item:
                print(i.__dict__)



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
        # Parei em Valor do Titulo


        # Printa todos os campos da classe..
        # print(self.__dict__)

class CNAB440_Trailler():

    def __init__(self, line):

        # Definições de posição
        trailer_id_registro = [0, 1]

        # Definição de estrutura
        self.trailer_id_registro = line[trailer_id_registro[0]:trailer_id_registro[1]]


if __name__ == '__main__':
    print('Hello Gays')

    file_cnab = open('CNAB440.txt', 'r')
    new_cnab = CNAB440(file_cnab)
    new_cnab.print_cnabs()