# Doris Docker-Compose Image

To start, run

```sh
docker-compose -f docker-compose-doris.yaml up
```

or `detached`

```sh
docker-compose -f docker-compose-doris.yaml up -d
```

Example queries on a connected mysql client on port 9030

```sql
CREATE SCHEMA MyDB


CREATE TABLE IF NOT EXISTS MyDB.example_unique_table
(
    user_id         LARGEINT        NOT NULL,
    user_name       VARCHAR(50)     NOT NULL,
    city            VARCHAR(20),
    age             SMALLINT,
    sex             TINYINT
)
UNIQUE KEY(user_id)
DISTRIBUTED BY HASH(user_id)
PROPERTIES( "replication_num"="1", "enable_unique_key_merge_on_write"="false");

-- drop table MyDB.example_unique_table

```

Jupyter Notebooks are available locally on `localhost:8888` while the default
apache doris frontend is available on `localhost:9030`

The special network is added for WSL compatibility, otherwise one can likely just use the 'host' network
