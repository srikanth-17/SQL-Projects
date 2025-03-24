CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(15),
    city VARCHAR(50),
    country VARCHAR(50)
);

-- Sample Data
INSERT INTO Customers VALUES 
(1, 'Alice', 'Smith', 'alice.smith@example.com', '9876543210', 'New York', 'USA'),
(2, 'Bob', 'Johnson', 'bob.johnson@example.com', '8765432109', 'Los Angeles', 'USA'),
(3, 'Charlie', 'Brown', 'charlie.brown@example.com', '7654321098', 'Chicago', 'USA'),
(4, 'David', 'Williams', 'david.w@example.com', '6543210987', 'San Francisco', 'USA');


CREATE TABLE Accounts (
    account_id INT PRIMARY KEY,
    customer_id INT,
    account_type VARCHAR(20),  -- Savings, Checking
    balance DECIMAL(12,2),
    created_at TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Sample Data
INSERT INTO Accounts VALUES 
(101, 1, 'Savings', 15000.00, '2024-01-01 09:00:00'),
(102, 2, 'Checking', 50000.00, '2024-01-10 10:00:00'),
(103, 3, 'Savings', 12000.00, '2024-01-15 11:30:00'),
(104, 4, 'Checking', 60000.00, '2024-01-20 14:00:00');


CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY,
    account_id INT,
    amount DECIMAL(10,2),
    transaction_type VARCHAR(10),  -- Credit or Debit
    date TIMESTAMP,
    status VARCHAR(15),  -- Success, Failed
    remarks TEXT,
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);

-- Sample Data
INSERT INTO Transactions VALUES 
(201, 101, 1000.00, 'Credit', '2024-03-01 09:15:00', 'Success', 'Salary deposit'),
(202, 101, 500.00, 'Debit', '2024-03-02 10:30:00', 'Success', 'Online shopping'),
(203, 102, 1200.00, 'Credit', '2024-03-03 11:45:00', 'Success', 'Freelance payment'),
(204, 102, 300.00, 'Debit', '2024-03-04 12:00:00', 'Failed', 'Payment declined'),
(205, 103, 15000.00, 'Debit', '2024-03-05 13:30:00', 'Success', 'Loan repayment');


CREATE TABLE Alerts (
    alert_id INT PRIMARY KEY,
    transaction_id INT,
    alert_type VARCHAR(50),  -- Fraud, Large Transaction
    created_at TIMESTAMP,
    resolved BOOLEAN,
    FOREIGN KEY (transaction_id) REFERENCES Transactions(transaction_id)
);

-- Sample Data
INSERT INTO Alerts VALUES 
(301, 205, 'Large Transaction', '2024-03-05 14:00:00', FALSE),
(302, 204, 'Failed Transaction', '2024-03-04 12:30:00', TRUE);


