#-----------------------------------------------------------------------------
#Essa classe possui métodos CRUD >> Create, Read, Update, Delete
#-----------------------------------------------------------------------------                 
import psycopg2

#-----------------------------------------------------------------------------
# Criação da classe e função '__init__'
#-----------------------------------------------------------------------------  
class AppBD:
    def __init__(self):
        print('Integração GUI-Database Python')

#-----------------------------------------------------------------------------
# Função para conexão com o banco de dados
#-----------------------------------------------------------------------------        
    def abrirConexao(self):
        try: # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
          self.connection = psycopg2.connect(user="seu_usuario_aqui",
                                  password="sua_senha_de_usuario_aqui",
                                  host="seu_host_aqui",
                                  port="porta_do_bando_de_dados_aqui",
                                  database="base_de_dados_aqui")
        
        except (Exception, psycopg2.Error) as error : # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
            if(self.connection):
                print("Falha ao se conectar ao Banco de Dados", error)

#-----------------------------------------------------------------------------
# Função para seleção de todos os produtos
#-----------------------------------------------------------------------------                 
    def selecionarDados(self):
        try: # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
            self.abrirConexao() # chamar a função de conexão ao banco de dados (sempre deve ser executada antes de um comando SQL)
            cursor = self.connection.cursor() # determinar um cursor para o comando SQL (também é obrigatório para execução de comandos SQL)
    
            print("Selecionando todos os produtos")
            sql_select_query = """select * from public."PRODUTO"
                                    ORDER BY "CODIGO" ASC """ # Comando SQL que será executado por essa função  
                    
            
            cursor.execute(sql_select_query) # execução do comando SQL pelo cursor
            registros = cursor.fetchall() # armazenar todos os resultados do comando SQL
            print(registros) # Exibir os resultados do comando SQL no terminal
                
    
        except (Exception, psycopg2.Error) as error: # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
            print("Error in select operation", error) # imprimir no terminal o erro encontrado durante o 'try' da função
    
        finally:
            # Fechar conexão com o banco de dados (sempre deve ser implementado após os comandos SQL para liberar o banco de dados)
            # Como essa função é apenas de seleção de dados, não é necessário realizar 'commit' pois não houve alteração no banco de dados
            if (self.connection): # teste de condição - caso a função não tenha feito uma conexão, não será necessário fechar essa conexão
                cursor.close() # liberar cursor
                self.connection.close() # liberar conexão
                print("A conexão com o PostgreSQL foi fechada.")
        
        return registros # retorna os resultados do comando SSQL quando a função 'selecionarDados' for chamada

#-----------------------------------------------------------------------------
# Função para adição de produtos
#-----------------------------------------------------------------------------                 
    def inserirDados(self, codigo, nome, preco):
        try: # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
          self.abrirConexao() # chamar a função de conexão ao banco de dados (sempre deve ser executada antes de um comando SQL)
          cursor = self.connection.cursor() # determinar um cursor para o comando SQL (também é obrigatório para execução de comandos SQL)
          postgres_insert_query = """ INSERT INTO public."PRODUTO" 
          ("CODIGO", "NOME", "PRECO") VALUES (%s,%s,%s)""" # Comando SQL que será executado por essa função
          record_to_insert = (codigo, nome, preco) # lista das variáveis com os valores que serão inseridos (valores serão atribuidos na criação da GUI)
          cursor.execute(postgres_insert_query, record_to_insert) # execução do comando SQL pelo cursor com os valores das variáveis
          self.connection.commit() # executar 'commit' do comando para efetuar a respectiva alteração no banco de dados
          count = cursor.rowcount # contar a quantidade de linhas o comando 'execute' do cursor criou
          print (count, "Registro inserido com successo na tabela PRODUTO") # imprimir no terminal o retorno dos registros alterados
        
        except (Exception, psycopg2.Error) as error : # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
          if(self.connection):
              print("Falha ao inserir registro na tabela PRODUTO", error) # imprimir no terminal o erro encontrado durante o 'try' da função
        
        finally:
            # Fechar conexão com o banco de dados (sempre deve ser implementado após os comandos SQL para liberar o banco de dados)
            if(self.connection): # teste de condição - caso a função não tenha feito uma conexão, não será necessário fechar essa conexão
                cursor.close() # liberar cursor
                self.connection.close() # liberar conexão
                print("A conexão com o PostgreSQL foi fechada.")
                
#-----------------------------------------------------------------------------
# Função para atualização de um produto
#-----------------------------------------------------------------------------                 
    def atualizarDados(self, codigo, nome, preco):
        try: # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
            self.abrirConexao() # chamar a função de conexão ao banco de dados (sempre deve ser executada antes de um comando SQL)    
            cursor = self.connection.cursor() # determinar um cursor para o comando SQL (também é obrigatório para execução de comandos SQL)

            # serão impressos no terminal os registros ANTES e DEPOIS para possibilitar a visualização da execução da função
            print("Registro Antes da Atualização ")
            sql_select_query = """select * from public."PRODUTO" 
            where "CODIGO" = %s""" # Comando SQL que será executado por essa função
            cursor.execute(sql_select_query, (codigo,)) # execução do comando SQL pelo cursor
            record = cursor.fetchone() # armazenar o resultado do comando SQL
            print(record) # Exibir o resultado do comando SQL no terminal    
            
            # Atualizar registro
            sql_update_query = """Update public."PRODUTO" set "NOME" = %s, 
            "PRECO" = %s where "CODIGO" = %s""" # Comando SQL que será executado por essa função
            cursor.execute(sql_update_query, (nome, preco, codigo)) # execução do comando SQL pelo cursor
            self.connection.commit() # executar 'commit' do comando para efetuar a respectiva alteração no banco de dados
            count = cursor.rowcount # contar a quantidade de linhas o comando 'execute' do cursor alterou
            print(count, "Registro atualizado com sucesso! ") # imprimir no terminal o retorno dos registros alterados
           
            print("Registro Depois da Atualização ")
            sql_select_query = """select * from public."PRODUTO" 
            where "CODIGO" = %s""" # Comando SQL que será executado por essa função
            cursor.execute(sql_select_query, (codigo,)) # execução do comando SQL pelo cursor
            record = cursor.fetchone() # armazenar o resultado do comando SQL
            print(record) # Exibir o resultado do comando SQL no terminal   
        
        except (Exception, psycopg2.Error) as error: # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
            print("Erro na Atualização", error) # imprimir no terminal o erro encontrado durante o 'try' da função    
        
        finally:
            # Fechar conexão com o banco de dados (sempre deve ser implementado após os comandos SQL para liberar o banco de dados)
            if (self.connection): # teste de condição - caso a função não tenha feito uma conexão, não será necessário fechar essa conexão
                cursor.close() # liberar cursor
                self.connection.close() # liberar conexão
                print("A conexão com o PostgreSQL foi fechada.")

#-----------------------------------------------------------------------------
# Função para a exclusão de um produto
#-----------------------------------------------------------------------------                 
    def excluirDados(self, codigo):
        try: # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
            self.abrirConexao() # chamar a função de conexão ao banco de dados (sempre deve ser executada antes de um comando SQL)    
            cursor = self.connection.cursor() # determinar um cursor para o comando SQL (também é obrigatório para execução de comandos SQL)    
            
            # Atualizar registro
            sql_delete_query = """Delete from public."PRODUTO" 
            where "CODIGO" = %s""" # Comando SQL que será executado por essa função
            cursor.execute(sql_delete_query, (codigo, )) # execução do comando SQL pelo cursor

            self.connection.commit() # executar 'commit' do comando para efetuar a respectiva alteração no banco de dados
            count = cursor.rowcount # contar a quantidade de linhas o comando 'execute' do cursor excluiu
            print(count, "Registro excluído com sucesso! ") # imprimir no terminal o retorno dos registros alterados        
        
        except (Exception, psycopg2.Error) as error: # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
            print("Erro na Exclusão", error) # imprimir no terminal o erro encontrado durante o 'try' da função    
        
        finally:
            # Fechar conexão com o banco de dados (sempre deve ser implementado após os comandos SQL para liberar o banco de dados)
            if (self.connection): # teste de condição - caso a função não tenha feito uma conexão, não será necessário fechar essa conexão
                cursor.close() # liberar cursor
                self.connection.close() # liberar conexão
                print("A conexão com o PostgreSQL foi fechada.")
                
#-----------------------------------------------------------------------------
