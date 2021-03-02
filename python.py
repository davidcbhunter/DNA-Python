#numbers = []

#for x in range(1,11):
#    numbers.append(x)
#print(numbers)


#for x in range(len(numbers)):
#    numbers[x] = numbers[x] * 2
#print(numbers)




import random

chemicals  = ["A","T","C","G"]
start = "ATG"
end = ["TAG","TGA","TAA"]

gene = []
gene.append(start)
#gene.append(end[random.randint(0,2)])
#print(gene)


#we need a function to make a group of three chemicals
def make_codon():
    codon = ""
    for x in range(3):
        codon = codon + chemicals[random.randint(0,3)]
    if codon == start:
        return make_codon()
        #print("start")
    if codon in end:
        return make_codon()
    return codon
    

#for x in range(100):
#    make_codon()

#print(make_codon())
#add 10 codons to gene
for x in range(10):
    gene.append(make_codon())

#add the end codon
gene.append(end[random.randint(0,2)])

#show the gene
print(gene)