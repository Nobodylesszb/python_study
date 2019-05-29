create table if not exists china_district_poly(
  "id" SERIAL PRIMARY KEY,
	"geom" geometry,
	"province" varchar(100),
	"city" VARCHAR(100),
	"district" varchar(100),
	"adcode" FLOAT8
)

CREATE INDEX china_district_poly_geom
ON china_district_poly
USING GIST (geom);

create table if not exists bussiness_poly
(
  "id" SERIAL PRIMARY KEY,
	"geom" geometry,
	"projectid" VARCHAR(50) not NULL,
	"name" VARCHAR(50) NULL,
	"type" VARCHAR(20) not NULL
)


CREATE INDEX bussiness_poly_geom
ON bussiness_poly
USING GIST (geom);


alter table parking_poi add column index serial;
update parking_poi set geom=st_SetSrid(st_MakePoint(lng, lat), 4326);

create index if not exists parking_poi_geom on parking_poi using GIST(geom)