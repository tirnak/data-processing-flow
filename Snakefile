rule all:
    input:
        "target_timestamps/File_A.xlsx",
        "target_timestamps/File_B.xlsx",
        "target_z_score/File_A.xlsx"

rule add_timestamps:
    input: "source/{file}"
    output: "target_timestamps/{file}"
    shell: "/usr/local/bin/add_timestamp.py {input} {output}"

rule add_z_score:
    input: "target_timestamps/File_A.xlsx"
    output: "target_z_score/File_A.xlsx"
    shell: "/usr/local/bin/add_z_score.py {input} {output}"
