# Contributing to the compiler

Instructions for contributing a recipe can be found [here](https://microsoft.github.io/DevCookbook/contribute/).

## How to clone and set up the repository

Please make a [fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) of the repository if you would like to make a contribution.

Clone your fork with `git clone`

``` bash
git clone https://github.com/<YOUR-GITHUB-USERNAME>/DevCookbook
```

### Linux

Change directory into the project:

``` bash 
cd DevCookbook
```

Create a virtual environment for installing packages:

``` bash
python3.9 -m venv .venv
```

Activate the virtual environment:

``` bash
source .venv/bin/activate
```

Install the required dependencies:

``` bash
pip install -r requirements.txt
```

### Windows

Change directory into the project:

``` powershell
cd DevCookbook
```

Create a virtual environment for installing packages:

``` powershell
python3.9 -m venv .venv
```

Activate the virtual environment:

``` powershell
.venv\Scripts\Activate.ps1
```

> Note, you may run into this error
>
> ``` powershell
> .\.venv\Scripts\Activate.ps1 : File C:\Users\<username>\devcookbook\.venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system.
> For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
> ```
> 
> To solve this problem run the following script in an elevated terminal:
>
> ``` powershell
> Set-ExecutionPolicy RemoteSigned
> ```
>
> [More information on PowerShell execution policies](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.1)

Install the required dependencies:

``` powershell
pip install -r requirements.txt
```

## Compile and run the site locally

``` bash
python compile.py -t dev
```

This will output the HTML and CSS that make up the static site in the `docs` directory.

You can serve this HTML using 

``` bash
python -m http.server --directory docs
```
