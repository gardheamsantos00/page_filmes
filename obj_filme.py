import front
import filme


benga = filme.Filme("República Benganelas : o Filme",
                    "é tipo um projeto x", "benga.jpg","benga.mp4")

macacos = filme.Filme("Planeta dos Macacos: A Guerra",
                      "César e seu grupo são forçados a entrar em uma guerra contra um exército de soldados liderados por um impiedoso coronel. Depois que vários macacos perdem suas vidas no conflito, César luta contra seus instintos e parte em busca de vingança. Dessa jornada, o futuro do planeta poderá estar em jogo.",
                      "http://t0.gstatic.com/images?q=tbn:ANd9GcQUkXYeQ6cvPsajthgZUnUna9mmn30nIuk4VhPumSsgELo5z2Zr",
                      "https://www.youtube.com/watch?v=DqkzzMYQI5g")

liga = filme.Filme("Liga da Justiça",
                   "Liga da Justiça é um futuro filme de super-herói americano de 2017 baseado na equipe homônima da DC Comics e distribuído pela Warner Bros. Pictures. Será o quinto filme do Universo Estendido DC",
                   "http://i0.wp.com/blackpipe.com.br/wp-content/uploads/2017/03/Justice-League.jpg?fit=900%2C500",
                   "https://www.youtube.com/watch?v=BZUm2lpPoKM")

avatar = filme.Filme("Avatar 2",
                     "A lenda dos mundos",
                     "http://sm.ign.com/ign_pt/screenshot/default/avatar-parque-disney-3_xxwr.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

mumia = filme.Filme("A Múmia",
                    "Nas profundezas do deserto, uma antiga rainha cujo destino foi injustamente tirado está mumificada. Apesar de estar sepultada em sua cripta, ela desperta nos dias atuais. Com uma maldade acumulada ao longo dos anos, ela espelha terror desde as areais do Oriente Médio até os becos de Londres",
                    "http://t3.gstatic.com/images?q=tbn:ANd9GcQzZCY8q-I_IhEtX6I9HfufmKugC7UFjr8e86QO3-ekuWEGX4WA",
                    "https://www.youtube.com/watch?v=gHHxaXgrRC0")

coisa = filme.Filme("It: A Coisa",
                    "Quando as crianças começam a desaparecer na cidade de Derry, no Maine, as crianças do bairro se unem para atacar Pennywise, um palhaço malvado, cuja história de assassinato e violência remonta há séculos.",
                    "http://br.web.img2.acsta.net/pictures/17/03/29/07/56/333222.jpg",
                    "https://www.youtube.com/watch?v=Q3me7yLtymY")

mulher_maravilha = filme.Filme("Mulher Maravilha",
                    "Treinada desde cedo para ser uma guerreira imbatível, Diana Prince nunca saiu da paradisíaca ilha em que é reconhecida como princesa das Amazonas. Quando o piloto Steve Trevor se acidenta e cai em uma praia do local, ela descobre que uma guerra sem precedentes está se espalhando pelo mundo e decide deixar seu lar certa de que pode parar o conflito. Lutando para acabar com todas as lutas, Diana percebe o alcance de seus poderes e sua verdadeira missão na Terra.",
                    "http://t1.gstatic.com/images?q=tbn:ANd9GcRyCdWToNKN9fqnTc58XbMF7XC6ryMq-BHICs0aq5_0SFYoK0h3",
                    "https://youtu.be/I6Gj8Fvukk4")

alien = filme.Filme("Alien: Covenant",
                    "A tripulação do navio-colônia Covenant, ligada a um remoto planeta no lado distante da galáxia, descobre o que eles acreditam ser um paraíso inexplorado, mas na verdade é um mundo escuro e perigoso",
                    "http://t1.gstatic.com/images?q=tbn:ANd9GcSrNlo5abb4Roe1BXKtE8XVHHfvw2t_IErOaKjvMOZh2KZTjGxD",
                    "https://www.youtube.com/watch?v=svnAD0TApb8")

guardiao_galaxia = filme.Filme("Guardiões da Galáxia Vol. 2",
                    "Os Guardiões precisam lutar para manter sua recém descoberta família unida, enquanto descobrem os mistérios sobre o verdadeiro pai de Peter Quill",
                    "http://t0.gstatic.com/images?q=tbn:ANd9GcT3jhaTLkrcaiAxYv7EamUq2R--8wK4l6wH9UwQi97iYwaYn4Zm",
                    "https://www.youtube.com/watch?v=4-i8nTNSQFI")

homem_aranha = filme.Filme("Homem-Aranha: De Volta ao Lar",
                    "Depois de atuar ao lado dos Vingadores, chegou a hora do pequeno Peter Parker voltar para casa e para a sua vida, já não mais tão normal. Lutando diariamente contra pequenos crimes nas redondezas, ele pensa ter encontrado a missão de sua vida quando o terrível vilão Abutre surge amedrontando a cidade. O problema é que a tarefa não será tão fácil como ele imaginava.",
                    "http://t2.gstatic.com/images?q=tbn:ANd9GcT4O7xrHjQ1NMu_9kg6E9HUO4X7KtB9lVpVLglQfWH2BJIke3IB",
                    "https://www.youtube.com/watch?v=39udgGPyYMg")



filmes = [avatar , mumia, coisa , mulher_maravilha , alien, guardiao_galaxia, homem_aranha,benga]
front.open_movies_page(filmes)
