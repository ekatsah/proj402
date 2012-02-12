insert into courses_category (name, description) values ('ROOT', 'root of the category tree');

insert into courses_category (name, description) values ('Biology', 'BA-BIOL, BA-IRBI, MA-BMOL...');
insert into courses_category (name, description) values ('Chemistry', 'BA-CHIM, MA-CHIM');
insert into courses_category (name, description) values ('Geography', 'BA-GEOG');
insert into courses_category (name, description) values ('Geology', 'BA-GEOL');
insert into courses_category (name, description) values ('Computing', 'BA-INFO, MA-INFO');
insert into courses_category (name, description) values ('Maths', 'BA-MATH, MA-MATH');
insert into courses_category (name, description) values ('Physics', 'BA-PHYS, MA-PHYS');

insert into courses_category (name, description) values ('BA-INFO1', 'First year in computer science');
insert into courses_category (name, description) values ('BA-INFO2', 'Second year in computer science');
insert into courses_category (name, description) values ('BA-INFO3', 'Third year in computer science');
insert into courses_category (name, description) values ('MA-INFO1', 'First year of the master in computer science');

insert into courses_category (name, description) values ('Artificial Intelligence', 'IA stuff and topics');
insert into courses_category (name, description) values ('Algorithm Optimisation', 'Mega mathematical brain needed');
insert into courses_category (name, description) values ('Beer drinking', 'Ballmer peak related things');

insert into courses_category_holds values (1, 1, 2);
insert into courses_category_holds values (2, 1, 3);
insert into courses_category_holds values (3, 1, 4);
insert into courses_category_holds values (4, 1, 5);
insert into courses_category_holds values (5, 1, 6);
insert into courses_category_holds values (6, 1, 7);
insert into courses_category_holds values (7, 1, 8);
insert into courses_category_holds values (8, 6, 9);
insert into courses_category_holds values (9, 6, 10);
insert into courses_category_holds values (10, 6, 11);
insert into courses_category_holds values (11, 6, 12);
insert into courses_category_holds values (12, 12, 13);
insert into courses_category_holds values (13, 12, 14);
insert into courses_category_holds values (14, 12, 15);
insert into courses_category_holds values (15, 2, 16);
insert into courses_category_holds values (16, 2, 17);
insert into courses_category_holds values (17, 2, 18);

insert into courses_category_contains values (1, 12, 1);
insert into courses_category_contains values (2, 12, 2);
insert into courses_category_contains values (3, 12, 3);
insert into courses_category_contains values (4, 12, 4);
insert into courses_category_contains values (5, 12, 7);
insert into courses_category_contains values (6, 12, 8);
insert into courses_category_contains values (7, 12, 12);
insert into courses_category_contains values (8, 12, 13);
insert into courses_category_contains values (9, 12, 14);
insert into courses_category_contains values (10, 13, 5);
insert into courses_category_contains values (11, 13, 6);
insert into courses_category_contains values (12, 13, 9);
insert into courses_category_contains values (13, 13, 10);
insert into courses_category_contains values (14, 13, 11);

insert into courses_category (name, description) values ('Project 402', 'Zoidberg release');
insert into courses_category_contains values (15, 16, 15);
insert into courses_category_contains values (16, 16, 16);