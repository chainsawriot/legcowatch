create table individuals (
       inv_id integer primary key,
       name_en text,
       name_ch text
);

create table legislators (
       leg_id integer primary key,
       inv_id integer,
       term integer,
       constituency text
);

create table votings (
       vot_id integer primary key,
       inv_id integer,
       mot_id integer,
       decision text
);

create table motions (
       mot_id integer primary key,
       mover_inv_id integer,
       mover_type text,
       time_start text,
       time_vote text,
       vote_separate_mech integer,
       motion_en text,
       motion_ch text   
);
