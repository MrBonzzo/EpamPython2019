"""
Реализовать метод __str__, позволяющий выводить все папки и файлы из данной,
например так:

> print(folder1)

V folder1
|-> V folder2
|   |-> V folder3
|   |   |-> file3
|   |-> file2
|-> file1

А так же возможность проверить, находится ли файл или папка в другой папке:
> print(file3 in folder2)
True

"""


from collections import deque


class PrintableFolder:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __contains__(self, file):
        content_deque = deque(self.content)
        while content_deque:
            current_item = content_deque.popleft()
            if file == current_item:
                return True
            elif isinstance(current_item, PrintableFolder):
                content_deque.extend(current_item.content)
        return False

    def __str__(self):
        ret_str = f'V {self.name}\n'
        for c in self.content:
            if isinstance(c, PrintableFolder):
                temp_str = f'|-> {c}'
                temp_str = ['|   ' + f for f in temp_str.split('\n')]
                temp_str = '\n'.join(temp_str)[4:]
                ret_str += f'{temp_str}\n'
            else:
                ret_str += f'|-> {c}\n'
        ret_str = ret_str[:-1]
        return ret_str


class PrintableFile:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'


if __name__ == '__main__':
    file1 = PrintableFile('file1')
    file2 = PrintableFile('file2')
    file3 = PrintableFile('file3')
    folder3 = PrintableFolder('folder3', [file3])
    folder2 = PrintableFolder('folder2', [folder3, file2])
    folder1 = PrintableFolder('folder1', [folder2, file1])
    print(folder1)
    print(file2 in folder2)
    print(file1 in folder3)
    print(file3 in folder1)
