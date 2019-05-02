{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf400
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww20480\viewh14440\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 // The following code was produced by Django using `python manage.py sqlmigrate delivery 0001_initial`\
// 	This command generates the SQL command to be issued to the SQLite database, but doesn\'92t\
//	execute the command.\
//\
//	The syntax for the command is `python manage.py sqlmigrate <app_name> <migration_name>`\
\
CREATE TABLE "delivery_vehicle" (\
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
	"model" varchar(60) NOT NULL, "color" varchar(60) NOT NULL, \
	"year" varchar(60) NOT NULL\
);\
\
CREATE TABLE "delivery_driver" (\
	"user_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
	"ssn" varchar(10) NOT NULL, \
	"name" varchar(50) NOT NULL, \
	"email" varchar(80) NOT NULL, \
	"state" varchar(80) NOT NULL, \
	"city" varchar(80) NOT NULL, \
	"company" varchar(80) NOT NULL\
);\
\
CREATE TABLE "delivery_delivery" (\
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
	"amount" integer NOT NULL, "tip" integer NOT NULL, \
	"driver_id" integer NOT NULL REFERENCES "delivery_driver" ("user_id") DEFERRABLE INITIALLY DEFERRED, \
	"vehicle_id" integer NOT NULL REFERENCES "delivery_vehicle" ("id") DEFERRABLE INITIALLY DEFERRED\
);\
CREATE INDEX "delivery_delivery_driver_id_2f4bb46c" ON "delivery_delivery" ("driver_id");\
CREATE INDEX "delivery_delivery_vehicle_id_0fa023b8" ON "delivery_delivery" ("vehicle_id");}