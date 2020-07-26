<p align="center">
  <a href="https://github.com/nschloe/stacktags"><img alt="stacktags-logo" src="https://nschloe.github.io/stacktags/stacktags-logo-path.svg" width="50%"></a>
  <p align="center">StackOverflow tag history.</p>
</p>

[![gh-actions](https://img.shields.io/github/workflow/status/nschloe/stacktags/ci?style=flat-square)](https://github.com/nschloe/stacktags/actions?query=workflow%3Aci)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/stacktags.svg?style=flat-square)](https://pypi.org/pypi/stacktags/)
[![PyPi Version](https://img.shields.io/pypi/v/stacktags.svg?style=flat-square)](https://pypi.org/project/stacktags)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/stacktags.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/stacktags)
[![PyPi downloads](https://img.shields.io/pypi/dm/stacktags.svg?style=flat-square)](https://pypistats.org/packages/stacktags)

stacktags provides Python and command-line tools for collecting popularity data from
[GitHub stars](http://github.com/) and [StackOverflow tags](https://stackoverflow.com/)
and producing nice plots from it.

For example, the plot

![stackoverflow-shells](https://nschloe.github.io/stacktags/so-example.svg)

is produced with
```
stacktags-so-tag-history numpy scipy pandas matplotlib tensorflow
```
StackOverflow has a rate limit, so you might want to get a token and provide it to
stacktags.

Install with
```
pip install stacktags
```
and use the command-line tool as displayed. The `-h` switch gives more details.

## Gallery

A collection of the StackOverflow popularity of a number of topics.

#### Programming languages
![stackoverflow-programming-languages](https://nschloe.github.io/stacktags/stackoverflow-programming-languages.svg)

#### Version control systems
![stackoverflow-vcs](https://nschloe.github.io/stacktags/stackoverflow-vcs.svg)

#### Front-End frameworks
![stackoverflow-frontend-frameworks](https://nschloe.github.io/stacktags/stackoverflow-frontend-frameworks.svg)

#### Back-End frameworks
![stackoverflow-backend-frameworks](https://nschloe.github.io/stacktags/stackoverflow-backend-frameworks.svg)

#### Browsers
![stackoverflow-browsers](https://nschloe.github.io/stacktags/stackoverflow-browsers.svg)

#### Databases
![stackoverflow-databases](https://nschloe.github.io/stacktags/stackoverflow-databases.svg)

#### JavaScript package managers
![stackoverflow-javascript-package-managers](https://nschloe.github.io/stacktags/stackoverflow-javascript-package-managers.svg)

#### JavaScript testing frameworks
![stackoverflow-testing-frameworks](https://nschloe.github.io/stacktags/stackoverflow-javascript-testing-frameworks.svg)

#### Text editors
![stackoverflow-text-editors](https://nschloe.github.io/stacktags/stackoverflow-text-editors.svg)

#### Operating systems
![stackoverflow-operating-systems](https://nschloe.github.io/stacktags/stackoverflow-operating-systems.svg)

#### Mobile operating systems
<img src="https://nschloe.github.io/stacktags/stackoverflow-mobile-operating-systems.svg" width="60%">

#### Shells
![stackoverflow-shells](https://nschloe.github.io/stacktags/stackoverflow-shells.svg)

#### Code-hosting platforms
![stackoverflow-code-hosting-platforms](https://nschloe.github.io/stacktags/stackoverflow-code-hosting-platforms.svg)

#### Content-management systems
![stackoverflow-content-management-systems](https://nschloe.github.io/stacktags/stackoverflow-content-management-systems.svg)

#### Continuous-integration services
![stackoverflow-continuous-integration-services](https://nschloe.github.io/stacktags/stackoverflow-continuous-integration-services.svg)

#### Office suites
![stackoverflow-office-suites](https://nschloe.github.io/stacktags/stackoverflow-office-suites.svg)

#### Computer algebra systems
![stackoverflow-computer-algebra-systems](https://nschloe.github.io/stacktags/stackoverflow-computer-algebra-systems.svg)

#### DevOps
![stackoverflow-devops](https://nschloe.github.io/stacktags/stackoverflow-devops.svg)

#### Build systems
![stackoverflow-build-systems](https://nschloe.github.io/stacktags/stackoverflow-build-systems.svg)

#### Machine learning
![stackoverflow-machine-learning](https://nschloe.github.io/stacktags/stackoverflow-machine-learning.svg)

#### Scientific Python
![stackoverflow-scientific-python](https://nschloe.github.io/stacktags/stackoverflow-scientific-python.svg)

#### Python plotting
![stackoverflow-python-plotting](https://nschloe.github.io/stacktags/stackoverflow-python-plotting.svg)

#### Python testing
![stackoverflow-python-testing](https://nschloe.github.io/stacktags/stackoverflow-python-testing.svg)

#### Popular JavaScript packages
![stackoverflow-popular-javascript](https://nschloe.github.io/stacktags/stackoverflow-popular-javascript.svg)

#### Linux desktop environments
![stackoverflow-~stackoverflow-linux-desktop-environments](https://nschloe.github.io/stacktags/stackoverflow-linux-desktop-environments.svg)


#### Serialization formats
![~stackoverflow-serialization-formats](https://nschloe.github.io/stacktags/~stackoverflow-serialization-formats.svg)


### Related projects

 * [Stack Overflow Trends](https://insights.stackoverflow.com/trends)

### License
This software is published under the [GPLv3 license](https://www.gnu.org/licenses/gpl-3.0.en.html).
