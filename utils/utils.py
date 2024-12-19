directions_plus = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up  # right  # down  # left
directions_square = [
    (-1, -1),  # Top-left
    (-1, 0),  # Top
    (-1, 1),  # Top-right
    (0, -1),  # Left
    (0, 1),  # Right
    (1, -1),  # Bottom-left
    (1, 0),  # Bottom
    (1, 1),  # Bottom-right
]
directions_corners = [
    (-1, -1),  # Top-left
    (-1, 1),  # Top-right
    (1, -1),  # Bottom-left
    (1, 1),  # Bottom-right
]


def find_first_str_in_matrix(grid: list[list[str]], test):
    for ridx, r in enumerate(grid):
        for cidx, c in enumerate(r):
            if c == test:
                return (ridx, cidx)


# Creates a matrix based on passed in amounts 0 indexed
def create_matrix(rows, cols, char_override="."):
    return [[char_override for _ in range(cols)] for _ in range(rows)]


def pretty_print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))


def flip_dir(dir: tuple[int, int]):
    return (dir[0] * -1, dir[1] * -1)


def string_to_grid(string_grid: str):
    # Split the string into rows
    rows = string_grid.strip().split("\n")

    # Convert each row into a list of values
    grid = [list(row) for row in rows]

    return grid


def in_bounds(maxr: int, maxc: int, coord: tuple[int, int]) -> bool:
    if 0 <= coord[0] < maxr and 0 <= coord[1] < maxc:
        return True
    return False
