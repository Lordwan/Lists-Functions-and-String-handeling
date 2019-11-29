dna_input = input("Please provide the DNA sequence: ")

n = 3
dna_string = [dna_input[i:i + n] for i in range(0, len(dna_input), n)]



def dnadecode(decode):
    dna_list = []
    for protien in decode:

        if protien == 'ATT' or protien == 'ATC' or protien == 'ATA':
            dna_list.append("Isoleucine")

        elif protien == 'CTT' or protien == 'CTC' or protien == 'CTA' or protien == 'CTG' or protien == 'TTA' or protien == 'TTG':
            dna_list.append("Leucine")

        elif protien == 'GTT' or protien == 'GTC' or protien == 'GTA' or protien == 'GTG':
            dna_list.append("Valine")

        elif protien == 'TTT' or protien == 'TTC':
            dna_list.append("Phenylalanine")

        elif protien == 'ATG':
            dna_list.append("Methionine")

        else:
            dna_list.append("Amino acid X")
    return dna_list


print("Present:  " + str(dnadecode(dna_string)) + "\n")

# TASK 2

with open('DNA.txt') as file:
    contents = ""

    for line in file:
        contents = contents + line
        contents = contents.replace('\n', '')


def mutate(alter):
    new_contents = list(alter)
    index_int = new_contents.index("a")
    print("The small character 'a' is placed at index: " + str(index_int) + "\n")


(mutate(contents))

with open('normalDNA.txt', 'r+') as file:
    normal_contents = ""

    for line in file:
        normal_contents = normal_contents + line
        normal_contents = normal_contents.replace('\n', '')


def txtTranslate(file_contents):
    global translated_contents
    n = 3
    translated_contents = [file_contents[i:i + n] for i in range(0, len(file_contents), n)]
    return translated_contents


dnadecode(normal_contents)

print("The normalDNA text file input is :" + "\n" + str(txtTranslate(normal_contents)) + "\n")
print("The protiens present in the normalDNA text file is :" + "\n" + str(dnadecode(translated_contents)) + "\n")

with open('mutatedDNA.txt', 'r+') as file:
    mutated_contents = ""

    for line in file:
        mutated_contents = mutated_contents + line
        mutated_contents = mutated_contents.replace('\n', '')

print("The mutatedDNA text file input is :" + "\n" + str(txtTranslate(mutated_contents)) + "\n")
print("The protiens present in the mutatedDNA text file is :" + "\n" + str(dnadecode(translated_contents)) + "\n")
