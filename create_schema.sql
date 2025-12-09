DROP DATABASE IF EXISTS cs122a;
CREATE DATABASE cs122a;
USE cs122a;

-- Q1: User and Agent Creator/Client (SQL DDL for entity(ies) table(s) only)

CREATE TABLE User (
  uid INTEGER,
  username VARCHAR(255),
  email VARCHAR(255),

  PRIMARY KEY (uid)
);

CREATE TABLE AgentCreator (
  uid INTEGER,
  payout VARCHAR(255),
  bio VARCHAR(255),
  
  PRIMARY KEY (uid),
  FOREIGN KEY (uid) REFERENCES User(uid)
);

CREATE TABLE AgentClient (
  uid INTEGER,
  cardno VARCHAR(255),
  cardholder VARCHAR(255),
  expire VARCHAR(255),
  cvv VARCHAR(255),
  zip VARCHAR(255),
  interests VARCHAR(255),
  
  PRIMARY KEY (uid),
  FOREIGN KEY (uid) REFERENCES User(uid)
);

-- Q2: Base and Customized Model (SQL DDL for entity(ies) table(s) only)

CREATE TABLE BaseModel (
  bmid INTEGER,
  creator_uid INTEGER NOT NULL,
  description VARCHAR(255),

  PRIMARY KEY (bmid),
  FOREIGN KEY (creator_uid) REFERENCES AgentCreator(uid)
);

CREATE TABLE CustomizedModel (
  mid INTEGER,
  bmid INTEGER NOT NULL,

  PRIMARY KEY (mid),
  FOREIGN KEY (bmid) REFERENCES BaseModel(bmid)
	ON DELETE CASCADE
);

-- Q3: Configurations (SQL DDL for entity(ies) table(s) only)

CREATE TABLE Configuration (
  cid INTEGER,
  client_uid INTEGER NOT NULL,
  content VARCHAR(255),
  labels VARCHAR(255),

  PRIMARY KEY (cid),
  FOREIGN KEY (client_uid) REFERENCES AgentClient(uid)
);

-- Q4: Internet Services: LLM/Data Storage (SQL DDL for entity(ies) table(s) only)

CREATE TABLE InternetService (
  sid INTEGER,
  endpoints VARCHAR(1000),
  provider VARCHAR(255),

  PRIMARY KEY (sid)
);

CREATE TABLE LLMService (
  sid INTEGER,
  domain VARCHAR(255),

  PRIMARY KEY (sid),
  FOREIGN KEY (sid) REFERENCES InternetService(sid)
);

CREATE TABLE DataStorage (
  sid INTEGER,
  type VARCHAR(255),

  PRIMARY KEY (sid),
  FOREIGN KEY (sid) REFERENCES InternetService(sid)
);


-- Q5: Write additional SQL DDL for relationship(s) table(s) below

CREATE TABLE ModelServices (
    bmid INTEGER,
    sid INTEGER,
    version VARCHAR(20),

    PRIMARY KEY (bmid, sid),

    FOREIGN KEY (bmid) REFERENCES BaseModel(bmid),
    FOREIGN KEY (sid) REFERENCES InternetService(sid)
);

CREATE TABLE ModelConfigurations (
   cid INTEGER,
   mid INTEGER NOT NULL,
   bmid INTEGER NOT NULL,
   duration INTEGER,

   PRIMARY KEY (cid, mid),
   FOREIGN KEY (mid) REFERENCES CustomizedModel(mid),
   FOREIGN KEY (bmid) REFERENCES BaseModel(bmid)
);
