# SELECT
`SELECT` 문법

## Basic
```sql
SELECT field FROM table_name;

SELECT field1, field2 FROM table_name;

SELECT field1 AS field_name, field2 FROM table_name;

SELECT * FROM table_name;

SELECT field1, field2 / 6000 FROM table_name;
```

## ORDER BY
```sql
SELECT field FROM table_name ORDER BY field1 [ASC:DESC], field2 [ASC:DESC], ...
```

1. 기본 값은 `ASC`
2. 여러 값을 기준으로 정렬하면 순서대로 정렬한다.
    - python sorted 함수에서 key 값에 tuple을 제공하는 경우와 동일.
3. `NULL` 값은 우선 순위가 가장 낮다.
    - `ASC`를 사용하면 가장 먼저.
    - `DESC`를 사용하면 가장 아래.

## Filter
### DISTINCT
조회 결과에서 중복된 레코드를 제거.

`SELECT` 다음에 작성.
```SQL
SELECT DISTINCT field FROM table_name;
```

### WHERE
조회 시 특정 검색 조건을 지정.

```SQL
SELECT field FROM table_name WHERE conditions;
```

#### condition 목록 및 간단한 용례
```sql
=, >=, <=, !=, IS, LIKE, IN, BETWEEN, AND, OR
```

1. `BETWEEN 1000 AND 5000`
2. `field IS NULL`
3. `field LIKE '%son'`,  `field LIKE '__a'`

#### LIKE
LIKE는 와일드 카드와 많이 함께 사용하여 특정 문자열 패턴을 선택하는데 쓰인다.

- % : 아무 문자 0개 이상과 매칭.
- _ : 아무 문자 1개와 매칭.

## LIMIT
결과에서 특정 개수만 뽑아내는 문법.

### Basic syntax

offset + 1 부터 row_count 개 만큼의 record만 뽑아낸다.

offset 값을 작성하지 않으면 처음부터 센다.

```SQL
SELECT
    ..
FROM
    ..
LIMIT [offset, ] row_count
```


### OFFSET KW
OFFSET 키워드 사용하면 아래와 같이 작성할 수 있다.

```SQL
SELECT
    ..
FROM
    ..
LIMIT 4 OFFSET 2;
```

### 예제

```SQL
SELECT field1, field2, ... FROM table_name ORDER BY field2 DESC LIMIT 7;
```

## GROUP BY

```sql
SELECT
  field1, field2, ..., aggragation(field_n)
FROM
  table_name
GROUP BY
  field1, field2, ...
```

레코드를 그룹화하는 문법.

주로 집계함수와 같이 사용하여 데이터에 대한 특정한 정보를 나타낼 때 쓰인다.

집계 함수를 `SELECT`에 작성하면 그룹을 기준으로 각 필드 정보를 나타내고, 각 그룹의 특정 필드에 대한 aggregation 함수를 적용한 필드를 추가하여 반환한다.

`GROUP BY` 절에 필드를 둘 이상 정의하면 두 필드의 조합을 기준으로 그룹을 만든다.

예 : ('a', 'b')와 ('a', 'c')

### aggregation function
```sql
SUM, AVG, MAX, MIN, COUNT
```

### HAVING
일반 필드에 대한 조건문은 `WHERE`, 집계 함수에 대한 조건문은 `HAVING`!

집계 함수에 대한 조건을 작성할 때는 HAVING절을 사용한다.

이는 SQL의 내부적인 실행 순서와 더불어 기본 필드와 집계 함수에 대한 조건을 나누기 위함.

```SQL
SELECT
  field1, field2, ..., AGGREGATION(fieldn) AS AGG
FROM
  table_name
GROUP BY
  field1, field2, ...
HAVING
  AGG condition;
```

### 주의 사항
#### 1. SELECT와 GROUP BY
`SELECT`에 선언한 필드는 `GROUP BY`에 선언한 필드의 부분 집합이어야 한다. (단, 집계 함수에 작성된 필드는 GROUP BY에 선언한 필드에 없어도 괜찮다.)

(어찌보면 당연한게, GROUP BY에는 없는 필드를 SELECT에서 작성해버리면 GROUP BY가 정상적으로 동작하지 않는다. 그룹화를 이미 어떤 필드의 집합으로 했는데, 해당 집합에 포함되지 않은 필드를 선택하는게 애시당초 가능한 일인가?)

#### 2. 집계 함수
집계 함수는 필드에 제약 조건이 없다. `SELECT`나 `GROUP BY`에 있든 없든 정상적으로 동작한다.

## 참조 - SELECT 문 관련 실행 순서
![alt text](image.png)