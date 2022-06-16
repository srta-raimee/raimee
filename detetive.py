''''
alunos: Larissa Raimee Gomes, Pedro Ghezzi, Isabela Navarro
'''''

import time
exit = False

print('**** o desaparecimento do villager Ferreiro ***')
print('''Regras de jogo:
1. Use as regras de inferência para escolher as respostas corretas.
2. Leia com atenção as dicas e as descobertas feitas ao longo do jogo
3. No final, temos 2 escolhas possíveis para um final de caso. Escolha com sabedoria!
4. Divirta-se!''')
time.sleep(15)

print('''Era uma tarde quente de novembro quando o Iron Golem guardião da TautoloVila estava sentado em 
sua poltrona reclinável de madeira- feita especialmente para seu tamanho gigante- quando recebeu a notícia de que 
o Ferreiro estava desaparecido já faziam 24 horas, sem deixar nenhuma pista além de uma trilha de farelos de Doritos
que iam de encontro com a Floresta do Medo, localizada do lado de fora dos muros que cercavam o local.
Foram levantadas diversas hipóteses sobre o ocorrido e os villagers já pensavam em solicitar ajuda, quando Iron golem, 
com toda sua sabedoria de guardião, decidiu que montaria uma assembléia com os principais villagers de TatutoloVila para
decidir como proceder com esse desaparecimento repentino de um cidadão de bem tão querido pela comunidade.''')
time.sleep(25)

print('''Horas depois, inicia-se a assembleia para deliberar sobre as pistas adquiridas e ações a serem tomadas. O presidente da
vila, Sr. Narigudo, veio imediatamente da cidade vizinha quando soube do caso e agora iria dirigir o debate.''')

print('''Sr. Narigudo: Muito bem amigos e companheiros de trajetória. Estamos aqui por um motivo já conhecido
e agora irei expôr as pistas e possíveis soluções que temos sobre o paradeiro de nosso amigo Ferreiro.
Fiquem atentos e anotem em suas cadernetas!
Lá vai...''')
time.sleep(15)

print('''o Ferreiro pode estar na floresta, 
então pode estar lá porque está fugindo de um creeper que ameaaçava a região!
1. p -> q''')
time.sleep(8)

print('''se o Ferreiro pode ter fugido de um creeper que ameaçava a região,
então ele pode pode estar correndo risco e precisa de ajuda.
2. q -> r''')
time.sleep(8)

print('''se o Ferrreiro corre perigo e precisa de ajuda, então devemos chamar a Srta.Raimee, detetive particular famosíssima,
para ajudar a resolver esse dilema.
3. r -> s  ''')
time.sleep(8)

print('''De repente, Iron Golen levanta a mão e tenta protestar.
Golen: Desculpa interromper, mas por que precisamos chamar essa tal de Raimee?
Eu consigo me virar perfeitamente bem contra qualquer inimigo que tente nos atacar!''')
time.sleep(8)

print('''Sr. Narigudo: Infelizmente essa é uma questão de votação, não podemos simplesmente
descartar a ajuda da Srta. Raimee num caso como esse. ''')
time.sleep(6)

print('''Iron Golem não acha que Srta. Raimee seja necessária para resolver esse dilema
4. ~s ''')
time.sleep(6)


while not exit:
    print('''Já que o villager corre perigo e precisa de ajuda, todos optaram por chamar a Srta. Raimee para ajudar 
nessa investigação, mesmo o Iron golem não achando necessário. Então vamos de...
1. Modus Tollens entre 3 e 4
2. O villager que se dane
3. Modus Ponens entre 3 e 4
4. Modus tollens entre 2 e 4''')
    c = input('Qual regra de inferência devemos aplicar? ')
    time.sleep(4)
    n= "1"
    n2= "2"
    n3 = "3"
    n4 = "4"
    if c.isdigit() and c == n:
        print('''Srta. Raimee: Viu? Foi só eu chegar que o Ferreiro já está menos ferrado! HAHAHA TENDEU? FERRADO! 
        BADUM TSSS!
        6. ~r''')
        while not exit:
            print(''' Srta. Raimee chega e acompanha o Golem até a entrada da Floresta do Medo. Conversando sobre
estratégias de procurar por pistas mais exatas do que a trilha de Doritos esfarelados que guiavam até ali.
Srta. Raimee: Caramba, a trilha de salgadinho acaba logo na entrada da floresta. Será que ele guardou na
mochila ou---''')
            time.sleep(6)
            print('''Iron Golem: SHHHH!!! UM CREEPER VEM VINDO AÍ.''')
            print('''Os dois olham em direção ao Creeper, assustados. 
Srta. Raimee: O Ferreiro pode ter fugido desse creeper aí que aparentemente tá ameaçando a região, então ele
pode estar precisando de ajuda...''')
            print('''Golem: ... talvez não precise de ajuda. A trilha de Salgadinho mostra que ele não chegou perto
de onde o Creeper está, ou seja...''')
            time.sleep(13)
            print('''1. Modus Ponens 2,6: O Ferreiro estava fugindo do creeper
2. Modus Tollens 2,7: O Ferreiro não estava fugindo do Creeper
3. Modus Tollens 2,6: O Ferreiro não estava fugindo do Creeper''')
            c1= input('Qual regra de inferência devemos aplicar? ')
            time.sleep(4)
            if c1.isdigit() and c1 == n or c1== n2:
                print('Hmm... resposta incorreta. Tente novamente.')
            elif c1.isdigit() and c1 == n3:
                print('''Golem: é isso aí. Ele não estava fugindo do creeper! Pelo menos sabemos que ninguém
corre o risco de ser explodido.
7. ~q''')
                while not exit:
                    print('''Iron Golem e Srta. Raimee caminham um pouco mais a dentro na trilha, procurando por
pegadas ou vestígios quando Srta. Raimee parece ter uma epifania.''')
                    time.sleep(5)
                    print('''Srta. Raimee: ESPERA UM POUCO AÍ! - diz ela. Golem para imediatamente e olha para ela
curioso esperando sua indagação. - o Ferreiro poderia estar na floresta quando estivesse fugindo do Creeper ali. Mas já concluimos
que o homem nem chegou ali perto, ou seja, não está fugindo do Crepeer. Sabe o que isso significa?''')
                    time.sleep(7)
                    print('''Golem: Que o villager já morreu mas de outra forma?!
Srta. Raimee: CLARO QUE NÃO! Significa que ele...
1. Modus Tollens 1,7: O Ferreiro se aprofundou na floresta do medo
2. Modus Tollens 1,7: O Ferreiro definitivamente não está na Floresta do Medo
3. Modus Tollens 2,6: O Ferreiro com certeza está na floresta''')
                    c2 = input('Qual regra de inferência devemos aplicar? ')
                    if c2.isdigit() and c2== n or c2== n3:
                        print("Resposta incorreta. Tente Novamente")
                    elif c2.isdigit() and c2== n2:
                        print('''Srta. Raimee: Okay, sabemos que ele não está na floresta... Mas então onde
mais ele pode estar?? Você conhece algum lugar onde ele possa estar ou que costuma frequentar??
8. ~p''')
                        while not exit:
                             time.sleep(8)
                             print('''Iron Golem: Na verdade, não. Ele gosta de passar o dia no trabalho, na PUC- TautoloVila
ficar em casa maratonando séries e filmes diversos, já até me convidou para ver junto com ele! Faz tempo
que não vou na casa dele, inclusive''')
                             time.sleep(10)
                             print('''
Isso me lembra que hoje estreou a 250º temporada de Stranger Minethings. Imagina só ir na casa do Ferreiro
e ele estivesse lá maratonando? Seria hilário! HAHA ''')
                             time.sleep(15)
                             print('''Srta. Raimee: Espera aí! Vocês não foram verificar a casa do Ferreiro??!! - Gritou 
extremamente bolada com a possibilidade de todo esse tempo de buscas ter sido em vão.- Vamos AGORA
até lá. Eu não tô acreditando que você não foi lá...''')
                             time.sleep(15)
                             print('''Iron Golem: Pelo menos agora sabemos que o Ferreiro pode estar na Floresta do Medo
ou na própria casa maratonando Stranger MineThings no Mineflix - disse, ficando vermelho de vergonha.
P v T ''')
                             time.sleep(15)
                             print('''Iron Golem e Srta. Raimee foram correndo pelas ruas de Tautolovila, cruzaram ruas sem olhar
para os lados e quase foram atropelados por um bando de ovelhas desgovernadas duas vezes... Tudo isso
para chegarem no destino final; a casa do Ferreiro''')
                             time.sleep(8)
                             print('''srta. Raimee: é aqui que descobrimos a verdade, pelo visto.''')
                             time.sleep(1)
                             print('''Golem: Bom.. Se sabemos que ele podia estar na floresta ou em casa maratonando Stranger'
Minethings, e já descobrimos que ele não está na Floresta...
Nesse momento, ambos pararam em frente à porta da casa do Villager desaparecido. Srta. Raimee colocou a mão na maçaneta
(um Golem como o Iron Golem não conseguiria abrir, tem mãos muito grandes!) e se preparou para abri-la.''')
                             time.sleep(18)
                             print('''Golem: No três...''')
                             time.sleep(1)
                             print('ambos: 1...')
                             time.sleep(2)
                             print('ambos: 2...')
                             time.sleep(3)
                             print('ambos: 3!!!')
                             print('''E a porta foi aberta. Tanto o Golem quanto Srta. Raimee ficaram embasbacados ao
perceberem que...
1. Silogismo Destrutivo 5,8: O Villager desaparecido estava o tempo todo em casa assistindo Mineflix, são e salvo
2. Modus Tollens 1,7: O villager continua na floresta
3. Adição 8: O villager desaparecido não estava na floresta, mas deixou um bilhete na mesa dizendo que estava na faculdade 
PUC-TautoloVila chorando na biblioteca pois não sabia fazer Tabela Verdade.''')
                             c3= input('Qual regra de inferência devemos aplicar para o melhor final? ')
                             if c3.isdigit() and c3 == n2:
                                 print('Resposta incorreta, tente novamente!')
                             elif c3.isdigit() and c3== n:
                                 print('''Após a grande descoberta de que o villager desaparecido estava o tempo todo na própia casa,
O presidente Sr. Narigudo foi informado do ocorrido e todos decidiram que a melhor punição para o Ferreiro- após ter causado tanta comoção desnecessária- 
seria jogá-lo no rio que passava há uns 2km dali. Alguns dizem  que o Ferreiro decidiu mudar de cidade de tão envergonhado que ficou, outros dizem
que ele ameaçou uma vingança grandiosa, mas o que realmente importa é que nada assim ocorrerá novamente.
9. T ''')
                                 time.sleep(25)
                                 print('''Parabéns! Você salvou a pequena cidade de TautoloVila e encontrou o Villager desaparecido com
a ajuda da incrível Srta. Raimee e do destemido Iron Golem. Você recebeu um pack de diamantes do Sr Narigudo como agradecimento por seus serviços,
além de uma bela safra de cenouras ofertada pelos moradores da cidade. Obrigada pela colaboração e até mais!''')
                                 exit = True
                                 break


                             elif c3.isdigit() and c3== n3:
                                 print('''Após abrirem a porta, Golem e Srta. Raimee encontraram um bilhete sobre a mesa do villager desaparecido dizendo
que ele estaria o tempo todo em casa ou na PUC- TautoloVila naquele fim de semana tentando resolver uma lista de exercícios de Lógica Matemática, 
e como a casa estava vazia só restava uma opção...
o presidente sr. Narigudo foi informado do ocorrido e todos decidiram que o melhor a se fazer seria ligar para a profª Rafa para ajudar o pobre
do Ferreiro, que nas palavras do presidente estava "extremamente ferrado" na matéria de Lógica Matemática e que isso era mais comum
do que aparentava ser. Toda a cidade se solidariezou com a causa, e meses depois o Ferreiro já havia concluído todos os trabalhos que foram pedidos pela Prof.
O Ferreiro prometeu jamais desaparecer novamente, e dizem por aí que ele até se tornou monitor da matéria! O que realmente importa é que ele está bem novamente,
e que esse trabalho merece um 10!
T v U''')
                                 time.sleep(25)
                                 print('''Parabéns! Você salvou a pequena cidade de TautoloVila e encontrou o Villager desaparecido com
a ajuda da incrível Srta. Raimee e do destemido Iron Golem. Você recebeu um pack de diamantes do Sr Narigudo como agradecimento por seus serviços
além de uma bela safra de cenouras ofertada pelos moradores da cidade. Obrigada pela colaboração e até mais!''')
                                 time.sleep(20)
                                 exit = True
                                 break
                             else:
                                 print('Por favor, digite um número válido!')

                    else:
                        print('Por favor, digite um número válido!')


    elif c.isdigit() and c == n2:
        print('Que investigador horrível você é! Para de preguiça e vai atrás de resolver esse caso, batata.')
    elif c.isdigit() and c == n3 or c== n4:
        print('Incorreto. Tente novamente.')
    else:
        print('Por favor, digite um número válido!')
