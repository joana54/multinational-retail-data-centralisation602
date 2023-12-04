ALTER TABLE orders_table
    ALTER COLUMN date_uuid TYPE UUID USING date_uuid::uuid,
    ALTER COLUMN date_uuid SET NOT NULL;

ALTER TABLE orders_table
    ALTER COLUMN user_uuid TYPE UUID USING user_uuid::uuid,
    ALTER COLUMN user_uuid SET NOT NULL;

ALTER TABLE orders_table
    ALTER COLUMN card_number TYPE VARCHAR(19),
    ALTER COLUMN card_number SET NOT NULL;

ALTER TABLE orders_table
    ALTER COLUMN store_code TYPE VARCHAR(12),
    ALTER COLUMN store_code SET NOT NULL;

ALTER TABLE orders_table
    ALTER COLUMN product_code TYPE VARCHAR(11),
    ALTER COLUMN product_code SET NOT NULL;

ALTER TABLE orders_table
    ALTER COLUMN product_quantity TYPE SMALLINT,
    ALTER COLUMN product_quantity SET NOT NULL;




ALTER TABLE dim_users
    ALTER COLUMN first_name TYPE VARCHAR(255),
    ALTER COLUMN first_name SET NOT NULL;

ALTER TABLE dim_users
    ALTER COLUMN last_name TYPE VARCHAR(255),
    ALTER COLUMN last_name SET NOT NULL;

ALTER TABLE dim_users
        ALTER COLUMN date_of_birth TYPE DATE,
        ALTER COLUMN date_of_birth SET NOT NULL;

ALTER TABLE dim_users
    ALTER COLUMN country_code TYPE VARCHAR(2),
    ALTER COLUMN country_code SET NOT NULL;

ALTER TABLE dim_users
    ALTER COLUMN user_uuid TYPE UUID USING user_uuid::uuid,
    ALTER COLUMN user_uuid SET NOT NULL;

ALTER TABLE dim_users
    ALTER COLUMN join_date TYPE DATE,
    ALTER COLUMN join_date SET NOT NULL;



ALTER TABLE dim_store_details
    ALTER COLUMN longitude TYPE FLOAT;

ALTER TABLE dim_store_details
    ALTER COLUMN locality TYPE VARCHAR(255);

ALTER TABLE dim_store_details
        ALTER COLUMN store_code TYPE VARCHAR(12),
        ALTER COLUMN store_code SET NOT NULL;

ALTER TABLE dim_store_details
    ALTER COLUMN staff_numbers TYPE SMALLINT USING staff_numbers::SMALLINT,
    ALTER COLUMN staff_numbers SET NOT NULL;

ALTER TABLE dim_store_details
    ALTER COLUMN opening_date TYPE DATE,
    ALTER COLUMN opening_date SET NOT NULL;

ALTER TABLE dim_store_details
    ALTER COLUMN store_type TYPE VARCHAR(255);

ALTER TABLE dim_store_details
    ALTER COLUMN latitude TYPE FLOAT;

ALTER TABLE dim_store_details
    ALTER COLUMN country_code TYPE VARCHAR(2),
    ALTER COLUMN country_code SET NOT NULL;

ALTER TABLE dim_store_details
    ALTER COLUMN continent TYPE VARCHAR(255),
    ALTER COLUMN continent SET NOT NULL;




ALTER TABLE dim_users
    ALTER COLUMN first_name TYPE VARCHAR(255),
    ALTER COLUMN first_name SET NOT NULL;

ALTER TABLE dim_users
    ALTER COLUMN last_name TYPE VARCHAR(255),
    ALTER COLUMN last_name SET NOT NULL;

ALTER TABLE dim_users
        ALTER COLUMN date_of_birth TYPE DATE,
        ALTER COLUMN date_of_birth SET NOT NULL;

ALTER TABLE dim_users
    ALTER COLUMN country_code TYPE VARCHAR(2),
    ALTER COLUMN country_code SET NOT NULL;

ALTER TABLE dim_users
    ALTER COLUMN user_uuid TYPE UUID USING user_uuid::uuid,
    ALTER COLUMN user_uuid SET NOT NULL;

ALTER TABLE dim_users
    ALTER COLUMN join_date TYPE DATE,
    ALTER COLUMN join_date SET NOT NULL;



ALTER TABLE dim_products
    ADD COLUMN IF NOT EXISTS weight_class VARCHAR(20);

ALTER TABLE dim_products
    ALTER COLUMN weight TYPE FLOAT USING weight::DOUBLE PRECISION,
    ALTER COLUMN weight SET NOT NULL;

UPDATE dim_products
    SET weight_class = 'Light'
    WHERE weight < 2;

UPDATE dim_products
    SET weight_class = 'Mid_Sized'
    WHERE weight >= 2 AND weight < 40;

UPDATE dim_products
    SET weight_class = 'Heavy'
    WHERE weight >= 40 AND weight < 140;

UPDATE dim_products
    SET weight_class = 'Truck_Required'
    WHERE weight >= 140;

ALTER TABLE dim_products
    ALTER COLUMN product_price TYPE FLOAT USING product_price::DOUBLE PRECISION,
    ALTER COLUMN weight SET NOT NULL;

ALTER TABLE dim_products
    ALTER COLUMN "EAN" TYPE VARCHAR(17),
    ALTER COLUMN "EAN" SET NOT NULL;

ALTER TABLE dim_products
    ALTER COLUMN product_code TYPE VARCHAR(11),
    ALTER COLUMN product_code SET NOT NULL;

ALTER TABLE dim_products
    ALTER COLUMN date_added TYPE DATE,
    ALTER COLUMN date_added SET NOT NULL;

ALTER TABLE dim_products
    ALTER COLUMN uuid TYPE UUID USING uuid::UUID,
    ALTER COLUMN uuid SET NOT NULL;

ALTER TABLE dim_products
    ALTER COLUMN removed TYPE VARCHAR(25),
    ALTER COLUMN removed SET NOT NULL;

ALTER TABLE dim_products
    ALTER COLUMN date_added SET NOT NULL;




ALTER TABLE dim_date_times
    ALTER COLUMN time_period TYPE VARCHAR(10),
    ALTER COLUMN time_period SET NOT NULL;

ALTER TABLE dim_date_times
    ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID,
    ALTER COLUMN time_period SET NOT NULL;

ALTER TABLE dim_date_times
    ALTER COLUMN time_period SET NOT NULL;



ALTER TABLE dim_card_details
    ALTER COLUMN card_number TYPE VARCHAR(19),
    ALTER COLUMN card_number SET NOT NULL;

ALTER TABLE dim_card_details
    ALTER COLUMN expiry_date TYPE DATE,
    ALTER COLUMN expiry_date SET NOT NULL;

ALTER TABLE dim_card_details
    ALTER COLUMN card_provider TYPE VARCHAR(40),
    ALTER COLUMN card_provider SET NOT NULL;

ALTER TABLE dim_card_details
    ALTER COLUMN date_payment_confirmed TYPE DATE,
    ALTER COLUMN date_payment_confirmed SET NOT NULL;


ALTER TABLE dim_products 
ADD PRIMARY KEY (product_code);

ALTER TABLE dim_date_times 
ADD PRIMARY KEY (date_uuid);

ALTER TABLE dim_card_details 
ADD PRIMARY KEY (card_number);

ALTER TABLE dim_store_details 
ADD PRIMARY KEY (store_code);

ALTER TABLE dim_users 
ADD PRIMARY KEY (user_uuid);


ALTER TABLE orders_table 
ADD CONSTRAINT product_constraint 
FOREIGN KEY (product_code) 
REFERENCES dim_products (product_code);

ALTER TABLE orders_table 
ADD CONSTRAINT card_constraint 
FOREIGN KEY (card_number) 
REFERENCES dim_card_details (card_number);

ALTER TABLE orders_table 
ADD CONSTRAINT date_times_constraint 
FOREIGN KEY (date_uuid) 
REFERENCES dim_date_times (date_uuid);

ALTER TABLE orders_table 
ADD CONSTRAINT user_constraint 
FOREIGN KEY (user_uuid) 
REFERENCES dim_users (user_uuid);

ALTER TABLE orders_table 
ADD CONSTRAINT store_constraint 
FOREIGN KEY (store_code) 
REFERENCES dim_store_details (store_code);