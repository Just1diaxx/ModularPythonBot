import aiosqlite

async def create_table(table_name, columns):
    column_definitions = ", ".join([f"{col_name} {col_type}" for col_name, col_type in columns.items()])
    async with aiosqlite.connect('database.db') as db:
        await db.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                {column_definitions}
            )
        ''')
        await db.commit()


async def insert_data(table_name, data):
    columns = ", ".join(data.keys())
    placeholders = ", ".join(["?" for _ in data])
    values = tuple(data.values())
    
    async with aiosqlite.connect('database.db') as db:
        await db.execute(f'''
            INSERT INTO {table_name} ({columns}) VALUES ({placeholders})
        ''', values)
        await db.commit()


async def update_data(table_name, data, condition):
    set_clause = ", ".join([f"{key} = ?" for key in data.keys()])
    condition_clause = " AND ".join([f"{key} = ?" for key in condition.keys()])
    values = tuple(data.values()) + tuple(condition.values())
    
    async with aiosqlite.connect('database.db') as db:
        await db.execute(f'''
            UPDATE {table_name} SET {set_clause} WHERE {condition_clause}
        ''', values)
        await db.commit()


async def delete_data(table_name, condition):
    condition_clause = " AND ".join([f"{key} = ?" for key in condition.keys()])
    values = tuple(condition.values())
    
    async with aiosqlite.connect('database.db') as db:
        await db.execute(f'''
            DELETE FROM {table_name} WHERE {condition_clause}
        ''', values)
        await db.commit()


async def get_data(table_name, condition):
    condition_clause = " AND ".join([f"{key} = ?" for key in condition.keys()])
    values = tuple(condition.values())
    
    async with aiosqlite.connect('database.db') as db:
        cursor = await db.execute(f'''
            SELECT * FROM {table_name} WHERE {condition_clause}
        ''', values)
        row = await cursor.fetchall()
        return row
