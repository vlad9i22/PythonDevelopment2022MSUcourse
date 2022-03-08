from re import sub
from shlex import split
import cmd, sys
import readline
import pynames
from inspect import getmembers
from typing import Callable, List, Dict, Tuple
from pynames import GENDER, LANGUAGE

def get_subclasses(class_name: str) -> Tuple[List[str], List[Callable]]:
    subclasses: List[str] = []
    classes_examples = []
    my_eval_str = 'pynames.generators.' + class_name.lower()
    for i in getmembers(eval(my_eval_str)):
        if i[0].find("Generator") > 0 and 'get_name_simple' in dir(i[1]) and i[0] != 'FromListGenerator':
            subclasses.append(i[0])
            classes_examples.append(i[1])
    return (subclasses, classes_examples)

def convert_names_to_subclasses(subclasses: List[str]) -> Dict[str, str]:
    subclasses_names = {}
    for class_name in subclasses:
        find_full = class_name.find('Full')
        if find_full == -1:
            find_full = class_name.find('Names')
        if find_full == -1:
            subclasses_names[class_name] = class_name
        else:
            subclasses_names[class_name[0:find_full]] = class_name
    return subclasses_names


class pyname_shell(cmd.Cmd):
    intro = "Welcome to pyname shell!"
    prompt = "(pyname) "
    main_classes = dict(getmembers(pynames.generators))['__all__']
    print(main_classes)

    def do_generate(self, arg):
        params = split(arg)
        gender = 'm'
        for args in params:
            if args[0].lower() in GENDER.ALL:
                if args[0] == 'm':
                    gender = GENDER.MALE
                elif args[0] == 'f':
                    gender = GENDER.FEMALE
        params_len = len(params)
        if params_len == 0 or params[0].lower() not in self.main_classes:
            if params_len == 0:
                print("Not enough parametrs")
            else:
                print("No such class")
        else:
            subclasses: Tuple[List[str], List[Callable]] = get_subclasses(params[0])
            if len(subclasses) == 0:
                print("Didn't find any possible classes")
            else:
                subclasses_names: Dict[str, str] = convert_names_to_subclasses(subclasses[0])
                if params_len > 1:
                    if params[1] in subclasses_names.keys():
                        user_subclass_name = params[1]
                        program_subclass_name = subclasses_names[user_subclass_name]
                        pyname_generator = subclasses[1][subclasses[0].index(program_subclass_name)]()
                    else:
                        default_class_name = list(subclasses_names.keys())[0]
                        program_subclass_name = subclasses_names[default_class_name]
                        pyname_generator = subclasses[1][0]()
                else:
                    default_class_name = list(subclasses_names.keys())[0]
                    print("Running default: " + default_class_name)
                    pyname_generator = subclasses[1][0]()
            print(pyname_generator.get_name_simple(gender))
                        
                        



if __name__ == '__main__':
    pyname_shell().cmdloop()