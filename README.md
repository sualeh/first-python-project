# First Python Project

Reference Python project for [UNH Manchester COMP-880](https://courses.unh.edu/class/202210/15141) with use of external libraries, unit tests, CI builds.


## Explain

- What does .gitignore do?
- How do you know if you have different versions of Python installed?
  How do you know which version of Python will be used on the command-line
- What does a virtual environment do?
- How do you write unit tests? How do you test boundary conditions?


## Try Out

- Clone this project to your computer, using git from the command-line.
- Create a new Python project in PyCharm, set up a virtual environment, and open this project. 
- Install required libraries.
- Run the code in PyCharm.


## Awesome List

- [Atlassian git Tutorial](https://www.atlassian.com/git/tutorials/what-is-version-control)
- [PyCharm - Get Started](https://www.jetbrains.com/help/pycharm/quick-start-guide.html)
- [Python documentation](https://docs.python.org/3/)
- [pytest documentation](https://docs.pytest.org/en/7.1.x/contents.html)
- [The Linux Command Line by William Shotts](https://linuxcommand.org/lc3_learning_the_shell.php)


-----

## Appendix with Notes

### Set up Project and Create .gitignore
- Use [gitignore.io](https://www.toptal.com/developers/gitignore?templates=python,venv,pycharm+all) and select Python, venv, and Pycharm+all
- Run `git init` and commit changes
- Check build status in GitHub Actions with every push


### Create Virtual Environment From the Command-line

- Linux-based OS (Ubuntu, MacOS, Ubuntu on WSL)
  - Use bash in your project directory
  - Create virtual environment `python -m venv venv-linux`
  - Activate virtual environment `source venv-linux/bin/activate`
  - Run `pip -V` to confirm activation
- Windows
  - Use PowerShell in your project directory
  - Create virtual environment `python -m venv venv-win`
  - Activate virtual environment `.\venv-win\Scripts\Activate.ps1`
  - Run `pip -V` to confirm activation


### Install and Freeze Dependencies

- Run `pip install pandas` in an activated environment (for example)
- Run `pip freeze > requirements.txt`  
- To install required libraries, run `pip install -r requirements.txt`
