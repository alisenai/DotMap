# DotMap
## Intro
A simple python script for managing dotfiles.

Dot files are called `dot`s and are split into `group`s to help distinguish them.
Using this script, any group may be installed, or all at once.


## Usage
Basic usage is as follows:
```
$ python3 DotMap.py -h
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
 $ 
 ```

## Eamples
### Managing Groups
**Creating a Group:**

**Example: Creating a new group with the name `polybar`, which can then store dot files within it.**
```
python3 DotMap.py --create-group polybar
```

**Listing Existing Groups:**
```
python3 DotMap.py --list-groups
```

**Example: Deleting the group `polybar` and all the `dot`s within it.**
```
python3 DotMap.py --delete-group polybar
```

### Managing Dots
**Example: Adding a polybar dotfile to the `polybar` group.**
```
python3 DotMap.py --add-dot polybar ~/.config/polybar/config dots/polybar/config
```

This will create a copy of `~/.config/polybar/config` to `dots/polybar/config` and create a dot reference under the`polybar` group

**Example: Delete a polybar dotfile from the `polybar` group.**
```
python3 DotMap.py --delete-dot polybar dots/polybar/config
```


