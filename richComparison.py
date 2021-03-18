class Filme:

    def __init__(self, titulo, diretor):
        self.__diretor = diretor
        self.__titulo = titulo

    def __eq__(self, outro_filme):
        return self.__titulo == outro_filme.__titulo

    def __repr__(self):
        return f'\n\t\tTítulo: {self.__titulo}\n\t\tDiretor: {self.__diretor}'


class Colecao:
    def __init__(self, nome):
        self.nome = nome
        self.__filmes = []

    def __add__(self, filme):
        self.__filmes.append(filme)
        return self

    def __str__(self):
        return f'Coleção: {self.nome}\nFilmes: {self.__filmes}'

    def tenho_o_filme(self, filme_procurado):
        meus_filmes = self.pega_todos_os_filmes()
        return filme_procurado in meus_filmes

    def pega_todos_os_filmes(self):
        return self.__filmes


colecao_filmes_blockbuster = Colecao('Filmes blockbuster')
colecao_filmes_blockbuster += Filme('O Poderoso Chefão', 'Francis Ford Coppola')
colecao_filmes_blockbuster += Filme('La la land', 'Damien Chazelle')
colecao_filmes_blockbuster += Filme('A Teoria de Tudo', 'James Marsh')

print(colecao_filmes_blockbuster)
print(f'Tenho o filme La la land? {colecao_filmes_blockbuster.tenho_o_filme(Filme("La la land", ""))}')
