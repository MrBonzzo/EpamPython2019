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

# read the file dna.fasta

from collections import Counter, defaultdict

dna = None

with open("files/dna.fasta", "r") as dna_file:
    dna = defaultdict(str)
    gene = ""
    for line in dna_file:
        if line.startswith('>'):
            gene = line[1:].rstrip()
        else:
            dna[gene] += line.rstrip()




def translate_from_dna_to_rna(dna):
    
    """your code here"""
    rna = {}
    for d in dna:
        rna[d] = dna[d].replace("T", "U")
        rna[d] = rna[d][:len(rna[d]) - (len(rna[d]) % 3)]
    return rna


def count_nucleotides(dna):
    
    """your code here"""
    num_of_nucleotides = {}
    for d in dna:
        num_of_nucleotides[d] = Counter(dna[d])
    return num_of_nucleotides

rna_codon_table = None
with open("files/rna_codon_table.txt", "r") as table:
    rna_codon_table = {}
    for line in table:
        line = line.rstrip().split()
        for i, triplet_or_protein in enumerate(line):
            if i % 2 == 0:
                rna_codon_table[triplet_or_protein] = ""
            else:
                rna_codon_table[line[i - 1]] = triplet_or_protein


def translate_rna_to_protein(rna):
    
    """your code here"""
    protein = {}
    for r in rna:
        protein[r] = ""
        for i in range(len(rna[r]) // 3):
            triplet = rna[r][i * 3: i * 3 + 3]
            protein[r] += rna_codon_table[triplet] if rna_codon_table[triplet] != "Stop" else " "
        protein[r] = protein[r].split()
    return protein
