# Ariadne

## 🕸️ Description
**Ariadne** is an interactive maze visualization and solving toolkit built in Python. It showcases classic and advanced pathfinding algorithms like **DFS**, **BFS**, **A\***, and **Dijkstra**, all visualized with Tkinter.

But Ariadne is more than a mere visualizer - it is a playground for comparing algorithms, a game where you can race against the solver, a database for analyzing solve-time trends, and a full-stack project complete with a **React companion interface**.

## ⟢ Motivation
I'm building Ariadne out of a love for puzzles, mythology and film. I think it's super cool to do homage to the legend of Ariadne, Theseus, and the Minotaur through efficient algorithms. Plus, it is a useful toolkit for maze-solving algorithms. All in all, it combines:
- Computer science fundamentals
- Frontend interface design
- Realtime performance tracking
- SQL-backed persistence

Thus, the mythically-inspired app provides multiple "threads" through complex mazes - visual, algorithmic, and human.

## 🚀 Quick Start
### 1. Clone the Repository
```
git clone https://github.com/josequiceno2000/ariadne.git
cd ariadne
```
### 2. Set Up Environment (Recommended)
```
python3 -m venv env
source env/bin/activate # On Windows: env\Scripts\activate
```

### 3. Install Debendencies
```
pip instal -r requirements.txt
```

### 4. Launch Ariadne
```
python3 -m ariadne
```

## 🛠️ Usage
### Tech Stack
| Layer | Tech |
| --- | --- |
| GUI | Python + Tkinter |
| Core Logic | OOP + Algorithms |
| Data | SQLite |
| Web Companion | React + Node.js |
| Visualization | Tkinter Canvas, Matplotlib |

### Under the Hood
When you launch Ariadne:
1. **Choose Maze Options**
    Select grid size, generation algorithm, and solver.
2. **Watch it Work**
    As the solver runs, see:
    - Color-coded visiten cells
    - True path highlighted
    - Real-time metrics (time, steps)
3. **Control the Maze**
    - Adjust speed of animation
    - Toggle between autoplay and vs mode
4. **Play and Compete**
    - Use arrow keys to navigate
    - Beat the algorithm to the finish
    - Compare results in stats view

## 🤝 Contributing
Ariadne is in active development. I'd love collaborate!
### Setup Instructions:
```
git clone https://github.com/yourusername/ariadne.git # Use your real username
cd ariadne
python3 -m venv env
source env/bin/activate # On Windows: env\Scripts\activate
pip install -r requirements.txt
```
### Ways to Contribute
- Add new algorithms or heuristics
- Optimize animation rendering
- Expand SQLite queries and analytics
- Build out React frontend features
- Help with UI + accessibility
- Suggest new game modes and themes