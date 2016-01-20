# eudaq-configuration
Configuration repository and start scripts for specific EUDAQ deployments

This repository holds all necessary configuration files and specific start stcripts for the deployment of EUDAQ with a given telescope installation.

The configuration files and scripts contain hardcoded values tuned to the respective detector and test beam environment, such as threshold values or network IP addresses.

Users are asked to fork this repository in order to have a starting version for developing and optimizing the configuration files including their own detectors. Updates of the telescope configuration can be fetched by merging the upstream changes from this repository via

```
git remote add upstream https://github.com/eudaq/eudaq-configuration.git
git pull upstream master
```