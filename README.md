# System Register

Shows all active instances that run on a computing resource

## Workflow

The application requires an initial list of processes which will be monitored, then the system's process tree will be checked for all the active instances of a process, saving those instances in a separate output file (a so-called *process register*).

After all the process registers have benn created, the application checks if any instance has stopped, and if true, it will raise an alert.
