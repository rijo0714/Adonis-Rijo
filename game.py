import random

class ScrabbleDeBloques:
    def __init__(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.letter_points = {
            'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1,
            'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
            'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1,
            'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
            'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4,
            'Z': 10
        }
        self.players = []
        self.current_player_index = 0

    def add_player(self, name):
        player = {
            'name': name,
            'score': 0,
            'tiles': self.generate_tiles(7)  # Cada jugador comienza con 7 fichas
        }
        self.players.append(player)
    
    def generate_tiles(self, count):
        return random.choices(list(self.letter_points.keys()), k=count)

    def display_board(self):
        for row in self.board:
            print(' '.join(row))
    
    def display_player_tiles(self, player):
        print(f"{player['name']}'s tiles: {', '.join(player['tiles'])}")
    
    def place_word(self, player, word, row, col, direction):
        # Verificar que las letras estén en las fichas del jugador
        if not all(letter in player['tiles'] for letter in word):
            print("Letra no disponible en las fichas del jugador.")
            return False
        
        # Colocar la palabra en el tablero
        if direction == 'H':
            if col + len(word) > 15:
                print("La palabra se sale del tablero.")
                return False
            for i in range(len(word)):
                self.board[row][col + i] = word[i]
                player['tiles'].remove(word[i])
        elif direction == 'V':
            if row + len(word) > 15:
                print("La palabra se sale del tablero.")
                return False
            for i in range(len(word)):
                self.board[row + i][col] = word[i]
                player['tiles'].remove(word[i])
        else:
            print("Dirección inválida.")
            return False
        
        # Calcular y actualizar la puntuación del jugador
        score = sum(self.letter_points[letter] for letter in word)
        player['score'] += score
        player['tiles'].extend(self.generate_tiles(len(word)))  # Reemplazar fichas usadas
        return True

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.display_board()
        self.display_player_tiles(player)
        word = input(f"{player['name']}, ingresa la palabra a colocar: ").upper()
        row = int(input("Ingresa la fila (0-14): "))
        col = int(input("Ingresa la columna (0-14): "))
        direction = input("Ingresa la dirección (H/V): ").upper()
        
        if self.place_word(player, word, row, col, direction):
            print(f"{player['name']} ha colocado la palabra {word}.")
        else:
            print(f"{player['name']} no ha podido colocar la palabra {word}.")
        
        # Cambiar al siguiente jugador
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
    
    def display_scores(self):
        for player in self.players:
            print(f"{player['name']} tiene {player['score']} puntos.")
    
    def start_game(self):
        while True:
            self.play_turn()
            self.display_scores()
            cont = input("¿Continuar el juego? (s/n): ").lower()
            if cont != 's':
                break

if __name__ == "__main__":
    game = ScrabbleDeBloques()
    game.add_player("Jugador 1")
    game.add_player("Jugador 2")
    game.add_player("Jugador 3")
    game.add_player("Jugador 4")
    game.add_player("Jugador 5")
    game.start_game()
