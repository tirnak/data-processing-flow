rule all:
    input: "source/File_A.xlsx"
    output: "target_timestamps/File_A.xlsx"
    shell: "/usr/local/bin/add_timestamp.py {input} {output}"