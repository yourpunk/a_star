# 🧠 A* Pathfinding in BlockWorld

Welcome to a symbolic chaos engine disguised as a search problem.  
This project implements an optimized **A\*** pathfinder for a block-stacking environment where state explosion is a feature, not a bug.

I built this to test how clean logic and strong heuristics can crush exponential search spaces — without sacrificing transparency or control.

---

## 💡 Core Idea

BlockWorld is a planning sandbox: multiple stacks of blocks, a defined goal, and simple rules that combine into complex outcomes.  
The goal: reach the target state in as few moves as possible.

This implementation uses:
- ✅ Custom state representation optimized for hashing and mutation
- ✅ A* algorithm with a minimalistic, priority-driven control loop
- ✅ Heuristic tailored for symbolic displacement and stack depth
- ✅ Logging and config hooks for behavior tracing

---

## ⚙️ How It Works

Each move (stack, unstack, move-to-table) modifies the world state.  
The heuristic estimates the cost to goal by analyzing:
- Block misplacements
- Stack fragmentation
- Depth penalties

That’s all wrapped in a fast, `heapq`-based A* loop that avoids redundant paths and terminates early when optimality is reached.

---

## 📁 Structure

```bash
blockworld_astar/
├── star.py         # A* search + heuristic (my domain logic lives here)
├── blockworld.py   # Environment simulator
├── eval.py         # Launcher and testing setup
├── problems/       # Configurable input sets
└── README.md       # You're looking at it
```

---

## ▶️ Running the Search
```bash
python eval.py
```
You’ll see step count, explored states, and final result.
Tweak `eval.py` or drop new configs into `problems/` to test edge cases.

---

## 🔬 Example Output

```bash
Goal reached in 12 moves.
States explored: 34
Search time: 0.016s
```

---

## 🧠 Why It Matters

Most people treat A* like a black box — plug in a heuristic and hope it works.
I wanted full control. I built this to:
- Understand symbolic search beyond toy grids
- Design a heuristic that reflects structural displacement
- Keep the implementation readable, traceable, and debuggable
If you're used to hardcoding rules, this might feel surgical. That’s the point.

---

## 🧰 Tech Stack

- **Language**: Python 3
- **Core Tools**: heapq, sets, custom OOP models
- **Paradigms**: AI planning, search optimization, symbolic modeling
- **Add-ons**: Optional debug output for state tree tracing

---

## 📜 License

MIT. Fork it, dissect it, rewrite it — just don’t turn it in as homework.

---

## 👤 Author
🦾 Crafted by Aleksandra Kenig (aka [yourpunk](https://github.com/yourpunk)) — game developer, systems thinker, and fan of algorithms that don’t lie.

### Wanna collab or argue about heuristics? Hit me up.
