# Bank Account Management System - Java

## Overview

Bank Account Management System is a console-based Java application that demonstrates core object-oriented programming concepts through a practical banking scenario. The system allows users to perform typical banking operations such as deposits, withdrawals, balance inquiries, and transaction history tracking.

## Business Context

This project simulates a basic banking system where customers can manage their accounts. The application provides a user-friendly menu-driven interface for performing financial transactions while maintaining a secure and accurate account ledger.

## Problem Statement

The system solves the following requirements:
- Create and manage customer bank accounts
- Perform deposit and withdrawal operations with validation
- Maintain transaction history (last 5 transactions)
- View current account balance
- Provide error handling for invalid operations (insufficient balance, invalid amounts)

## Features

1. **Account Creation** - Initialize a new account with account holder name and zero balance
2. **Deposit Operations** - Add funds to account with validation for positive amounts
3. **Withdraw Operations** - Remove funds with checks for sufficient balance
4. **Transaction History** - Track and display the last 5 transactions
5. **Balance Inquiry** - View current account balance
6. **Error Handling** - Comprehensive exception handling for invalid transactions
7. **Menu-Driven Interface** - User-friendly console interface for easy navigation

## Architecture

### Class Structure

**Account.java** - Core account management class
- Private fields: accountHolder, balance, transactions (ArrayList)
- Methods: deposit(), withdraw(), addTransaction(), printMiniStatement(), getBalance()
- Features: RuntimeException for insufficient balance, transaction rollover after 5 entries

**Main.java** - Menu-driven user interface
- Scanner input handling with try-with-resources
- do-while loop for continuous menu operation
- Switch case for operation selection
- Exception handling for withdraw operations

## Installation

**Requirements:**
- Java Development Kit (JDK) 8 or higher
- No external dependencies required

**Compilation:**
```bash
javac *.java
```

**Execution:**
```bash
java Main
```

## Usage Examples

### Sample Session
```
Enter account holder name: J N Ravinandan

--- Menu ---
1. Deposit
2. Withdraw
3. View Transactions
4. Check Balance
5. Exit
Enter choice: 1
Enter amount to deposit: 5000
Deposited: 5000

--- Menu ---
Enter choice: 4
Current Balance: 5000

--- Menu ---
Enter choice: 3
Account: J N Ravinandan
Last 5 Transactions:
5000
```

## Key OOP Concepts Demonstrated

1. **Encapsulation** - Private fields with public methods for controlled access
2. **Data Validation** - Input validation in deposit/withdraw methods
3. **Exception Handling** - RuntimeException for business logic errors
4. **Collections** - ArrayList for dynamic transaction history
5. **Resource Management** - Try-with-resources for Scanner auto-closure
6. **State Management** - Account state tracking across operations

## Implementation Details

### Transaction Tracking Algorithm
- Maintains ArrayList of up to 5 recent transactions
- When 5th transaction is reached, oldest transaction is removed
- New transaction is always appended to the end

### Validation Rules
- Deposit amount must be > 0
- Withdrawal amount must be > 0
- Withdrawal amount must not exceed current balance
- Both operations update balance and add transaction entry

### Error Handling
- Invalid menu choices display "Invalid choice" message
- Withdrawal failures throw RuntimeException with "Insufficient balance" message
- Input validation prevents negative or zero amounts

## Testing Scenarios

1. Multiple deposits to increase balance
2. Withdraw more than balance (error handling)
3. View 5 transactions and verify rollover on 6th
4. Check balance consistency after multiple operations
5. Exit application gracefully

## Files

- **Account.java** - Account class with business logic
- **Main.java** - User interface and menu system
- **Account.class** - Compiled bytecode
- **Main.class** - Compiled bytecode

## Completed By

J N Ravinandan
SRM University (Vadapalani)