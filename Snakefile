rule all:
    input:
        "target_timestamps/File_A.xlsx",
        "target_timestamps/File_B.xlsx",
        "target_z_score/File_A.xlsx",
        "target_merged/Merged.xlsx",
        "target_success/true"

rule add_timestamps:
    input: "source/{file}"
    output: "target_timestamps/{file}"
    shell: "/usr/local/bin/add_timestamp.py {input} {output}"

rule add_z_score:
    input: "target_timestamps/File_A.xlsx"
    output: "target_z_score/File_A.xlsx"
    shell: "/usr/local/bin/add_z_score.py {input} {output}"

rule merge:
    input:  "target_z_score/File_A.xlsx",
            "target_timestamps/File_B.xlsx"
    output: "target_merged/Merged.xlsx"
    shell: "/usr/local/bin/merge_files.py {input[0]} {input[1]} {output}"

rule save_entries:
    input:  "target_merged/Merged.xlsx",
            "bender-database"
    output: "target_success/true"
    shell: "/usr/local/bin/save_entries.py {input[0]} {input[1]} {output}"
