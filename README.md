# Hysteresis 26-45 Python Projects

Collection of small-to-advanced Python portfolio projects (26–45).

- 27 Autocomplete (Trie)
- 28 File System Simulator
- 29 Maze Generator & Solver
- 30 Mini Search Engine (TF-IDF)
- 31 Social Graph
- 32 Mini Git
- 33 Log Analyzer
- 34 Spell Checker
- 35 Sudoku Solver
- 36 Expression Evaluator
- 37 Task Scheduler
- 38 Memory Allocator
- 39 URL Shortener
- 40 Stock Analyzer
- 41 Distributed Crawler & Search
- 42 Ride Sharing Backend
- 43 Distributed KV Store
- 44 Multiplayer Game Engine
- 45 K8s-like Scheduler Sim

Run examples: `python <project>/main.py` for foldered projects, or `python 27_autocomplete.py` etc.

## Run commands & sample outputs
- `python 27_autocomplete.py` ? `['python', 'pytorch', 'pycharm', 'pyramid', 'py']`
- `python 28_fs_sim.py` ? `['file.txt']` then `hello`
- `python 29_maze.py` ? `Path length: 85`
- `python 30_mini_search.py` ? `[(1, -0.8109...), (2, -0.8109...)]`
- `python 31_social_graph.py` ? `Recommend for Alice: ['Charlie']` / `Path Alice->Charlie: [...]`
- `python 32_mini_git.py` ? commits list then `Index after checkout: {'README.md': 'hello'}`
- `python 33_log_analyzer.py` ? `([('127.0.0.1', 2), ('10.0.0.2', 1)], [('200', 1), ('401', 1), ('404', 1)])`
- `python 34_spell_checker.py` ? `python`
- `python 35_sudoku.py` ? solved grid printed
- `python 36_expr_eval.py` ? `16.0`
- `python 37_scheduler.py` ? `hello`
- `python 38_allocator.py` ? `[(0, 100, True)]`
- `python 39_url_shortener.py` ? e.g., `KrthEZ -> https://example.com`
- `python 40_stock_analyzer.py` ? SMA/EMA arrays and `Trend: up`
- `python -m 41_crawler.main` ? `Search 'example': [...]`
- `python -m 42_rideshare.main` ? ride lifecycle events, `Fare: 20.93`
- `DEMO_DURATION=1 python -m 44_game_engine.main` ? room creation lines, `Rooms: ['room-1', 'room-2']`
- `python -m 45_k8s_sim.main` ? node states, e.g., `node-1 alive pods [...]`
