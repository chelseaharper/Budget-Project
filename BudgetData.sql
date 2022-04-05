CREATE TABLE Account (
    AccountID SERIAL PRIMARY KEY,
    AccountName VARCHAR(50) NOT NULL
);

CREATE TABLE User (
    UserID SERIAL PRIMARY KEY,
    UserName VARCHAR NOT NULL
);

CREATE TABLE Category (
    CategoryID SERIAL PRIMARY KEY,
    CategoryName VARCHAR NOT NULL,
    ParentID INTEGER NULL FOREIGN KEY ParentKey REFERENCES Category(CategoryID),
    Goal DECIMAL(14, 2) NULL,
    AccountID INTEGER NULL FOREIGN KEY AccountKey REFERENCES Account(AccountID),
);

CREATE TABLE TransactionSchedule (
    ScheduleID SERIAL PRIMARY KEY,
    ScheduleName VARCHAR NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NULL,
    LastRunDate DATE NULL,
    Frequency VARCHAR NOT NULL,
    FrequencyDays INTEGER NOT NULL,
    Amount DECIMAL(14, 2) NOT NULL,
    ScheduleDescription VARCHAR(30) NOT NULL,
    ScheduleCategory INTEGER NULL FOREIGN KEY CategoryKey REFERENCES Category(CategoryID),
    ScheduleLedger INTEGER NULL FOREIGN KEY LedgerKey REFERENCES Ledger(LedgerID),
    ScheduleUser INTEGER NULL FOREIGN KEY UserKey REFERENCES User(UserID),
);

CREATE TABLE Ledger (
    LedgerID SERIAL PRIMARY KEY,
    LedgerName VARCHAR NOT NULL,
    Balance DECIMAL(14, 2) NOT NULL,
    LedgerAccount INTEGER NULL FOREIGN KEY AccountKey REFERENCES Account(AccountID),
);

CREATE TABLE "Transaction" (
    TransactionID SERIAL PRIMARY KEY,
    Amount DECIMAL(14, 2) NOT NULL,
    TransactionDescription VARCHAR(30) NOT NULL,
    TransactionCategory INTEGER NULL FOREIGN KEY CategoryKey REFERENCES Category(CategoryID),
    TransactionDate DATE NOT NULL,
    TransactionLedger INTEGER NULL FOREIGN KEY LedgerKey REFERENCES Ledger(LedgerID),
    TransactionUser INTEGER NULL FOREIGN KEY UserKey REFERENCES User(UserID),
);

