# pylint: disable=broad-exception-caught
"""
    This is a python script that reads the output of a netcat session and translates it to ASCII
"""
import subprocess #Used to initiate the netcat session


def read_netcat_output(host, port):
    try:
        with subprocess.Popen(['nc', host, str(port)], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
            output, error = process.communicate()

            if process.returncode != 0:
                print(f"Error: {error.decode()}")
                return None
            
            # Print or process the output as needed
            return output.decode()        
    # Catch Exceptions (all)
    except Exception as e:
        print(f"An error occured: {e}")
        return None

def numbers_to_ascii(numbers):
    """Converts an array of numbers into an array of their ASCII values"""
    try:
        ascii_values = [chr(int(num)) for num in numbers]
        return "".join(ascii_values)
    except ValueError as e:
        print(f"Error: {e}")
        return None


def main():
    """Inititates the netcat session and then outputs the return as ASCII"""

    # We are targeting the following: nc mercury.picoctf.net 7449`
    # We first split the netcat array into an array of numbers on everyline break then pass that to out asciii parser.
    print(numbers_to_ascii(read_netcat_output("mercury.picoctf.net", 7449).splitlines()))
    return 0

if __name__ == "__main__":
    main()
