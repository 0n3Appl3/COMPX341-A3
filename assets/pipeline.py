import subprocess

commands = [
    ["npm", "install"],
    ["npm", "run", "build"],
    ["npm", "run", "start"],
    ["git", "add", "--all"],
    ["git", "commit", "-m", "COMPX341-22A-A3 Committing from CI/CD Pipeline"],
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
    main()