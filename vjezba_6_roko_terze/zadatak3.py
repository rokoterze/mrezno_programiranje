import dns

resolver=dns.resolver.Resolver()

def record(domain_name):
    #A
    answers_A = resolver.query(domain_name, 'A')
    print("A Records:")
    for rdata in answers_A:
        print(rdata)
        
    #PTR
    answers_PTR = resolver.query(domain_name, 'PTR')
    print("\nPTR Records:")
    for rdata in answers_PTR:
        print(rdata)
    
    #MX
    answers_MX = resolver.query(domain_name, 'MX')
    print("\nMX Records:")
    for rdata in answers_MX:
        print(rdata)
        
domain_name=input("Enter the domain name: ")

record(domain_name)