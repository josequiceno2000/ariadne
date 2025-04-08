import pytest
from unittest.mock import patch, MagicMock, Mock
from ariadne.ui.app import Point, Line, Window, Cell


# Testing Window
@patch("ariadne.ui.maze_canvas.Tk")
@patch("ariadne.ui.maze_canvas.Canvas")
def test_window_initializes_canvas(mock_canvas, mock_tk):
    mock_root = MagicMock()
    mock_canvas_instance = MagicMock()

    mock_tk.return_value = mock_root
    mock_canvas.return_value = mock_canvas_instance

    window = Window(800, 600)

    mock_tk.assert_called_once()
    mock_canvas.assert_called_once_with(mock_root, width=800, height=600)
    mock_canvas_instance.pack.assert_called_once()
    mock_root.protocol.assert_called_once_with("WM_DELETE_WINDOW", window.close)

@patch("ariadne.ui.maze_canvas.Tk")
@patch("ariadne.ui.maze_canvas.Canvas")
def test_close_stops_running(mock_canvas, mock_tk):
    window = Window(800, 600)
    assert not window._Window__running

    window.__running = True
    window.close()
    assert not window._Window__running

@patch("ariadne.ui.maze_canvas.Tk")
@patch("ariadne.ui.maze_canvas.Canvas")
def test_wait_for_close_starts_loop_and_calls_redraw(mock_canvas, mock_tk):
    window = Window(800, 600)
    
    call_count = {"n": 0}
    def fake_redraw():
        call_count["n"] += 1
        window.close()
    
    window.redraw = fake_redraw
    window.wait_for_close()

    assert call_count["n"] == 1

@patch("ariadne.ui.maze_canvas.Canvas")
@patch("ariadne.ui.maze_canvas.Tk")
def test_window_different_sizes(mock_tk, mock_canvas):
    for width, height in [(100, 200), (300, 500), (1200, 800), (640, 300)]:
        Window(width, height)
        mock_canvas.assert_called_with(mock_tk.return_value, width=width, height=height)

# Testing Points and Lines
@pytest.mark.parametrize("x, y", [
    (0, 20),
    (90, 180),
    (240, 322),
    (15, 15),
    (300, 460)
]) 
def test_point_initialization(x, y):
    p = Point(x, y) 
    assert p.x == x
    assert p.y == y


@pytest.mark.parametrize("x1, y1, x2, y2", [
    (19, 24, 200, 300),
    (190, 240, 20, 30),
    (70, 400, 400, 70),
    (20, 21, 301, 250),
    (5, 190, 43, 50),
])
def test_line_draw_calls_create_line_correctly(x1, y1, x2, y2):
    canvas = Mock()
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    line = Line(p1, p2)

    line.draw(canvas, fill_color="red")

    canvas.create_line.assert_called_once_with(
        x1, y1, x2, y2,
        fill = "red",
        width = 2
    )

@patch("ariadne.ui.maze_canvas.Canvas")
@patch("ariadne.ui.maze_canvas.Tk")
def test_window_draw_line_delegates_to_line_draw(mock_tk, mock_canvas):
    mock_canvas_instance = mock_canvas.return_value

    mock_line = MagicMock()

    window = Window(800, 600)
    window.draw_line(mock_line, fill_color="blue")

    mock_line.draw.assert_called_once_with(mock_canvas_instance, "blue")

# Testing Cells
@pytest.fixture
@patch("ariadne.ui.maze_canvas.Canvas")
@patch("ariadne.ui.maze_canvas.Tk")
def mock_window(mock_tk, mock_canvas):
    window = Window(500, 500)
    window.draw_line = Mock()

    canvas_mock = window._Window__canvas
    canvas_mock.winfo_width.return_value = 500
    canvas_mock.winfo_height.return_value = 500

    return window

@pytest.mark.parametrize("x1, y1, x2, y2", [
    (100, 100, 300, 250),
    (250, 80, 90, 100),
    (60, 22, 22, 65),
    (141, 142, 25, 490),
    (50, 32, 35, 60),
    (250, 80, 300, 10),
])
def test_cell_draws_four_walls(x1, y1, x2, y2, mock_window):
    cell = Cell(x1, y1, x2, y2, mock_window)
    cell.draw("blue")

    assert mock_window.draw_line.call_count == 4


@pytest.mark.parametrize("x1, y1, x2, y2", [
    (100, 100, 300, 250),
    (250, 80, 90, 100),
    (60, 22, 22, 65),
    (141, 142, 25, 490),
    (50, 32, 35, 60),
    (250, 80, 300, 10),
])
def test_cell_draws_only_selected_walls(x1, y1, x2, y2, mock_window):
    cell = Cell(x1, y1, x2, y2, mock_window)
    cell.has_top_wall = True
    cell.has_right_wall = False
    cell.has_bottom_wall = True
    cell.has_left_wall = False

    cell.draw("orange")
    assert mock_window.draw_line.call_count == 2

@pytest.mark.parametrize("x1, y1, x2, y2", [
    (50, 100, 300, 250),
    (250, 80, 400, 100),
    (60, 91, 22, 65),
    (141, 142, 25, 89),
    (50, 32, 255, 60),
    (250, 10, 300, 10),
])
def test_cell_draws_with_correct_coordinates(x1, y1, x2, y2, mock_window):
    cell = Cell(x1, y1, x2, y2, mock_window)
    cell.draw("green")

    expected_lines = [
        ((x1, y1), (x2, y1)), # top
        ((x2, y1), (x2, y2)), # right
        ((x2, y2), (x1, y2)), # bottom
        ((x1, y2), (x1, y1)), # left
    ]

    for i, ((px1,py1), (px2, py2)) in enumerate(expected_lines):
        args = mock_window.draw_line.call_args_list[i][0]
        line = args[0]
        assert isinstance(line, Line)
        assert (line.point1.x, line.point1.y) == (px1, py1)
        assert (line.point2.x, line.point2.y) == (px2, py2)

@pytest.mark.parametrize("x1, y1, x2, y2", [
    (1000, 1000, 2050, 2050),
    (-1000, -1000, -2050, -2050),
    (-5, 499, -1, 501),
])
def test_cell_out_of_bounds_does_not_draw(x1, y1, x2, y2, mock_window):
    cell = Cell(x1, y1, x2, y2, mock_window)
    cell.draw("black")
    mock_window.draw_line.assert_not_called()