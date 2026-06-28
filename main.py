import sys
import os

def main():
    builtins = ['echo', 'type', 'exit']

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command = input()

        if command == "exit":
            break

        elif command.startswith("echo"):
            print(command[5:])

        elif command.startswith("type"):
            disect = command.split()
            cmd = disect[1]

            # Check builtins first
            if cmd in builtins:
                print(f"{cmd} is a shell builtin")

            else:
                found = False

                # Read PATH
                path_dirs = os.environ.get("PATH", "").split(os.pathsep)

                # Search every directory
                for directory in path_dirs:
                    full_path = os.path.join(directory, cmd)

                    if (
                        os.path.isfile(full_path)
                        and os.access(full_path, os.X_OK)
                    ):
                        print(f"{cmd} is {full_path}")
                        found = True
                        break

                if not found:
                    print(f"{cmd}: not found")

        else:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
