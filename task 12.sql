create database clg_management;
use clg_management;
create table student(std_id int primary key auto_increment, std_name varchar(50),dept varchar(50), age int);
insert into student(std_name,dept,age)values("keerthi","management",24),("riya","commerce",25),("diya","electronics",23),("rithu","computer science",22);
select * from student;
create table departments(dept_id int primary key, dept_name varchar(50));
insert into departments(dept_id, dept_name)values(1,"management"),(2,"commerce"),(3,"electronics"),(4,"computer science");
select * from departments;
create table entrollments(ent_id int primary key auto_increment, std_id int, course varchar(50),fees decimal(10,2),foreign key (std_id) references student(std_id));
insert into entrollments(std_id, course,fees)values(1,"python",25000),(1,"java",30000),(2,"powerbi",28000),(3,"excel",45000),(4,"mysql",38000);
select * from entrollments;

delimiter //

create procedure add_std(in p_name varchar(50),p_dept varchar(50),p_age int)
begin
insert into student(std_name, dept, age)values(p_name,p_dept,p_age);
end //

delimiter ;
start transaction;
call add_std("sooraj","management",25);
call add_std("gokul","commerce",27);
delete from student where std_id in(5,6);
drop procedure if exists add_std;

savepoint student_savepoint;
rollback;
rollback to savepoint student_savepoint;
commit;

SELECT d.dept_name AS department,COUNT(DISTINCT s.std_id) AS student_count,SUM(e.fees) AS total_revenue
FROM departments d JOIN student s ON d.dept_name = s.dept LEFT JOIN entrollments e ON s.std_id = e.std_id GROUP BY d.dept_id, d.dept_name
HAVING COUNT(DISTINCT s.std_id) > 1;

SELECT s.std_name AS name, s.dept AS department, COUNT(e.ent_id) AS total_courses_enrolled, SUM(e.fees) AS total_fee_paid FROM student s JOIN entrollments e ON s.std_id = e.std_id
GROUP BY s.std_id, s.std_name, s.dept HAVING COUNT(e.ent_id) > 1;

create view std_report as select s.std_name as student_name, s.dept as department_name,e.course,e.fees as fee
from student s join entrollments e on s.std_id=e.std_id;

SELECT student_name, department_name, SUM(fee) AS total_fee FROM std_report GROUP BY student_name, department_name HAVING SUM(fee) > 50000;

insert into student(std_name, dept, age) values("aami", "electronics", 22);
delete from student where std_name in("sooraj");


