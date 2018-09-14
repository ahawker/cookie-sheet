"""
    pre_gen_project.py
    ~~~~~~~~~~~~~~~~~~

    Script that is triggered before Cookiecutter starts generating the project.
"""
import sys
import json


def stderr(msg):
    sys.stderr.write('{}\n'.format(msg))
    sys.stderr.flush()


def validate_context(context):
    """
    Validate Cookiecutter context variables used to generate the project.
    """
    for key, value in context.items():
        if not value:
            value_type = type(value)
            if value_type in (bool, int, float):
                stderr('WARNING: Key "{}" of type "{}" using falsey value "{}"'.format(key, value_type.name, value))
                continue
            stderr('ERROR: Variable "{}" is not set'.format(key))
            break
    else:
        return 0
    raise SystemExit("Cannot create project, invalid context")


def main(args):
    context = {{ cookiecutter }}
    validate_context(context)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
