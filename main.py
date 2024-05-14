from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

def make_tree(string: str):
    G = nx.Graph()
    node = set()

    for _ in string:
        if _.isalpha():
            node.add(_)

    for _ in node:
        G.add_node(_)

    tree_set = dict()
    tree = string.split(";")
    for _ in tree:
        _ = ''.join(_.split())
        parts = _.split(":")
        if len(parts) > 1:
            tree_set[parts[0]] = [i for i in parts[1] if i.isalpha()]

    for node, neighbors in tree_set.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Создаем фигуру Matplotlib
    fig, ax = plt.subplots()

    # Рисуем граф
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=1000, font_size=12, font_weight='bold', ax=ax)

    # Сохраняем изображение в файл
    plt.savefig('graph_image.png')
    plt.close(fig)  # Закрываем фигуру после сохранения, чтобы не использовать память впустую
    return tree_set

def bfs_shortest_path(tree, start, goal):
    # Очередь для хранения путей, которые необходимо исследовать
    queue = deque([[start]])

    # Множество для хранения посещенных узлов
    visited = set()

    while queue:
        # Получаем и удаляем первый путь из очереди
        path = queue.popleft()
        # Получаем последний узел из пути
        node = path[-1]

        # Если узел уже был посещен, пропускаем его
        if node in visited:
            continue

        # Помечаем узел как посещенный
        visited.add(node)

        # Если мы достигли целевого узла, возвращаем путь
        if node == goal:
            return path

        # Добавляем все соседние узлы в очередь
        for neighbor in tree.get(node, []):
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)

    # Если путь не найден, возвращаем пустой список
    return []

def draw_graph_from_list(tree, path, start, goal, filename):
    G = nx.Graph()

    for node in path:
        if node in tree:
            for neighbor in tree[node]:
                if neighbor in path:
                    G.add_edge(node, neighbor)

    # Создаем фигуру Matplotlib
    fig, ax = plt.subplots()

    # Определяем цвета узлов
    color_map = []
    for node in G:
        if node == start:
            color_map.append('green')
        elif node == goal:
            color_map.append('red')
        else:
            color_map.append('yellow')

    # Рисуем граф
    pos = nx.spring_layout(G)  # Задание положения узлов для стабильного отображения
    nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=1000, font_size=12, font_weight='bold', ax=ax, edge_color='black')

    # Сохраняем изображение в файл
    plt.savefig(filename)
    plt.close(fig)  # Закрываем фигуру после сохранения

def complete():
    global text1, text2

    if len(text2) > 0 and len(text1) > 0:
        clear_window()

        tree = make_tree(text1)  # сохраняем результат в переменной
        start_node = list(tree.keys())[0]

        image = Image.open("graph_image.png")
        tk_image = ImageTk.PhotoImage(image.resize((400, 600)))
        label = ttk.Label(window, image=tk_image)
        label.image = tk_image  # Чтобы избежать сборщика мусора удаления изображения
        label.pack(side="left", padx=10, pady=10, anchor="w")  # Размещаем слева с отступами и выравниваем по левому краю

        path = bfs_shortest_path(tree, start_node, text2)

        if path:
            draw_graph_from_list(tree, path, start_node, text2, 'path_graph_image.png')
            path_image = Image.open("path_graph_image.png")
            tk_path_image = ImageTk.PhotoImage(path_image.resize((400, 600)))
            path_label = ttk.Label(window, image=tk_path_image)
            path_label.image = tk_path_image  # Чтобы избежать сборщика мусора удаления изображения
            path_label.pack(side="right", padx=10, pady=10, anchor="e")  # Размещаем справа с отступами и выравниваем по правому краю

    else:
        error.pack()  # Предупреждение о заполнении всех полей, если они не заполнены

def on_enter(event):
    global text1, text2

    if combobox.get() == "Ввод графа":
        text1 = new_window1.get()
    else:
        text2 = new_window2.get()

def start():
    btn.pack_forget()
    menu()

def menu():
    combobox.place(relx=0.5, rely=0.4, anchor="c")
    btn = ttk.Button(text="ВЫПОЛНИТЬ", command=complete)
    btn.place(relx=0.5, rely=0.5, anchor="c")

def selected(event):
    selection = combobox.get()
    if selection == "Ввод графа":
        global new_window1
        example_text2.place_forget()

        example_text1.place(relx=0.5, rely=0.3, anchor="c")
        new_window1 = Entry(window)
        new_window1.place(relx=0.5, rely=0.435, anchor="c", relwidth=0.18, relheight=0.035)
        new_window1.bind("<Return>", on_enter)

        if len(text1) != 0:
            new_window1.insert(0, text1)

    if selection == "Выбор узла":
        global new_window2
        example_text1.place_forget()

        example_text2.place(relx=0.5, rely=0.3, anchor="c")
        new_window2 = Entry(window)
        new_window2.place(relx=0.5, rely=0.435, anchor="c", relwidth=0.18, relheight=0.035)
        new_window2.bind("<Return>", on_enter)

        if len(text2) != 0:
            new_window2.insert(0, text2)

window = Tk()
window.title("QuickBFS")
window.geometry("800x600+560+240")
window.resizable(False, False)
methods = [
    "Ввод графа",
    "Выбор узла",
]

error = ttk.Label(text="Заполните все поля !", font=("Arial", 14), foreground='red')
example_text1 = ttk.Label(text="Введите дерево в виде A: B, C; B: A, D, E", font=("Arial", 10))
example_text2 = ttk.Label(text="Введите узел для которого вам нужен кратчайший путь", font=("Arial", 10))
text1, text2 = '', ''

combobox = ttk.Combobox(values=methods, state="readonly")
combobox.bind("<<ComboboxSelected>>", selected)

btn = ttk.Button(text="START", command=start)
btn.pack(expand=True, ipadx=200, ipady=60)

window.mainloop()
