#with open("arquivo.txt") as file:
#    for line in file:
#        print line
#
#arq = open('ping.log','r')
#content = arq. read()
#print (content)



def data_log(index_data_fim): #Retorna a data
    
    index_data_fim

    return (line[:index_data_fim])



def endereco_log(index_end_inicio, index_end_fim): #Retorna o endereço
    
    end_inicio = index_end_inicio + 4 #Corrige o index para o começo do endereço
    end_fim = index_end_fim - 2 #Corrige o index para o fim do endereço

    if inicio_endereco > 0:
             return (line[end_inicio:end_fim])



def latencia_log(index_lat_inicio, index_lat_fim): #Retorna o endereço pingado em referencia ao arquivo
    
    latencia_inicio = index_lat_inicio + 5 #Corrige o index para o começo do endereço
    latencia_fim = index_lat_fim - 1  #Corrige o index para o fim do endereço

    if inicio_latencia > 0:
             return (line[latencia_inicio:latencia_fim])

def mysql_connection():

    cnxn = pyodbc.connect("DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost;DATABASE=pinglog;UID=dugeon;PASSWORD=Aztx2390;")
    cursor = cnxn.cursor()

with open("ping.log") as file: #Abre o arquivo
    
    for line in file: #Lê arquivo linha a linha

        ping_sucedido = True

        fim_data = line.find(":") + 6 #Pega o index do fim da data

        inicio_endereco = line.find('rom') #Pega o index do começo do enedreço pingado
        fim_endenreco = line.find("icmp") #Pega o index do fim do endereço pingado

        if ((line.find('rom') > 0) and (line.find('Unreachable') < 0)):

            ping_sucedido = True

            inicio_latencia = line.find('time=') #Pega o index do começo da latencia
            fim_latencia = line.find("ms") #Pega o index do fim da latencia           
            
            print(data_log(fim_data))

            print(endereco_log(inicio_endereco, fim_endenreco))

            print(latencia_log(inicio_latencia, fim_latencia))

            print(ping_sucedido)

            print("\n\n\n")            



        if ((line.find('Unreachable') > 0)):

            ping_sucedido = False

            print(data_log(fim_data))

            print(endereco_log(inicio_endereco, fim_endenreco))

            print(ping_sucedido)

            print("\n")