--  a script that lists all cities contained in the database hbtn_0d_usa.
SELECT id, name, state_id FROM cities
FULL JOIN states
ORDER BY id;
