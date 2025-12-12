# 🧠 Intelligent Vacuum Cleaner Agent – Tkinter GUI Simulation

A fully interactive **Intelligent Vacuum Cleaner Agent** implemented in Python with a modern **Tkinter GUI**, real-time animation, start/stop/reset controls, and dynamic environment generation.  
This system simulates how an intelligent agent senses, navigates, and cleans a 2D grid environment using AI-based decision logic.

---

## 🌟 Features

### ✔ Graphical User Interface (Tkinter)
- Animated vacuum agent
- Dynamic red/green cell visualization
- Smooth movement and cleaning transitions
- Clean UI layout with modern styling

### ✔ Intelligent Agent Behavior
- Automatic detection of dirty cells  
- Cleans on arrival (model-based decision making)  
- Snake-pattern traversal ensures full coverage  
- Suitable for AI and robotics coursework

### ✔ User Controls
| Button | Function |
|--------|----------|
| **START** | Runs the simulation |
| **STOP** | Pauses execution immediately |
| **RESET** | Generates a new random grid with random dirty cells |

### ✔ Random Environment Generation
Each reset produces a **brand-new grid**, ensuring variability for demonstration and testing.

---

## 🧩 Problem Statement

Design an intelligent agent capable of:
- Navigating a discrete environment
- Detecting dirty tiles
- Cleaning them autonomously
- Visualizing its behavior through a GUI

This simulation follows the **Intelligent System Design Process**, including:
1. Problem Definition  
2. Environment Modeling  
3. Agent Design  
4. Control Strategy  
5. Simulation Output  

---

## 🏗 System Architecture

```
┌────────────────────────────┐
│   User Interface (GUI)      │
│   - Canvas Grid             │
│   - Start/Stop/Reset        │
└─────────────┬──────────────┘
              │
┌─────────────▼──────────────┐
│   Intelligent Agent         │
│   - Movement Logic          │
│   - Cleaning Behavior       │
│   - State Updates           │
└─────────────┬──────────────┘
              │
┌─────────────▼──────────────┐
│   Environment Model         │
│   - Grid Representation     │
│   - Dirt Placement          │
│   - Status Tracking         │
└────────────────────────────┘
```

---

## 🖼 Screenshots (Optional)

Add your screenshots here:

```
![Initial State](screenshots/initial.png)
![Final State](screenshots/final.png)
```

---

## 🚀 How to Run

### **1. Install Python 3**
Download from https://www.python.org/

### **2. Run the file**
```
python intelligent_vacuum_agent_gui_updated.py
```

No external libraries required.

---

## 📂 File Structure

```
📦 Intelligent-Vacuum-Agent/
 ┣ 📜 intelligent_vacuum_agent_gui_updated.py
 ┗ 📜 README.md
```

---

## 🔍 Agent Control Strategy

1. Agent begins at **(0,0)**  
2. Uses **snake-pattern traversal**:
   - Even rows → left to right  
   - Odd rows → right to left  
3. At each cell:
   - If dirty → **clean immediately**
4. Stops after all cells cleaned  
5. Displays **Final State Diagram**

This ensures **completeness**, **determinism**, and **full grid coverage**.

---

## 🎓 Academic Value

This project is ideal for:
- Artificial Intelligence course submissions  
- B.Tech / B.E final-year demonstrations  
- Intelligent Agent assignments  
- HCI + Robotics coursework  
- AI portfolio projects  

---

## 📌 Future Enhancements

- Heuristic (A*) cleaning path  
- Battery consumption simulation  
- Multiple agents  
- Obstacles in grid  
- Voice-assisted agent feedback  
- Export simulation to GIF / video  

---

## 🧑‍💻 Author

**Deva Harshini**  
B.Tech Computer Science & Engineering  

---

## 📜 License

This project is open-source and available under the **MIT License**.

