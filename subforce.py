import dns.resolver
# Function to query each of the subdomain combinations from the subcreate function
def query (subd):
    try:
        test = dns.resolver.resolve(subd)
        for rdata in test:
            return True
    except:
        return False
# Function to append subdomain prefixes to the root domain, and return each mutation
def subcreate():
    # Get input from user
    root = input("Root domain: ")
    subs = input("Path to subdomain list: ")
    output = input("Output file name: ")
    output = (output + ".txt")
    # Open output file
    f = open(output,'w')
    # For loop that opens subs file, returns each line appended to the root domain
    with open(subs) as file:
        for line in file:
           sub = str(line+"."+root)
           subdomain = sub.replace("\n","")
           # If query function returns true, subdomain is printed. If it returns false, nothing is printed
           validate = query(subdomain)
           if validate:
               print("[+] " + subdomain)
               # Write results to file
               f.write(subdomain + '\n')
   # Close output file
    f.close()
# Invoke subcreate function
subcreate()
