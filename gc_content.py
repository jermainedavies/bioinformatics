def gc_content(filename):

    clean_list = []
    final_list = []
    nucleotides = ["A","T","C","G"]
    gc = ["C","G"]
    count = 0
    second_count = 0
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
                final_list.append(clean_list[j])

            elif j % 2 != 0:
                num = 0
                den = 0
                for base in clean_list[j]:
                    den+=1
                    if base in gc:
                        num +=1
                gc_percent = f": {(num/den)*100}%"
                final_list[second_count] += gc_percent
                second_count += 1

    return final_list

print(gc_content("rosalind_gc.txt"))
