class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None        # Начальный узел
        self.tail = None        # Конечный узел

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node: Node = Node(data)         # Инициализируем новый узел
        if self.head is None:               # Если список пуст,
            self.head = new_node            # то новый узел становится и головным
            self.tail = new_node            # и конечным одновременно
        else:
            temp: Node = self.head          # Во временный узел запоминаем текущий головной узел
            self.head = new_node            # Новой головой становится новый узел
            self.head.next_node = temp      # ссылку на второй узел после головного берем из временного узла

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node: Node = Node(data)         # Инициализируем новый узел
        if self.head is None:               # Если список пуст,
            self.head = new_node            # то новый узел становится и головным
            self.tail = new_node            # и конечным одновременно
        else:
            self.tail.next_node = new_node  # У текущего хвоста указываем ссылку на новый узел-хвост
            self.tail = new_node            # Новым хвостом становится новый узел

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string
