# Import the Neo4jService class
from .neo4j_service import Neo4jService

# Connection details
NEO4J_URI = "neo4j://localhost:7687/"  # Assuming your database name is "django1"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = "12345678"

# Example usage in a Django view
def my_view(request):
    # Create Neo4jService instance with connection details
    neo4j_service = Neo4jService(NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD)
    
    # Example query
    query = "MATCH (n) RETURN n LIMIT 5"
    
    # Execute the query
    result = neo4j_service.run_query(query)
    
    # Close the Neo4j driver
    neo4j_service.close()
    
    # Process the result and return the response
