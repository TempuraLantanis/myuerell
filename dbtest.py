from sqlalchemy import create_engine
connection_string = "mysql+mysqlconnector://user1:pscale_pw_abc123@us-east.connect.psdb.cloud:3306/sqlalchemy"
engine = create_engine(connection_string, echo=True)