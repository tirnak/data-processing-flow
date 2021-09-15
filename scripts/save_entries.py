#!/usr/bin/env python3
import sys
import uuid
import pandas as pd
from pathlib import Path


# imitate saving to a database
def save_to_db(db_name, entry):
    entry_id = str(uuid.uuid1())
    entry_file_path = Path(db_name, entry_id + ".log")
    with open(entry_file_path,"w") as f:
        f.write(entry)


wrong_argument_exit_code: int = 22

if not len(sys.argv) == 4:
    print("Three arguments are expected: input file, database name, output success mark file. Actual " + str(sys.argv), file=sys.stderr)
    sys.exit(wrong_argument_exit_code)

file_to_parse: str = sys.argv[1]
data: pd.DataFrame = pd.read_excel(file_to_parse, index_col=0)

db_name: str = sys.argv[2]
for index, row in data.iterrows():
    save_to_db(db_name, str(row))

file_to_create = Path(sys.argv[3])
file_to_create.touch(mode=0o666, exist_ok=True)
