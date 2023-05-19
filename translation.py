codonTable={
        'AUA':'ILE', 'AUC':'ILE', 'AUU':'ILE', 'AUG':'MET',
        'ACA':'THR', 'ACC':'THR', 'ACG':'THR', 'ACU':'THR',
        'AAC':'ASN', 'AAU':'ASN', 'AAA':'Lys', 'AAG':'Lys',
        'AGC':'SER', 'AGU':'SER', 'AGA':'ARG', 'AGG':'ARG',             
        'CUA':'LEU', 'CUC':'LEU', 'CUG':'LEU', 'CUU':'LEU',
        'CCA':'PRO', 'CCC':'PRO', 'CCG':'PRO', 'CCU':'PRO',
        'CAC':'HIS', 'CAU':'HIS', 'CAA':'GIN', 'CAG':'GIN',
        'CGA':'ARG', 'CGC':'ARG', 'CGG':'ARG', 'CGU':'ARG',
        'GUA':'VAL', 'GUC':'VAL', 'GUG':'VAL', 'GUU':'VAL',
        'GCA':'ALA', 'GCC':'ALA', 'GCG':'ALA', 'GCU':'ALA',
        'GAC':'ASP', 'GAU':'ASP', 'GAA':'GLU', 'GAG':'GLU',
        'GGA':'GLY', 'GGC':'GLY', 'GGG':'GLY', 'GGU':'GLY',
        'UCA':'SER', 'UCC':'SER', 'UCG':'SER', 'UCU':'SER',
        'UUC':'PHE', 'UUU':'PHE', 'UUA':'LEU', 'UUG':'LEU',
        'UAC':'TYR', 'UAU':'TYR', 'UAA':'STOP', 'UAG':'STOP',
        'UGC':'CYS', 'UGU':'CYS', 'UGA':'STOP', 'UGG':'TRP',
    }
dnaNucleotides=["A", "T", "C", "G"]
rnaNucleotides=["A", "U", "C", "G"]

def navigation(): #navigation for menu
  while True:
    navChoice=int(input(f"Please enter the number next to the action you would like to perform below: \n\n[0] : Go home.\n[1] : Quit\n\nSelection:   "))
    match navChoice:
      case 0:
        goHome()
        break
      case 1:
        quit()
      case _:
        print(f"Your selection of '{navChoice}' was not recognized. Please try again.")

def goHome(): #homepage
  global again
  while True:
    again = 1
    print(f"Hello! Welcome to the ultimate super spiffy DNA/RNA translator 3000!\n")
    navChoice=int(input(f"Please enter the number based on the starting value you plan on inputting: \n\n[0] : DNA\n[1] : RNA\n\nSelection: "))
    match navChoice:
      case 0:
        dna()
        break
      case 1:
        rna()
        break
      case _:
        print(f"Your selection of '{navChoice}' was not recognized. Please try again.")

#asset declaration
tempList=[]
aaList=[]
looseNucleotides=[]
again=1 #loop control var, 1=True, 0=False

def dna(): #decodes DNA
  global again
  while again==1:
    tempList=[]
    aaList=[]
    dna=input(f"Please enter your DNA sequence below: \n")
    dnaList=[]
    for nucleotide in dna: #converts str into DNA only if character is one of DNA's nucleotides else prints that the char was removed. 
      if nucleotide.upper() in dnaNucleotides:
        dnaList.append(nucleotide.upper())
      else: 
        print(f"Invalid character '{nucleotide}' received. Removed. ")
    rnaList=[]
    for bp in dnaList:
      match bp.upper(): #appends an rna nucleotide to rnaList depending on what case/dna nucleotide is
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


    while len(rnaList) > 0: #while there is still something in rnaList
        for i in range(3): #below block repeats three times if possible
          try: #adds first item in rnaList and then removes said item, then converts to str and finds corresponding amino acid in codonTable.
            tempList.append(rnaList[0])
            rnaList.pop(0) 
            tempStr="".join(tempList)
            for codon in codonTable:
              if codon == tempStr:
                aaList.append(codonTable[codon])
          except IndexError: #if, despite the fact that the 3 codon loop is still going on, a base pair cannot be appended because it is not found
            print(f"Extra nucleotides found:\n\n{', '.join(tempList)}\n\n") #then a list of extra nucleotides are printed based on what has alredy been added to temp list how cool!!
            break
        tempList.clear() #clears list/str so that the next codon sequence can be read accurately
        tempStr=None

    print(f"Amino Acid List: {', '.join(aaList)}")
    again=int(input(f"\n\nWould you like to decode another DNA sequence? Enter the number corresponding to your decision below.\n[0] : No, go to main menu.\n[1] : Yes\nSelection:  "))#again question
    match again:
      case 0:
        print(f"\nProceeding to navigation...\n")
        navigation()
        break
      case 1:
        print(f"\nProceeding again...\n")

def rna(): #decodes, strikingly similar to the above code. variables are just changed slightly. 
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
    again=int(input(f"\n\nWould you like to decode another RNA sequence? Enter the number corresponding to your decision below.\n[0] : No, go to main menu.\n[1] : Yes\nSelection:  "))
    match again:
      case 0:
        print(f"\nProceeding to navigation...\n")
        navigation()
        break
      case 1:
        print(f"\nProceeding again...\n")
goHome()
