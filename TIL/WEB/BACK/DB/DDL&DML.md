# DDL
## CREATE
Basic syntax
```sql
CREATE TABLE table_name (
    col_name, data_type, constraints,
    col_name, data_type, constraints,
    ...,
);
```

Example
```sql
CREATE TABLE examples (
    ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL
    FK INTEGER,
    FOREIGN KEY (FK) REFERENCES ref_table(pk)
);
```

## ALTER
### ADD COLUMN
```sql
ALTER TABLE table_name
ADD COLUMN col_name data_type constraints;
```

### RENAME COLUMN
```sql
ALTER TABLE table_name
RENAME col_name TO new_col_name;
```


### DROP COLUMN
```sql
ALTER TABLE table_name
DROP COLUMN col_name;
```

### RENAME TABLE
```sql
ALTER TABLE table_name
RENAME TO new_table_name;
```

## DROP
```SQL
DROP TABLE table_name;
```

# DML
## INSERT
```SQL
INSERT INTO table_name (c1, c2, c3, ...)
VALUES (v1, v2, ...), (v1, v2, v3, ...), ...;
```

## UPDATE
Basic syntax
```SQL
UPDATE table_name
SET col1_name = expression1, col2_name = expression2, ...,
[WHERE condition];
```

Multiple updates
```sql
UPDATE zoo
SET species = CASE Name
    WHEN 'Lion' THEN 'Panthera leo'
    WHEN 'Elephant' THEN 'Loxodonta africana'
    WHEN 'Giraffe' THEN 'Giraffa camelopardalis'
    WHEN 'Monkey' THEN 'Cebus capucinus'
END;
```

## DELETE
```SQL
DELETE FROM articles
[WHERE condition];
```