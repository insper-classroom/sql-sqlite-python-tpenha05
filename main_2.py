from db.db_utils import *

tabela = Tabelinha('db\database_alunos_auto.db','Estudantes2','ID INTEGER PRIMARY KEY AUTOINCREMENT,Nome TEXT NOT NULL, Curso TEXT NOT NULL,AnoIngresso INTEGER','Nome,Curso,AnoIngresso')
# tabela.criar_tabela()
dados = [('Ana Costa','Computação', 2019),
    ('Pedro Penha','Física',2021),
    ('Carla Pinheiro','Computação',2020),
    ('João Cordibello','Matemática',2018),
    ('Maria Desponds','Química',2022),]
# tabela.inserir_dados(dados)
print(tabela.ver_dados('*','id=2'))
tabela.atualizar_dados('Curso','Física','Curso = "Matemática"')
tabela.delete_dados('ID = 3')
print(tabela.ver_dados('*',''))
