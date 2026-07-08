def ola(nome, ge):
    if ge == "masculino":
        return (f'ola, {nome}, bem vindo')
    elif ge == "feminino":
        return (f'ola, {nome}, bem vinda')
    else:
        return (f'ola, {nome}, boas vindas')
txt1=ola('leo','masculino')
print(txt1)
txt1=ola('mila','feminino')
print(txt1)
txt1=ola('alan','neutro')
print(txt1)