# Frase na tela - Implemente um programa que escreve na tela a frase "O primeiro programa a gente nunca esquece!".

# Etiqueta - Elabore um programa que escreve seu nome completo na primeira linha, seu endereço na segunda e o CEP e telefone na terceira.

# Letra de música - Faça um programa que mostre na tela uma letra de música que você gosta (proibido letras do Justin Bieber).

# Tabela de notas - Você foi contratado ou contratada por uma escola pra fazer o sistema de boletim dos alunos. Como primeiro passo, 
# escreva um programa que produza a seguinte saída:

# ex1: 

# print("O primeiro programa a gente nuncan esquece!")

# ex2:

# nomeCompleto = "Lucas Soares Simao"
# endereco = "Rua Fulano de Tal, 21"
# cepTelefone = "58000-000/83 988888-8888"

# print(f"""
# Nome Completo = {nomeCompleto}
# Endereço = {endereco}
# CEP/Telefone = {cepTelefone}
# """)

# ex3:

# print("""
# Have you got colour in your cheeks?
# Do you ever get that fear that you can't shift the type
# That sticks around like summat in your teeth?
# Are there some aces up your sleeve?
# Have you no idea that you're in deep?
# I've dreamt about you nearly every night this week
# How many secrets can you keep?
# 'Cause there's this tune I found
# That makes me think of you somehow
# And I play it on repeat
# Until I fall asleep
# Spilling drinks on my settee

# (Do I wanna know)
# If this feeling flows both ways?
# (Sad to see you go)
# Was sorta hoping that you’d stay
# (Baby, we both know)
# That the nights were mainly made
# For saying things that you can’t say tomorrow day
# """)


# ex4:

# print("""
# ALUNO (A)  NOTA
# =========  ====
# ALINE      9.0
# MÁRIO      DEZ
# SÉRGIO     4.5
# SHIRLEY    7.0
# """)

# ex5:

print("""
Cadastro de Clientes
0 - Fim
1 - Inclui
2 - Altera
3 - Exclui
4 - Consulta
Digite uma opção: 
""")

opcao = str(input("Digite uma opção: "))

print (f"\nVocê digitou a opção '{opcao}'.")