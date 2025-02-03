CREATE SCHEMA messages;

-- dynamic table
DROP TABLE IF EXISTS core."ChatGroup" CASCADE;
CREATE TABLE core."ChatGroup" (
	"id" INTEGER PRIMARY KEY NOT NULL,
	"create_timestamp" timestamp NOT NULL default NOW(),
	"last_sent_message" timestamp,
    "admin_user_id" INTEGER NOT NULL,
    CONSTRAINT user_id_chat_group_fkey FOREIGN KEY ("admin_user_id") REFERENCES authsystem."User"("id")
);

-- dynamic table
DROP TABLE IF EXISTS core."Message" CASCADE;
CREATE TABLE core."Message" (
	"id" INTEGER PRIMARY KEY NOT NULL,
	"create_timestamp" timestamp NOT NULL default NOW(),
    "edit_timestamp" timestamp,
    "content" TEXT NOT NULL DEFAULT '',
    "edit_content" TEXT,
    "user_id" INTEGER not null,
    "chat_group_id" INTEGER not null,
	CONSTRAINT user_id_message_fkey FOREIGN KEY ("user_id") REFERENCES authsystem."User"("id"),
    CONSTRAINT chat_group_id_message_fkey FOREIGN KEY ("chat_group_id") REFERENCES core."ChatGroup"("id") ON DELETE CASCADE
);

-- dynamic table
DROP TABLE IF EXISTS core."ChatGroupUsers" CASCADE;
CREATE TABLE core."ChatGroupUsers" (
	"id" INTEGER PRIMARY KEY NOT NULL,
	"chat_group_id" INTEGER NOT NULL,
    "user_id" INTEGER NOT NULL,
    "add_timestamp"  timestamp NOT NULL default NOW(),
    "remove_timestamp" timestamp,
	CONSTRAINT user_id_chat_group_users_fkey FOREIGN KEY ("user_id") REFERENCES authsystem."User"("id") ON DELETE CASCADE,
    CONSTRAINT chat_group_id_chat_group_users_fkey FOREIGN KEY ("chat_group_id") REFERENCES core."ChatGroup"("id") ON DELETE CASCADE
);