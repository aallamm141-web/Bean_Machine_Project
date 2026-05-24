Bean Machine (Galton Board) Simulator

A Python-based terminal simulation of the **Galton Board**, demonstrating the **Central Limit Theorem** through a random walk process.

How it Works

1. Input: You specify the number of balls and the number of slots.
2. Simulation: Each ball drops through levels, bouncing **Left** or **Right** with a 50% probability ($p = 0.5$).
3. Visualization: The program prints the path of each ball and generates a vertical histogram using `*` to show the final distribution.

📊 Statistical Concept

This project visualizes how individual random events (ball bounces) collectively form a **Normal Distribution** (Bell Curve). The more balls you drop, the clearer the curve becomes.

<img width="2143" height="3998" alt="image" src="https://github.com/user-attachments/assets/685d60a5-c354-42d9-89c0-d29290ec57d0" />

💻 Usage

Run the script using Python:

```bash
python bean_machine.py

```

1. Enter the number of balls (e.g., `100`).
2. Enter the number of slots (e.g., `10`).
3. Observe the paths and the resulting distribution!

 🛠️ Technologies

Language:Python 3.x
Libraries:`random` (Standard Library)

---
