# Lista de notas dos estudantes
notas = [7.5, 8.0, 6.5, 9.0, 10.0]

#Funçao regular para calcular a média
def calcular_media(notas):
    total = sum(notas)                  # precisa estar indentado
    media = total / len(notas)          # idem
    return media                        # idem

# Função lambda para arredondar a média para duas casas decimais
arredondar_media = lambda media: round(media, 2)

# Calcular a média
media = calcular_media(notas)
media_arredondada = arredondar_media(media)

# Verificar se os estudantes foram aprovados
situacao = "aprovado" if media_arredondada >= 7 else "Reprovado"

# Resultados
print("Notas:", notas)
print("Média:", media_arredondada)
print("Situacao:", situacao)