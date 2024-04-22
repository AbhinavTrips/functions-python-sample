import azure.functions as func
import logging

app = func.FunctionApp()

@app.cosmos_db_trigger(arg_name="azcosmosdb", container_name="src_container",
                        database_name="cf_db", connection="cosmicworkssql_DOCUMENTDB",
                         lease_container_name="leases", create_lease_container_if_not_exists="true")  
def cosmosdb_trigger(azcosmosdb: func.DocumentList):
    logging.info('Python CosmosDB triggered.')
