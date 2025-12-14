import matplotlib.pyplot as plt

# Classe para representar um livro
class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    def __str__(self):
       return f"{self.titulo} por {self.autor} | Gênero: {self.genero} | Quantidade: {self.quantidade}"

# Lista para armazenar os livros
biblioteca = []

# Função para adicionar um livro à biblioteca
def adicionar_livro(titulo, autor, genero, quantidade):
    novo_livro = Livro(titulo, autor, genero, quantidade)
    biblioteca.append(novo_livro)
    print(f"'{titulo}' foi adicionado à biblioteca.")
# Função para listar todos os livros
def listar_livros():
    print("Lista de Livros na Biblioteca:")
    for livro in biblioteca:
        print(livro)
# Função para buscar um livro pelo título
def buscar_por_titulo(titulo):
    for livro in biblioteca:
        if livro.titulo.lower() == titulo.lower():
            print("Livro encontrado:")
            print(livro)
            return livro
    print(f"Livro '{titulo}' não encontrado.")
    return None
# Adicionar alguns livros à biblioteca
adicionar_livro("Dom Quixote", "Miguel de Cervantes", "Romance", 3)
adicionar_livro("Orgulho e Preconceito", "Jane Austen", "Romance", 5)
adicionar_livro("1984", "George Orwell", "Distopia", 4)
adicionar_livro("Cem Anos de Solidão", "Gabriel García Márquez", "Realismo Mágico", 2)
adicionar_livro("O Apanhador no Campo de Centeio", "J.D. Salinger", "Ficção", 6)
# Listar todos os livros
listar_livros()
# Buscar um livro pelo título
buscar_por_titulo("1984")
buscar_por_titulo("Harry Potter")  # exemplo de não encontrado
# Criar gráfico de quantidade de livros por gênero
generos = [livro.genero for livro in biblioteca]
quantidades = {}
for livro in biblioteca:
    if livro.genero in quantidades:
        quantidades[livro.genero] += livro.quantidade
    else:
        quantidades[livro.genero] = livro.quantidade
# Criar o gráfico
plt.bar(quantidades.keys(), quantidades.values(), color='skyblue')
plt.xlabel("Gênero")
plt.ylabel("Quantidade de Livros")
plt.title("Distribuição de Livros por Gênero na Biblioteca")
# Adicionar rótulos em cima das barras
for i, (genero, qtd) in enumerate(quantidades.items()):
    plt.text(i, qtd + 0.1, str(qtd), ha='center')
plt.show()