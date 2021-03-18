from abc import ABCMeta, abstractmethod


class Programa(metaclass = ABCMeta):
    def __init__(self, nome, ano):
        self._nome = nome
        self.__ano = ano
        self.__likes = 0

    @abstractmethod
    def __str__(self):
        return f'Título: {self._nome.title()}, Ano: {self.__ano},' \
               f' Likes: {self.__likes}'

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    def __str__(self):
        return super().__str__() + f', Duração: {self.__duracao} segundos'

    @property
    def duracao(self):
        return self.__duracao


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas

    def __str__(self):
        return super().__str__() + f', Temporadas: {self.__temporadas}'


class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta]
playlist = Playlist('Playlist de fim de semana', filmes_e_series)
print(f'Tamanho da playlist {len(playlist)}')

for programa in playlist:
    categoria = 'Filme' if hasattr(programa, 'duracao') else 'Série'
    print(f'{categoria} - {programa}')
