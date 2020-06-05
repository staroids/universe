<br /><br />
<p align="center">
  <img src="https://docs.staroid.com/_images/staroid_logo.svg" width="250px" />
</p>
<br />

# ⭐️ Universe

This repo is the source for projects listed in Staroid [Universe](https://staroid.com/universe). Staroid Universe is a project registry in [Staroid](https://staroid.com), a Cloud platform for open-source projects that [funds its developers](https://staroid.com/site/starrank).

## Registries

Universe provides 3 class of registries depending on the maturity of the project as a service.

- Incubator
- Production
- Enterprise
 
## Review criteria

It sounds a lot. But don't worry. We're here to help you go through the review. Don't hesitate to make a pull request and ask review.

We'd like to build a consistent expectation on projects in each class. We believe these review criteria help your user to have more confidence in your project. For personal use or  professional use, as well as for mission-critical work.

### Incubator

 - Usability
   - The primary function should work out of the box without requiring external dependencies and resources.
 - Community
   - A community should present so users can ask questions and get help.
 - License
   - The project should have a License file in the repository.
   - The project shouldn't have any software license violations.
 - Security
   - The project need to be secure enough to prevent unintended use.
 - Privacy
   - The project should handle user data securely.
   - The project shouldn't collect unnecessary data from user.
  - Cost optimization
   - The project should use a minimum amount of resources to complete its designed task.

### Production

 - Availability
   - Shows 99.95% availability with more than 7200 hours of total instance run time for last 30 days in incubation.
 - Fault tolerance
   - Able to recover automatically from container crash/vm migration.
 - Automatic upgrade
   - The project should upgrade to the new version without human intervention.
 - Backup
   - The project should provide a way to backup and restore data.


### Enterprise

 - Commercial support option
   - The project need to provides one or more certified commercial support options.
 - Automatic backup
   - Backup for essential data needs to be created automatically.


## Add your project

1. Make sure your project runs on Staroid platform by creating [staroid.yaml](https://docs.staroid.com/references/staroid_yaml.html).
2. Set 'Launch permission' to 'Public' in the release tab.
3. Fork this repository and write [package.yaml](https://github.com/staroids/universe/blob/master/package.yaml_template) in `/incubator/<your project name>` directory.

4. Make a pull request.

## Request class change

Move your project package.yaml to 'production' or 'enterprise' directory and create a pull request.
