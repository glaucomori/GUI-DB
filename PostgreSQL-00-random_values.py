#importar biblioteca
import psycopg2
from faker import Faker

# Conectar ao banco de dados
connection = psycopg2.connect(user="seu_usuario_aqui",
                                password="sua_senha_de_usuario_aqui",
                                host="seu_host_aqui",
                                port="porta_do_bando_de_dados_aqui",
                                database="base_de_dados_aqui")
print('Conexão bem sucedida!')

# criar cursor
cursor = connection.cursor()

# geração de dados aleatórios
fake = Faker('pt_BR')
n = 100 # quantidade de linhas de dados aleatórios
for i in range(n):
    codigo = int(i+1)
    nome = 'Produto_' + str(i+1)
    preco = fake.pyfloat(
        left_digits = 3, 
        right_digits = 2,
        positive = True,
        min_value = 5,
        max_value = 1000
        )
    print(nome)
    print(preco)
    # as variáveis 'codigo', 'nome' e 'preco' foram escolhidas por serem as colunas presentes na tabela que será usada.

    # Executar o comando SQL
    comandoSQL = """INSERT INTO public."PRODUTO" ("CODIGO", "NOME", "PRECO") values (%s, %s, %s)"""
    registro = (codigo, nome, preco)
    cursor.execute(comandoSQL, registro)

# Executar o commit da conexão
connection.commit()
print('Inserção realizada com sucesso!')

# Desconectar do banco de dados e cursor
connection.close()
