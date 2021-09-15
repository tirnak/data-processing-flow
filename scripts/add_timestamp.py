#!/usr/bin/env python3
import sys
import pandas as pd
import time

wrong_argument_exit_code: int = 22

if len(sys.argv) < 3 or len(sys.argv) > 3:
    print("Only one argument is expected: file to add timestamps to. Actual " + str(sys.argv), file=sys.stderr)
    sys.exit(wrong_argument_exit_code)

file_to_parse: str = sys.argv[1]
data: pd.DataFrame = pd.read_excel(file_to_parse)

data["time_started"] = time.time()

file_to_write: str = sys.argv[2]
writer = pd.ExcelWriter(file_to_write)
data.to_excel(writer)
writer.save()
