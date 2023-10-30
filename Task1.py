# This is task 1: to-do list
class Todo:
    list1 = []

    @classmethod
    def todo(cls):
        run = input("on or off?")
        while run == 'on':
            query = input('please enter delete or add')
            print()
            query1 = 'delete'
            query2 = 'add'
            if query == query1:
                print('Please enter number of task you want to delete')
                print()
                num = int(input())
                del cls.list1[num - 1]
                print(cls.list1)
            elif query == query2:
                new = input('please enter the task you want to add')
                print()
                cls.list1.append(new)
                print(cls.list1)
            else:
                print('Invalid query')
            run = input("on or off?")


Todo.todo()
