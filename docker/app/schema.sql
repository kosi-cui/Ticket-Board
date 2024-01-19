CREATE TABLE IF NOT EXISTS step (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    next_step INTEGER,
    FOREIGN KEY (next_step) REFERENCES step(id)
);

CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    curr_step INTEGER,
    agent TEXT NOT NULL,
    FOREIGN KEY (curr_step) REFERENCES step(id)
);

-- Test data
INSERT IGNORE INTO step(id, title, next_step) VALUES (10, 'Step 10', NULL);
INSERT IGNORE INTO step(id, title, next_step) VALUES (9, 'Step 9', 10);
INSERT IGNORE INTO step(id, title, next_step) VALUES (8, 'Step 8', 9);
INSERT IGNORE INTO step(id, title, next_step) VALUES (7, 'Step 7', 8);
INSERT IGNORE INTO step(id, title, next_step) VALUES (6, 'Step 6', 7);
INSERT IGNORE INTO step(id, title, next_step) VALUES (5, 'Step 5', 6);
INSERT IGNORE INTO step(id, title, next_step) VALUES (4, 'Step 4', 5);
INSERT IGNORE INTO step(id, title, next_step) VALUES (3, 'Step 3', 4);
INSERT IGNORE INTO step(id, title, next_step) VALUES (2, 'Step 2', 3);
INSERT IGNORE INTO step(id, title, next_step) VALUES (1, 'Step 1', 2);

INSERT IGNORE INTO tickets(id, title, curr_step, agent) VALUES (3, 'Ticket 3', 3, 'Agent 3');
INSERT IGNORE INTO tickets(id, title, curr_step, agent) VALUES (2, 'Ticket 2', 2, 'Agent 2');
INSERT IGNORE INTO tickets(id, title, curr_step, agent) VALUES (1, 'Ticket 1', 1, 'Agent 1');