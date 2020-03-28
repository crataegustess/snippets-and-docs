# file types in terraform

These differ by version as the prcoess has evolved

## v0.12

- main.tf
- variables.tf
- some_specific_thing.tf
- override.tf or some_specific_thing_override.tf (not usually checked in / environment specific)

There is a hierachy to the application of overrides - https://www.terraform.io/docs/configuration/override.html

## v0.11

- main.tf
- terraform.tfvars or *.auto.tfvars
- some_specific_thing.tf
- override.tf or some_specific_thing_override.tf (not usually checked in / environment specific)
