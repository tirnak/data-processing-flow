# data-processing-flow
This project is an implementation of simple configurable data processing flow.

### Glossary
Processing folder - folder, used by jobs either to get input (source) or to store output (target)

### Software requirements
- Pairs of processing folders are described. For each pair, where there is a file in the source folder, but not in target folder, a particular job should run. Job will create a file in the target folder.
- Check of folder pairs at regular interval
- Paths to jobs and respective folders can be configured
- Flow should be able to restart, not triggering the whole flow
- Statuses of the last job runs should be somehow exposed as success, preliminary or error

#### Jobs functionality
First Job
- adds to each row a timestamp for start of the processing
Second Job
- calculates mean of values in "nav" column
- adds to each row a z-score, based on "nav" column value and calculated mean
Third Job
- merges file A and file B on "isin" column

Script outside of the flow
- saves merged file to a fictive database.

### Non-funcitonal requirements
- Panda is expected to be used (DataFrame)
- Python is to be used.

### TBC (Assumptions)
- if file is generated in target processing folder - job is in "succcessful" status
- if job hasn't run yet - job is in "preliminary" status
- if job has run, but there is no file target processing folder - job is in "error" status
- When merging time_started generated for File A and File B, the earliest of the two will be taken
- The data in the input file is always valid, there is only one sheet per file
- It is fine to rerun any of the jobs once a minute. I.e. the jobs and input data is relatively lightweight
- Files can be preprocessed, so that they don't contain spaces

### TBA (Decisions)
- Docker should be used to have a cleaner installation and not to deal with dependency versions conflict
- In MVP logging in jobs will be done to stdout/stderr for simplicity. And then exposed via `docker logs [CONTAINER_NAME]`.
- For flow control, Snakemake could be used. With implicit dependency for the simplicity.
- There is no sense to create full-blown service, so the "Service1/2/3" will be just python scripts in MVP
- A regular job triggering can be done via crontab within resulting docker image
- Out of MVP scope: cleaning of input/intermediate/output files
- The interval to rerun the job will be 1 minute. As the minimum interval, supported by crontab.
- For the MVP, Python3 will be used. Type checks, format checks, unit testing is out of MPV.
- Minimum validation will be done for the MVP

#### project Configuration
Would consist of the following entries:
- array of job entries:
    - name
    - script to run
    - path to source processing folder
    - path to target processing folder
Provided as an argument on a startup:
- flow target folder. It must contain:
    - configuration file
    - folders, mentioned in that configuration file

#### Artifacts
- Dockerfile to create resulting image
- Scripts to be run
- Configuration file

#### Roadmap
- Write script, adding timestamps
- Write snakefile, calling the script

- Write script, adding z-score
- Extend snakefile to call added script

- Write script, adding merging of File A and File B
- Extend snakefile to call added script

- write Dockerfile to run snakefile and the scripts inside
- write docker-compose file to provide mounted directory

- add crontab to the dockerfile
- add "panoptes" server for the visualization
