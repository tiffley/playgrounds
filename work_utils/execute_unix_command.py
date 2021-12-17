import subprocess


def run_command(std):
    returncode = subprocess.run(std, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return returncode


# ---------------------- std cmd -----------------------------

def initial_command():
    return 'ls'


def std_create(li):
    commands = []
    for file in li:
        command = f'stat {file}'
        commands.append(command)
    return commands


#  -------------------------------------------------------

if __name__ == '__main__':
    std = initial_command()
    res = run_command(std)
    output = res.stdout.decode()
    li = output.split()
    print(li)

    commands = std_create(li)
    for command in commands:
        res = run_command(command)
        print(res.stdout)
