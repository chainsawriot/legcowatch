create table individuals (
       inv_id integer primary key,
       name_en text,
       name_ch text
);

create table legislators (
       leg_id integer primary key,
       inv_id integer references individuals(inv_id),
       term integer,
       constituency text
);

create table votings (
       vot_id integer primary key,
       inv_id integer references individuals(inv_id),
       mot_id integer references motions(mot_id),
       decision text
);

create table motions (
       mot_id integer primary key,
       mover_inv_id integer references individuals(inv_id),
       mover_type text,
       time_start integer,
       time_vote integer,
       vote_separate_mech integer,
       motion_en text,
       motion_ch text   
);
