seq="ATGCTGATATGGGGGGCCCCATAT"
ca=seq.count("A")
ct=seq.count("T")
cat = ca+ct
at_per= (cat/len(seq))*100
if at_per>=50:
     print("AT content is high")
else:
    print("AT content is low")
