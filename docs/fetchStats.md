## Quick Search

- [dropTableDatabase()](#droptabledatabase)
- [createTableDatabase()](#createtabledatabase)
- [insertVariableIntoTable(augmentName, first, second, third)](#insertvariableintotableaugmentname-first-second-third)
- [set_viewport_size(driver, width, height)](#set_viewport_sizedriver-width-height)
- [fetchStats()](#fetchstats)
- [getAugmentPlacement(augmentName, stage)](#getaugmentplacementaugmentname-stage)

## dropTableDatabase()

This function attempts to establish a [connection](https://docs.python.org/3/library/sqlite3.html#connection-objects) to a sqlite3 database called Augment_Stats.db. If successful, the function creates a [cursor](https://docs.python.org/3/library/sqlite3.html#cursor-objects) which [executes](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.execute) and [commits](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.commit) the SQL command: 
```
DROP TABLE IF EXISTS AugmentTable;
```
This command drops the table, AugmentTable, in the Augment_Stats.db if it exists. If executed correctly this results in a database Augment_Stats.db with no tables, 
and prints a successful completion statement. If the connection is refused for some reason, an error will be printed instead.

The purpose of this command in the bigger picture is to "refresh" the AugmentTable values so that augment stats are guaranteed to be the most up to date values.
The first step in that process is to drop the old values. This is where dropTableDatabase() is used (this process happens in [fetchStats()](#fetchstats)).

### Example Usage: 
Save this in testing.py:
```
def example_usage():
  dropTableDatabase();

example_usage()
```
Execute this command in shell:
```
python main/testing.py
```
Correct Expected Output:

```
Connected to SQLite3 Database
Successfully deleted table: AugmentTable
SQLite3 database connection closed
```

Failing Expected Output:

```
Failed to delete AugmentTable
SQLite3 database connection closed
```
## createTableDatabase()

This function creates the table AugmentTable in Augment_Stats.db with parameters for each of the 4 columns: augmentName, first (avg placement if chosen at 2-1), second (avg placement if chosen at 3-2), and third(avg placement if chosen at 4-2).

Similarly to dropTableDatabase and insertVariableIntoTable, this function first attempts to establish a [connection](https://docs.python.org/3/library/sqlite3.html#connection-objects) to the sqlite3 database: Augment_Stats.db. If successful, this function creates a [cursor](https://docs.python.org/3/library/sqlite3.html#cursor-objects) which [executes](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.execute) and [commits](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.commit) the SQL command: 
```
CREATE TABLE AugmentTable (augmentName TEXT NOT NULL UNIQUE PRIMARY KEY, first TEXT, second TEXT, third TEXT);
```
This command creates the table AugmentTable with column parameters, augmentName of type Text, NOT NULL (always has a value), UNIQUE, PRIMARY KEY (unique identifier for the data table), first of type Text, second of type Text, and third of type Text. 

If executed correctly it creates the empty AugmentTable with given parameters and prints a successful completion statement. If it fails, it will print an error statment.

The purpose of this function in the bigger picture is to create the main empty data table which will be filled by the webscraped results of new augmentNames and up to date stats. This is the second half of the "refresh" process called in [fetchStats()](#fetchstats).

### Example Usage: 
Save this in testing.py:
```
def example_usage():
  createTableDatabase();

example_usage()
```
Execute this command in shell:
```
python main/testing.py
```
Correct Expected Output:

```
Connected to SQLite3 Database
Successfully created table: AugmentTable
SQLite3 database connection closed
```

Failing Expected Output:

```
Failed to create AugmentTable
SQLite3 database connection closed
```
## insertVariableIntoTable(augmentName, first, second, third)
## set_viewport_size(driver, width, height)
## fetchStats()
## getAugmentPlacement(augmentName, stage)
