🚀 What You Will See
When you execute the viewer, you are witnessing a real-time reconstruction of a quantum-gravitational dataset. The simulation features:

The Trisolaris System: Real-time tracking of the stars Alpha, Beta, and Proxima, along with the stable orbit of the Trisolaris Planet.

Hilbert vs. SPHY: A toggleable state where you can observe the transition from erratic, chaotic oscillation to a perfect, phasic geometric lock (SPHY Sync).

Gravitational Grid: A visual representation of the SPHY field intensity, showing how space-time "stiffens" to support stable orbits.

Dynamic Trails: High-fidelity vertex traces that map the historical path of each celestial body, proving the lack of orbital decay.

🛠 Features & Controls
Maximization: Press F to toggle Fullscreen/Maximized window mode.

3D Navigation: * Right Click + Drag: Rotate the camera around the system center.

Mouse Scroll: Zoom in/out to inspect local planetary orbits or the entire stellar cluster.

HUD: Real-time telemetry display showing the current Frame, Sync Status, and navigation instructions.

📊 Dataset Requirement
The viewer is designed to read processed telemetry directly from a high-performance Parquet file.

Filename: trisolaris_sphy_data.parquet

Format: Compressed columnar storage for high-speed frame seeking.

💻 Technical Stack
Language: Python 3

Graphics Engine: py5 (Processing for Python)

Data Handling: pandas / numpy / pyarrow

Architecture: Harpia Quantum Deeptech - SPHY Engine v29

⚖️ Ethics and Justice
"We either seek Truth and Justice—immediate abundance and the end of scarcity—or we allow the soul of humanity to be bought by the illusions of control. This code is the first step toward a harmonic reality." — Deywe Okabe

How to Run
Ensure you have generated the dataset using the SPHY Generator script.

Install dependencies: pip install py5 pandas numpy pyarrow

Run the viewer:

Bash
python3 3_body_parquet_viewer.py
