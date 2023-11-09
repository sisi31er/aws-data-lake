1. Creating Subnets either with the cloudformation or in the aws frontend
2. creating db instances with the cloudformation file
3. loading the csv files into the databases with the following commands
   1. aws rds import-external-table-into-rds --db-instance-identifier <db-instance-identifier> --table-name <table-name> --s3-schema <s3-bucket-name> --s3-prefix <s3-folder-prefix> --format csv
   2. to create a stack --> in this case an example s3 bucket: aws cloudformation create-stack --stack-name uploadS3Bucket-2 --template-body file://temp-s3.yml --capabilities CAPABILITY_NAMED_IAM --role-arn arn:aws:iam::219152482593:role/glue-test-full-access
   3. to upload all files to a s3 bucket: aws s3 sync ../sample_data/tickit_data/ s3://data-lake-demo-2-219152482593-eu-central-1/ or if you just want one file aws s3 cp ../sample_data/tickit_data/category.csv s3://data-lake-demo-2-219152482593-eu-central-1/




Create the databases

1. Step 
Create the databases locally and create a .sql backup file
mysqldump -u root -p myinstance1 -r ~/Desktop/replica.sql

2. Step
Open the dump.sql file in Notepad++ and hit CTRL+H to find and replace the string “utf8mb4_0900_ai_ci” and replaced it with “utf8mb4_general_ci“.

3. Step 
Upload the backup file then to the aws database 
mysql -u admin -p -h mydbinstance1.c2yecud4ozdu.eu-central-1.rds.amazonaws.com ecomm < dump.sql

(with postgres you can parse the data directly from the csv files because is faster then mysql and mssql)

aws cloudformation deploy --stack-name data-lake-demo-glue-all --template-file ./cloudformation/demo-glue.yml --capabilities CAPABILITY_NAMED_IAM


tabellen in korrektem format in korrekt bezeichnete tabelle laden
aws databases anpassen (auch gut um nochmal alle Schritte durchzugehen)
WECHSELN ZU JAVA 8 oder nicht?? --> vielleicht mal Versuch
Spark connections zu allen Databases aufbauen
spark jobs ausführen lassen? fehlt dafür noch was??
