# EtherCar

# Executive Summary

EtherCar is our Web 3.0 luxury rental car application designed to allow users to experience luxury travel.  The purpose of this tool is to give clients the ability to find vehicles that match their respective lifestyles.  From touring the streets of New York to cruising the beaches of Miami, EtherCar will enhance your trips, all with an ironclad layer of security offered by the Ethereum Blockchain.

## How To Run
1. Download NodeJS https://nodejs.org/en/download/
2. Run `npm install`. It will install dependencues on package.json
3. Run `npx truffle compile`. This uses truffle to compile the contract.
4. Run `npx truffle develop`. Truffle suite contains a personal blockchain that we can use for testing purposes. You should see an output similar to the following:
    ```
    Truffle Develop started at http://127.0.0.1:9545/

    Accounts:
    (0) 0xdfb772fba7631b5bfde93cc3e2b0e488d1a17b2a
    ...
    (9) 0x974779d6a98264043e8bb1c8b0cf93d9c7141a29

    Private Keys:
    ...

    truffle(develop)>
    ```
5. In the terminal `truffle(develop)>`, run `migrate`.
6. Copy contract address to app.py
    ```
    2_deploy_contracts.js
    =====================

    Replacing 'Rental'
    ------------------
    > transaction hash:    0x02917cc0f53fb5c36a6eb166f6848a44f32f17c2f732ac9b9c9b098dbe7fac71
    > Blocks: 0            Seconds: 0
    > contract address:    0x56528890De031184b007694D73965CE82CfcA043
    ```

7. Open another terminal window, and run this:
    ```
    $ pip3 install web3
    $ python3 app.py
    ```


## Sample Prompts (Amazon Lex)
? What is your current age 25

? By what age, would you prefer to retire? 65

? How much do you have in liquid cash savings (USD) 50000

? Would you like your portfolio to be conservative[1], conservatively moderate[2], or moderate[3]? 3

? How much would you like to invest in stocks and bonds? 40000

## Sample Output/Response
You can retire in
['Paris/France', 'Hamilton/Canada', 'Milan/Italy', 'Bucaramanga/Colombia', 'Madrid/Spain', 'Delhi/India']


# For Users -- General Overview & Flow

Part 1: Data inputs will be generated to determine the years in retirement, size and risk profile of the user's investment portfolio, and historical growth rates of indices.    

Part 2: Users will forecast the performance of their portfolio at the age they wish to retire until the time they choose to retire. Historical price data will be used to generate Monte Carlo simulations to compute total savings (mean) for the time, which elapses btwn the user's current age and the year they prefer to retire.

Part 3: This total cash savings, in addition to asset appreciation will be exported to the Cost of Living Calculator to determine the list of viable cities where the user can retire.

# List of Cities within Scope of Analysis
Hamilton (Bermuda)
<br>
Hong Kong
<br>
Los Angeles
<br>
Paris
<br>
Milan
<br>
Bucaramanga (Colombia)
<br>
Mardrid
<br>
Delhi
<br>
Hamilton (Canada)


---

# Documents

###Team Presentation (Slides)
<br>
https://docs.google.com/presentation/d/1elToGQYKbCMz6aAhTmMEh6qNynDNbQPG_OPiWubgP3Q/edit?usp=sharing


###Team Charter
<br>
https://docs.google.com/document/d/1lY8t0cZMxxiIFc68L89hNWnGC5Kwznit7YF4jXzV9yA/edit?usp=sharing
---

## Technologies

Required programs, libraries, systems, and overall dependencies:
<br>
Python (version 3.0 or later)
<br>
`Pathlib`
<br>
`pandas`
<br>
`%matplotlib`
<br>
`hvplot.pandas`
<br>
`sqlalchemy`
<br>
`numpy`
<br>
`simulation`
<br>
`fileio`
<br>
`fire==0.4.0`
<br>
pip==22.0.4
<br>
prompt-toolkit==3.0.28
<br>
questionary==1.10.0
<br>
setuptools==58.1.0
<br>
six==1.16.0
<br>
termcolor==1.1.0
<br>
wcwidth==0.2.5
<br>
wheel==0.37.1
<br>
---

## Installation Guide

`pip install Voila`
<br>
`pip install Fire`
<br>
`pip install folium`
<br>
`conda install -c pyviz hvplot geoviews`

---

## Usage of Retirement Global 2.0 App

Getting User info:

```python
import questionary
def get_retire_plan_user():
    age = questionary.text("What is your current age").ask()
    retirement_age = questionary.text("By what age, would you prefer to retire?").ask()
    savings = questionary.text("How much do you have in liquid cash savings (USD)").ask()
    portfolio_type = questionary.text("Would you like your portfolio to be conservative[1], conservatively moderate[2], or moderate[3]? (Enter 1, 2, or 3)").ask()
    total_stocks_bonds = questionary.text("How much would you like to invest in stocks and bonds?").ask()
        
    age = int(age)
    retirement_age = int(retirement_age)
    savings = float(savings)
    portfolio_type = int(portfolio_type)
    total_stocks_bonds = float(total_stocks_bonds)
    return age, retirement_age, savings, portfolio_type, total_stocks_bonds
```

Snippet of Monte Carlo code

```python
output = simulation.run_mc_output(df_portfolio, portfolio_type, years_to_retirement)
output
output.calc_cumulative_return()
```

## View of Amazon Lex Screen
![view_Lex_screen](https://github.com/gatsbyz/blue-sky-retirement-plus/blob/Reggie/Amazon_Lex_screen.png)

## Short Clip of Amazon Lex Chatbot
![view_Lex_screen](https://github.com/gatsbyz/blue-sky-retirement-plus/blob/Reggie/Lex_clip.mp4)

## Forecast Simulation
![sample_output_MC](https://user-images.githubusercontent.com/11021924/168452488-f5470627-b15b-4166-8dd5-ace160e4e9c0.png)


---

# Useful GitHub commands for Group Coordination

`git checkout -b [BRANCH_NAME]`: new branch

`git checkout [BRANCH_NAME]`: change branch

`git branch` : which branch am I in

when i wanna push code:
<br>
`git add -A` / `git add filename`
<br>
`git commit -m "COMMIT_MESSAGE"`
<br>
`git push`
if this doesn’t work
`git pull --rebase origin master` then try `git push` again

`git branch -D {BRANCH_NAME}` delete branch

---

## Contributors

Tracy Davis
<br>
Reginald Hyppolite
<br>
Jesse Lee
<br>
Wonkyung Lee
<br>
Tyler Shubert

BIG THANKS to all the great TAs and Professor Vinicio DeSola

---

## License
MIT