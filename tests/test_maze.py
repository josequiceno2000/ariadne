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

@patch("ariadne.core.maze.time.sleep", return_value=None)
@patch("ariadne.core.maze.Cell")
def test_maze_draw_calls_cell_draw_and_animate(mock_cell, mock_sleep):
    mock_window = MagicMock()
    mock_cell_instance = MagicMock()
    mock_cell.return_value = mock_cell_instance

    Maze(0, 0, 2, 2, 15, 30, mock_window)

    assert mock_cell_instance.draw.call_count == 4
    assert mock_window.redraw.call_count == 4
    assert mock_sleep.call_count == 4

@patch("ariadne.core.maze.Cell")
def test_maze_cells_have_correct_coordinates(mock_cell):
    mock_window = MagicMock()
    cell_size_x = 10
    cell_size_y = 10

    Maze(0, 0, 2, 2, cell_size_x, cell_size_y, mock_window)

    expected_calls = [
        call(0, 0, 10, 10, mock_window),
        call(0, 10, 10, 20, mock_window),
        call(10, 0, 20, 10, mock_window),
        call(10, 10, 20, 20, mock_window)
    ]

    mock_cell.assert_has_calls(expected_calls, any_order=False)