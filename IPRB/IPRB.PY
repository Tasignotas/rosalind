# Rosalind problem id: IPRB
# The Mendelian probability of getting a dominant allele


if __name__ == '__main__':
    f = open('rosalind_iprb.txt', 'r')
    data = f.readline().split()
    
    # K - number of homozygous with dominant allele:
    k = float (data[0])
    
    # M - number of heterozygous organisms:
    m = float (data[1])
    
    # N - number of homozygous with recessive allele:
    n = float (data[2])
    
    # The probability of getting a dominant feature in
    # the mating of the given number of organisms:
    
    prob = (k/(k+m+n)) + (m/(k+m+n))*(k/(k+m+n-1)) + (m/(k+m+n))*((m-1)/(k+m+n-1))*(3.0/4) + (m/(k+m+n))*(n/(k+m+n-1))*(1.0/2) + (n/(k+m+n))*(k/(k+m+n-1)) + (n/(k+m+n))*(m/(k+m+n-1))*(1.0/2)
    print prob
