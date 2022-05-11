import sys
import subprocess

commands = [
    ["npm", "install"],
    ["npm", "run", "build"],
    ["npm", "run", "start"],
    ["git", "add", "--all"],
    ["git", "commit", "-m", "[commit message here]"],
    ["git", "push", "-u", "origin", "main"]
]

def main():
    # Install modules and dependencies.
    subprocess.run(commands[0])
    
    # Attempt to build the application.
    try:
        # Build the application.
        subprocess.check_output(commands[1])

        # Git add, commit and push to repository.
        subprocess.run(commands[3])
        subprocess.run(commands[4])
        subprocess.run(commands[5])
    except subprocess.CalledProcessError:
        # Script detected an error building the application and has been prevented from being committed and deployed.
        print("\n####################################################\n" + 
              "An error has occurred when building the application.\n" +
              "Check your code and try again.\n" +
              "####################################################\n")
        return

    # Deploy the application.
    subprocess.run(commands[2])

if __name__ == "__main__":
    # Get length of number of arguments in the command.
    arguments_length = len(sys.argv)

    if arguments_length == 2:
        # Set custom commit message.
        commands[4][3] = sys.argv[1]
        # Begin script.
        main()
    elif arguments_length > 2:
        # User has entered too many arguments in the command.
        print("\n####################################################\n" + 
              "There are too many arguments!\n" +
              "USAGE: python3 pipeline.py \"<commit message>\"\n" +
              "####################################################\n")
    else:
        # User has not entered a commit message.
        print("\n####################################################\n" + 
              "You need to enter a commit message!\n" +
              "USAGE: python3 pipeline.py \"<commit message>\"\n" +
              "####################################################\n")