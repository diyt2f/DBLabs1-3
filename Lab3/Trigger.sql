--after update, insert

DROP TRIGGER IF EXISTS "after_update_insert_trigger" ON "Book";
DROP TABLE "BookLog";

CREATE TABLE "BookLog"(
"ID" serial PRIMARY KEY,
"BookLogID" BIGINT,
"BookName" text
);


CREATE OR REPLACE FUNCTION after_update_insert_func() RETURNS TRIGGER as $trigger$
DECLARE
	
BEGIN
	IF new."PageCount" <= 350 THEN
		RAISE NOTICE 'PageCount <= 350, so the book is short.';
		INSERT INTO "BookLog"("BookLogID", "BookName") VALUES (new."BookID", new."Name" || ' (Short)');
	ELSE
		RAISE NOTICE 'PageCount >= 350, so the book is long.';
		INSERT INTO "BookLog"("BookLogID", "BookName") VALUES (new."BookID", new."Name" || ' (Long)');
	END IF;
	IF new."PageCount" = 666 THEN
		RAISE EXCEPTION 'PageCount == 666, so the book is unlucky and should not be present in our shop.';
	END IF;
RETURN NEW;
END;
$trigger$ LANGUAGE plpgsql;

CREATE TRIGGER "after_update_insert_trigger"
AFTER UPDATE OR INSERT ON "Book"
FOR EACH ROW
EXECUTE procedure after_update_insert_func(); 



INSERT INTO "Book"("BookID", "Name", "PageCount")
VALUES ('5321112353','Book 555', '340'), ('5122313','The Big Book 5', '909'), ('32123255', 'Python Book', '241') ;

UPDATE "Book" SET "PageCount" = 555 WHERE "Name" = 'The Big Book 5';

--UPDATE "Book" SET "PageCount" = 666 WHERE "Name" = 'Python Book';
