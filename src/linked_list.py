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

    def insert_beginning(self, data) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node: Node = Node(data)         # Инициализируем новый узел
        if self.head is None:               # Если список пуст,
            self.head = new_node            # то новый узел становится и головным
            self.tail = new_node            # и конечным одновременно
        else:
            temp: Node = self.head          # Во временный узел запоминаем текущий головной узел
            self.head = new_node            # Новой головой становится новый узел
            self.head.next_node = temp      # ссылку на второй узел после головного берем из временного узла

    def insert_at_end(self, data) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node: Node = Node(data)         # Инициализируем новый узел
        if self.head is None:               # Если список пуст,
            self.head = new_node            # то новый узел становится и головным
            self.tail = new_node            # и конечным одновременно
        else:
            self.tail.next_node = new_node  # У текущего хвоста указываем ссылку на новый узел-хвост
            self.tail = new_node            # Новым хвостом становится новый узел

    def delete_beginning(self) -> None:
        """Удаляет узел с данными из начала связанного списка"""
        if self.head is None:                   # Если список пуст, то нечего удалять
            return
        elif self.head != self.tail:            # Если список состоит более, чем из одного узла,
            self.head = self.head.next_node     # то головным узлом становится следующий за ним
        else:
            self.head = None                    # Если в списке только один узел
            self.tail = None                    # то удаляем его, очищая весь список

    def delete_at_end(self) -> None:
        """Удаляет узел с данными из конца связанного списка"""
        if self.head is None:                   # Если список пуст, то нечего удалять
            return
        elif self.head != self.tail:            # Если список состоит более, чем из одного узла,
            temp = self.head
            while temp.next_node != self.tail:  # Перебираем все узлы в поисках предпоследнего узла
                temp = temp.next_node
            self.tail = temp                    # Предпоследний узел становится конечным в списке
            self.tail.next_node = None          # и он не ссылается на какой-либо другой узел
        else:
            self.head = None                    # Если в списке только один узел
            self.tail = None                    # то удаляем его, очищая весь список

    def to_list(self) -> list:
        node = self.head                        # Начинаем обход списка с головного узла
        if node is None:                        # Если его нет, то
            return []                           # возвращаем пустой список

        ll_data_list = []
        while node:                             # Пока не дошли до конца списка
            ll_data_list.append(node.data)      # получаем данные из узла и
            node = node.next_node               # переходим к следующему узлу
        return ll_data_list

    def get_data_by_id(self, key_id) -> dict:
        node = self.head                        # Начинаем обход списка с головного узла
        if node is None:                        # Если его нет, то
            return {}                           # возвращаем пустой список

        while node:
            try:
                if node.data['id'] == key_id:   # Если находим значение по ключу в узле
                    return node.data            # то возвращаем это значение
            except TypeError:                   # Обрабатываем ошибку, если в узле неподходящие данные
                print('Данные не являются словарем или в словаре нет id.')
            finally:
                node = node.next_node           # Переходим к следующему узлу

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
