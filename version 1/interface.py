import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graph import * 

def CreateGraph_1():
    G = Graph()
    AddNode(G, Node("A", 1, 20))
    AddNode(G, Node("B", 8, 17))
    AddNode(G, Node("C", 15, 20))
    AddNode(G, Node("D", 18, 15))
    AddNode(G, Node("E", 2, 4))
    AddNode(G, Node("F", 6, 5))
    AddNode(G, Node("G", 12, 12))
    AddNode(G, Node("H", 10, 3))
    AddNode(G, Node("I", 19, 1))
    AddNode(G, Node("J", 13, 5))
    AddNode(G, Node("K", 3, 15))
    AddNode(G, Node("L", 4, 10))
    AddSegment(G, "AB", "A", "B")
    AddSegment(G, "AE", "A", "E")
    AddSegment(G, "AK", "A", "K")
    AddSegment(G, "BA", "B", "A")
    AddSegment(G, "BC", "B", "C")
    AddSegment(G, "BF", "B", "F")
    AddSegment(G, "BK", "B", "K")
    AddSegment(G, "BG", "B", "G")
    AddSegment(G, "CD", "C", "D")
    AddSegment(G, "CG", "C", "G")
    AddSegment(G, "DG", "D", "G")
    AddSegment(G, "DH", "D", "H")
    AddSegment(G, "DI", "D", "I")
    AddSegment(G, "EF", "E", "F")
    AddSegment(G, "FL", "F", "L")
    AddSegment(G, "GB", "G", "B")
    AddSegment(G, "GF", "G", "F")
    AddSegment(G, "GH", "G", "H")
    AddSegment(G, "ID", "I", "D")
    AddSegment(G, "IJ", "I", "J")
    AddSegment(G, "JI", "J", "I")
    AddSegment(G, "KA", "K", "A")
    AddSegment(G, "KL", "K", "L")
    AddSegment(G, "LK", "L", "K")
    AddSegment(G, "LF", "L", "F")
    return G

window = tk.Tk()
window.title("Graph Viewer")

button_frame = tk.Frame(window)
button_frame.pack(side="top", fill="x", pady=10)

graph_frame = tk.Frame(window)
graph_frame.pack(side="top", fill="both", expand=True)

selected_node = None

def esconder():
    for widget in graph_frame.winfo_children():
        widget.destroy()

def on_click(event, g):
    global selected_node
    x, y = event.xdata, event.ydata
    if x is None or y is None:
        return

    closest_node = GetClosest(g, x, y)
    if closest_node:
        selected_node = closest_node
        messagebox.showinfo("Nodo Seleccionado", f"Has seleccionado el nodo: {selected_node.name}")
    else:
        messagebox.showwarning("Advertencia", "No se ha seleccionado un nodo válido.")

def show_neighbors():
    if not selected_node:
        messagebox.showwarning("Advertencia", "No se ha seleccionado un nodo.")
        return

    neighbors = selected_node.neighbors
    new_graph = Graph()
    AddNode(new_graph, selected_node)
    for neighbor in neighbors:
        AddNode(new_graph, neighbor)
        AddSegment(new_graph, f"{selected_node.name}{neighbor.name}", selected_node.name, neighbor.name)

    esconder() 
    fig, ax = plt.subplots(figsize=(5, 5))
    Plot(new_graph)
    ax.set_title(f"Vecinos de {selected_node.name}")

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.get_tk_widget().pack(fill="both", expand=True)
    canvas.draw()

def show_graph():
    esconder() 
    G = CreateGraph_1()
    fig, ax = plt.subplots(figsize=(5, 5))
    Plot(G)
    ax.set_title("Gráfico de Ejemplo")

    fig.canvas.mpl_connect('button_press_event', lambda event: on_click(event, G))

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.get_tk_widget().pack(fill="both", expand=True)
    canvas.draw()

def load_graph():
    esconder()
    D = Data('datos.txt')
    fig, ax = plt.subplots(figsize=(5, 5))
    Plot(D)
    ax.set_title("Gráfico Inventado")

    fig.canvas.mpl_connect('button_press_event', lambda event: on_click(event, D))

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.get_tk_widget().pack(fill="both", expand=True)
    canvas.draw()

def file_graph():
    esconder()  
    filename = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    F = Data(filename)
    fig, ax = plt.subplots(figsize=(5, 5))
    Plot(F)
    ax.set_title("Gráfico Cargado")

    fig.canvas.mpl_connect('button_press_event', lambda event: on_click(event, F))

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.get_tk_widget().pack(fill="both", expand=True)
    canvas.draw()

btn_show_graph = tk.Button(button_frame, text="Gráfico Ejemplo", command=show_graph)
btn_show_graph.pack(side="left", padx=5)

btn_load_graph = tk.Button(button_frame, text="Gráfico Inventado", command=load_graph)
btn_load_graph.pack(side="left", padx=5)

btn_file_graph = tk.Button(button_frame, text="Gráfico Cargado", command=file_graph)
btn_file_graph.pack(side="left", padx=5)

btn_show_neighbors = tk.Button(button_frame, text="Mostrar vecinos", command=show_neighbors)
btn_show_neighbors.pack(side="left", padx=5)

window.mainloop()
