import java.util.ArrayList;

class Account {

    private String accountHolder;
    private double balance;
    private ArrayList<Double> transactions;

    public Account(String accountHolder, double balance) {
        this.accountHolder = accountHolder;
        this.balance = balance;
        this.transactions = new ArrayList<>();
    }

    public void deposit(double amount) {
        if (amount <= 0) {
            System.out.println("Invalid deposit amount");
            return;
        }

        balance += amount;
        addTransaction(amount);
        System.out.println("Deposited: " + amount);
    }

    public void withdraw(double amount) {
        if (amount <= 0) {
            System.out.println("Invalid withdrawal amount");
            return;
        }

        if (amount > balance) {
            System.out.println("Error: Insufficient balance");
            return;
        }

        balance -= amount;
        addTransaction(-amount);
        System.out.println("Withdrawn: " + amount);
    }

    private void addTransaction(double amount) {
        if (transactions.size() == 5) {
            transactions.remove(0);
        }
        transactions.add(amount);
    }

    public void printMiniStatement() {
        System.out.println("\nLast 5 Transactions:");
        for (double t : transactions) {
            System.out.println(t);
        }
    }

    public double getBalance() {
        return balance;
    }
}