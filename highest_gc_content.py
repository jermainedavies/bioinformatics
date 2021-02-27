def gc_content(filename):

    clean_list = []
    final_list = []
    gc_dict = {}
    nucleotides = ["A","T","C","G"]
    gc = ["C","G"]
    id_list = []
    nucleotide_list = []
    count = 0
    second_count = 0
    max_percent = 0
    with open(filename, "r") as opened_file:
        text=opened_file.read().strip().split()
        print(text)

        for i in range(len(text)):
            if text[i].startswith(">"):
                clean_list.append(text[i])
                if count !=0:
                    count+=1
            try:
                if text[i].startswith(">")==False:
                    if text[i-1].startswith(">") == True:
                        clean_list.append(text[i])
                        count+=1
                    elif text[i-1].startswith(">") == False:
                        clean_list[count]+=text[i]

            except IndexError:
                pass

        for j in range(len(clean_list)):
            if j % 2 == 0:
                id_list.append(clean_list[j])

            elif j % 2 != 0:
                num = 0
                den = 0
                for base in clean_list[j]:
                    den+=1
                    if base in gc:
                        num +=1
                gc_percent = (num/den)*100
                nucleotide_list.append(gc_percent)

    # for d in final_list:
    #     gc_dict.update(d)

                gc_dict = zip(id_list, nucleotide_list)
                gc_dict = dict(gc_dict)
                highest_gc = max(gc_dict, key=gc_dict.get)

                for key,value in gc_dict.items():
                    if key == max(gc_dict, key=gc_dict.get):
                        max_percent = value

    return highest_gc,max_percent


print(gc_content("rosalind_gc.txt"))

#returns ('>Rosalind_9048', 52.319309600862994)
