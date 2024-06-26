# QuickBFS

QuickBFS — это приложение на Python с графическим интерфейсом пользователя (GUI) для визуализации графов и поиска кратчайшего пути между узлами с использованием алгоритма поиска в ширину (BFS). Это приложение создано с использованием Tkinter для GUI, NetworkX для операций с графами и Matplotlib для их визуализации.

## Особенности

- Ввод графа в виде списка смежности.
- Визуализация всего графа.
- Поиск и визуализация кратчайшего пути между двумя узлами с использованием BFS.
- Отображение графа и кратчайшего пути бок о бок.

## Требования

- Python 3.x
- Tkinter
- NetworkX
- Matplotlib
- Pillow (PIL)

## Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/yourusername/QuickBFS.git
    ```
2. Перейдите в каталог проекта:
    ```sh
    cd QuickBFS
    ```
3. Установите необходимые пакеты

## Использование

1. Запустите приложение:
    ```sh
    python main.py
    ```
2. При запуске нажмите кнопку "START" для начала.
3. Используйте выпадающее меню для выбора метода ввода:
    - **Ввод графа**: Введите граф в формате `A: B, C; B: A, D, E`. 
    - **Выбор узла**: Введите узел, для которого вам нужен кратчайший путь.
    - (Нужно нажать ENTER, чтобы данные сохранились в окне.
4. После ввода необходимой информации нажмите "ВЫПОЛНИТЬ".
5. Приложение отобразит весь граф с левой стороны и граф кратчайшего пути с правой стороны.


