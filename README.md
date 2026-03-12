# 🚀 Hysteresis 26–45 Python Projects

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Projects](https://img.shields.io/badge/Projects-19-success)
![Algorithms](https://img.shields.io/badge/Algorithms-Data%20Structures-orange)
![Distributed Systems](https://img.shields.io/badge/Systems-Distributed-purple)
![License](https://img.shields.io/badge/License-Open%20Source-green)

A curated collection of **Python system design and algorithm projects** ranging from:

* Data Structures
* Search Engines
* Distributed Systems
* Backend Simulation
* Game Engines
* Kubernetes Scheduler Simulation

All projects are **standalone**, lightweight, and require **no external dependencies**.

---

# 📚 Project Catalog

| ID | Project                      | Category              |
| -- | ---------------------------- | --------------------- |
| 27 | Autocomplete (Trie)          | Data Structures       |
| 28 | File System Simulator        | System Design         |
| 29 | Maze Generator & Solver      | Algorithms            |
| 30 | Mini Search Engine (TF-IDF)  | Information Retrieval |
| 31 | Social Graph                 | Graph Algorithms      |
| 32 | Mini Git                     | Version Control       |
| 33 | Log Analyzer                 | Data Processing       |
| 34 | Spell Checker                | NLP                   |
| 35 | Sudoku Solver                | Backtracking          |
| 36 | Expression Evaluator         | Parsing               |
| 37 | Task Scheduler               | OS Concepts           |
| 38 | Memory Allocator             | Operating Systems     |
| 39 | URL Shortener                | Backend Design        |
| 40 | Stock Analyzer               | Data Analysis         |
| 41 | Distributed Crawler & Search | Distributed Systems   |
| 42 | Ride Sharing Backend         | System Design         |
| 43 | Distributed KV Store         | Databases             |
| 44 | Multiplayer Game Engine      | Networking            |
| 45 | Kubernetes-like Scheduler    | Cloud Systems         |

---

# 🗂 Project Folder Structure

```
python-projects/
│
├── 27_autocomplete.py
├── 28_filesystem.py
├── 29_maze.py
├── 30_search_engine.py
├── 31_social_graph.py
├── 32_mini_git.py
├── 33_log_analyzer.py
├── 34_spell_checker.py
├── 35_sudoku_solver.py
├── 36_expression_eval.py
├── 37_task_scheduler.py
├── 38_memory_allocator.py
├── 39_url_shortener.py
├── 40_stock_analyzer.py
│
├── 41_crawler/
│   ├── main.py
│   ├── crawler.py
│   ├── index.py
│   └── seeds.py
│
├── 42_rideshare/
│   ├── main.py
│   ├── models.py
│   └── service.py
│
├── 43_kv_store/
│   ├── server.py
│   ├── client.py
│   └── storage.py
│
├── 44_game_engine/
│   ├── main.py
│   ├── rooms.py
│   └── player.py
│
└── 45_scheduler/
    ├── main.py
    ├── node.py
    └── pod.py
```

---

# ⚙️ How to Run

### Single-file projects

```
python 27_autocomplete.py
python 28_filesystem.py
python 35_sudoku_solver.py
```

---

### Folder-based projects

```
python -m 41_crawler.main
python -m 42_rideshare.main
python -m 44_game_engine.main
```

---

# 🧠 System Architecture Overview

## Distributed Crawler & Search Engine (Project 41)

```
          +-------------+
          |  Seed URLs  |
          +------+------+
                 |
                 v
           +-----+------+
           |  Crawler   |
           +-----+------+
                 |
                 v
           +-----+------+
           | HTML Parser|
           +-----+------+
                 |
                 v
           +-----+------+
           |  Indexer   |
           +-----+------+
                 |
                 v
           +-----+------+
           | Search API |
           +------------+
```

**Workflow**

1. Seed URLs start the crawl
2. Pages are fetched
3. Links are extracted
4. Text content is indexed
5. Queries return ranked results

---

## Distributed Key-Value Store (Project 43)

```
          +-----------+
Client -->|  Server   |
          +-----+-----+
                |
                v
          +-----+-----+
          | In-Memory |
          |  Storage  |
          +-----------+
```

Supports operations:

* SET key value
* GET key
* DELETE key
* TTL expiration
* Pub/Sub messaging

---

## Kubernetes-like Scheduler (Project 45)

```
           +----------+
           |  Pods    |
           +----+-----+
                |
                v
          +-----+-----+
          | Scheduler |
          +-----+-----+
                |
      +---------+----------+
      |         |          |
   Node-1    Node-2     Node-3
```

Scheduler assigns pods to nodes based on:

* CPU capacity
* Memory availability
* Node load balancing

---

# 📊 Example Outputs

### Autocomplete

```
['python', 'pytorch', 'pycharm', 'pyramid', 'py']
```

---

### Maze Solver

```
Path length: 85
```

---

### URL Shortener

```
KrthEZ -> https://example.com
```

---

### Distributed Crawler

```
Mini search ready. Type a query (or 'exit').

> link.springer.com
1. https://link.springer.com (score=6.000)
2. https://www.springer.com (score=4.000)
```

---

Distributed Crawler & Search (Project 41)

Run:

python -m 41_crawler.main

Output:

Mini search ready. Type a query (or 'exit').

> link.springer.com
1. https://link.springer.com (score=6.000)
2. https://www.springer.com (score=4.000)
3. https://gemini.google.com (score=2.000)
4. https://www.anthropic.com (score=2.000)
5. https://platform.openai.com (score=2.000)

> mits.ac.in
1. https://nptel.ac.in (score=4.000)
🚖 Ride Sharing Backend (Project 42)
Ride requested
Driver assigned
Ride started
Ride completed
Fare: 20.93
🎮 Multiplayer Game Engine (Project 44)
Rooms: ['room-1', 'room-2']
☸ Kubernetes-like Scheduler Simulator (Project 45)
Node-1 -> Pod A
Node-2 -> Pod B
Node-3 -> Pod C
🎯 Learning Goals

These projects demonstrate:

Data Structures

Algorithms

Backend Architecture

Distributed Systems

Search Engine Design

Graph Algorithms

Cloud Scheduling Concepts

---

# Recent Run Outputs (Mar 12, 2026)

### Ride Sharing Backend (Project 42)

Command:

```
python -m 42_rideshare.main
```

Output:

```
[driver_assigned] {'ride_id': 'f9b20506', 'passenger_id': 'p1', 'driver_id': 'd1', 'pickup': (12.91, 77.6), 'dropoff': (12.95, 77.64), 'status': 'driver_assigned', 'requested_at': 1773289301.082239, 'started_at': None, 'ended_at': None, 'fare': None}
[ride_started] {'ride_id': 'f9b20506', 'passenger_id': 'p1', 'driver_id': 'd1', 'pickup': (12.91, 77.6), 'dropoff': (12.95, 77.64), 'status': 'in_progress', 'requested_at': 1773289301.082239, 'started_at': None, 'ended_at': None, 'fare': None}
[ride_completed] {'ride_id': 'f9b20506', 'passenger_id': 'p1', 'driver_id': 'd1', 'pickup': (12.91, 77.6), 'dropoff': (12.95, 77.64), 'status': 'completed', 'requested_at': 1773289301.082239, 'started_at': None, 'ended_at': None, 'fare': 20.93}
Fare: 20.93
```

### Distributed KV Store (Project 43)

Command:

```
C:\\Users\\abhis\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe -m 43_kv_store.main
```

Output:

```
Hash ring node for 'user:1': nodeC
b'OK\n'
b'bar\n'
```

### Kubernetes-like Scheduler (Project 45)

Command:

```
C:\\Users\\abhis\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe -m 45_k8s_sim.main
```

Output:

```
node-0 dead pods []
node-1 alive pods ['pod-6', 'pod-7', 'pod-4', 'pod-9', 'pod-1', 'pod-3']
node-2 alive pods ['pod-2', 'pod-8', 'pod-5', 'pod-0']
```

⚙ Requirements

Python 3.8+

Check version:

python --version
⭐ Purpose

This repository acts as a Python backend & system design portfolio containing 19 practical projects covering core software engineering concepts.
