seq1 = "attagcacc"
seq2 = "aatcgcaccaaa"

def similarity_percentage(seq1,seq2):


  same_bases = 0
  i = 0

  if len(seq1) < len(seq2):
    seq1, seq2 = seq2, seq1


  if len(seq1) != len(seq2):
    difference = len(seq1) - len(seq2)
    for j in range(difference):
      seq2 += "x"


  for base in seq1:
    if seq1[i] == seq2[i]:
      same_bases +=1
    i += 1

  similarity = (same_bases/len(seq1))*100
  return f"similarity between the two sequences is {similarity}%"

print(similarity_percentage(seq1,seq2))

# returns 58.333333333333336%