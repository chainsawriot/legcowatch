create table individuals (
       inv_id integer primary key,
       name_en text,
       name_ch text
);

create table legislators (
       leg_id integer primary key,
       inv_id integer,
       year integer,
       group varchar(255)
);

create table motions (
       mot_id integer primary key,
       startdate date,
       votedate
);
