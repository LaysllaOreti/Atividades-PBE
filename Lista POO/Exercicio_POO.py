#Parte 1
class ItemBiblioteca:
    def __init__(self, titulo, ano_publicacao, disponibilidade=True):
        if ano_publicacao <= 0:
            print("O ano de publicação deve ser maior que 0")
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.disponibilidade = disponibilidade
        
    def emprestar(self):
        if not self.disponibilidade:
            raise Exception("Esse livro já está emprestado")
        self.disponibilidade = False
        
    def devolver(self):
        if self.disponibilidade:
            raise Exception("Esse livro está disponível")
        self.disponibilidade = True
        
    def obter_informacao(self):
        status = "Sim" if self.disponibilidade else "Não" #Irá colocar o Status de Disponível se a sentença for verdadeira
        return f"Título: {self.titulo}, Ano: {self.ano_publicacao}, Disponível: {disponibilidade}"

#Parte 2
class ColecaoLivros:
    def __init__(self, titulo, ano_publicacao, disponivel):
        super().__init__(titulo, ano_publicacao, disponibilidade)
        self.livros = []
    
    def adicionar_livro(self, livro:ItemBiblioteca):
        self.livros.append(livro)
    
    def verificar_disponibilidade_colecao(self):
        for livro in self.livros:
            if not livro.disponibilidade:
                return False
        return True
        
    def obter_informacao(self):
        retorno = super().obter_informacao()
        for livro in self.livros:
            retorno += f'\n {self.obter_informacao()}'
        return retorno

livroA = ItemBiblioteca(titulo: "ABC", ano_publicacao: 2005, disponibilidade: True)
livroB = ItemBiblioteca(titulo: "DEF", ano_publicacao: 2006, disponibilidade: True)

colecao = ColecaoLivros(titulo: "Minha Coleção", ano_publicacao: 2000, disponibilidade: False)