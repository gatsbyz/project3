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

6. Open another terminal window, and run this:
    ```
    $ pip3 install web3
    $ python3 app.py
    ```