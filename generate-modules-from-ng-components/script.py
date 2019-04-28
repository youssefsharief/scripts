import os
import re
import string

gradparent_folder = 'components'

def camel(match):
    return match.group(1) + match.group(2).upper()

REG = r"(.*?)-([a-zA-Z])"

def getCapitalizedName(filename):
    s = re.sub(REG, camel, filename, 0)
    lst = [word[0].upper() + word[1:] for word in s.split()]
    s = " ".join(lst)
    return s


def crateFileInFolder(parent_folder, module_file_name, ModuleName, ComponentName):
    with open(os.path.join(gradparent_folder, parent_folder, module_file_name), 'w') as file:
        file.write("""
// Angular Imports
import { NgModule } from '@angular/core';
// This Module's Components
import { """ + ComponentName + """ } from './"""+parent_folder+""".component';
@NgModule({
    imports: [
    ],
    declarations: [
        """ + ComponentName  + """,
    ],
    exports: [
        """ + ComponentName + """,
    ]
})
export class """ + ModuleName + """ {
}
        """
    )

for parent_folder in os.listdir(gradparent_folder):
    ModuleName = getCapitalizedName(parent_folder) + 'Module'
    ComponentName = getCapitalizedName(parent_folder) + 'Component'
    module_file_name = parent_folder + '.module.ts'
    crateFileInFolder(parent_folder, module_file_name, ModuleName, ComponentName)
