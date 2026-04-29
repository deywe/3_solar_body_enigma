import py5
import pandas as pd
import numpy as np

# --- VARIÁVEIS DE NAVEGAÇÃO ---
df = None
cam_dist = 1500
cam_lat = py5.PI/3.5
cam_lon = 0
current_frame = 0

# Armazenamento de rastros para reconstrução visual
trails = {
    "Alfa": [], "Beta": [], "Proxima": [], "Planet": []
}
TRAIL_MAX = 100 # Comprimento do rastro visível

def setup():
    global df
    py5.size(1280, 720, py5.P3D)
    py5.window_resizable(True)
    py5.color_mode(py5.HSB, 255)
    
    try:
        df = pd.read_parquet("trisolaris_sphy_data.parquet")
        print(f"✅ Visualizador carregado: {len(df)} frames disponíveis.")
    except:
        print("❌ Arquivo Parquet não encontrado. Rode o gerador primeiro!")
        py5.exit_sketch()

def draw():
    global current_frame, cam_dist, cam_lat, cam_lon
    if df is None: return
    
    py5.background(5)
    
    # --- CÂMERA E INTERAÇÃO ---
    py5.translate(py5.width/2, py5.height/2, -cam_dist)
    py5.rotate_x(cam_lat)
    py5.rotate_z(cam_lon)
    
    # Leitura do Frame Atual
    row = df.iloc[current_frame]
    sync_mode = row['is_syncing']
    
    # Grid SPHY
    draw_grid(1.0 if sync_mode else 0.0)
    
    # --- RENDERIZAÇÃO DE NODOS ---
    names = [("Alfa", 30), ("Beta", 15), ("Proxima", 160), ("Planet", 140)]
    
    for name, hue in names:
        # Coordenadas do Parquet
        pos = np.array([row[f"{name}_x"], row[f"{name}_y"], row[f"{name}_z"]])
        
        # Gerenciar Rastro (Trail)
        trail_list = trails[name]
        trail_list.append(pos)
        if len(trail_list) > TRAIL_MAX: trail_list.pop(0)
        
        # Desenhar Rastro
        py5.no_fill()
        py5.stroke(hue, 150, 255, 120)
        py5.begin_shape()
        for p in trail_list:
            py5.vertex(p[0], p[1], p[2])
        py5.end_shape()
        
        # Desenhar Corpo
        py5.push_matrix()
        py5.translate(pos[0], pos[1], pos[2])
        py5.no_stroke()
        py5.fill(hue, 120, 255, 200)
        size = 35 if name != "Planet" else 12
        py5.sphere(size)
        if name != "Planet": # Glow das estrelas
            py5.fill(hue, 80, 255, 40)
            py5.sphere(size * 1.6)
        py5.pop_matrix()

    draw_hud(sync_mode, current_frame)
    
    # Avanço de Frame
    current_frame = (current_frame + 1) % len(df)

def draw_grid(sync):
    py5.no_fill()
    py5.stroke(140, 100, 255, 15 + (sync * 25))
    for i in range(1, 5):
        py5.ellipse(0, 0, i*300, i*300)

def draw_hud(sync, f):
    py5.hint(py5.DISABLE_DEPTH_TEST)
    py5.camera() # Reseta para 2D
    py5.fill(255)
    mode = "ON (SPHY HARMONY)" if sync else "OFF (HILBERT CHAOS)"
    py5.text(f"TRISOLARIS REPLAY | FRAME: {f} | SYNC: {mode}", 30, 40)
    py5.text("F: MAXIMIZAR | MOUSE DIR: ROTACIONAR | SCROLL: ZOOM", 30, 60)
    py5.hint(py5.ENABLE_DEPTH_TEST)

# --- CONTROLES ---

def mouse_wheel(event):
    global cam_dist
    cam_dist += event.get_count() * 70
    cam_dist = py5.constrain(cam_dist, 200, 8000)

def mouse_dragged():
    global cam_lat, cam_lon
    if py5.mouse_button == py5.RIGHT:
        cam_lon += (py5.mouse_x - py5.pmouse_x) * 0.01
        cam_lat -= (py5.mouse_y - py5.pmouse_y) * 0.01
        cam_lat = py5.constrain(cam_lat, 0.05, py5.HALF_PI * 0.95)

def key_pressed():
    if py5.key.lower() == 'f':
        # Maximizar/Tela Cheia
        py5.set_full_screen(not py5.is_full_screen())

if __name__ == "__main__":
    py5.run_sketch()
