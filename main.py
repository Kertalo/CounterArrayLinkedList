class CounterArrayLinkedList:
    def __init__(self):
        self.array = []
        self.counters = []

    def add(self, item, index=None):
        if index is None:
            self.array.append(item)
            if len(self.counters) > 0:
                self.counters.append(self.counters[-1])
            else:
                self.counters.append(0)
        else:
            self.recount_counters(index)
            self.array.insert(index, item)
            self.counters.insert(index, 0)

    def remove(self, item):
        if item in self.array:
            index = self.array.index(item)
            self.recount_counters(index)
            del self.array[index]
            del self.counters[index]

    def display(self):
        print("Список:")
        for i in range(len(self.array)):
            print(f"{self.array[i]} (счетчик: {self.counters[i]})")

    def increment_counter(self, item):
        if item in self.array:
            index = self.array.index(item)
            self.counters[index] += 1
        else:
            print(f"{item} не найден в списке.")

    def recount_counters(self, index):
        for i in range(index, len(self.array)):
            self.counters[i] += 1


# Подпрограмма для добавления элемента в список
def add_item(linked_list):
    item = input("Введите элемент списка: ")
    index = input("Введите индекс, куда нужно добавить элемент (или нажмите Enter, чтобы добавить в конец): ")
    if index.isdigit():
        linked_list.add(item, int(index))
    else:
        linked_list.add(item, None)

# Подпрограмма для удаления элемента из списка
def remove_item(linked_list):
    item = input("Введите элемент списка: ")
    linked_list.remove(item)

# Подпрограмма для вывода списка со счетчиками
def display_list(linked_list):
    linked_list.display()

# Основная программа
if __name__ == '__main__':
    choice = 0
    counter_array_linked_list = CounterArrayLinkedList()
    while choice != 4:
        print("Выберите операцию:")
        print("1. Добавить элемент в список")
        print("2. Удалить элемент из списка")
        print("3. Вывести список со счетчиками")
        print("4. Выход")
        choice = int(input("Введите номер выбранной операции: "))
        if choice == 1:
            add_item(counter_array_linked_list)
        elif choice == 2:
            remove_item(counter_array_linked_list)
        elif choice == 3:
            display_list(counter_array_linked_list)
        elif choice == 4:
            print("Программа завершена.")
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
