'''Em uma lista de convidados, um nome foi incluído por engano.
Remova o nome "Pedro" da lista abaixo:
convidados = ["Ana", "Pedro", "Lucas", "Pedro", "Marina"]'''
convidados = ["Ana", "Pedro", "Lucas", "Pedro", "Marina"]
for i in convidados:
    if "Pedro" in convidados:
        convidados.remove("Pedro")
print(convidados)
