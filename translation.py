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
def dna():
  while True:
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
    print(f"\n\nRna squence: {rna}")


    while len(rnaList) > 0:
        for i in range(3):
          try:
            tempList.append(rnaList[0])
            rnaList.pop(0)
          except IndexError:
            print(f"Extra nucleotides found:\n\n")
            break
          finally:
            tempList.clear()
            tempStr=None
        tempStr="".join(tempList)
        for codon in codonTable:
          if codon == tempStr:
              aaList.append(codonTable[codon])
    print(f"AAList: {', '.join(aaList)}")

goHome()
