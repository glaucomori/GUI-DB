import tkinter as tk
from tkinter import ttk
import PSQL_CRUD as crud

#-----------------------------------------------------------------------------
# # Definição da classe e função __init__
#-----------------------------------------------------------------------------
class PrincipalBD:
    # Essa função irá determinar os componentes presentes na interface gráfica e suas posições
    def __init__(self, win):
        self.objBD = crud.AppBD() # definir um objeto do banco de dados com base na classe com as funções CRUD (importado na 3ª linha do código).
        
        # COMPONENTES
        
        # Rótulos
        # o módulo 'tkinter.Label()' é o que define um rótulo (aqui está 'tk.Label()' devido à chamada 'import tkinter as tk' na 1ª linha do código)
        self.lbCodigo = tk.Label(win, text='Código do Produto:') # 'win' é o parâmetro que será passado junto com a função e 'text' é a string que aparecerá no rótulo
        self.lblNome = tk.Label(win, text='Nome do Produto:')
        self.lblPreco = tk.Label(win, text='Preço:')
        
        # Caixas de Texto
        # o módulo 'tkinter.Entry()' é o que define uma caixa de texto (aqui está 'tk.Entry()' devido à chamada 'import tkinter as tk' na 1ª linha do código)
        self.txtCodigo = tk.Entry(bd=2, width=33) # 'bd' é o tamanho da borda e 'width' é o tamanho da caixa de texto
        self.txtNome = tk.Entry(bd=2, width=33)
        self.txtPreco = tk.Entry(bd=2, width=33)

        # Botões
        # o módulo 'tkinter.Button()' é o que define botão (aqui está 'tk.Button()' devido à chamada 'import tkinter as tk' na 1ª linha do código)
        # 'win' é o parâmetro que será passado junto com a função, 'text' é a string que aparecerá no botão, 'height' é a altura que o botão terá
        # 'width' é a largura que o botão terá, 'bg' é a cor do background do botão, 'command' é o comando que o botão executará ao ser pressionado/clicado
        self.btnCadastrar=tk.Button(win, text='Cadastrar', height= 1, width=10, bg='lightgrey', command=self.fCadastrarProduto) # ao clicar nesse botão a função 'fCadastrarProduto' será chamada     
        self.btnAtualizar=tk.Button(win, text='Atualizar', height= 1, width=10, bg='lightgrey', command=self.fAtualizarProduto) # ao clicar nesse botão a função 'fAtualizarProduto' será chamada        
        self.btnExcluir=tk.Button(win, text='Excluir', height= 1, width=10, bg='lightgrey', command=self.fExcluirProduto) # ao clicar nesse botão a função 'fExcluirProduto' será chamada        
        self.btnLimpar=tk.Button(win, text='Limpar', height= 1, width=10, bg='lightgrey', command=self.fLimparTela) # ao clicar nesse botão a função 'fLimparTela' será chamada                
        
        #----- Componente TreeView --------------------------------------------
        
        # Dados das colunas
        self.dadosColunas = ("Código", "Nome", "Preço") # definição os nomes que as colunas receberão (será usado para criar a grade com os valores)           

        # Grade com os valores
        # o módulo 'ttk.Treeview()' é o que define uma grade de valores. O parâmetro 'win' é o parâmetro que será passado junto com a função
        # 'columns' são as colunas da grade, ' show='headings' ' exibe os nomes das colunas na grade, 'selectmode' é o modo de seleção permitido para essa grade
        # o selectmode 'browse' permite que um item da grade seja selecionado por vez e isso será necessário para as interações dessa interface gráfica
        self.treeProdutos = ttk.Treeview(win, 
                                       columns=self.dadosColunas,
                                       show='headings',
                                       selectmode='browse')
        
        # Barra de rolagem
        # o módulo 'ttk.Scrollbar()' é o que define uma barra de rolagem. O parâmetro 'win' é o parâmetro que será passado junto com a função
        # 'orient' é a orientação da barra de rolagem (vertical, horizontal), 'command' é a ação que está atrelada à barra de rolagem
        # 'self.treeProdutos.yview' indica que a barra de rolagem está relacionada a visualização da grade e ao eixo y dessa visualização
        self.verscrlbar = ttk.Scrollbar(win,
                                        orient="vertical",
                                        command=self.treeProdutos.yview)
        self.verscrlbar.pack(side ='right', fill ='x') # posição da barra de rolagem

        # Conectar a barra de rolagem com a grade 
        # o método 'configure' é o que define as configurações da grade. O parâmetro 'yscrollcommand' é relacionado à movimentação do campo de visão no eixo y
        # 'self.verscrlbar.set' indica que a movimentação da grede no eixo y estará atrelada à barra de rolagem definida anteriormente
        self.treeProdutos.configure(yscrollcommand=self.verscrlbar.set)
        
        # Rótulo das colunas
        # o método 'headings' é o que define os rótulos que a grade apresentará.
        self.treeProdutos.heading("Código", text="Código") # o primeiro parâmetro passado é a definição da coluna e 'text' é a string que esse rótulo da coluna receberá
        self.treeProdutos.heading("Nome", text="Nome")
        self.treeProdutos.heading("Preço", text="Preço")

        # Formatação das colunas
        # o método 'column' é o que define as colunas que a grade apresentará. O primeiro parâmetro passado é a definição da coluna
        #'minwidth' é a largura mínima da coluna, 'width' é a largura da coluna, 'anchor' é a justificação dos dados. 'CENTER' indica dados centralizados
        self.treeProdutos.column("Código",minwidth=0,width=60, anchor=tk.CENTER)
        self.treeProdutos.column("Nome",minwidth=0,width=230)
        self.treeProdutos.column("Preço",minwidth=0,width=60, anchor=tk.CENTER)

        self.treeProdutos.pack(padx=10, pady=10) # posição da grade
        
        # o método 'bind' conecta eventos. Nesse caso está atrelando a seleção da grade com a função 'apresentarRegistrosSelecionados' 
        # "<<TreeviewSelect>>" é o parâmetro que indica que o método 'bind' receberá os dados da seleção da grade (ao clicar em alguma linha da grade)
        self.treeProdutos.bind("<<TreeviewSelect>>", 
                               self.apresentarRegistrosSelecionados)
        #---------------------------------------------------------------------
        #posicionamento dos componentes na janela
        #---------------------------------------------------------------------  
        # o método place é o que define o posicionamento dos componentes situando-os nos eixos x e y.
        self.lbCodigo.place(x=50, y=30)
        self.txtCodigo.place(x=200, y=30)
        
        self.lblNome.place(x=50, y=60)
        self.txtNome.place(x=200, y=60)
        
        self.lblPreco.place(x=50, y=90)
        self.txtPreco.place(x=200, y=90)
               
        self.btnCadastrar.place(x=50, y=120)
        self.btnAtualizar.place(x=150, y=120)
        self.btnExcluir.place(x=250, y=120)
        self.btnLimpar.place(x=350, y=120)
                   
        self.treeProdutos.place(x=50, y=160)
        self.verscrlbar.place(x=405, y=160, height=225)

        # após as definições iniciais essa função __init__ chamará a função 'carregarDadosIniciais'. Assim já haverão dados sendo exibidos assim que o programa iniciar.
        self.carregarDadosIniciais()

#-----------------------------------------------------------------------------
# Definição da função 'apresentarRegistrosSelecionados'
#----------------------------------------------------------------------------- 
    # Essa função irá apresentar os dados que forem selecionados na grade para os respectivos campos das caixas de texto
    def apresentarRegistrosSelecionados(self, event):
        self.fLimparTela() # chama a função 'fLimparTela'
        for selection in self.treeProdutos.selection(): # cláusula 'if' para os dados da linha selecionada na grade (referenciados mais acima no código)
            item = self.treeProdutos.item(selection) # atribui os dados da linha selecionada a uma lista de nome 'item'
            codigo,nome,preco = item["values"][0:3]  # atribui os dados da lista 'item'(limitados a três valores conforme parâmetro) para as variáveis codigo, nome e preco
            self.txtCodigo.insert(0, codigo) # insere o valor do codigo(parâmetro dessa linha) para a caixa de texto referente ao codigo 
            self.txtNome.insert(0, nome) # insere o valor do nome(parâmetro dessa linha) para a caixa de texto referente ao nome
            self.txtPreco.insert(0, preco) # insere o valor do preço(parâmetro dessa linha) para a caixa de texto referente ao preço

#-----------------------------------------------------------------------------
# Definição da função 'carregarDadosIniciais'
#-----------------------------------------------------------------------------
    # Essa função irá carregar os dados iniciais quando o programa for iniciado e quando for necessário recarregar os valores(como um atualização, por exemplo)
    def carregarDadosIniciais(self):
        try: # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
          self.iid = 0 # define a variável 'iid' que será usada nessa função
          registros=self.objBD.selecionarDados() # recebe o retorno da função 'selecionarDados' do objeto do banco de dados e atribui à variável 'registros'
          print("************ dados disponíveis no BD ***********")
          for item in registros: # cláusula de recursividade para cada item(lista) obtida no retorno da função 'selecionarDados' do objeto do banco de dados
              codigo=item[0] # atribui à variável codigo o primeiro valor de cada lista(que sabemos ser o codigo por estar assim definido na função 'selecionarDados')
              nome=item[1] # atribui à variável nome o segundo valor de cada lista(que sabemos ser o nome por estar assim definido na função 'selecionarDados')
              preco=item[2] # atribui à variável preco o primeiro valor de cada lista(que sabemos ser o preco por estar assim definido na função 'selecionarDados')
              print("Código = ", codigo)
              print("Nome = ", nome)
              print("Preço  = ", preco, "\n")

              # o método 'insert' cria um novo item e adiciona-o à grade. 
              # O primeiro parâmetro é a identificação de onde inserir o item, e a string vazia sinaliza que será um novo elemento(uma nova linha na grade)
              # O segundo parâmetro é index do local onde o item será inserido e o valor 'end' indica o final da grade
              # 'iid' é o identificador do item criado, 'values' são os valores associados ao item criado
              self.treeProdutos.insert('', 'end',
                                   iid=self.iid,
                                   values=(codigo,
                                           nome,
                                           preco))
              self.iid = self.iid + 1 # incrementa o 'iid' pois precisa ser um valor único para cada inserção através do método acima
          print('Dados da Base')        
        except: # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
          print('Ainda não existem dados para carregar')

#-----------------------------------------------------------------------------
# Definição da função 'fLerCampos'
#-----------------------------------------------------------------------------
    # Essa função lerá os dados da tela(presentes nas caixas de texto)
    def fLerCampos(self):
        try: # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
          print("************ dados disponíveis ***********") 
          codigo = int(self.txtCodigo.get()) # atribui à variável 'codigo' o valor que estiver presente na caixa de texto 'txtCodigo'
          print('codigo', codigo)
          nome=self.txtNome.get() # atribui à variável 'nome' o valor que estiver presente na caixa de texto 'txtNome'
          print('nome', nome)
          preco=float(self.txtPreco.get()) # atribui à variável 'preco' o valor que estiver presente na caixa de texto 'txtPreco'
          print('preco', preco)
          print('Leitura dos Dados com Sucesso!')
        except: # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
          print('Não foi possível ler os dados.')
        return codigo, nome, preco # retorna as variaveis 'codigo', 'nome' e 'preco' como resultado ao final dessa função

#-----------------------------------------------------------------------------
# Definição da função 'fCadastrarProduto'
#-----------------------------------------------------------------------------
    # Essa função irá cadastrar um produto, criando uma linha de dados referente a esse produto e adicionando ao banco de dados
    def fCadastrarProduto(self):
        try: # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
          print("************ dados disponíveis ***********")
          codigo, nome, preco= self.fLerCampos() # as variáveis 'codigo', 'nome' e 'preco' receberão os respectivos valores presentes nas caixas de texto
          self.objBD.inserirDados(codigo, nome, preco) # chama a função 'inserirDados' do objeto do banco de dados, passando como parâmetros os valores das caixas de texto

          # o método 'insert' cria um novo item e adiciona-o à grade. 
          # O primeiro parâmetro é a identificação de onde inserir o item, e a string vazia sinaliza que será um novo elemento(uma nova linha na grade)
          # O segundo parâmetro é index do local onde o item será inserido e o valor 'end' indica o final da grade
          # 'iid' é o identificador do item criado, 'values' são os valores associados ao item criado
          self.treeProdutos.insert('', 'end',
                                iid=self.iid,
                                values=(codigo,
                                        nome,
                                        preco))
          self.iid = self.iid + 1 # incrementa o 'iid' pois precisa ser um valor único para cada inserção através do método acima

          #recarregar dados na tela
          self.treeProdutos.delete(*self.treeProdutos.get_children()) # apaga a grade de valores atuais para poder carregar uma nova grade
          self.carregarDadosIniciais() # chama a função 'carregarDadosIniciais'
          self.fLimparTela() # chama a função 'fLimparTela'
          print('Produto Cadastrado com Sucesso!')
        except: # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
          print('Não foi possível fazer o cadastro.')

#-----------------------------------------------------------------------------
# Definição da função 'fAtualizarProduto'
#-----------------------------------------------------------------------------
    # Essa função irá atualizar os dados do produto apresentado nas caixas de texto
    def fAtualizarProduto(self):
        try: # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
          print("************ dados disponíveis ***********")
          codigo, nome, preco= self.fLerCampos() # as variáveis 'codigo', 'nome' e 'preco' receberão os respectivos valores presentes nas caixas de texto
          self.objBD.atualizarDados(codigo, nome, preco) # chama a função 'atualizarDados' do objeto do banco de dados, passando como parâmetros os valores das caixas de texto
          
          #recarregar dados na tela
          self.treeProdutos.delete(*self.treeProdutos.get_children()) # apaga a grade de valores atuais para poder carregar uma nova grade
          self.carregarDadosIniciais() # chama a função 'carregarDadosIniciais'
          self.fLimparTela() # chama a função 'fLimparTela'
          print('Produto Atualizado com Sucesso!')
        except: # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
          print('Não foi possível fazer a atualização.')

#-----------------------------------------------------------------------------
# Definição da função 'fExcluirProduto'
#-----------------------------------------------------------------------------
    # Essa função irá excluir os dados do produto apresentado nas caixas de texto
    def fExcluirProduto(self):
        try: # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
          print("************ dados disponíveis ***********")
          codigo, nome, preco= self.fLerCampos() # as variáveis 'codigo', 'nome' e 'preco' receberão os respectivos valores presentes nas caixas de texto
          # nessa linha de código acima foram definidas as variáveis 'nome' e 'preco' (para evitar erros) pois a função 'fLerCampos' irá retornar esses valores também
          self.objBD.excluirDados(codigo) # chama a função 'excluirDados' do objeto do banco de dados, passando como parâmetro o valor de código da caixa de texto
          
          #recarregar dados na tela
          self.treeProdutos.delete(*self.treeProdutos.get_children()) # apaga a grade de valores atuais para poder carregar uma nova grade
          self.carregarDadosIniciais() # chama a função 'carregarDadosIniciais'
          self.fLimparTela() # chama a função 'fLimparTela'
          print('Produto Excluído com Sucesso!')
        except: # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
          print('Não foi possível fazer a exclusão do produto.')

#-----------------------------------------------------------------------------
# Definição da função 'fLimparTela'
#-----------------------------------------------------------------------------
    # Essa função irá limpar os dados das caixas de texto
    def fLimparTela(self):
        try: # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
          print("************ dados disponíveis ***********")
          self.txtCodigo.delete(0, tk.END) # exclui o dado de código da sua caixa de texto
          self.txtNome.delete(0, tk.END) # exclui o dado de nome da sua caixa de texto
          self.txtPreco.delete(0, tk.END) # exclui o dado de preço da sua caixa de texto
          print('Campos Limpos!')
        except: # tratamento de erros com 'try' e 'except' é fundamental para criar um programa confiável
          print('Não foi possível limpar os campos.')

#-----------------------------------------------------------------------------
# Programa Principal
#-----------------------------------------------------------------------------
# Comandos para a criação da janela
janela=tk.Tk() # definição da interface gráfica
principal=PrincipalBD(janela) # chamada à classe 'PrincipalBD' e à função __init__ (descritas no início do cógido)
janela.title('Tabela de Preço dos Produtos') # Título que a interface gráfica receberá
janela.geometry("460x430") # definido o tamanho da interface gráfica
janela.mainloop() # determinado que a interface gráfica se manterá aberta até que o usuário feche-a
#-----------------------------------------------------------------------------
