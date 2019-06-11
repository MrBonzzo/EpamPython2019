"""
Написать тесты(pytest) к предыдущим 3 заданиям, запустив которые,
я бы смог бы проверить их корректность
"""

import pytest
import task1
import task2
import task3


file1 = task1.PrintableFile('file1')
file2 = task1.PrintableFile('file2')
file3 = task1.PrintableFile('file3')
folder3 = task1.PrintableFolder('folder3', [file3])
folder2 = task1.PrintableFolder('folder2', [folder3, file2])
folder1 = task1.PrintableFolder('folder1', [folder2, file1])
folder1_str = ('V folder1\n'
               '|-> V folder2\n'
               '|   |-> V folder3\n'
               '|   |   |-> file3\n'
               '|   |-> file2\n'
               '|-> file1')
folder2_str = ('V folder2\n'
               '|-> V folder3\n'
               '|   |-> file3\n'
               '|-> file2')
folder3_str = ('V folder3\n'
               '|-> file3')


@pytest.mark.parametrize('file, str_file', [
    (folder3, folder3_str),
    (folder2, folder2_str),
    (folder1, folder1_str),
    (file3, 'file3'),
    (file2, 'file2'),
    (file1, 'file1')
    ])
def test_task1_to_str(file, str_file):
    assert str(file) == str_file


@pytest.mark.parametrize('folder, file, is_contains', [
    (folder1, file1, True),
    (folder1, folder2, True),
    (folder1, file3, True),
    (folder2, file1, False),
    (folder3, file3, True),
    (folder3, file1, False)
    ])
def test_task1_contains(folder, file, is_contains):
    assert (file in folder) is is_contains


graph1 = task2.Graph({'A': ['C', 'D'], 'B': [], 'C': ['B'], 'D': ['B']})
graph2 = task2.Graph({'A': ['B', 'D'], 'B': ['C'], 'C': [], 'D': ['A']})
graph3 = task2.Graph({'A': [], 'B': [], 'C': [], 'D': []})


@pytest.mark.parametrize('graph_, bfs_result', [
    (graph1, 'ACDB'),
    (graph2, 'ABDC'),
    (graph3, 'ABCD')
    ])
def test_task2_graph_itterations(graph_, bfs_result):
    assert list(graph_) == list(bfs_result)


ceasar = task3.CeasarSipher()


@pytest.mark.parametrize('msg, shifted_message, shifted_another_message', [
    ('abcdefghijklmnopqrstuvwxyz',
     'efghijklmnopqrstuvwxyzabcd',
     'hijklmnopqrstuvwxyzabcdefg')
    ])
def test_task3_ceasar_sipher(msg, shifted_message, shifted_another_message):
    ceasar.message = msg
    ceasar.another_message = msg
    assert ceasar.message == shifted_message
    assert ceasar.another_message == shifted_another_message
