import front
import filme


benga = filme.Filme("Rep�blica Benganelas : o Filme",
                    "� tipo um projeto x", "benga.jpg","benga.mp4")

macacos = filme.Filme("Planeta dos Macacos: A Guerra",
                      "C�sar e seu grupo s�o for�ados a entrar em uma guerra contra um ex�rcito de soldados liderados por um impiedoso coronel. Depois que v�rios macacos perdem suas vidas no conflito, C�sar luta contra seus instintos e parte em busca de vingan�a. Dessa jornada, o futuro do planeta poder� estar em jogo.",
                      "http://t0.gstatic.com/images?q=tbn:ANd9GcQUkXYeQ6cvPsajthgZUnUna9mmn30nIuk4VhPumSsgELo5z2Zr",
                      "https://www.youtube.com/watch?v=DqkzzMYQI5g")

liga = filme.Filme("Liga da Justi�a",
                   "Liga da Justi�a � um futuro filme de super-her�i americano de 2017 baseado na equipe hom�nima da DC Comics e distribu�do pela Warner Bros. Pictures. Ser� o quinto filme do Universo Estendido DC",
                   "http://i0.wp.com/blackpipe.com.br/wp-content/uploads/2017/03/Justice-League.jpg?fit=900%2C500",
                   "https://www.youtube.com/watch?v=BZUm2lpPoKM")

avatar = filme.Filme("Avatar 2",
                     "A lenda dos mundos",
                     "http://sm.ign.com/ign_pt/screenshot/default/avatar-parque-disney-3_xxwr.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

mumia = filme.Filme("A M�mia",
                    "Nas profundezas do deserto, uma antiga rainha cujo destino foi injustamente tirado est� mumificada. Apesar de estar sepultada em sua cripta, ela desperta nos dias atuais. Com uma maldade acumulada ao longo dos anos, ela espelha terror desde as areais do Oriente M�dio at� os becos de Londres",
                    "http://t3.gstatic.com/images?q=tbn:ANd9GcQzZCY8q-I_IhEtX6I9HfufmKugC7UFjr8e86QO3-ekuWEGX4WA",
                    "https://www.youtube.com/watch?v=gHHxaXgrRC0")

coisa = filme.Filme("It: A Coisa",
                    "Quando as crian�as come�am a desaparecer na cidade de Derry, no Maine, as crian�as do bairro se unem para atacar Pennywise, um palha�o malvado, cuja hist�ria de assassinato e viol�ncia remonta h� s�culos.",
                    "http://br.web.img2.acsta.net/pictures/17/03/29/07/56/333222.jpg",
                    "https://www.youtube.com/watch?v=Q3me7yLtymY")

mulher_maravilha = filme.Filme("Mulher Maravilha",
                    "Treinada desde cedo para ser uma guerreira imbat�vel, Diana Prince nunca saiu da paradis�aca ilha em que � reconhecida como princesa das Amazonas. Quando o piloto Steve Trevor se acidenta e cai em uma praia do local, ela descobre que uma guerra sem precedentes est� se espalhando pelo mundo e decide deixar seu lar certa de que pode parar o conflito. Lutando para acabar com todas as lutas, Diana percebe o alcance de seus poderes e sua verdadeira miss�o na Terra.",
                    "http://t1.gstatic.com/images?q=tbn:ANd9GcRyCdWToNKN9fqnTc58XbMF7XC6ryMq-BHICs0aq5_0SFYoK0h3",
                    "https://youtu.be/I6Gj8Fvukk4")

alien = filme.Filme("Alien: Covenant",
                    "A tripula��o do navio-col�nia Covenant, ligada a um remoto planeta no lado distante da gal�xia, descobre o que eles acreditam ser um para�so inexplorado, mas na verdade � um mundo escuro e perigoso",
                    "http://t1.gstatic.com/images?q=tbn:ANd9GcSrNlo5abb4Roe1BXKtE8XVHHfvw2t_IErOaKjvMOZh2KZTjGxD",
                    "https://www.youtube.com/watch?v=svnAD0TApb8")

guardiao_galaxia = filme.Filme("Guardi�es da Gal�xia Vol. 2",
                    "Os Guardi�es precisam lutar para manter sua rec�m descoberta fam�lia unida, enquanto descobrem os mist�rios sobre o verdadeiro pai de Peter Quill",
                    "http://t0.gstatic.com/images?q=tbn:ANd9GcT3jhaTLkrcaiAxYv7EamUq2R--8wK4l6wH9UwQi97iYwaYn4Zm",
                    "https://www.youtube.com/watch?v=4-i8nTNSQFI")

homem_aranha = filme.Filme("Homem-Aranha: De Volta ao Lar",
                    "Depois de atuar ao lado dos Vingadores, chegou a hora do pequeno Peter Parker voltar para casa e para a sua vida, j� n�o mais t�o normal. Lutando diariamente contra pequenos crimes nas redondezas, ele pensa ter encontrado a miss�o de sua vida quando o terr�vel vil�o Abutre surge amedrontando a cidade. O problema � que a tarefa n�o ser� t�o f�cil como ele imaginava.",
                    "http://t2.gstatic.com/images?q=tbn:ANd9GcT4O7xrHjQ1NMu_9kg6E9HUO4X7KtB9lVpVLglQfWH2BJIke3IB",
                    "https://www.youtube.com/watch?v=39udgGPyYMg")



filmes = [avatar , mumia, coisa , mulher_maravilha , alien, guardiao_galaxia, homem_aranha,benga]
front.open_movies_page(filmes)
