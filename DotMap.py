import os
import json
import shutil
import argparse

# Better help formatting
formatter = lambda prog: argparse.HelpFormatter(prog, max_help_position=52)
# Create a input parser and argument group
parser = argparse.ArgumentParser(formatter_class=formatter, description="Dot File Manager", add_help=False)
main_commands = parser.add_mutually_exclusive_group()
# Add arguments
main_commands.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Show help')
main_commands.add_argument('--install', metavar="{GROUP | ALL}", help="Installs dot files")
main_commands.add_argument('--create-group', metavar="{NAME}", help="Creates dot file group")
main_commands.add_argument('--delete-group', metavar="{GROUP}", help="Deletes dot file group")
main_commands.add_argument('--add-dot', metavar=("{GROUP}", "{SOURCE_DIR}", "{SAVE_DIR}"), nargs=3, help="Adds a dot file to a group")
main_commands.add_argument('--delete-dot', metavar=("{GROUP}", "{SAVE_DIR}"), nargs=2, help="Deletes a dot file from a group")
parser.add_argument('--list-groups', action='store_true', help="Lists dot file groups")
parser.add_argument('--list-dots', metavar="{GROUP}", help="Lists dot files within a given group")
parser.add_argument('--list', action='store_true', help="Lists all stored dot files")
# Parse inputs
args = parser.parse_args()


# Installs a given group's dots
def install_group(group: str, dots_data):
    if group in dots_data:
        print("  [Installing group: %s]" % group.lower())
        for dest_file in dots_data[group]:
            print("    [Installing file %s to %s]" % (dots_data[group][dest_file], dest_file))
            source_file = os.path.abspath(dots_data[group][dest_file])
            if os.path.isfile(source_file):
                os.makedirs(os.path.dirname(dest_file), exist_ok=True)
            if (os.path.isfile(source_file) and os.path.isfile(dest_file)) or (os.path.isdir(source_file) and os.path.isdir(dest_file)):
               print("      [%s exists! Creating backup]" % dest_file)
               shutil.move(dest_file, dest_file.rstrip('\\').rstrip('/')+".dotback")
               print("      [Done]")
            os.system("ln -s '%s' '%s'" % (source_file, os.path.abspath(dest_file)))
            print("    [Done]")
        print("  [Done]")
    else:
        print("  [Group %s not found]" % group)


# Adds a new dot to manage
def add_dot(group: str, source_dir: str, save_dir: str, dots_data):
    # source_dir = os.path.abspath(source_dir)
    if group in dots_data:
        if os.path.isfile(source_dir):
            try:
                os.makedirs(os.path.dirname(save_dir), exist_ok=True)
                shutil.copy(source_dir, save_dir)
                dots_data[group][source_dir] = save_dir
                print("[Added dot]")
                print("  [Source Directory: %s]" % source_dir)
                print("  [Save Directory: %s]" % save_dir)
            except IOError as e:
                print("[Source file not found]")
        elif os.path.isdir(source_dir):
            try:
                shutil.copytree(source_dir, save_dir)
                dots_data[group][source_dir] = save_dir
                print("[Added dot]")
                print("  [Source Directory: %s]" % source_dir)
                print("  [Save Directory: %s]" % save_dir)
            except IOError as e:
                print(e)
                print("[Could not add directory]")
        else:
            print("[Source file not found]")
    else:
        print("  [Group %s not found]" % group)


# Lists all tracked dots
def list_dots(group: str, indent_count: int, dots_data):
    if group in dots_data:
        for i in range(indent_count):
            print("  ", end="")
        print("[%s]:" % group)
        if len(dots_data[group]) > 0:
            for dot_file in dots_data[group]:
                for j in range(indent_count + 1):
                    print("  ", end="")
                print("[%s] -> [%s]" % (dots_data[group][dot_file], dot_file)) # RENDERED IN REVERSE!
        else:
            for j in range(indent_count + 1):
                print("  ", end="")
            print("[No dots stored]")
                
    else:
        print("[Group %s not found]" % group)


# Read data json
with open("dots/dots.json") as dots_file:
    dots_data = json.load(dots_file)

# Addding a dot to a group
if args.add_dot:
    add_dot(args.add_dot[0], args.add_dot[1], args.add_dot[2], dots_data)


# Deleting a dot from a group
if args.delete_dot:
    group, dot = args.delete_dot[0], args.delete_dot[1]
    if group in dots_data:
        if dot in dots_data[group]:
            os.remove(dots_data[group][dot])
            del dots_data[group][dot]
        else:
            print("[Dot %s not found]" % dot)
    else:
        print("[Group %s not found]" % group)

# Creates a dot group
if args.create_group:
    print("[Creating group: %s]" % args.create_group, end='')
    dots_data[args.create_group] = {}
    print("[Ok]")

# Deltes a dot group
if args.delete_group:
    print("[Deleting group: %s]" % args.delete_group, end='')
    del dots_data[args.delete_group]
    # TODO: Delete associated data from dots folder
    print("[Ok]")

# Lists managed groups and dots
if args.list:
    print("[DotMap:]")
    if len(dots_data) > 0:
        for group in dots_data:
            list_dots(group, 1, dots_data)
    else:
        print("  [No dots stored]")

# List managed groups
if args.list_groups:
    print("[Groups:]")
    for group in dots_data:
        print("- %s" % group)

# List managed dots
if args.list_dots:
    list_dots(args.list_dots, 0, dots_data)

# Install dots
if args.install:
    print("[Installing dot files]")
    if args.install.lower() == "all":
        for group in dots_data:
            install_group(group, dots_data)
    else:
        install_group(args.install, dots_data)
    print("[Done installing dot files]")

with open("dots/dots.json", "w") as dots_file:
    json.dump(dots_data, dots_file)
