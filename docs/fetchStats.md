## Quick Search

- [dropTableDatabase()](#droptabledatabase)
- [createTableDatabase()](#createtabledatabase)
- [insertVariableIntoTable(augmentName, first, second, third)](#insertvariableintotableaugmentname-first-second-third)
- [set_viewport_size(driver, width, height)](#set_viewport_sizedriver-width-height)
- [fetchStats()](#fetchstats)
- [getAugmentPlacement(augmentName, stage)](#getaugmentplacementaugmentname-stage)

## dropTableDatabase()

This function attempts to establish a connection to a sqlite3 database called Augment_Stats.db and sends the SQL command to execute: 
```
DROP TABLE IF EXISTS AugmentTable;
```
This command drops the table, AugmentTable, in the Augment_Stats.db if it exists. If executed correctly this results in a database Augment_Stats.db with no tables, 
and prints a successful completion statement. If the connection is refused for some reason, an error will be printed instead.

The purpose of this command in the bigger picture is to "refresh" the AugmentTable values so that augment stats are guaranteed to be the most up to date values.
The first step in that process is to drop the old values. This is where dropTableDatabase() is used.

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
## insertVariableIntoTable(augmentName, first, second, third)
## set_viewport_size(driver, width, height)
## fetchStats()
## getAugmentPlacement(augmentName, stage)
