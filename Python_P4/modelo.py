
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1
    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self): #__str__ é a representaçao textual do objeto (dunder str -> str especial)
        return f" {self.nome} - {self.ano} - {self._likes} Likes"

# Forma de fazer para herdar dados da classe Programa
# Chamamos de HERANÇA isso
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)  #É UMA FUNÇÃO QUE CHAMA O INICIALIZADOR DA CLASSE MÃE (NESSE CASO O PROGRAMA)
        self.duracao = duracao

    def __str__(self):
           return f" {self.nome} - {self.ano} - {self.duracao} Min - {self._likes} Likes"

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)  #É UMA FUNÇÃO QUE CHAMA O INICIALIZADOR DA CLASSE MÃE (NESSE CASO O PROGRAMA)
        self.temporadas = temporadas
    def __str__(self):
           return f" {self.nome} - {self.ano} - {self.temporadas} Temp - {self._likes} Likes"

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item): # METODO QUE FAZ A CLASSE FICAR ITERAVEL
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    #@property
    def __len__(self):
        return len(self._programas)

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
tmep = Filme("todo em pânico", 1999, 100)
demolidor = Serie("demolidor", 2016,2)


vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f"Tamanho do playlist: {len(playlist_fim_de_semana)}")

for programa in playlist_fim_de_semana:
    print(programa)

#print(f"Tá ou não está? {demolidor in playlist_fim_de_semana}")