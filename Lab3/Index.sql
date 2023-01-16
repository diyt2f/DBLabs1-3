-- BTree

DROP INDEX if exists or_index;

explain analyze select * from "Purchase" where "BankTransactionNumber" = 'UA35253253523';
explain analyze select * from "Purchase" where "BankTransactionNumber" = 'UA35253253523' and "BankTransactionNumber" = 'US352355' and "BankTransactionNumber" = 'UA19658577';
explain analyze select * from "Purchase" where "BankTransactionNumber" != 'UA35253253523' and "BankTransactionNumber" != 'US352355'  and "BankTransactionNumber" != 'UA19658577' and "BankTransactionNumber" != 'UA28533621';

CREATE INDEX or_index ON "Purchase"("BankTransactionNumber");

explain analyze select * from "Purchase" where "BankTransactionNumber" = 'UA35253253523';
explain analyze select * from "Purchase" where "BankTransactionNumber" = 'UA35253253523' and "BankTransactionNumber" = 'US352355' and "BankTransactionNumber" = 'UA19658577';
explain analyze select * from "Purchase" where "BankTransactionNumber" != 'UA35253253523' and "BankTransactionNumber" != 'US352355'  and "BankTransactionNumber" != 'UA19658577' and "BankTransactionNumber" != 'UA28533621';

-- BRIN

DROP INDEX if exists or_brin_index;

explain analyze select * from "Purchase" where "BankTransactionNumber" = 'UA35253253523' ;
explain analyze select count("Sum") from "Purchase" where "BankTransactionNumber" != 'UA35253253523';
explain analyze select count("Sum") from "Purchase" where "BankTransactionNumber" = 'UA35253253523' and "BankTransactionNumber" = 'US352355' and "BankTransactionNumber" = 'UA19658577';
explain analyze select count("Sum") from "Purchase" where "BankTransactionNumber" != 'UA35253253523' and "BankTransactionNumber" != 'US352355' and "BankTransactionNumber" != 'UA19658577' and "BankTransactionNumber" != 'UA28533621';

CREATE INDEX or_brin_index on "Purchase" using brin ("BankTransactionNumber") with(pages_per_range=128);

explain analyze select * from "Purchase" where "BankTransactionNumber" = 'UA35253253523' ;
explain analyze select count("Sum") from "Purchase" where "BankTransactionNumber" != 'UA35253253523';
explain analyze select count("Sum") from "Purchase" where "BankTransactionNumber" = 'UA35253253523' and "BankTransactionNumber" = 'US352355' and "BankTransactionNumber" = 'UA19658577';
explain analyze select count("Sum") from "Purchase" where "BankTransactionNumber" != 'UA35253253523' and "BankTransactionNumber" != 'US352355' and "BankTransactionNumber" != 'UA19658577' and "BankTransactionNumber" != 'UA28533621';

