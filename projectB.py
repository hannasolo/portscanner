# Programmer: Hanna Rumpler
# Quickstart Cybersecurity Bootcamp
# Python Module
# Project B
# Instructions:
#       scan for all ports 1-1025
#       If port is open, append port number.
#       All exceptions (I.e.: "host not available", "host name could not be resolved") should also be logged
#       Record start/end time & date at the beginning/end of the file
import sys
import pyfiglet
from printy import printy, inputy
import socket
from datetime import datetime

def port_scanner(host, output):
    try:
        # Scan the ports between 1 and 1025
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.1)

            result = sock.connect_ex((host, port))

            # Check if the port is open
            if result == 0:
                print("Port {}: open".format(port))
                output.write(str(port) + ": open \n")
            sock.close()

    # Print message to console if there is keyboard interrupt
    except KeyboardInterrupt:
        print("\n User has decided to exiting the program!")
        sys.exit()

    # Log the Hostname Error in the output file
    except socket.gaierror:
        hostname_err = "Err: Hostname could not be resolved!"
        print(hostname_err)
        output.write(hostname_err)
        sys.exit()

    # Log Host not available error in output file
    except socket.herror:
        host_err = "Err: Host not available!"
        print(host_err)
        output.write(host_err)
        sys.exit()

    # Log timeout error in output file
    except socket.timeout:
        timeout_err = "Err: Timeout!"
        print(timeout_err)
        output.write(timeout_err)
        sys.exit()

def main():
    # ascii banner
    banner = pyfiglet.figlet_format("portscanner", font="isometric3", width = 200)
    author = pyfiglet.figlet_format("by hanna", font="tombstone", width = 50)
    printy(f"[p]{banner}@ \n [m]{author}@ ")

    start_scanner = inputy("[c]Enter \"start (s)\" to start scanning ports on a provided host. Enter \"quit (q)\" to quit. \n")

    if start_scanner == "start" or start_scanner == "s":
        print("Let's get to work!")
        # Create the output file
        output = open("output.txt", "w")
        output.write(banner)
        # Get the current time and date and log it in an output file
        start_time = datetime.now().strftime("%m-%d-%Y %H:%M")
        print("Start Date and Time: ", start_time)
        output.write("Start Date and Time: " + start_time)

        # Log host prompt and hostname to output file
        host = input("Enter a host to scan: \n")
        output.write("\nHost: " + host + "\n")
        print("Scanning Host: " + host)

        # Format the output file so it's easy to see the ports listed
        output.write("Ports: \n")
        port_scanner(host, output)

        end_time = datetime.now().strftime("%m-%d-%Y %H:%M")
        print("End Date and Time: ", end_time)
        output.write("End Date and Time: " + end_time)
        output.close()
    elif start_scanner == "quit" or start_scanner == "q":
        print("Goodbye!")
        sys.exit()

main()