<p align="center">
  <a href="https://github.com/nschloe/hotware"><img alt="hotware-logo" src="https://nschloe.github.io/hotware/hotware-logo-path.svg" width="50%"></a>
  <p align="center">How popular is it?</p>
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

For example, the plots

![github-nschloe](https://nschloe.github.io/hotware/nschloe.svg) | ![stackoverflow-shells](https://nschloe.github.io/hotware/so-example.svg)
:-------------------:|:------------------:|

are produced with
```
hotware-gh-star-history nschloe/meshio nschloe/quadpy -m 30 -t githubtoken0123 -o nschloe.svg
```
```
hotware-so-tag-history numpy scipy pandas matplotlib tensorflow
```
Both GitHub and StackOverflow have a rate limit, so you might want to get a token and
provide it to hotware.

Install with
```
pip install hotware
```
and use the command-line tools as displayed. The `-h` switch gives more details.

## Gallery

A collection of the GitHub/StackOverflow popularity of a number of topics.

#### Programming languages
![github-programming-languages](https://nschloe.github.io/hotware/github-programming-languages.svg) | ![stackoverflow-programming-languages](https://nschloe.github.io/hotware/stackoverflow-programming-languages.svg)
:-------------------:|:------------------:|

#### Version control systems
![github-vcs](https://nschloe.github.io/hotware/github-version-control-systems.svg) | ![stackoverflow-vcs](https://nschloe.github.io/hotware/stackoverflow-vcs.svg)
:-------------------:|:------------------:|

#### Front-End frameworks
![github-frontend-frameworks](https://nschloe.github.io/hotware/github-frontend-frameworks.svg) | ![stackoverflow-frontend-frameworks](https://nschloe.github.io/hotware/stackoverflow-frontend-frameworks.svg)
:-------------------:|:------------------:|

#### Back-End frameworks
![github-backend-frameworks](https://nschloe.github.io/hotware/github-backend-frameworks.svg) | ![stackoverflow-backend-frameworks](https://nschloe.github.io/hotware/stackoverflow-backend-frameworks.svg)
:-------------------:|:------------------:|

#### Browsers
![github-browsers](https://nschloe.github.io/hotware/github-browsers.svg) | ![stackoverflow-browsers](https://nschloe.github.io/hotware/stackoverflow-browsers.svg)
:-------------------:|:------------------:|

#### Databases
![github-databases](https://nschloe.github.io/hotware/github-databases.svg) | ![stackoverflow-databases](https://nschloe.github.io/hotware/stackoverflow-databases.svg)
:-------------------:|:------------------:|

#### JavaScript package managers
![github-javascript-package-managers](https://nschloe.github.io/hotware/github-javascript-package-managers.svg) | ![stackoverflow-javascript-package-managers](https://nschloe.github.io/hotware/stackoverflow-javascript-package-managers.svg)
:-------------------:|:------------------:|

#### JavaScript testing frameworks
![github-javascript-testing-frameworks](https://nschloe.github.io/hotware/github-javascript-testing-frameworks.svg) | ![stackoverflow-testing-frameworks](https://nschloe.github.io/hotware/stackoverflow-javascript-testing-frameworks.svg)
:-------------------:|:------------------:|

#### Text editors
![github-text-editors](https://nschloe.github.io/hotware/github-text-editors.svg) | ![stackoverflow-text-editors](https://nschloe.github.io/hotware/stackoverflow-text-editors.svg)
:-------------------:|:------------------:|

#### Operating systems
![github-operating-systems](https://nschloe.github.io/hotware/github-operating-systems.svg) | ![stackoverflow-operating-systems](https://nschloe.github.io/hotware/stackoverflow-operating-systems.svg)
:-------------------:|:------------------:|

#### Mobile operating systems
<img src="https://nschloe.github.io/hotware/stackoverflow-mobile-operating-systems.svg" width="60%">

#### Shells
![github-shells](https://nschloe.github.io/hotware/github-shells.svg) | ![stackoverflow-shells](https://nschloe.github.io/hotware/stackoverflow-shells.svg)
:-------------------:|:------------------:|

#### Code-hosting platforms
![github-code-hosting-platforms](https://nschloe.github.io/hotware/github-code-hosting-platforms.svg) | ![stackoverflow-code-hosting-platforms](https://nschloe.github.io/hotware/stackoverflow-code-hosting-platforms.svg)
:-------------------:|:------------------:|

#### Content-management systems
![github-content-management-systems](https://nschloe.github.io/hotware/github-content-management-systems.svg) | ![stackoverflow-content-management-systems](https://nschloe.github.io/hotware/stackoverflow-content-management-systems.svg)
:-------------------:|:------------------:|

#### Continuous-integration services
![github-continuous-integration-services](https://nschloe.github.io/hotware/github-continuous-integration-services.svg) | ![stackoverflow-continuous-integration-services](https://nschloe.github.io/hotware/stackoverflow-continuous-integration-services.svg)
:-------------------:|:------------------:|

#### Office suites
![github-office-suites](https://nschloe.github.io/hotware/github-office-suites.svg) | ![stackoverflow-office-suites](https://nschloe.github.io/hotware/stackoverflow-office-suites.svg)
:-------------------:|:------------------:|

#### Computer algebra systems
![github-computer-algebra-systems](https://nschloe.github.io/hotware/github-computer-algebra-systems.svg) | ![stackoverflow-computer-algebra-systems](https://nschloe.github.io/hotware/stackoverflow-computer-algebra-systems.svg)
:-------------------:|:------------------:|

#### DevOps
![github-devops](https://nschloe.github.io/hotware/github-devops.svg) | ![stackoverflow-devops](https://nschloe.github.io/hotware/stackoverflow-devops.svg)
:-------------------:|:------------------:|

#### Build systems
![github-build-systems](https://nschloe.github.io/hotware/github-build-systems.svg) | ![stackoverflow-build-systems](https://nschloe.github.io/hotware/stackoverflow-build-systems.svg)
:-------------------:|:------------------:|

#### Machine learning
![github-machine-learning](https://nschloe.github.io/hotware/github-machine-learning.svg) | ![stackoverflow-machine-learning](https://nschloe.github.io/hotware/stackoverflow-machine-learning.svg)
:-------------------:|:------------------:|

#### Scientific Python
![github-scientific-python](https://nschloe.github.io/hotware/github-scientific-python.svg) | ![stackoverflow-scientific-python](https://nschloe.github.io/hotware/stackoverflow-scientific-python.svg)
:-------------------:|:------------------:|

#### Python plotting
![github-python-plotting](https://nschloe.github.io/hotware/github-python-plotting.svg) | ![stackoverflow-python-plotting](https://nschloe.github.io/hotware/stackoverflow-python-plotting.svg)
:-------------------:|:------------------:|

#### Python testing
![github-python-testing](https://nschloe.github.io/hotware/github-python-testing.svg) | ![stackoverflow-python-testing](https://nschloe.github.io/hotware/stackoverflow-python-testing.svg)
:-------------------:|:------------------:|

#### Popular JavaScript packages
![github-popular-javascript](https://nschloe.github.io/hotware/github-popular-javascript.svg) | ![stackoverflow-popular-javascript](https://nschloe.github.io/hotware/stackoverflow-popular-javascript.svg)
:-------------------:|:------------------:|


### Related projects

 * [Stack Overflow Trends](https://insights.stackoverflow.com/trends)

### License
This software is published under the [GPLv3 license](https://www.gnu.org/licenses/gpl-3.0.en.html).
