schema = """
	CREATE TABLE IF NOT EXISTS addresses (
        address_id INTEGER PRIMARY KEY AUTOINCREMENT,
        street VARCHAR(120) NOT NULL,
        street2 VARCHAR(120),
        city VARCHAR(120) NOT NULL,
        state VARCHAR(2) NOT NULL,
        zip_cdoe VARCHAR(10) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS branches (
        branch_id INTEGER PRIMARY KEY AUTOINCREMENT,
        address_id INT NOT NULL,
        name VARCHAR(60)
    );

    CREATE TABLE IF NOT EXISTS warehouses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        branch_id INTEGER, 
        FOREIGN KEY (branch_id) REFERENCES branches(branch_id)
    );

    CREATE TABLE IF NOT EXISTS pricing_buckets (
        bucket_id INTEGER PRIMARY KEY AUTOINCREMENT,
        codename VARCHAR(120),
        margin_percent REAL,
        dividend REAL
    );

    CREATE TABLE IF NOT EXISTS clients (
        client_id INTEGER PRIMARY KEY AUTOINCREMENT,
        address_id INT,
        branch_id INT, 
        pricing_bucket_id INT, 
        name VARCHAR(100),
        ytd_spent REAL, 
        mtd_spent REAL,
        average_daily_spent REAL,
        FOREIGN KEY (address_id) REFERENCES addresses(address_id),
        FOREIGN KEY (branch_id) REFERENCES branches(branch_id),
        FOREIGN KEY (pricing_bucket_id) REFERENCES pricing_buckets(bucket_id)
    );

    CREATE TABLE IF NOT EXISTS contacts (
        contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INT,
        name VARCHAR(100),
        email VARCHAR(100),
        phone VARHCAR(100),
        FOREIGN KEY (client_id) REFERENCES clients(client_id)
    );
	  
    CREATE TABLE IF NOT EXISTS client_notes (
      note_id INTEGER PRIMARY KEY AUTOINCREMENT,
      client_id INT,
      title VARCHAR(120),
      content VARCHAR(2500),
      FOREIGN KEY (client_id) REFERENCES clients(client_id)
    );
"""
print(schema)