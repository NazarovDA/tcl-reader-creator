# coding: UTF-8
import json
import time
import logging
import datetime as dt

logging.basicConfig(filename="logs/module_logs.log", level=logging.INFO)
log = logging.getLogger("KeyError")
program_name = "i don't choose now"


class Module:
    def __init__(self):
        self.settings: dict = {
            "module": {
                "property": {
                    "DESCRIPTION": None,
                    "NAME": None,
                    "VERSION": None,
                    "INTERNAL": None,
                    "OPAQUE_ADDRESS_MAP": None,
                    "AUTHOR": None,
                    "DISPLAY_NAME": None,
                    "INSTANTIATE_IN_SYSTEM_MODULE": None,
                    "EDITABLE": None,
                    "REPORT_TO_TALKBACK": None,
                    "ALLOW_GREYBOX_GENERATION": None,
                    "REPORT_HIERARCHY": None
                }
            },
            "fileset": {
                "QUARTUS_SYNTH": {
                    "property": {
                        "TOP_LEVEL": None,
                        "ENABLE_RELATIVE_INCLUDE_PATHS": None,
                        "ENABLE_FILE_OVERWRITE_MODE": None
                    }
                },
                "files": {

                }
            },
            "parameter": {},
            "interface": {}
        }

    def __log_key_error(self, err):
        log.exception(f"{dt.datetime.now()}\n{err}\n")

    def __uncorrect_file_load(self, err):
        log.exception(f"{dt.datetime.now()}\n{err}\n")

    def write_to_json(self, filename=None):

        if filename is None:
            filename = f"{self.settings['module']['property']['NAME']}.json"

        with open(filename, "w") as writeFile:
            json.dump(self.settings, writeFile, indent=1)

    def write_to_tcl(self, filename=None):
        f"""
        Saving .tcl doc {self.settings['module']['property']['NAME']}
        :return: None
        """

        if filename is None:
            filename = f"{self.settings['module']['property']['NAME']}.tcl"

        with open(filename, "w") as writeFile:
            writeFile.write(f"# TCL File Generated by {program_name}\n"
                            f"{time.asctime()}\n"
                            f"DO NOT MODIFY\n"
                            f"\n"
                            f"\n"
                            f"#\n"
                            f"# {self.settings['module']['property']['NAME']} "
                            f"{self.settings['module']['property']['NAME']} "
                            f"v{self.settings['module']['property']['VERSION']}\n"
                            f"# {time.asctime()}\n"
                            f"#\n"
                            f"#\n"
                            f"\n"
                            f"#\n"
                            f"# request TCL package from ACDS 16.1\n"
                            f"#\n"
                            f"package require -exact qsys 16.1\n"
                            f"\n"
                            f"\n")  # heading

            # module properties
            writeFile.write(f"#\n"
                            f"# module {self.settings['module']['property']['NAME']}\n"
                            f"#\n")
            for prop in self.settings['module']['property']:
                writeFile.write(f"set_module_property {prop} {self.settings['module']['property'][prop]}\n")

            # file sets
            try:

                writeFile.write(f"\n"
                                f"\n"
                                f"#\n"
                                f"#file sets\n"
                                f"#\n")
                d = self.settings['fileset']

                for fileset in d:
                    if fileset != "files":
                        writeFile.write(f'add_fileset {fileset} {fileset} "" "" \n')
                        actualDict = d[fileset]
                        for prop in actualDict['property']:
                            writeFile.write(f'set_fileset_property {fileset} {prop} {actualDict["property"][prop]}\n')
                    if fileset == 'files':
                        actualDict = d[fileset]
                        for file in actualDict:
                            writeFile.write(f"add_fileset_file {file}"
                                            f" {actualDict[file]['type']}"
                                            f" PATH {actualDict[file]['PATH']}"
                                            f"{' TOP_LEVEL_FILE' if actualDict[file]['status'] is not None else ''}")
                            writeFile.write('\n') if actualDict[file]['status'] is not None else writeFile.write('')

            except KeyError:
                self.__log_key_error(KeyError)

            # parameters
            try:
                writeFile.write(f"\n"
                                f"\n"
                                f"#\n"
                                f"#parameters\n"
                                f"#\n")
                d = self.settings['parameter']

                for param in d:
                    writeFile.write(
                        f'add_parameter {param} {d[param]["property"]["TYPE"]} '
                        f'{d[param]["property"]["DEFAULT_VALUE"]}\n')

                    for prop in d[param]["property"]:
                        writeFile.write(f"set_parameter_property {param} {prop} "
                                        f"{d[param]['property'][prop]}\n")

            except KeyError:
                self.__log_key_error(KeyError)

            # interface
            try:
                d = self.settings['interface']
                for param in d:
                    writeFile.write(f"\n"
                                    f"\n"
                                    f"#\n"
                                    f"#connection point {param}\n"
                                    f"#\n"
                                    f"add_interface {param} {d[param]['endpoint']} end\n")
                    for prop in d[param]['property']:
                        writeFile.write(f"set_interface_property {param} {prop} {d[param]['property'][prop]}\n")

                    try:
                        for port in d[param]['ports']:
                            writeFile.write(
                                f"add_interface_port {param} {d[param]['ports'][port]['name']} "
                                f"{port} {d[param]['ports'][port]['IO_type']} {d[param]['ports'][port]['value']}\n")
                    except KeyError:
                        self.__log_key_error(KeyError)

                    try:
                        for assignment in d[param]['assignment']:
                            writeFile.write(
                                f"set_interface_assignment {param} {assignment} {d[param]['assignment'][assignment]}\n")
                    except KeyError:
                        pass
                        self.__log_key_error(KeyError(f"excepted no assigment in {param}"))

            except KeyError:
                self.__log_key_error(KeyError)

    def read_file(self, filename: str):
        if filename[-4:] == ".tcl":
            return self.__read_tcl(filename=filename)

        elif filename[-5:] == ".json":
            with open(filename, "r") as file:
                self.settings = json.load(file)

        elif filename[-4:] != ".tcl" or filename[-5:] != ".json":
            # if we took not .tcl or .json file
            self.__uncorrect_file_load(Exception(f"Unexpected format to open.\n"
                                                 f"Expected: .tcl\n"
                                                 f"Received: {filename[-4:]}\n"
                                                 f"Filename: {filename}"))

    def __read_tcl(self, filename):
        with open(filename) as file:
            for row in file:
                if row.startswith("#") or row.startswith(" ") or row.startswith("\n") or row.startswith("package"):
                    continue
                subrows = row.split(" ")
                command = subrows.pop(0).split("_")
                if command[0] == "add":
                    self.__add(
                        command=command,
                        row=subrows
                    )
                elif command[0] == "set":
                    self.__set(
                        command=command,
                        row=subrows
                    )
                else:
                    log.error(f"wrong command '{row[:-1]}'\n")

            return self.settings

    def __add(self, command: list, row: list):
        if len(command) == 2:
            try:
                newDict = self.settings[command[1]]
            except KeyError:
                newDict = self.settings[command[1]] = {}

            commandDict = newDict[row[0]] = {}

        if command[1] == 'interface' and command[0] == "add" and len(command) == 2:
            try:
                nd = self.settings[command[1]]
                del nd
            except KeyError:
                self.settings[command[1]] = {}
            try:
                newDict = self.settings[command[1]][row[0]]
            except KeyError:
                newDict = self.settings[command[1]][row[0]] = {}

            newDict.update(
                {
                    'endpoint': row[1]
                }
            )

        elif len(command) == 3:
            if command[1] == 'fileset' and command[2] == 'file':
                try:
                    d = self.settings[command[1]]["files"]
                except KeyError:
                    d = self.settings[command[1]]["files"] = {}
                try:
                    newDict: dict = d[row[0]]
                except KeyError:
                    newDict = d[row[0]] = {}

                newDict.update(
                    {
                        "type": row[1],
                        row[2]: row[3],
                        "status": row[4][:-1] if len(row) == 5 else None
                    }
                )
            elif command[2] == 'port':
                try:
                    ports = self.settings[command[1]][row[0]]['ports']
                    del (ports)
                except KeyError:
                    self.settings[command[1]][row[0]]['ports'] = {}
                try:
                    newDict = self.settings[command[1]][row[0]]['ports'][row[2]]
                except KeyError:
                    newDict = self.settings[command[1]][row[0]]['ports'][row[2]] = {}

                newDict.update(
                    {
                        "IO_type": row[3],
                        "name": row[1],
                        "value": row[4][:-1],
                    }
                )

    def __set(self, command: list, row: list):
        if len(row) == 2:
            try:
                newDict = self.settings[command[1]][command[2]]

                newDict.update(
                    {
                        row[0]: row[1][:-1]
                    }
                )
            except Exception:
                log.exception(KeyError)

        elif len(row) == 3:
            try:
                newDict = self.settings[command[1]][row[0]][command[2]]
            except KeyError:
                newDict = self.settings[command[1]][row[0]][command[2]] = {}

            newDict.update(
                {
                    row[1]: row[2][:-1]
                }
            )
