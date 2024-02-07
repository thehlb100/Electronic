import math
def calculate_subnet_info():
    used_hosts = int(input("Enter the number of hosts: "))
    used_nets = int(input("Enter the number of networks: "))
    ip = input("Enter the IP address: ")

    results = ""
    

    # Extract the first octet to determine the IP class
    first_octet = int(ip.split('.')[0])

    # Determine the IP class
    ip_class = ""
    if 1 <= first_octet <= 126:
        ip_class = 'A'
    elif 128 <= first_octet <= 191:
        ip_class = 'B'
    elif 192 <= first_octet <= 223:
        ip_class = 'C'
    else:
        return "Invalid IP address. This function only supports Class A, B, and C addresses."

    # Calculate the necessary subnet bits
    total_subnets = 2 ** (math.ceil(math.log2(used_nets)))
    subnet_bits = math.ceil(math.log2(total_subnets))

    # Calculate the necessary host bits
    total_hosts = 2 ** (math.ceil(math.log2(used_hosts + 2)))  # '+ 2' accounts for network and broadcast addresses
    host_bits = math.ceil(math.log2(total_hosts))

    # Determine the default subnet mask based on the IP class
    default_subnet_mask = ""
    if ip_class == 'A':
        default_subnet_mask = '255.0.0.0'
    elif ip_class == 'B':
        default_subnet_mask = '255.255.0.0'
    elif ip_class == 'C':
        default_subnet_mask = '255.255.255.0'

    # Calculate the applied subnet mask based on the number of subnet bits
    binary4 = str('1'*subnet_bits) + ('0'*host_bits) 
    binary = int(binary4)

    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary%10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
   

    # Display the results
    result_string = f"""
        IP Address: {ip}
        IP Class: {ip_class}
        Default Subnet Mask: {default_subnet_mask}
        Applied Subnet Mask: {decimal}
        Subnet Bits: {subnet_bits}
        Host Bits: {host_bits}
    """
    print(result_string)
calculate_subnet_info()
