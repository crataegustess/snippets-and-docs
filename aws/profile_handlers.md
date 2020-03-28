# how to handle profile and creds safely

There are a number of options for handling aws profiles for the command line, the work in different ways and have different strengths

## aws configure
Python based. This is the awscli built-in profile configuration tool. Roles, sts and multifactor auth are more tricky and involve a lot of typing per command

[aws reference page](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
[full featured tutorial](http://aws-cloud.guru/aws-cli-configure-roles/)

- uses .aws/config and .aws/credentials which makes configurations safer to show when training others!

## aws-profile
Python based. Good for handling multi factor auth sessions and roles

[pypi reference page](https://pypi.org/project/aws-profile/)

- does not honour parent_profile (it's an [aws-vault](https://github.com/99designs/aws-vault/issues/448) thing)
- picks up profiles and role configuration from .aws/credentials only
- thus lots of content duplication

## aws-vault
Go based. Handles role assumption, multi factor auth sessions and key chain backed credential management

[99designs github page](https://github.com/99designs/aws-vault)

- great [documentation](https://github.com/99designs/aws-vault/blob/master/USAGE.md)
- less easy to set up on service machines, more for local machines and humans!
- picks up role definitions by default from .aws/config but can be told to reference elsewhere (like .aws/credentials to avoid duplication if using aws-profile as well). Just set the `AWS_CONFIG_FILE` environment variable