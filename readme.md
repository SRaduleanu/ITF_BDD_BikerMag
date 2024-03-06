## Final project for the ITFactory Manual and Automated Testing Course

### Project description:
-   Framework used: BDD
-   Feature files that contain different scenarios (simple, outline)
-   Tags that separate different tests (@T1, @T2, etc)
-   Use of multiple selectors
-   The code is structured in folders for **features, pages** and **steps**
-   The tests were made on the www.bikermag.ro website and consists of:\
        - @T1 - Scenario outline that tests the login with different invalid passwords\
        - @T2 - Scenario that tests the login with valid password\
        - @T3 - Scenario that tests the logout feature\
        - @T4 - Scenario that tests searching for a product in the search bar

---
### Installing/cloning the project:
* Open Git Bash
* Change the current working directory to the location where you want the cloned directory using the `cd` command
* Type `git clone` and paste the URL link of the repository
```
git clone https://github.com/SRaduleanu/ITF_BDD_BikerMag
```
* Press **Enter** to create your local clone
---
### Installing dependencies:
* Open the terminal and type the following command:
```
pip install -r requirements.txt
```
* Press **Enter** to install
---
### Running the tests:
All commands to be entered in the terminal
1. **Running tests:**
```
behave
```
2. **Running specific tests:**
```
behave --tags=tag_value (E.g. T1)
```
3. **Running tests with report:**
```
behave -f behave_html_formatter:HTMLFormatter -o behave-report.html
```
4. **Running specific tests with report:**
```
behave -f html-o behave-report --tags=tag_value
```