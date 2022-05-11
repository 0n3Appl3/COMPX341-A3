import subprocess

commands = [
    ["npm", "install"],
    ["npm", "run", "build"],
    ["npm", "run", "start"]
]

def main():
    subprocess.Popen(commands[0])
    subprocess.Popen(commands[1])
    subprocess.Popen(commands[2])

if __name__ == "__main__":
    main()