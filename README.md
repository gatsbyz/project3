###ETHERCAR

##Executive Summary 

EtherCar is an on-chain platform for car rentals. Among the numerous benefits that come with blockchain technology, privacy and data security is a critical one. Consumer data is constantly at risk of data breaches leading to not just millions of accounts getting compromised, but also leading to billions of dollars in industry losses. With blockchain-enabled technology, we can better protect consumer data and privacy through wallet-enabled transactions. 


##How To Run 

1. Go to the website (Streamlit). 
2. Enter the inputs in the sidebar to specify the duration of the rental. 
3. Select the car to rent among the choices. 
4. Verify the transaction in your wallet. 


##Documents

1. Team Presentations (Slides) <https://docs.google.com/presentation/d/1elToGQYKbCMz6aAhTmMEh6qNynDNbQPG_OPiWubgP3Q/edit#slide=id.g13b7972c535_0_71>

2. Team Charter <https://docs.google.com/document/d/1lY8t0cZMxxiIFc68L89hNWnGC5Kwznit7YF4jXzV9yA/edit#>


##Tech Dependencies 
Required programs, libraries, systems, and overall dependencies: 
Solidity 0.5.16
Python (version 3.0 or later)
Ganache
Truffle
JS Node
JSOn
Web3
HTTPProvider
Calendar
email.mime
re
sre_constants
click
streamlit 
pandas
pathlib 

##Smart Contract

Two smart contracts are called into the program: 
1. Rental.sol - process the rental using the rent function
2. RenterSystem.sol - process the payment using the addRenter, checkOut, balanceOf, balanceOfRenter, and makePayment functions

##Technical Notes

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