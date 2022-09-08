from inspect import _void
import mysql.connector



def create_server_connection(host_name, user_name, user_password, db_name): #Cria uma conexão com o banco
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful") #Retorna que a conexão foi bem sucedida
    except Error as err:
        print(f"Error: '{err}'")

    return connection



def execute_query(connection, query): #cria consultas ao DB
    cursor = connection.cursor()
    
    cursor.execute(query)
    connection.commit()
    print("Query successful")
    print(query)
    print("/n/n/n")


    """
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
    """


connection = create_server_connection("localhost", "python", "*aztx23*", "pinglog")


def data_log(index_data_fim): #Retorna a data
    
    index_data_fim

    return (line[:index_data_fim])



def endereco_log(index_end_inicio, index_end_fim): #Retorna o endereço
    
    end_inicio = index_end_inicio + 4 #Corrige o index para o começo do endereço
    end_fim = index_end_fim - 2 #Corrige o index para o fim do endereço

    if inicio_endereco > 0:
             return (line[end_inicio:end_fim])



def latencia_log(index_lat_inicio, index_lat_fim): #Retorna a latencia
    
    latencia_inicio = index_lat_inicio + 5 #Corrige o index para o começo da latencia
    latencia_fim = index_lat_fim - 1  #Corrige o index para o fim da latencia

    if inicio_latencia > 0:
             return (line[latencia_inicio:latencia_fim])





with open("ping.log") as file: #Abre o arquivo
    
    for line in file: #Lê arquivo linha a linha

        ping_sucedido = True

        fim_data = line.find(":") + 6 #Pega o index do fim da data

        inicio_endereco = line.find('rom') #Pega o index do começo do enedreço pingado
        fim_endenreco = line.find("icmp") #Pega o index do fim do endereço pingado

        
        
        if ((line.find('rom') > 0) and (line.find('Unreachable') < 0)):

            ping_sucedido = 1

            inicio_latencia = line.find('time=') #Pega o index do começo da latencia
            fim_latencia = line.find("ms") #Pega o index do fim da latencia           
            
            data_log_text = str(data_log(fim_data))

            endereco_log_text = str(endereco_log(inicio_endereco, fim_endenreco))

            latencia_log_text = str(latencia_log(inicio_latencia, fim_latencia))

            ping_sucedido_text = str(ping_sucedido)

            salvar_ping = "INSERT INTO log (log_data,endereco,pingvalue,pingsucedido) VALUES ('" + data_log_text + "','" + endereco_log_text + "'," + latencia_log_text + ",'" + ping_sucedido_text + "');"

            execute_query(connection, salvar_ping)



        if ((line.find('Unreachable') > 0)):

            ping_sucedido = 0


            data_log_text = str(data_log(fim_data))

            endereco_log_text = str(endereco_log(inicio_endereco, fim_endenreco))

            latencia_log_text = str(999999)

            ping_sucedido_text = str(ping_sucedido)

            salvar_ping = "INSERT INTO log (log_data,endereco,pingvalue,pingsucedido) VALUES ('" + data_log_text + "','" + endereco_log_text + "'," + latencia_log_text + ",'" + ping_sucedido_text + "');"

            execute_query(connection, salvar_ping)





