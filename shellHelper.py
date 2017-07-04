# shell helper
# basically runs a command and returns the output and any err

from subprocess import Popen, PIPE

def runCommand(command, input=None):
    program = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err  = program.communicate(input)
    
    return output, err