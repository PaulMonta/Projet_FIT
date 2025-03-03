import sqlite3

# ✅ Fonction de connexion
def create_connection(db_file):
    """ Crée une connexion SQLite et retourne l'objet connexion """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"✅ Connected to {db_file}")
    except sqlite3.Error as e:
        print(f"❌ Erreur : {e}")
    return conn

# ✅ Fonction générique pour créer une table
def create_table(conn, create_table_sql):
    try:
        conn.execute(create_table_sql)
        print("✅ Table créée avec succès")
    except sqlite3.Error as e:
        print(f"❌ Erreur lors de la création de la table : {e}")

# ✅ Création des tables
def create_body_metrics_table(conn):
    sql = """CREATE TABLE IF NOT EXISTS body_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                weight REAL NOT NULL,
                measurements TEXT,
                bmi REAL,
                calories_burned REAL
            );"""
    create_table(conn, sql)

def create_workouts_table(conn):
    sql = """CREATE TABLE IF NOT EXISTS workouts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                type TEXT NOT NULL,
                duration INTEGER NOT NULL,
                calories_burned REAL,
                notes TEXT
            );"""
    create_table(conn, sql)

def create_nutrition_table(conn):
    sql = """CREATE TABLE IF NOT EXISTS nutrition (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                meal TEXT NOT NULL,
                calories INTEGER,
                protein REAL,
                carbs REAL,
                fat REAL
            );"""
    create_table(conn, sql)

def create_lifestyle_table(conn):
    sql = """CREATE TABLE IF NOT EXISTS lifestyle (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                sleep_hours REAL NOT NULL,
                stress_level INTEGER,
                mood TEXT,
                fatigue_level INTEGER
            );"""
    create_table(conn, sql)

def create_body_measurements_table(conn):
    sql = """CREATE TABLE IF NOT EXISTS body_measurements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                waist_cm REAL,
                biceps_cm REAL,
                thigh_cm REAL,
                chest_cm REAL
            );"""
    create_table(conn, sql)

def create_daily_activity_table(conn):
    sql = """CREATE TABLE IF NOT EXISTS daily_activity (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                steps INTEGER,
                distance_km REAL,
                active_calories INTEGER
            );"""
    create_table(conn, sql)

# ✅ Insérer des données (exemple pour body_metrics)
def insert_body_metrics(conn, date, weight, measurements=None, bmi=None, calories_burned=None):
    sql = """INSERT INTO body_metrics (date, weight, measurements, bmi, calories_burned)
             VALUES (?, ?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(sql, (date, weight, measurements, bmi, calories_burned))
    conn.commit()
    return cur.lastrowid

# ✅ Exécution du script
if __name__ == "__main__":
    db_file = "fitness_tracker.db"
    conn = create_connection(db_file)
    
    if conn is not None:
        # 🔹 Création de toutes les tables
        create_body_metrics_table(conn)
        create_workouts_table(conn)
        create_nutrition_table(conn)
        create_lifestyle_table(conn)
        create_body_measurements_table(conn)
        create_daily_activity_table(conn)
        
        # 🔹 Fermer la connexion
        conn.close()
    else:
        print("❌ Erreur : Impossible de créer la connexion à la base de données.")
