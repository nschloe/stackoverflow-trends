<p align="center">
  <a href="https://github.com/nschloe/hotware"><img alt="hotware-logo" src="https://nschloe.github.io/hotware/hotware-logo-path.svg" width="50%"></a>
  <p align="center">StackOverflow tag history.</p>
</p>

[![gh-actions](https://img.shields.io/github/workflow/status/nschloe/hotware/ci?style=flat-square)](https://github.com/nschloe/hotware/actions?query=workflow%3Aci)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/hotware.svg?style=flat-square)](https://pypi.org/pypi/hotware/)
[![PyPi Version](https://img.shields.io/pypi/v/hotware.svg?style=flat-square)](https://pypi.org/project/hotware)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/hotware.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/hotware)
[![PyPi downloads](https://img.shields.io/pypi/dm/hotware.svg?style=flat-square)](https://pypistats.org/packages/hotware)

hotware provides Python and command-line tools for collecting popularity data from
[GitHub stars](http://github.com/) and [StackOverflow tags](https://stackoverflow.com/)
and producing nice plots from it.

For example, the plot

![stackoverflow-shells](https://nschloe.github.io/hotware/so-example.svg)

is produced with
```
hotware-so-tag-history numpy scipy pandas matplotlib tensorflow
```
StackOverflow has a rate limit, so you might want to get a token and provide it to
hotware.

Install with
```
pip install hotware
```
and use the command-line tool as displayed. The `-h` switch gives more details.

## Gallery

A collection of the StackOverflow popularity of a number of topics.

#### Programming languages
![stackoverflow-programming-languages](https://nschloe.github.io/hotware/stackoverflow-programming-languages.svg)

#### Version control systems
![stackoverflow-vcs](https://nschloe.github.io/hotware/stackoverflow-vcs.svg)

#### Front-End frameworks
![stackoverflow-frontend-frameworks](https://nschloe.github.io/hotware/stackoverflow-frontend-frameworks.svg)

#### Back-End frameworks
![stackoverflow-backend-frameworks](https://nschloe.github.io/hotware/stackoverflow-backend-frameworks.svg)

#### Browsers
![stackoverflow-browsers](https://nschloe.github.io/hotware/stackoverflow-browsers.svg)

#### Databases
![stackoverflow-databases](https://nschloe.github.io/hotware/stackoverflow-databases.svg)

#### JavaScript package managers
![stackoverflow-javascript-package-managers](https://nschloe.github.io/hotware/stackoverflow-javascript-package-managers.svg)

#### JavaScript testing frameworks
![stackoverflow-testing-frameworks](https://nschloe.github.io/hotware/stackoverflow-javascript-testing-frameworks.svg)

#### Text editors
![stackoverflow-text-editors](https://nschloe.github.io/hotware/stackoverflow-text-editors.svg)

#### Operating systems
![stackoverflow-operating-systems](https://nschloe.github.io/hotware/stackoverflow-operating-systems.svg)

#### Mobile operating systems
<img src="https://nschloe.github.io/hotware/stackoverflow-mobile-operating-systems.svg" width="60%">

#### Shells
![stackoverflow-shells](https://nschloe.github.io/hotware/stackoverflow-shells.svg)

#### Code-hosting platforms
![stackoverflow-code-hosting-platforms](https://nschloe.github.io/hotware/stackoverflow-code-hosting-platforms.svg)

#### Content-management systems
![stackoverflow-content-management-systems](https://nschloe.github.io/hotware/stackoverflow-content-management-systems.svg)

#### Continuous-integration services
![stackoverflow-continuous-integration-services](https://nschloe.github.io/hotware/stackoverflow-continuous-integration-services.svg)

#### Office suites
![stackoverflow-office-suites](https://nschloe.github.io/hotware/stackoverflow-office-suites.svg)

#### Computer algebra systems
![stackoverflow-computer-algebra-systems](https://nschloe.github.io/hotware/stackoverflow-computer-algebra-systems.svg)

#### DevOps
![stackoverflow-devops](https://nschloe.github.io/hotware/stackoverflow-devops.svg)

#### Build systems
![stackoverflow-build-systems](https://nschloe.github.io/hotware/stackoverflow-build-systems.svg)

#### Machine learning
![stackoverflow-machine-learning](https://nschloe.github.io/hotware/stackoverflow-machine-learning.svg)

#### Scientific Python
![stackoverflow-scientific-python](https://nschloe.github.io/hotware/stackoverflow-scientific-python.svg)

#### Python plotting
![stackoverflow-python-plotting](https://nschloe.github.io/hotware/stackoverflow-python-plotting.svg)

#### Python testing
![stackoverflow-python-testing](https://nschloe.github.io/hotware/stackoverflow-python-testing.svg)

#### Popular JavaScript packages
![stackoverflow-popular-javascript](https://nschloe.github.io/hotware/stackoverflow-popular-javascript.svg)


### Related projects

 * [Stack Overflow Trends](https://insights.stackoverflow.com/trends)

### License
This software is published under the [GPLv3 license](https://www.gnu.org/licenses/gpl-3.0.en.html).
