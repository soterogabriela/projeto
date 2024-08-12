import streamlit as st

# Título da aplicação
st.title("Teste de Temperamento")

# Descrição ou instruções
st.write("Responda às perguntas abaixo para descobrir qual é o seu temperamento dominante. Ai sim você poderá postar diariamente sobre ele rs")

# Pontuação inicial para cada temperamento
colerico = 0
sanguineo = 0
fleumatico = 0
melancolico = 0

# Pergunta 1
pergunta_1 = st.radio(
    "Como você reage em situações de pressão?",
    ('Mantenho a calma e sou paciente 😌', 'Fico estressado, mas tento resolver 😤', 'Procuro me afastar para evitar conflitos 🤔', 'Tomo o controle e decido rapidamente 💪')
)

if pergunta_1 == 'Mantenho a calma e sou paciente 😌':
    fleumatico += 1
elif pergunta_1 == 'Fico estressado, mas tento resolver 😤':
    melancolico += 1
elif pergunta_1 == 'Procuro me afastar para evitar conflitos 🤔':
    sanguineo += 1
elif pergunta_1 == 'Tomo o controle e decido rapidamente 💪':
    colerico += 1

# Pergunta 2
pergunta_2 = st.radio(
    "Como você se sente em situações sociais?",
    ('Gosto de estar com muitas pessoas 🎉', 'Prefiro observar mais do que interagir 👀', 'Sou tímido e evito interações sociais 😶', 'Gosto de interagir, mas com um grupo seleto 🤝')
)

if pergunta_2 == 'Gosto de estar com muitas pessoas 🎉':
    sanguineo += 1
elif pergunta_2 == 'Prefiro observar mais do que interagir 👀':
    melancolico += 1
elif pergunta_2 == 'Sou tímido e evito interações sociais 😶':
    fleumatico += 1
elif pergunta_2 == 'Gosto de interagir, mas com um grupo seleto 🤝':
    colerico += 1

# Pergunta 3
pergunta_3 = st.radio(
    "Como você lida com mudanças?",
    ('Abraço mudanças e adapto rapidamente 🌟', 'Tenho dificuldade, mas eventualmente me adapto 😅', 'Evito mudanças e prefiro estabilidade 🏠', 'Gosto de mudanças, mas me sinto ansioso 😰')
)

if pergunta_3 == 'Abraço mudanças e adapto rapidamente 🌟':
    colerico += 1
elif pergunta_3 == 'Tenho dificuldade, mas eventualmente me adapto 😅':
    melancolico += 1
elif pergunta_3 == 'Evito mudanças e prefiro estabilidade 🏠':
    fleumatico += 1
elif pergunta_3 == 'Gosto de mudanças, mas me sinto ansioso 😰':
    sanguineo += 1

# Pergunta 4
pergunta_4 = st.radio(
    "Como você lida com críticas?",
    ('Aceito e reflito sobre elas 🤔', 'Fico magoado e tento melhorar 😔', 'Tendo a ignorá-las 🙉', 'Respondo de forma defensiva 🚫')
)

if pergunta_4 == 'Aceito e reflito sobre elas 🤔':
    fleumatico += 1
elif pergunta_4 == 'Fico magoado e tento melhorar 😔':
    melancolico += 1
elif pergunta_4 == 'Tendo a ignorá-las 🙉':
    sanguineo += 1
elif pergunta_4 == 'Respondo de forma defensiva 🚫':
    colerico += 1

# Botão para enviar as respostas
if st.button("Enviar"):
    # Determinando o temperamento dominante
    resultado = ""
    meme_url = ""
    
    if max(colerico, sanguineo, fleumatico, melancolico) == colerico:
        resultado = ("Ah, Nathan, não poderia ser diferente, igualzin sua colega! Seu temperamento dominante é Colérico. Você é o tipo de pessoa que "
                     "acredita que uma reunião de equipe não é completa sem uma boa dose de caos. 'Porque, claro, controlar a situação "
                     "é sempre mais divertido do que deixar as coisas seguirem seu curso!'")
        meme_url = "https://images3.memedroid.com/images/UPLOADED76/5e4844ca58021.jpeg"  # Meme zoando o temperamento Colérico
    elif max(colerico, sanguineo, fleumatico, melancolico) == sanguineo:
        resultado = ("Olha só, um verdadeiro animador de festas! Seu temperamento dominante é Sanguíneo. Você está sempre por aí, "
                     "fazendo piadas e mantendo todo mundo animado, mesmo quando ninguém pediu uma performance. 'Seja o que for que "
                     "você esteja fazendo, lembre-se de que o mundo não gira em torno de uma animação de grupo!'")
        meme_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHsZgWov-Zz7iFgosvTQHjWtBo7SN1Yka-ysJ9P1Sfz8Ma1XhnUzriX3eYA9mLZHuPgWE&usqp=CAU"  # Meme zoando o temperamento Sanguíneo
    elif max(colerico, sanguineo, fleumatico, melancolico) == fleumatico:
        resultado = ("Uau, Nathan! Parece que seu temperamento dominante é Fleumático. Se você não se importar com o fato de que a "
                     "maioria das pessoas acha que você está apenas esperando um momento tranquilo para finalmente explodir. 'Claro, "
                     "você pode se achar a encarnação da serenidade, mas sabemos como você fica quando tá com fome!'")
        meme_url = "https://images3.memedroid.com/images/UPLOADED481/5e4302477b5da.jpeg"  # Meme zoando o temperamento Fleumático
    elif max(colerico, sanguineo, fleumatico, melancolico) == melancolico:
        resultado = ("Seu temperamento dominante é Melancólico. Você é o pensador profundo que nunca está satisfeito com o 'é o que é'. "
                     "Às vezes parece que você está em uma eterna reflexão filosófica. 'Vamos lá, Nathan, o mundo não precisa de mais dramas!'")
        meme_url = "https://pbs.twimg.com/media/Cb76yvoWwAAylds?format=png&name=360x360"  # Meme zoando o temperamento Melancólico

    # Mostrando o resultado com meme
    st.write("Resultado:")
    st.write(resultado)
    st.image(meme_url)

# Créditos
st.write(" Gabriela Sotero, 2024 ✨")
