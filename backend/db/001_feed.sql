CREATE SCHEMA core;

-- static table
DROP TABLE IF EXISTS core."Sport" CASCADE;
CREATE TABLE core."Sport" (
	"id" INTEGER PRIMARY KEY NOT NULL,
	"name" varchar(30) NOT NULL,
	"description" varchar(2000) NOT NULL DEFAULT '', 
    "number_of_players" INTEGER NOT NULL
);

INSERT INTO core."Sport" ("id", "name", "description", "number_of_players") VALUES
(1,'football', 'Test', 22),
(2,'basketball', 'Test', 10),
(3,'volleyball', 'Test', 12),
(4,'tennis', 'Test', 2),
(5,'table tenis', 'Test', 2),
(6,'badminton', 'Test', 2);



-- dynamic
DROP TABLE IF EXISTS core."Feed" CASCADE;
CREATE TABLE core."Feed" (
    "id" UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    "creation_timestamp" TIMESTAMP NOT NULL DEFAULT NOW(),
    "edit_timestamp" TIMESTAMP,
    "user_id" INTEGER NOT NULL,
    "description" TEXT NOT NULL DEFAULT '',
    "sport_id" INTEGER NOT NULL,
    "likes" INTEGER NOT NULL DEFAULT 0,
    "impacts" INTEGER NOT NULL DEFAULT 0,
    CONSTRAINT user_id_fkey FOREIGN KEY ("user_id") REFERENCES authsystem."User"("id"),
    CONSTRAINT sport_id_fkey FOREIGN KEY ("sport_id") REFERENCES core."Sport"("id")
);