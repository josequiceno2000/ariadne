import pytest
from unittest.mock import MagicMock, patch, call
from ariadne.core.maze import Maze

@patch("ariadne.core.maze.Cell")
def test_maze_creates_correct_number_of_cells(mock_cell):
    mock_window = MagicMock()
    num_rows = 5
    num_cols = 13
    cell_size_x = 20
    cell_size_y = 11

    maze = Maze(10, 10, num_rows, num_cols, cell_size_x, cell_size_y, mock_window)

    assert len(maze._cells) == num_cols
    for column in maze._cells:
        assert len(column) == num_rows

    assert mock_cell.call_count == num_cols * num_rows