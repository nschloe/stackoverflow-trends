<p align="center">
  <a href="https://github.com/nschloe/sotrends"><img alt="sotrends-logo" src="https://nschloe.github.io/sotrends/sotrends-logo-path.svg" width="50%"></a>
  <p align="center">StackOverflow tag history.</p>
</p>

[![PyPi Version](https://img.shields.io/pypi/v/sotrends.svg?style=flat-square)](https://pypi.org/project/sotrends)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/sotrends.svg?style=flat-square)](https://pypi.org/pypi/sotrends/)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/sotrends.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/sotrends)
[![PyPi downloads](https://img.shields.io/pypi/dm/sotrends.svg?style=flat-square)](https://pypistats.org/packages/sotrends)

[![gh-actions](https://img.shields.io/github/workflow/status/nschloe/sotrends/ci?style=flat-square)](https://github.com/nschloe/sotrends/actions?query=workflow%3Aci)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/sotrends.svg?style=flat-square)](https://codecov.io/gh/nschloe/sotrends)
[![LGTM](https://img.shields.io/lgtm/grade/python/github/nschloe/sotrends.svg?style=flat-square)](https://lgtm.com/projects/g/nschloe/sotrends)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

sotrends provides Python and command-line tools for collecting popularity data from
[GitHub stars](http://github.com/) and [StackOverflow tags](https://stackoverflow.com/)
and producing nice plots from it.

For example, the plot

![stackoverflow-shells](https://nschloe.github.io/sotrends/so-example.svg)

is produced with

```
sotrends-so-tag-history numpy scipy pandas matplotlib tensorflow
```

StackOverflow has a rate limit, so you might want to get a token and provide it to
sotrends.

Install with

```
pip install sotrends
```

and use the command-line tool as displayed. The `-h` switch gives more details.

## Gallery

A collection of the StackOverflow popularity of a number of topics.

#### Programming languages

![stackoverflow-programming-languages](https://nschloe.github.io/sotrends/stackoverflow-programming-languages.svg)

#### Version control systems

![stackoverflow-vcs](https://nschloe.github.io/sotrends/stackoverflow-vcs.svg)

#### Front-End frameworks

![stackoverflow-frontend-frameworks](https://nschloe.github.io/sotrends/stackoverflow-frontend-frameworks.svg)

#### Back-End frameworks

![stackoverflow-backend-frameworks](https://nschloe.github.io/sotrends/stackoverflow-backend-frameworks.svg)

#### Browsers

![stackoverflow-browsers](https://nschloe.github.io/sotrends/stackoverflow-browsers.svg)

#### Databases

![stackoverflow-databases](https://nschloe.github.io/sotrends/stackoverflow-databases.svg)

#### JavaScript package managers

![stackoverflow-javascript-package-managers](https://nschloe.github.io/sotrends/stackoverflow-javascript-package-managers.svg)

#### JavaScript testing frameworks

![stackoverflow-testing-frameworks](https://nschloe.github.io/sotrends/stackoverflow-javascript-testing-frameworks.svg)

#### Text editors

![stackoverflow-text-editors](https://nschloe.github.io/sotrends/stackoverflow-text-editors.svg)

#### Operating systems

![stackoverflow-operating-systems](https://nschloe.github.io/sotrends/stackoverflow-operating-systems.svg)

#### Mobile operating systems

<img src="https://nschloe.github.io/sotrends/stackoverflow-mobile-operating-systems.svg" width="60%">

#### Shells

![stackoverflow-shells](https://nschloe.github.io/sotrends/stackoverflow-shells.svg)

#### Code-hosting platforms

![stackoverflow-code-hosting-platforms](https://nschloe.github.io/sotrends/stackoverflow-code-hosting-platforms.svg)

#### Content-management systems

![stackoverflow-content-management-systems](https://nschloe.github.io/sotrends/stackoverflow-content-management-systems.svg)

#### Continuous-integration services

![stackoverflow-continuous-integration-services](https://nschloe.github.io/sotrends/stackoverflow-continuous-integration-services.svg)

#### Office suites

![stackoverflow-office-suites](https://nschloe.github.io/sotrends/stackoverflow-office-suites.svg)

#### Computer algebra systems

![stackoverflow-computer-algebra-systems](https://nschloe.github.io/sotrends/stackoverflow-computer-algebra-systems.svg)

#### DevOps

![stackoverflow-devops](https://nschloe.github.io/sotrends/stackoverflow-devops.svg)

#### Build systems

![stackoverflow-build-systems](https://nschloe.github.io/sotrends/stackoverflow-build-systems.svg)

#### Machine learning

![stackoverflow-machine-learning](https://nschloe.github.io/sotrends/stackoverflow-machine-learning.svg)

#### Scientific Python

![stackoverflow-scientific-python](https://nschloe.github.io/sotrends/stackoverflow-scientific-python.svg)

#### Python plotting

![stackoverflow-python-plotting](https://nschloe.github.io/sotrends/stackoverflow-python-plotting.svg)

#### Python testing

![stackoverflow-python-testing](https://nschloe.github.io/sotrends/stackoverflow-python-testing.svg)

#### JavaScript visualization

![stackoverflow-javascript-visualization](https://nschloe.github.io/sotrends/stackoverflow-javascript-visualization.svg)

#### Popular JavaScript packages

![stackoverflow-popular-javascript](https://nschloe.github.io/sotrends/stackoverflow-popular-javascript.svg)

#### Linux desktop environments

![stackoverflow-~stackoverflow-linux-desktop-environments](https://nschloe.github.io/sotrends/stackoverflow-linux-desktop-environments.svg)

#### Serialization formats

![stackoverflow-serialization-formats](https://nschloe.github.io/sotrends/stackoverflow-serialization-formats.svg)

#### Messaging platforms

![stackoverflow-messaging-platforms](https://nschloe.github.io/sotrends/stackoverflow-messaging-platforms.svg)

#### CSS frameworks

![stackoverflow-css-frameworks](https://nschloe.github.io/sotrends/stackoverflow-css-frameworks.svg)

### Related projects

- [Stack Overflow Trends](https://insights.stackoverflow.com/trends)
