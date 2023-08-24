import sqlite3

# def inicialização(arquivo_database,nome_table):
#     conn = sqlite3.connect(arquivo_database)
#     cursor = conn.cursor()
#     cursor.execute(f"DROP TABLE {nome_table}")

# def cria_tabelas(cursor,nome_table,string_colunas):
    
class Tabelinha():
    """
    self.str_colunas é um strings em que é necessário passar o nome da colunas
    e o tipo de dado ex: TEXT NOT NULL

    self.colunas é uma string com nome das colunas 
    """
    def __init__(self, nome_database, nome_tabela, str_colunas, colunas):
        self.nome_database = nome_database
        self.nome_tabela = nome_tabela
        self.str_colunas = str_colunas
        self.colunas = colunas

    def criar_tabela(self):
        conn = sqlite3.connect(self.nome_database)
        cursor = conn.cursor()
        # cursor.execute(f"""DROP TABLE {self.nome_tabela}""")
        cursor.execute(f"""
CREATE TABLE IF NOT EXISTS {self.nome_tabela}(
                {self.str_colunas})
               """)
        
    def inserir_dados(self,dados):
        conn = sqlite3.connect(self.nome_database)
        cursor = conn.cursor()
        values = '?'
        for contador in range(len(dados[0])-1):
            values += ',?'
        cursor.executemany(f"""
INSERT INTO {self.nome_tabela} ({self.colunas})
VALUES ({values});
""",dados)  
        conn.commit()
        conn.close()

    def ver_dados (self, parametro_select, parametro_where):
        conn = sqlite3.connect(self.nome_database)
        cursor = conn.cursor()
        if parametro_where == '':
            cursor.execute(f"""
        SELECT {parametro_select} FROM {self.nome_tabela}""")
        else:
             cursor.execute(f"""
        SELECT {parametro_select} FROM {self.nome_tabela} WHERE {parametro_where}""")    
        resultado = cursor.fetchall()
        conn.close()
        return resultado

    def atualizar_dados(self,coluna,valor, parametro_where):
        conn = sqlite3.connect(self.nome_database)
        cursor = conn.cursor()
        cursor.execute(f"""
        UPDATE {self.nome_tabela} SET {coluna}='{valor}' WHERE {parametro_where} 
""")
        conn.commit()
        conn.close()
    
    def delete_dados(self,parametro_where):
        conn= sqlite3.connect(self.nome_database)
        cursor = conn.cursor()
        cursor.execute(f"""DELETE FROM {self.nome_tabela} WHERE {parametro_where}""")
        conn.commit()
        conn.close()




    