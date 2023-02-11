class BaseDBClient:
    def find_one(self, table_name: str, query: dict):
        raise NotImplementedError

    def insert(self, table_name: str, query: dict):
        raise NotImplementedError

    def update(self, table_name: str, filtered_query: dict, update_query: dict):
        raise NotImplementedError

    def find(self, table_name: str, query: dict):
        raise NotImplementedError

    def delete(self, table_name: str, query: dict):
        raise NotImplementedError
