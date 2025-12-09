DROP DATABASE IF EXISTS cs122a_project;
CREATE DATABASE cs122a_project;
USE cs122a_project;

-- Q1: User and Agent Creator/Client (SQL DDL for entity(ies) table(s) only)

CREATE TABLE User (
  uid INTEGER,
  username VARCHAR(255),
  email VARCHAR(255),

  PRIMARY KEY (uid)
);

CREATE TABLE AgentCreator (
  uid INTEGER,
  payoutaccount VARCHAR(255),
  bio VARCHAR(255),
  
  PRIMARY KEY (uid),
  FOREIGN KEY (uid) REFERENCES User(uid)
);

CREATE TABLE AgentClient (
  uid INTEGER,
  cardnumber VARCHAR(255),
  cardholdername VARCHAR(255),
  expirationdate VARCHAR(255),
  cvv VARCHAR(255),
  zip VARCHAR(255),
  interests VARCHAR(255),
  
  PRIMARY KEY (uid),
  FOREIGN KEY (uid) REFERENCES User(uid)
);

-- Q2: Base and Customized Model (SQL DDL for entity(ies) table(s) only)

CREATE TABLE BaseModel (
  bmid INTEGER,
  uid INTEGER NOT NULL,
  description VARCHAR(255),

  PRIMARY KEY (bmid),
  FOREIGN KEY (uid) REFERENCES AgentCreator(uid)
);

CREATE TABLE CustomizedModel (
  mid INTEGER UNIQUE,
  bmid INTEGER NOT NULL,

  PRIMARY KEY (bmid, mid),
  FOREIGN KEY (bmid) REFERENCES BaseModel(bmid)
	ON DELETE CASCADE
);

-- Q3: Configurations (SQL DDL for entity(ies) table(s) only)

CREATE TABLE Configuration (
  cid INTEGER,
  uid INTEGER NOT NULL,
  content VARCHAR(255),
  labels VARCHAR(255),

  PRIMARY KEY (cid),
  FOREIGN KEY (uid) REFERENCES AgentClient(uid)
);

-- Q4: Internet Services: LLM/Data Storage (SQL DDL for entity(ies) table(s) only)

CREATE TABLE InternetService (
  sid INTEGER,
  endpoint VARCHAR(255),
  provider VARCHAR(255),

  PRIMARY KEY (sid)
);

CREATE TABLE LLMService (
  sid INTEGER,
  domain VARCHAR(255),

  PRIMARY KEY (sid),
  FOREIGN KEY (sid) REFERENCES InternetService(sid)
);

CREATE TABLE DataStorageService (
  sid INTEGER,
  type VARCHAR(255),

  PRIMARY KEY (sid),
  FOREIGN KEY (sid) REFERENCES InternetService(sid)
);


-- Q5: Write additional SQL DDL for relationship(s) table(s) below

CREATE TABLE Utilizes (
    bmid INTEGER,
    sid INTEGER,
    version VARCHAR(20),

    PRIMARY KEY (bmid, sid),

    FOREIGN KEY (bmid) REFERENCES BaseModel(bmid),
    FOREIGN KEY (sid) REFERENCES InternetService(sid)
);

CREATE TABLE Uses (
   cid INTEGER,
   mid INTEGER NOT NULL,
   bmid INTEGER NOT NULL,
   duration TIME,

   PRIMARY KEY (cid),
   FOREIGN KEY (mid) REFERENCES CustomizedModel(mid),
   FOREIGN KEY (bmid) REFERENCES BaseModel(bmid)
);
