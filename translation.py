codonTable={
        'AUA':'Ile', 'AUC':'Ile', 'AUU':'Ile', 'AUG':'Met',
        'ACA':'Thr', 'ACC':'Thr', 'ACG':'Thr', 'ACU':'Thr',
        'AAC':'Asn', 'AAU':'Asn', 'AAA':'Lys', 'AAG':'Lys',
        'AGC':'Ser', 'AGU':'Ser', 'AGA':'Arg', 'AGG':'Arg',             
        'CUA':'Leu', 'CUC':'Leu', 'CUG':'Leu', 'CUU':'Leu',
        'CCA':'Pro', 'CCC':'Pro', 'CCG':'Pro', 'CCU':'Pro',
        'CAC':'His', 'CAU':'His', 'CAA':'Gin', 'CAG':'Gin',
        'CGA':'Arg', 'CGC':'Arg', 'CGG':'Arg', 'CGU':'Arg',
        'GUA':'Val', 'GUC':'Val', 'GUG':'Val', 'GUU':'Val',
        'GCA':'Ala', 'GCC':'Ala', 'GCG':'Ala', 'GCU':'Ala',
        'GAC':'Asp', 'GAU':'Asp', 'GAA':'Glu', 'GAG':'Glu',
        'GGA':'Gly', 'GGC':'Gly', 'GGG':'Gly', 'GGU':'Gly',
        'UCA':'Ser', 'UCC':'Ser', 'UCG':'Ser', 'UCU':'Ser',
        'UUC':'Phe', 'UUU':'Phe', 'UUA':'Leu', 'UUG':'Leu',
        'UAC':'Tyr', 'UAU':'Tyr', 'UAA':'STOP', 'UAG':'STOP',
        'UGC':'Cys', 'UGU':'Cys', 'UGA':'STOP', 'UGG':'Trp',
    }
dnaNucleotides=["A", "T", "C", "G"]
rnaNucleotides=["A", "U", "C", "G"]

def navigation():
  navChoice=int(input(f"Please enter the number next to the action you would like to perform below: \n\n[0] : Go home.\n[1] : Quit\n\nSelection:   "))
  match navChoice:
    case 0:
      goHome()
    case 1:
      quit()

def goHome():
  print(f"Hello! Welcome to the ultimate super spiffy DNA/RNA/Protein translator 3000!\n")
  navChoice=int(input(f"Please enter the number based on the starting value you plan on inputting: \n\n[0] : DNA\n[1] : RNA \n[2] : Amino Acid (2-letter abbreviation)\n\nSelection: "))
  match navChoice:
    case 0:
      dna()
    case 1:
      rna()
    case 3:
      aminoAcid()

tempList=[]
aaList=[]
looseNucleotides=[]
again=1

def dna():
  global again
  while again==1:
    tempList=[]
    aaList=[]
    looseNucleotides=[]
    dna=input(f"Please enter your DNA sequence below: \n")
    dnaList=[]
    for nucleotide in dna:
      if nucleotide.upper() in dnaNucleotides:
        dnaList.append(nucleotide.upper())
      else: 
        print(f"Invalid character '{nucleotide}' received. Removed. ")
    rnaList=[]
    for bp in dnaList:
      match bp.upper():
        case "A":
          rnaList.append("U")
        case "T":
          rnaList.append("A")
        case "C":
          rnaList.append("G")
        case "G":
          rnaList.append("C")
    rna = "".join(rnaList)
    print(f"\n\nRNA squence: {rna}")


    while len(rnaList) > 0:
        for i in range(3):
          try:
            tempList.append(rnaList[0])
            rnaList.pop(0)
            tempStr="".join(tempList)
            for codon in codonTable:
              if codon == tempStr:
                aaList.append(codonTable[codon])
          except IndexError: #if, despite the fact that the 3 codon loop is still going on, a base pair cannot be appended because it is not found
            print(f"Extra nucleotides found:\n\n{', '.join(tempList)}\n\n") #then a list of extra nucleotides are printed based on what has alredy been added to temp list how cool!!
            break
        tempList.clear()
        tempStr=None

    print(f"Amin Acid List: {', '.join(aaList)}")
    again=int(input(f"\n\nWould you like to decode another DNA sequence? Enter the number corresponding to your decision below.\n[0] : No, return home\n[1] : Yes\nSelection:  "))
    match again:
      case 0:
        print(f"\nReturning home...\n")
        goHome()
        break
      case 1:
        print(f"\nProceeding again...\n")

def rna():
  global again
  while again==1:
    tempList=[]
    aaList=[]
    looseNucleotides=[]
    rna=input(f"Please enter your RNA sequence below: \n")
    rnaList=[]
    for nucleotide in rna:
      if nucleotide.upper() in rnaNucleotides:
        rnaList.append(nucleotide.upper())
      else: 
        print(f"Invalid character '{nucleotide}' received. Removed. ")
    dnaList=[]
    for bp in rnaList:
      match bp.upper():
        case "A":
          dnaList.append("T")
        case "U":
          dnaList.append("A")
        case "C":
          dnaList.append("G")
        case "G":
          dnaList.append("C")
    dna = "".join(dnaList)
    print(f"\nDNA squence: {dna}")


    while len(rnaList) > 0:
        for i in range(3):
          try:
            tempList.append(rnaList[0])
            rnaList.pop(0)
            tempStr="".join(tempList)
            for codon in codonTable:
              if codon == tempStr:
                aaList.append(codonTable[codon])
          except IndexError: 
            print(f"Extra nucleotides found:\n\n{', '.join(tempList)}\n\n") 
            break
        tempList.clear()
        tempStr=None

    print(f"Amino Acid List: {', '.join(aaList)}")
    again=int(input(f"\n\nWould you like to decode another RNA sequence? Enter the number corresponding to your decision below.\n[0] : No, return home\n[1] : Yes\nSelection:  "))
    match again:
      case 0:
        print(f"\nReturning home...\n")
        goHome()
        break
      case 1:
        print(f"\nProceeding again...\n")
goHome()
