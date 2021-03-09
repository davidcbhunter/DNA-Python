import random

chemicals  = ["A","T","C","G"]
start = "ATG"
end = ["TAG","TGA","TAA"]

class Gene:
    #we need a function to make a group of three chemicals
    def make_codon(self):
        codon = ""
        for x in range(3):
            codon = codon + chemicals[random.randint(0,3)]
        if codon == start:
            return self.make_codon()
            #print("start")
        if codon in end:
            return self.make_codon()
        return codon
    
    def __init__(self,codon_number):
        self.codon_list = []
        self.codon_list.append(start)
        for x in range(codon_number):
            self.codon_list.append(self.make_codon())
        self.codon_list.append(end[random.randint(0,2)])
        
    

gene1 = Gene(24)

for codon in gene1.codon_list:
    print(codon)