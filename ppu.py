# Script for to update the pip utility and all installed packages (libraries) to the latest versions
# Copyright (C) 2021 Zalexanninev15

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import subprocess as sbp
import pip

print('''PipPackagesUpdater  Copyright (C) 2021  Zalexanninev15
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.''')
print('\nPipPackagesUpdater v1.0.2 by Zalexanninev15')

# Update pip
print("\n[!] Updating the 'pip' package manager...\n\nShell:")
sbp.run('pip install --upgrade pip', shell=True)
print('\n[+] Completed!\n')

# List of all packages
print('[!] Looking for all the installed packages...')
pkgs = eval(str(sbp.run('pip list -o --format=json', shell=True, stdout=sbp.PIPE).stdout, encoding='utf-8'))
print('[+] A list of packages has been created!\n')

# Update all packages
print('[!] Updating the installed packages...')
for pkg in pkgs:
    print('[!] Updating the package ' + pkg['name'] + '...\n\nShell:')
    sbp.run('pip install --upgrade ' + pkg['name'], shell=True)
    print('\n[+] The ' + pkg['name'] +' package has been updated!')

print('\n[+] All packages updated!')
