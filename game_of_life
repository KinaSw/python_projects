import curses
import random

def initialize_grid(height, width):
    """
    Tworzy losową planszę do gry.
    Zwraca: lista 2D (tablica) zawierająca 0 i 1, gdzie 1 oznacza żywą komórkę.
    """
    return [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]


def count_neighbors(grid, x, y):
    """
    Zlicza liczbę żywych sąsiadów dla komórki (x, y).
    Zwraca: liczba całkowita - ilość żywych sąsiadów.
    """
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for offset_x, offset_y in neighbors:
        neighbor_r, neighbor_c = x + offset_x, y + offset_y
        if 0 <= neighbor_r < len(grid) and 0 <= neighbor_c < len(grid[0]):
            count += grid[neighbor_r][neighbor_c]
    return count


def compute_next_generation(grid):
    """
    Oblicza następną generację komórek zgodnie z regułami Gry w Życie.
    Zwraca: nową tablicę 2D z kolejną generacją komórek.
    """
    new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            neighbors_count = count_neighbors(grid, x, y)
            if grid[x][y] == 1:
                new_grid[x][y] = 1 if neighbors_count in [2, 3] else 0
            else:
                new_grid[x][y] = 1 if neighbors_count == 3 else 0

    return new_grid


def draw_grid(stdscr, grid):
    """
    Wyświetla siatkę komórek na ekranie terminala.
    """
    stdscr.clear()
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            stdscr.addch(y, x, "#" if cell else " ")
    stdscr.refresh()


def game_loop(stdscr):
    """
    Główna pętla gry obsługująca wyświetlanie i aktualizację stanu planszy.
    Użytkownik może przechodzić do kolejnych generacji naciskając dowolny klawisz.
    Naciśnięcie 'q' kończy działanie programu.
    """
    # Ukrywa kursor, aby poprawić wygląd symulacji
    curses.curs_set(0)
    # Program czeka na wejście użytkownika
    stdscr.nodelay(False)
    stdscr.clear()

    # Pobranie rozmiaru terminala i dostosowanie planszy do jego wielkości
    height, width = stdscr.getmaxyx()
    # Uniknięcie problemów z krawędziami
    height, width = height - 1, width - 1
    grid = initialize_grid(height, width)

    while True:
        # Rysowanie aktualnej generacji planszy
        draw_grid(stdscr, grid)
        # Oczekiwanie na naciśnięcie klawisza
        key = stdscr.getch()

        if key == ord('q'):
            # Wyjście z programu po naciśnięciu 'q'
            break
        # Aktualizacja stanu gry zgodnie z zasadami
        grid = compute_next_generation(grid)


if __name__ == "__main__":
    # Uruchomienie pętli gry w trybie curses
    curses.wrapper(game_loop)
