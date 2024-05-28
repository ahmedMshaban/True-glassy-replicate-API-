# Databases

## Best practices

### Data Normalization

Definition: The process of organizing a database to reduce redundancy and improve data integrity.
Purpose: To ensure that each data point is atomic, represented only once, and efficiently managed within the relational model.

### Key Requirements (Based on E.F. Codd's 1972 Paper)

- Independence from Insertion, Update, and Deletion Anomalies: Avoids complex relationships that complicate data operations.
- Reduced Need for Restructuring: Minimizes restructuring needs as new data types are introduced, extending the lifespan of application programs.
- Informative to Users: Ensures the database model is easily interpretable by users.
- Neutral to Query Statistics: Statistics calculations should not depend on table designs.

### Normal Forms

### First Normal Form (1NF)

Requirements: Data must be atomic, uniquely identified by a primary key, and should not contain repeating groups.
Example: Splitting a table to separate attributes into their own table and ensuring no entity-type mismatch.

### Second Normal Form (2NF)

Requirements: Data must be in 1NF, and all non-key attributes must be fully dependent on the primary key.
Example: Removing partial dependencies by creating a separate table for products linked by a foreign key.

### Third Normal Form (3NF)

Requirements: Data must be in 2NF, and all non-key attributes must be independent of other non-key attributes (no transitive dependencies).
Example: Removing transitive dependencies by separating columns that depend on each other into different tables.

Give chatgpt example from 2.107 Database good practice

## References

- https://github.com/rdswyc

