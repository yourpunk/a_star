# 🧠 A* Pathfinding on BlockWorld
### Overview
This project is a *Python* implementation of the A* pathfinding algorithm applied to a simplified **"BlockWorld"** environment — a classic AI planning problem. It was developed as a school assignment and is now showcased as a learning pet project. My primary contribution lies in the implementation of the core logic ``(student.py)`` including the heuristic function and the A* search loop.

## 🧩 Features
- Custom state representation of block stacks.
- A* search algorithm with priority queue (min-heap).
- Heuristic based on the number of misplaced blocks and their positions.
- Easily extendable design using object-oriented principles.

## 📁 Files
```graphql
├── blockworld.py     # base environment class (provided)
├── student.py        # main logic for A* search and heuristic (my part 🩷)
├── eval.py           # basic script to test your implementation (provided)
├── problems/         # sample problem definitions and scenarios (provided)
└── README.md         # Project overview
```
## 🚀 Getting Started
To test the A* search algorithm, run:
```bash
python eval.py
```
> You can tweak the parameters inside ``eval.py`` to test different block configurations.

## 💡 What I’ve Learned
- How to implement A* algorithm from scratch.
- Designing state-based heuristics.
- Working with priority queues in Python (heapq).
- Debugging search algorithms and managing tree/graph exploration.

## 👤 Author
🚀 Created by Aleksandra Kenig (aka [yourpunk](https://github.com/yourpunk)).


💌 Wanna collab or throw some feedback? You know where to find me.
