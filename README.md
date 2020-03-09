##Sticky Notes

##### `* This is a sample sticky note application built using Django*`

Before starting the application set these following environment variables for database connection.
Currently, one can only connect a PostgreSQL database with the given driver.


```
export DB_NAME="project-db-name"
export DB_USER="project-db-username"
export DB_PASSWORD="project-db-password"
export DB_HOST="server-host-db"
export DB_PORT="server-port-db"
```

Available routes:
1. `/admin`
1. `/notes` [GET] and [POST]