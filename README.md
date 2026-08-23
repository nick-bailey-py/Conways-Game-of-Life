# Conways-Game-of-Life

Each cell is either alive (yellow) or dead (purple) and interacts with its eight surrounding neighbors

Underpopulation: Any live cell with < 2 live neighbors dies.\

Survival: Any live cell with 2-3 live neighbors stays alive.
Overpopulation: Any live cell with > 3 live neighbors dies.
Reproduction: Any dead cell with exactly 3 live neighbors becomes a live cell.

To run, use "./run"
spatial_interaction_model.py produces the simulation (.png files) - adjust initial seed, boundary conditions, etc here
mov.py strings the .png frames into an .mp4 - adjust fps here
