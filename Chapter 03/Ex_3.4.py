seq="ATGCTGATATGGGGGGCCCCATAT"
ca=seq.count("A")
ct=seq.count("T")
cat = ca+ct
at_per= (cat/len(seq))*100
if at_per>80:
     print("AT content is veryhigh")
elif at_per>=70 and at_per<=79:
     print("AT content is high")
elif at_per>=60 and at_per<=69:
    print("AT content is medium")
else:
    print("AT content is low")
