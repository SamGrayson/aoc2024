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


def flip_dir(dir: tuple[int, int]):
    return (dir[0] * -1, dir[1] * -1)


def string_to_grid(string_grid: str):
    # Split the string into rows
    rows = string_grid.strip().split("\n")

    # Convert each row into a list of values
    grid = [list(row) for row in rows]

    return grid
