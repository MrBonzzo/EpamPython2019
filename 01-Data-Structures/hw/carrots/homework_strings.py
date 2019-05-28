""""

Задание 1

0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)

1) Построение статистики по входящим в последовательность ДНК нуклеотидам 
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])

2) Перевод последовательности ДНК в РНК (окей, Гугл)

3) Перевод последовательности РНК в протеин*


*В папке files вы найдете файл rna_codon_table.txt - 
в нем содержится таблица переводов кодонов РНК в аминокислоту, 
составляющую часть полипептидной цепи белка.


Вход: файл dna.fasta с n-количеством генов

Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена

 ** Если вы умеете в matplotlib/seaborn или еще что, 
 welcome за дополнительными баллами за
 гистограммы по нуклеотидной статистике.
 (Не забудьте подписать оси)

P.S. За незакрытый файловый дескриптор - караем штрафным дезе.

"""

from collections import Counter, defaultdict


def get_dna(path_to_file):
    """
    Инициализация ДНК.
    """
    with open(path_to_file, "r") as dna_file:
        dna = defaultdict(str)
        gene = ""
        for line in dna_file:
            if line.startswith('>'):
                gene = line[1:].rstrip()
            else:
                dna[gene] += line.rstrip()
    return dna


def translate_from_dna_to_rna(dna):
    """
    Перевод ДНК в РНК путем замены тимина урацилом.
    Сокращение длины РНК до длины, кратной 3-м.
    """
    rna = {}
    for d in dna:
        rna[d] = dna[d].replace("T", "U")
        rna[d] = rna[d][:len(rna[d]) - (len(rna[d]) % 3)]
    return rna


def count_nucleotides(dna):
    """
    Подсчет последовательности нуклеотидов ДНК для каждого гена.
    """
    num_of_nucleotides = {}
    for d in dna:
        num_of_nucleotides[d] = Counter(dna[d])
    return num_of_nucleotides


def get_rna_codon_table(path_to_file):
    """
    Получение таблицы переводов кодонов РНК в аминокислоту.
    """
    with open("files/rna_codon_table.txt", "r") as table:
        rna_codon_table = {}
        for line in table:
            line = line.rstrip().split()
            for i, protein in enumerate(line):
                if i % 2:
                    rna_codon_table[line[i - 1]] = protein
    return rna_codon_table


def translate_rna_to_protein(rna, rna_codon_table):
    """
    Перевод последовательности РНК в протеин.
    """
    protein = defaultdict(str)
    for r in rna:
        for i in range(len(rna[r]) // 3):
            triplet = rna[r][i * 3: i * 3 + 3]
            if rna_codon_table[triplet] != "Stop":
                protein[r] += rna_codon_table[triplet]
            else:
                protein[r] += "-"
    return protein


def write_to_file(path_to_file, data):
    """
    Выгрузка данных по каждому гену в файл
    """
    with open(path_to_file, "w") as output_file:
        for gene in data:
            output_file.write(f">{gene}\n")
            for i, element in enumerate(data[gene], 1):
                if i % 75:
                    output_file.write(f"{element}")
                else:
                    output_file.write(f"{element}\n")
            output_file.write("\n")


if __name__ == "__main__":
    path_to_dna_file = "files/dna.fasta"
    path_to_table_file = "files/rna_codon_table.txt"
    dna = get_dna(path_to_dna_file)
    rna = translate_from_dna_to_rna(dna)
    statistic = count_nucleotides(dna)
    rna_codon_table = get_rna_codon_table(path_to_table_file)
    protein = translate_rna_to_protein(rna, rna_codon_table)
    write_to_file("statistic.txt", {s: str(dict(statistic[s])) for s in statistic})
    write_to_file("rna.txt", rna)
    write_to_file("protein.txt", protein)
