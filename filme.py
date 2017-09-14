import webbrowser

class Filme():
    def __init__(self, titulo_filme, historia_filme, imagem,
               trailer_youtube):
        self.title = titulo_filme
        self.storyline = historia_filme
        self.poster_image_url = imagem
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
