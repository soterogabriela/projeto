import streamlit as st

# Configurando o título e a descrição do site
st.set_page_config(page_title="Pro Nathan ver", page_icon="🐉", layout="centered")
st.title("Nathan, Dragões à Vista! Tudo sobre a 1ª Temporada de House of the Dragon :D 🐉")

# Introdução
st.header("Resuminho")
st.write("""
Ei, Nathan! Essa série é um spin-off de 'Game of Thrones' que te leva 200 anos antes dos eventos da série original. A série fala da ruína da Casa Targaryen e a eletrizante guerra civil conhecida como a Dança dos Dragões. É pura intriga, traição (gatilhos) e batalhas espetaculares, com dragões dominando os céus de Westeros. Assiste logo pra gente fofocar! 🔥🐉
""")

# Abas para os episódios
tabs = st.tabs(["RESUMÃO", "QUEM É ESSE POVO?", "OS DRAGÕES <3", "IMPORTANTÍSSIMO SE PULAR JÁ ERA, VOU COLOCAR VÍRUS NA TUA MÁQUINA"])

with tabs[0]:
    st.subheader("Resumão")
    st.write("""
    Jovem, segura essa bomba que veio direto dos corredores de Porto Real! Na primeira temporada de "House of the Dragon", a série mergulha no reinado de Viserys I, que foi um rei meio fraquinho, sabe? Ele reinou uns 130 anos depois que Aegon conquistou Westeros. A coisa toda começou com ele dividindo o trono de ferro com Aemma Targaryen, mas eles só tiveram uma filha, a Rhaenyra, que acabou sendo rainha, mas o resto, bem, foi resto mesmo.

    Viserys tentou várias vezes ter um filho homem, mas não rolava. Aí, o cara se casou de novo com Alicent Hightower, que era amiga da filha dele, a Rhaenyra, quando eram pré-adolescentes. Eles se separaram quando Alicent casou com o pai dela e aí a coisa ficou meio estranha.

    Essas duas nutriram uma competição desde então, que só piorou quando tiveram filhos. E olha que os Targaryen tinham fama de só casarem entre eles mesmos, hein?

    Rhaenyra casou com Laenor Velaryon, que deu uma de finado pra fugir com o amante. Aí, ela se casou com o tio, o Daemon, que é bem brabo. A Rhaenyra teve vários filhos, e a Alicent também teve uns com o Viserys I, incluindo o Aegon II, que acabou sendo coroado rei depois da morte do pai.

    E aí, Nathan, deu ruim! A Rhaenyra não aceitou a coroação do irmão e entrou em trabalho de parto prematuro, dando à luz uma criança morta. Enquanto isso, o Daemon reuniu um conselho pra planejar a guerra que tava por vir.

    No finalzinho da temporada, Rhaenyra mandou os filhos com os dragões pra anunciar a coroação dela e buscar aliados. Só que o Lucerys, um dos filhos, foi pra Ponta Tempestade, mas acabou encontrando o Aemond, que tinha pego um dragão que era meio que da ex do Daemon.

    As filhas da ex ficaram chateadas com a situação e brigaram com o Aemond. Ele acabou matando o Lucerys e o dragão dele numa briga aérea. A temporada terminou com a Rhaenyra recebendo a notícia dessa confusão toda na Pedra do Dragão. Cabuloso né? Partiu fofocassssssss
    """)

with tabs[1]:
    st.subheader("Quem é esse povo todo?")
    st.write("""
    E aí, meu príncipe 🤴, vou te contar quem são os verdadeiros jogadores nesse tabuleiro de intrigas de "House of the Dragon". Aqui tá só quem importa, saca só:

    Rhaenyra Targaryen é a filha primogênita do Rei Viserys I Targaryen. Desde jovem, ela é treinada para governar e é nomeada herdeira do Trono de Ferro, um fato que causa grande controvérsia em Westeros. Forte, determinada e corajosa, Rhaenyra luta para provar seu direito ao trono contra a resistência de uma sociedade patriarcal e os desafios apresentados por outros pretendentes ao trono.

    Daemon Targaryen é o irmão mais novo do Rei Viserys I Targaryen e tio de Rhaenyra. Ele é um guerreiro formidável, piloto de dragão e um homem de temperamento volátil e ambições elevadas. Daemon se vê como o legítimo herdeiro do trono, causando constantes conflitos na corte e com sua própria família.

    Viserys I Targaryen é o Rei de Westeros durante o início dos eventos de "House of the Dragon". Ele é um homem gentil e bem-intencionado, mas seu reinado é marcado por uma crescente tensão e instabilidade política devido à questão da sucessão. Viserys enfrenta o desafio de manter a paz enquanto lida com as ambições de seus parentes e nobres do reino.

    Alicent Hightower é a segunda esposa do Rei Viserys I Targaryen e mãe de vários de seus filhos, incluindo Aegon II Targaryen. Alicent é uma figura astuta e influente na corte, muitas vezes envolvida em intrigas políticas e conspirações. Sua lealdade à sua família e filhos a coloca em conflito direto com Rhaenyra e seus seguidores.

    Aegon II Targaryen é o filho mais velho do Rei Viserys I com sua segunda esposa, Alicent Hightower. Ele se considera o verdadeiro herdeiro do Trono de Ferro e disputa com sua meia-irmã Rhaenyra pelo direito de governar Westeros. Aegon é apoiado por uma poderosa facção dentro do reino, o que leva a uma amarga guerra civil conhecida como a Dança dos Dragões.

    Corlys Velaryon, também conhecido como "Serpente Marinha", é o chefe da Casa Velaryon, uma das casas mais ricas e poderosas de Westeros. Ele é um renomado explorador e almirante, casado com Rhaenys Targaryen, a "Rainha que Nunca Foi". Corlys é um importante aliado de Rhaenyra na luta pelo trono.

    Rhaenys Targaryen é a prima do Rei Viserys I e esposa de Corlys Velaryon. Conhecida como "A Rainha que Nunca Foi", Rhaenys foi preterida na linha de sucessão em favor de Viserys, apesar de ter um forte direito ao trono. Ela apoia a reivindicação de Rhaenyra e desempenha um papel crucial na guerra civil.

    Otto Hightower é o Mão do Rei Viserys I e pai de Alicent Hightower. Ele é um político astuto e manipulador, com grande influência na corte. Otto trabalha incansavelmente para promover os interesses de sua filha e netos, frequentemente em conflito com aqueles que apoiam Rhaenyra.

    Criston Cole é um cavaleiro da Guarda Real conhecido por sua habilidade com a espada e sua honra. Inicialmente um aliado próximo de Rhaenyra, ele eventualmente muda de lado e se torna um fervoroso defensor de Aegon II. Sua mudança de lealdade tem um impacto significativo na Dança dos Dragões.

    Harwin Strong, também conhecido como "Quebra-ossos", é um cavaleiro robusto e filho do Mão do Rei, Lyonel Strong. Ele é especulado como o amante de Rhaenyra Targaryen e o pai de seus filhos, o que alimenta rumores e tensões na corte. Sua lealdade a Rhaenyra é inquestionável, e ele se torna uma figura importante durante a guerra civil.
    """)

with tabs[2]:
    st.subheader("Os dragões <3")
    st.write("""
1. Syrax
             
Syrax é o dragão montado por Rhaenyra Targaryen. Nomeado em homenagem a uma deusa da mitologia valiriana, Syrax é uma fêmea imponente, de cor amarela. Rhaenyra monta Syrax desde jovem, e o dragão desempenha um papel crucial na guerra civil conhecida como a Dança dos Dragões.

2. Caraxes
             
Caraxes, também conhecido como "O Sangrento", é o dragão montado por Daemon Targaryen. Caraxes é um dragão vermelho e feroz, conhecido por sua agressividade e poder. Ele é um dos dragões mais temidos e desempenha um papel vital nos confrontos durante a guerra civil.

3. Vhagar
             
Vhagar é um dos dragões mais antigos e maiores de Westeros. Montado por Laena Velaryon e, mais tarde, por Aemond Targaryen, Vhagar é uma criatura colossal, temida por sua experiência em combate e seu tamanho imenso. Sua presença na guerra civil é um fator decisivo em várias batalhas.

4. Meleys
             
Meleys, também conhecida como a "Rainha Vermelha", é o dragão montado por Rhaenys Targaryen. Meleys é uma dragão vermelha e ágil, conhecida por sua velocidade e ferocidade. Rhaenys e Meleys são aliados importantes de Rhaenyra durante a Dança dos Dragões.

5. Vermax
             
Vermax é o dragão montado por Jacaerys Velaryon, o filho mais velho de Rhaenyra Targaryen. Vermax é um dragão jovem, mas é treinado para a guerra e participa ativamente nos confrontos durante a guerra civil.

6. Arrax
             
Arrax é o dragão montado por Lucerys Velaryon, outro filho de Rhaenyra Targaryen. Como Vermax, Arrax é um dragão jovem e desempenha um papel importante nas batalhas da Dança dos Dragões.

7. Sunfyre
             
Sunfyre, também conhecido como "Sunfyre, o Dourado", é o dragão montado por Aegon II Targaryen. Sunfyre é famoso por suas escamas douradas brilhantes e é considerado um dos dragões mais belos de sua época. Ele é um combatente feroz e leal ao seu cavaleiro.

8. Dreamfyre
             
Dreamfyre é um dragão fêmea montado por Helaena Targaryen, irmã e esposa de Aegon II. Dreamfyre é conhecida por sua graciosidade e habilidade de voo. Ela desempenha um papel menor na guerra, mas ainda é uma parte importante da coleção de dragões da Casa Targaryen.

9. Tessarion
             
Tessarion, conhecido como o "Dragão de Bronze", é montado por Daeron Targaryen, o irmão mais novo de Aegon II. Tessarion tem escamas de um azul brilhante com asas de bronze e é um adversário formidável em batalha.

10. Seasmoke
             
Seasmoke é um dragão montado por Laenor Velaryon e, posteriormente, por Addam Velaryon. Seasmoke é um dragão cinza-prateado que é rápido e ágil no ar. Ele participa de várias batalhas importantes durante a guerra civil.
    """)

with tabs[3]:
    st.subheader("IMPORTANTÍSSIMO SE PULAR JÁ ERA, VOU COLOCAR VÍRUS NA TUA MÁQUINA")
    st.header("Qual a casa que você pertence em GOT/HOD?")
    casa = st.selectbox(
        "Escolha a casa que você se identifica em GOT/House of the Dragon: ~ *AQUI SEPARA OS HOMENS DOS MENINOS*",
        ("None", "Stark", "Lannister", "Baratheon", "Greyjoy", "Tyrell", "Martell", "Bolton", "Targaryen")
    )

    st.write(f"Você selecionou a casa: {casa}")

    if casa == "Targaryen":
        st.success("🎉🎸 Parabéns! 🎉🎸 Você ganhou um show do Projeto Minduim 🎶 para me pagar o dobro de 29 beijos 😘😘 no Porks Samambaia 🐷 no dia 22/06! 📅🎉")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5VtjWbLDKDaH6bB5ZdddKCggrLlaVMrYS73UWzSWaTxo4JrOHKspAX1i1wo1DItySCl4&usqp=CAU", caption="😬")

    elif casa == "Stark":
        st.error("Muito maria vai com as outras sabia?")
    elif casa == "Lannister":
        st.error("Quer dizer que vc apoia o incesto?????????????? E ANÕESSSS???????????")
    elif casa == "Baratheon":
        st.error("Muito taurino da sua parte")
    elif casa == "Greyjoy":
        st.error("Você iria pro RJ com um amigo dividir apartamento e outras coisinhas a mais")
    elif casa == "Tyrell":
        st.error("Curte flores? 🌹")
    elif casa == "Martell":
        st.error("No alto da MONTANHA, num arranha céu rsssssssss. be careful with ur eyes")
    elif casa == "Bolton":
        st.error("é o q?")

# Conclusão
# Lista de músicas com URLs do YouTube
playlist = [
    {"title": "This Fire - Franz Ferdinand (ESSA AQUI É TOP)", "url": "https://www.youtube.com/watch?v=haW_ruZ_Be8"},
    {"title": "Fire - Kasabian (MTV de quando tu era nenê)", "url": "https://www.youtube.com/watch?v=agVpq_XXRmU"},
    {"title": "Light my Fire - The Doors (Sugestiva, fica ai no ar)", "url": "https://www.youtube.com/watch?v=cq8k-ZbsXDI"},
    {"title": "Essa é a melhor do CBJr, depois vem hoje sou eu que não mais te quero :D", "url": "https://www.youtube.com/watch?v=TwwhrJUJ_VA"},
]

# Criando uma lista suspensa para selecionar a música
options = [song["title"] for song in playlist]
selected_song = st.selectbox("🎵 Só musicão top pra acompanhar a leitura :D ", options)

# Encontrando a URL da música selecionada
for song in playlist:
    if song["title"] == selected_song:
        st.video(song["url"])

# Rodapé
st.write("by Gabriela Sotero")
st.write("Site criado com [Streamlit](https://streamlit.io/) - © 2024")
