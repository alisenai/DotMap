# DotMap
A simple python script for managing dotfiles.

# Usage
Running:
`python3 DotMap.py -h`
Will Return:
```
usage: DotMap.py
                 [-h | --install {GROUP | ALL} | --create-group {NAME} | --delete-group {GROUP} | --add-dot {GROUP} {SOURCE_DIR} {SAVE_DIR} | --delete-dot {GROUP} {SAVE_DIR}]
                 [--list-groups] [--list-dots {GROUP}] [--list]

Dot File Manager

optional arguments:
  -h, --help                                 Show help
  --install {GROUP | ALL}                    Installs dot files
  --create-group {NAME}                      Creates dot file group
  --delete-group {GROUP}                     Deletes dot file group
  --add-dot {GROUP} {SOURCE_DIR} {SAVE_DIR}  Adds a dot file to a group
  --delete-dot {GROUP} {SAVE_DIR}            Deletes a dot file from a group
  --list-groups                              Lists dot file groups
  --list-dots {GROUP}                        Lists dot files within a given
                                             group
  --list                                     Lists all stored dot files
```

