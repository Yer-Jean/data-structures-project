class Node:
    """Класс для узла очереди"""

    def __init__(self, data):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = None


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data)        # Создаем узел для очереди с переданными данными - data
        if self.head is None:    # Если головы очереди "нет", то значит она пустая,
            self.head = node     # Тогда инициализируем как передний, так и задний узлы
            self.tail = node     # с указателем на один и тот же узел
        else:
            self.tail.next_node = node  # Иначе - обновляем "хвост" очереди
            self.tail = node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        node_data_list = []  # Инициализируем список для данных из очереди
        node = self.head     # Начинаем с головы очереди
        if node is None:     # Если головы очереди "нет", то значит она пустая,
            return ''        # и, соответственно, возвращаем пустую строку
        node_data_list.append(self.head.data)      # Если очередь не пустая, то добавляем в список данные головного узла
        while node.next_node:                      # Пока есть следующий узел,
            node = node.next_node                  # то добавляем из него данные в список
            node_data_list.append(node.data)       # и переходим к следующему узлу
        return '\n'.join(data for data in node_data_list)   # Возвращаем строку с данными всех узлов от головы до хвоста
