# Provisioner Pre-Commit Hooks
This repo contains scripts for the purpose of pre-commit processing
(e.g. linting) of resource provision requests.

## Installation 

The scripts in this repo can be installed by running
`pip install .` 

## Execution
Running scripts:
```
➜  check-stack-names ./config/prod/*.yaml
- stack name 'foo_stack' does not match naming requirements
- stack name 'bar stack' does not match naming requirements

A stack name can contain only alphanumeric characters (case-sensitive)
and hyphens. It must start with an alphabetic character and can't be
longer than 128 characters.
```

## Pre-commit hook
The scripts can also be [used as a pre-commit hook](https://pre-commit.com/#2-add-a-pre-commit-configuration),
by including the following in `.pre-commit-config.yaml`: 
```
-   repo: https://github.com/Sage-Bionetworks-IT/pre-commit-provisioner
    rev: INSERT_VERSION
    hooks:
    -    id: compare-stack-and-file-names
    -    id: check-stack-names
```
replacing `INSERT_VERSION` with a version tag or commit SHA-1.

## Linters

The hook `compare-stack-and-file-names` can be run from the root of
a Git repo. It will look for any files ending in `.yaml` under the
directories `./config/prod/` & `./config/dev/`, render them as Jinja2
templates, then attempt to parse the result (as YAML files) and check
that the value of `stack_name` matches the file name (minus `.yaml`).

The hook `check-stack-names` behaves similarly, but instead of checking
that a given file name matches the stack name, it will just check that
a stack name matches the [constraints specified by
CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-using-console-create-stack-parameters.html)

Currently, no arguments or other parameters can be passed to these linters.
