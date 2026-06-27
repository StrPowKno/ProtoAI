# 🤖 ProtoAI

ProtoAI is a beginner AI project built in Python where an agent navigates a simple 2D grid world to collect a key and reach an exit.

The goal is to learn how AI decision-making works from the ground up using simple logic instead of machine learning libraries.

---

## 🧠 What it does

The AI controls a player in a 10x10 grid:

- Finds the key first
- Then finds the exit
- Avoids walls
- Makes decisions every frame

---

## 🗺️ World

- `@` = Player
- `*` = Key
- `E` = Exit
- `#` = Wall
- `.` = Empty space

---

## ⚙️ How it works

Each frame:

1. The game sends the current state to the AI
2. The AI decides a move (`w`, `a`, `s`, `d`)
3. The game applies the move
4. The world updates

---

## 📁 Structure

```
ProtoAI/
├── main.py
├── game.py
├── ai.py
└── README.md
```

---

## 🚀 Current AI behavior

- Moves toward the key
- Then moves toward the exit
- handles walls intelligently

---

## 🎯 Goals

- [x] Basic AI movement
- [x] Key collection
- [x] Exit system
- [ ] Wall avoidance
- [ ] Pathfinding (A*)
- [ ] Memory system
- [ ] Learning AI

---

## 🧪 Tech

- Python 3
- No external libraries

---

## 📌 Notes

This is a learning project. Expect messy code, experiments, and constant changes.

---

## 📜 License

MIT License
