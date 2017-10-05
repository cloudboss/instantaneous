# instantaneous

Ansible: the missing modules, filters, and plugins.

# Requirements

## Python libraries

[friend](https://github.com/cloudboss/friend)

Use of a Python virtualenv is recommended.

In a virtualenv, run:

```
pip install -r requirements.txt
```

# Usage

## Filter plugins

### snake_to_pascal

Convert "snake_case" strings to "PascalCase". If a dictionary is given instead of a string, the dictionary keys are recursively converted. If a list is given, the items of the list are converted according to the same rules. This is useful for keeping the Ansible idiom of using snake case variable names, while outputting pascal case in CloudFormation templates, for example.

#### Example

Somewhere in a playbook...

```
- hosts: localhost
  vars:
    app_stack:
      block_device_mappings:
        - device_name: /dev/sdf
          ebs:
            delete_on_termination: true
            encrypted: true
            volume_size: 500
            volume_type: gp2
  tasks:
    - name: expand cloudformation template
      template:
        src: path/to/stack.yml.j2
		dest: .cache/app_stack-{{ environment }}/stack.yml
```

And in the Jinja2 template `stack.yml.j2`:

```
Resources:
  AppServerLaunchConfiguration:
    Type: AWS::AutoScaling::LaunchConfiguration
    Properties:
      AssociatePublicIpAddress: false
      BlockDeviceMappings: {{ app_stack.block_device_mappings | snake_to_pascal | to_json }}
```

Yes, that does say `to_json` in a YAML file. JSON _is_ valid YAML, and doing it this way avoids indentation issues.

### snake_to_camel

Like `snake_to_pascal`, but outputs "camelCase" strings starting with lower case.

### camel_to_snake

Does the opposite of `snake_to_pascal` and `snake_to_camel`, converting either a camel case or pascal case string or object to snake case.

# License

MIT

# Author Information

Joseph Wright <joseph@cloudboss.co>
