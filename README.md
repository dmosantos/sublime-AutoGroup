AutoGroup
===================

Sublime Text 3 Plugin to auto send a view into a group.

Install
----

**Without Git** 

- Download the latest source from [GitHub](https://github.com/dmosantos/sublime-AutoGroup)
- Copy the sublime-AutoGroup folder to your Sublime Text "Packages" directory.

**With Git** 

- Clone the repository in your Sublime Text "Packages" directory:

    git clone https://github.com/dmosantos/sublime-AutoGroup.git


The "Packages" directory is located at:

|OS|Path|
|-|-|
|OS X|~/Library/Application Support/Sublime Text 2/Packages/|
|Linux|~/.config/sublime-text-2/Packages/|
|Windows|%APPDATA%/Sublime Text 2/Packages/|


What it does
-----

When you open a file, if the extension is pointed to a group, it is automatically directed to the group.


Config
-----

File: AutoGroup.sublime-settings

**Example:**
    {
        "ext-map": {
            "0": ["html"],
            "1": ["css"],
            "2": ["js"],
            "3": ["php"]
        }
    }
    

Credits
-------

**Created by**

Diego Marques
