rule all:
    input:
        "target_timestamps/File_A.xlsx",
        "target_timestamps/File_B.xlsx"

rule add_timestamps:
    input: "source/{file}"
    output: "target_timestamps/{file}"
    shell: "/usr/local/bin/add_timestamp.py {input} {output}"
