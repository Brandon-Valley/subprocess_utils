import subprocess


''' VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV '''
'''                                                                           
        Internal Functions
'''
''' VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV '''


def print_cmd_if_needed(cmd, print_cmd):
    if print_cmd:
        print('\n  Running cmd:  ', cmd, '...')   
        
        

''' VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV '''
'''                                                                           
        External Functions
'''
''' VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV '''

# try to use this first, if you get an error like below, try run_cmd_call()
    #     for arg in seq:
    # TypeError: 'bool' object is not iterable
def run_cmd_popen(cmd, print_output = False, print_cmd = False, shell = False):
    print_cmd_if_needed(cmd, print_cmd)
        
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1, shell = shell)
    for line in iter(p.stdout.readline, b''):
        if print_output:
            print (line)
    p.stdout.close()
    p.wait()

# try to only use this if run_cmd_popen does not work
def run_cmd_call(cmd, print_cmd = False, shell = False):
    print_cmd_if_needed(cmd, print_cmd)
    subprocess.call(cmd, shell = shell)



# silently returns True / False if running the given command in cmd would result in a fatal error
def fatal_error(cmd):
    try:
        subprocess.check_output(cmd.split(), stderr=subprocess.DEVNULL)
        return False
    except(subprocess.CalledProcessError):
        return True
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    