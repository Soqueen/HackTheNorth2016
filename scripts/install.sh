#!/bin/bash

database=""
dbuser=""
dbpw=""

function psql_cmd () {
    psql -c "$1" > /dev/null
}

function is_user () {
    psql postgres -tAc "SELECT 1 FROM pg_roles WHERE rolname='$1'" |
        grep -q 1
}

# START POSTGRES
/etc/init.d/postgresql start
echo

# DROP DATABASE AND USER
echo " * Dropping old database and user"
dropdb $database 2> /dev/null || :
is_user $dbuser && dropuser $dbuser 2> /dev/null
echo "   ...done."
echo

# CREATE TESTING USER
echo " * Creating $dbuser user"
psql_cmd "CREATE USER $dbuser WITH SUPERUSER ENCRYPTED PASSWORD '$dbpw'"
echo "   ...done."
echo

# FIX PERMISSIONS
echo " * Fixing PostgreSQL permissions"
hba=$(psql -t -P format=unaligned -c "show hba_file")
pgres="local   all             postgres                                peer"
lgrid="local   all             lgrid_app                               md5"
dbusr="local   all             $dbuser                                 md5"
grep -Fxq "$dbusr" $hba || sed -ie "/^$pgres/a $dbusr" $hba
grep -Fxq "$lgrid" $hba || sed -ie "/^$pgres/a $lgrid" $hba
echo "   ...done."
echo

# RESTART POSTGRES
/etc/init.d/postgresql restart
echo

# CREATE FRAMEWORK DATABASE
echo " * Creating $database database"
psql_cmd "CREATE DATABASE $database"
psql_cmd "GRANT ALL PRIVILEGES ON DATABASE $database TO $dbuser"
echo "   ...done."
echo

# SETUP FRAMEWORK DATABASE
echo " * Setting up tables in $database database"
psql $database < db.sql &> /dev/null
echo "   ...done."
echo