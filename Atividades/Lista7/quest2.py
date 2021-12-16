class Musica:
    pass
    def adicionarMusica (self, nome):
        self.nome = nome 
    def removerMusica (self, nome):
        if self.nome == self.nome:
            self.nome = 'Música removida'

musica_1 = Musica()
musica_1.adicionarMusica('vilarejo')
print (musica_1.nome)
musica_1.removerMusica('vilarejo')
print ("Música:", musica_1.nome)

class Playlist:
    def __init__ (self, nome):
        self.nome = nome
    def adicionarMusicaNaPlaylist (self, nomeMusica):
        self.nomeMusica = list(nomeMusica)

newplaylist = Playlist ('MPB')
newplaylist.adicionarMusicaNaPlaylist('relicario')

print("Playlist ", newplaylist.nome)
print("Música", newplaylist.nomeMusica)
