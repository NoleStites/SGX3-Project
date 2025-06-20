# SGX3 Coding Institute Repo

## 📌 API Endpoints

### `/`
**Method:** GET  
**Description:** Returns the first 10 rows of the dataset.  
**Example Response:**  
```json
[
  {"Incident ID": "...", "Published Date": "...", ...},
  ...
]
```

---

### `/head?count=<n>`
**Method:** GET  
**Description:** Returns the first `n` rows of the dataset.  
**Query Params:**
- `count` — Number of rows to return  
**Example:** `/head?count=5`

---

### `/shape`
**Method:** GET  
**Description:** Returns the number of rows and columns in the dataset.  
**Example Response:**
```json
{
  "rows": 20000,
  "columns": 12
}
```

---

### `/columns`
**Method:** GET  
**Description:** Returns the list of column names in the dataset.  
**Example Response:**
```json
["Incident ID", "Published Date", "Location", ...]
```

---

### `/UniqueValues?column=<column_name>`
**Method:** GET  
**Description:** Returns the unique values in the specified column.  
**Query Params:**
- `column` — Name of the column to analyze  
**Example:** `/UniqueValues?column=Category`

---

### `/ValueCountByYear?ColumnName=<col>&ColumnValue=<val>&Year=<yyyy>`
**Method:** GET  
**Description:** Filters the dataset by column name, a specific value, and a given year. Returns matching incidents.  
**Query Params:**
- `ColumnName` — Name of the column to filter  
- `ColumnValue` — Value to match in the column  
- `Year` — Year to filter by  
**Example:** `/ValueCountByYear?ColumnName=Category&ColumnValue=Traffic Hazard&Year=2023`

---

### `/BetweenTimes?hour1=<start>&hour2=<end>`
**Method:** GET  
**Description:** Returns all incidents that occurred between the specified hours (inclusive).  
**Query Params:**
- `hour1` — Start hour (0–23)  
- `hour2` — End hour (0–23)  
**Example:** `/BetweenTimes?hour1=6&hour2=9`

---
