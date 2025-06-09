# Nome completo do primeiro membro: [Mateus Pinheiro Carioca]
# RA do primeiro membro: [282046]
# Nome completo do segundo membro: [Felipe Pedral Cruz de Oliveira]
# RA do segundo membro: [220826]

'''
Implemente aqui a sua estratégia de ataque e a posição dos navios.
A estratégia de ataque deve ser implementada no método "jogar" e a posição dos navios no método "posicoes_navios".
A posição dos navios deve ser uma lista de objetos do tipo Navio, onde cada objeto contém o tamanho do navio e suas coordenadas.
A lista de navios deve conter todos os 5 navios, ou seja, um navio de tamanho 5, um de tamanho 4, dois de tamanho 3 e um de tamanho 2.

Observações:
- O tamanho dos navios é definido na constante NAVIOS, que é um dicionário onde cada chave é o nomes do navios e cada valor é o respectivo tamanho do navio.
- O tamanho do tabuleiro é definido na constante TABULEIRO_TAMANHO, que é um inteiro.
- O valor DESCONHECIDO representa uma posição vazia no tabuleiro.
- O valor NAVIO_ENCONTRADO representa uma posição onde um navio foi encontrado.
- O valor NAVIO_INTEIRO_ATINGIDO representa uma posição onde um navio foi atingido (todas as posições encontradas).
- Você pode consultar (mas não modificar) o arquivo constants.py para mais informações sobre os valores das constantes.
- Mais informações podem ser encontradas na documentação do projeto (arquivo README.md).'''

from constants import TABULEIRO_TAMANHO, NAVIOS, StatusTab
from classes._attack import Ataque
from classes._ship import Navio
from classes._pos_matriz import PosMatriz
from utils.helpers import get_adjacentes, dentro_limite
import random
class AlunoPlayer():
    """Classe que representa o jogador bot do aluno."""

    def __init__(self):
        """Inicializa o jogador.
        
        Atributos:
        movimentos_realizados -- Lista de movimentos já realizados pelo jogador.
        tabuleiro -- Tabuleiro do jogador (inicializado automaticamente assim que o jogo começa).
        nome -- Nome da equipe.
        """
        self.movimentos_realizados = list()
        self.tabuleiro = None           # o tabuleiro é inicializado automaticamente assim que o jogo começa
        self.nome = "{NOME_DA_EQUIPE}"  # substitua!


    def jogar(self, estado_atual_oponente, navios_afundados) -> Ataque:
        """Método para realizar uma jogada.

        Parâmetros:
        estado_atual_oponente -- O estado atual do tabuleiro.
        navios_afundados -- Lista de nomes navios afundados (em ordem de afundamento).

        Retorna um objeto do tipo Ataque com as coordenadas (x,y) da jogada.
        """

        ataques = []
        # acertou = False
        # if not acertou:
        
        
        for i in range(TABULEIRO_TAMANHO):
            if i % 2 == 0:
                for j in range(1, TABULEIRO_TAMANHO, 2):
                    current = [i,j]
                    if estado_atual_oponente[i][j].status == StatusTab.DESCONHECIDO.value and (i, j) not in self.movimentos_realizados:
                        return Ataque(i, j)
                    if estado_atual_oponente[i][j].status == StatusTab.NAVIO_ENCONTRADO.value and (i, j) not in self.movimentos_realizados:
                        print(f"acertou {estado_atual_oponente[i][j]}")
            else:
                for j in range(0, TABULEIRO_TAMANHO, 2):
                    if estado_atual_oponente[i][j].status == StatusTab.DESCONHECIDO.value and (i, j) not in self.movimentos_realizados:
                        return Ataque(i, j)
                    if estado_atual_oponente[i][j].status == StatusTab.NAVIO_ENCONTRADO.value and (i, j) not in self.movimentos_realizados:
                        print(f"acertou {estado_atual_oponente[i][j]}")
        


            

    def _area_livre(self, x, y, matriz_auxiliar, desocupado):
        for xi, yi in get_adjacentes(x, y):
            if dentro_limite(xi, yi) and matriz_auxiliar[xi][yi] != desocupado:
                return False
        return True
        



    def posicoes_navios(self) -> list[Navio]:
        """Determina as posições dos 5 navios no tabuleiro e retorna uma lista de objetos do tipo Navio.
        
        É preciso determinar as posições de TODOS os 5 navios, ou seja,
        um navio de tamanho 5, um de tamanho 4, dois de tamanho 3 e um de tamanho 2.
        O nome do navio será determinado automaticamente pelo tamanho do navio dentro da classe Navio."""
        
        navios = []
        
        # constante e matriz utilizados somente para auxiliar na definição de posições
        desocupado = 0
        matriz_auxiliar = [[desocupado for _ in range(TABULEIRO_TAMANHO)] for _ in range(TABULEIRO_TAMANHO)]
        
        linhas_disponiveis = []
        if random.randint(0, 1) == 0:
            linhas_disponiveis = [i for i in range(0, TABULEIRO_TAMANHO, 2)]
        else:
            linhas_disponiveis = [i for i in range(1, TABULEIRO_TAMANHO, 2)]
        
        random.shuffle(linhas_disponiveis)

        for tamanho in NAVIOS.values():
            colocado = False
            for linha in linhas_disponiveis:
                colunas_possiveis = list(range(TABULEIRO_TAMANHO - tamanho + 1))
                random.shuffle(colunas_possiveis)
                for col in colunas_possiveis:
                    coords = [(linha, col + i) for i in range(tamanho)]
                    if all(matriz_auxiliar[x][y] == desocupado for x, y in coords) and all(self._area_livre(x, y, matriz_auxiliar, desocupado) for x, y in coords):
                        for x, y in coords:
                            matriz_auxiliar[x][y] = tamanho
                        navios.append(Navio(tamanho, coords))
                        colocado = True
                        break
                if colocado:
                    break
        
        return navios
        
