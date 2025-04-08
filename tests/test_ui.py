import pytest
from unittest.mock import patch, MagicMock
from ariadne.ui.app import Window

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