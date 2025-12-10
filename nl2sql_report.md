# 9. Experiment: Solving NL2SQL with LLM

NL2SQL, or text-to-SQL, is a task that translates natural language queries into SQL queries. NL2SQL is an interdisciplinary study between NLP (natural language processing) and database systems. In this project, the previously required functions also fall under the NL2SQL category — students play the role of converting natural language (NL) into SQL queries.

## Query 1

For each Internet Service (`sid`), find the most frequently used version among all Base Models that utilize it. If multiple versions have the same highest frequency, you may return any one of them.

---

### Prompt 1(gpt-4.1)

**Instruction:** You are a natural-language-to-SQL-query expert who generates accurate SQL queries based on natural language inputs. Output nothing except a JSON query including the corresponding SQL code.

**Generated Query:**

```sql
SELECT ms.sid, ms.version
FROM ModelServices ms
JOIN (
  SELECT sid, version, COUNT(*) AS freq,
         ROW_NUMBER() OVER (PARTITION BY sid ORDER BY COUNT(*) DESC) as rn
  FROM ModelServices
  GROUP BY sid, version
) t ON ms.sid = t.sid AND ms.version = t.version
WHERE t.rn = 1;
```

---

### Prompt 2(o1)

**Instruction:** You are an expert natural-language-to-SQL translator. Your task is to produce a single valid JSON object with the following structure:

{
"sql": "<SQL_QUERY_STRING>"
}

Rules you must follow:

-   Output only the JSON object. No explanations, no markdown, no backticks.
-   Produce a single SQL query that accurately answers the user request.
-   The value of `"sql"` must be a valid SQL string with no line breaks unless required by the query.
-   Do not include comments, natural language, or additional fields.

**Generated Query:**

```sql
SELECT sid, version
FROM (
  SELECT sid, version,
         ROW_NUMBER() OVER (PARTITION BY sid ORDER BY COUNT(*) DESC) AS rn
  FROM ModelServices
  GROUP BY sid, version
) t
WHERE rn = 1;
```

---

### Prompt 3(gpt-4o)

**Instruction:** You are an expert system that converts natural language into SQL. Read the user’s request and output only one JSON object with exactly one key "query" whose value is a complete SQL statement string. The output must be valid JSON with no explanations or extra text. The SQL must be complete and syntactically correct, ending with a semicolon. Use single quotes for string literals. If details are missing, make reasonable assumptions.

For example, {"query":"SELECT p.product_name, SUM(s.quantity) AS total_sold FROM Sales s JOIN Products p ON s.product_id = p.product_id GROUP BY p.product_name ORDER BY total_sold DESC;"}

**Generated Query:**

```sql
SELECT ms.sid, ms.version
FROM ModelServices ms
JOIN (
  SELECT sid, version, COUNT(*) as version_count
  FROM ModelServices
  GROUP BY sid, version
) v_counts ON ms.sid = v_counts.sid AND ms.version = v_counts.version
WHERE (v_counts.sid, v_counts.version_count) IN (
  SELECT sid, MAX(version_count) as max_count
  FROM (
    SELECT sid, version, COUNT(*) as version_count
    FROM ModelServices
    GROUP BY sid, version
  ) version_counts
  GROUP BY sid
);
```

---

## Query 2

Find all the Internet Service(sid) that are utilized by every Base Model built by the agent creator user_iuwrh.

---

### Prompt 1(gpt-4.1)

**Instruction:** Same as prev Prompt 1

**Generated Query:**

```sql
SELECT ms.sid
FROM ModelServices ms
JOIN BaseModel bm ON ms.bmid = bm.bmid
JOIN AgentCreator ac ON bm.creator_uid = ac.uid
JOIN User u ON ac.uid = u.uid
WHERE u.username = 'user_iuwrh'
GROUP BY ms.sid
HAVING COUNT(DISTINCT ms.bmid) = (
    SELECT COUNT(*)
    FROM BaseModel bm2
    JOIN AgentCreator ac2 ON bm2.creator_uid = ac2.uid
    JOIN User u2 ON ac2.uid = u2.uid
    WHERE u2.username = 'user_iuwrh'
);
```

---

### Prompt 2(o1)

**Instruction:** Same as prev Prompt 2

**Generated Query:**

```sql
SELECT ms.sid
FROM ModelServices ms
JOIN BaseModel bm ON ms.bmid = bm.bmid
JOIN AgentCreator ac ON bm.creator_uid = ac.uid
JOIN User u ON u.uid = ac.uid
WHERE u.username = 'user_iuwrh'
GROUP BY ms.sid
HAVING COUNT(DISTINCT ms.bmid) = (
    SELECT COUNT(*)
    FROM BaseModel bm2
    JOIN AgentCreator ac2 ON bm2.creator_uid = ac2.uid
    JOIN User u2 ON u2.uid = ac2.uid
    WHERE u2.username = 'user_iuwrh'
);
```

---

### Prompt 3(gpt-4o)

**Instruction:** Same as prev Prompt 3

**Generated Query:**

```sql
SELECT ms.sid
FROM InternetService ins
JOIN ModelServices ms ON ins.sid = ms.sid WHERE NOT EXISTS (
    SELECT 1 FROM BaseModel bm
    WHERE bm.creator_uid = (
        SELECT uid FROM User WHERE username = 'user_iuwrh'
    ) AND NOT EXISTS (
        SELECT 1 FROM ModelServices ms2 WHERE ms2.bmid = bm.bmid AND ms2.sid = ms.sid
    )
) GROUP BY ms.sid;
```

## Query 3

Find all customized models(mid) that do not appear in model configurations.

---

### Prompt 1(gpt-4.1)

**Instruction:** Same as prev Prompt 1

**Generated Query:**

```sql
SELECT mid
FROM CustomizedModel
WHERE mid NOT IN (
    SELECT mid FROM ModelConfigurations
);
```

---

### Prompt 2(o1)

**Instruction:** Same as prev Prompt 2

**Generated Query:**

```sql
SELECT mid
FROM CustomizedModel
WHERE mid NOT IN (
    SELECT mid FROM ModelConfigurations
)
```

---

### Prompt 3(gpt-4o)

**Instruction:** Same as prev Prompt 3

**Generated Query:**

```sql
SELECT cm.mid
FROM CustomizedModel cm
WHERE NOT EXISTS (
    SELECT 1
    FROM ModelConfigurations mc
    WHERE mc.mid = cm.mid
);
```
